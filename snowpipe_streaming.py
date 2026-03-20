"""
Snowpipe Streaming - Multi-Channel IoT Sensor Data Ingestion
Each channel owns a partition of sensor_ids (hash-routed).
Data is pre-clustered before hitting the raw table, matching
the table's CLUSTER BY (TO_DATE(reading_timestamp), sensor_id).
"""

import hashlib
import json
import logging
import os
import time
import uuid
import random
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import Lock, Thread

from snowflake.ingest import SnowflakeStreamingIngestClient

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("snowpipe_streaming")


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
@dataclass
class SnowflakeConfig:
    account:          str
    user:             str
    role:             str
    database:         str
    schema:           str
    table:            str
    warehouse:        str
    private_key_path: str

    # Multi-channel config
    num_channels:    int   = 4          # parallelism — tune to warehouse size
    channel_prefix:  str   = "sensor_channel"

    # Batching / retry
    batch_size:      int   = 500
    flush_interval:  float = 2.0
    max_retries:     int   = 3
    retry_backoff:   float = 1.5


def load_config() -> SnowflakeConfig:
    return SnowflakeConfig(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        role=os.environ.get("SNOWFLAKE_ROLE", "snowpipe_streaming_role"),
        database=os.environ.get("SNOWFLAKE_DATABASE", "iot_streaming"),
        schema=os.environ.get("SNOWFLAKE_SCHEMA", "sensor_data"),
        table=os.environ.get("SNOWFLAKE_TABLE", "sensor_readings"),
        warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "streaming_wh"),
        private_key_path=os.environ["SNOWFLAKE_PRIVATE_KEY_PATH"],
        num_channels=int(os.environ.get("NUM_CHANNELS", "4")),
    )


# ---------------------------------------------------------------------------
# Domain object
# ---------------------------------------------------------------------------
@dataclass
class SensorReading:
    sensor_id:         str
    location_id:       str
    reading_type:      str
    reading_value:     float
    reading_timestamp: datetime
    metadata:          dict = field(default_factory=dict)


def to_snowflake_row(reading: SensorReading) -> dict:
    return {
        "READING_ID":          str(uuid.uuid4()),
        "SENSOR_ID":           reading.sensor_id,
        "LOCATION_ID":         reading.location_id,
        "READING_TYPE":        reading.reading_type,
        "READING_VALUE":       reading.reading_value,
        "READING_TIMESTAMP":   reading.reading_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "INGESTION_TIMESTAMP": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "METADATA":            json.dumps(reading.metadata),
    }


# ---------------------------------------------------------------------------
# Routing — deterministic hash of sensor_id → channel index
#
# Why sensor_id?
#   Table is CLUSTER BY (TO_DATE(reading_timestamp), sensor_id).
#   Routing by sensor_id means all rows for a given sensor always go
#   through the same channel → same Snowflake micro-partition range.
#   This pre-clusters data before it even lands, reducing compaction work.
# ---------------------------------------------------------------------------
def route_to_channel(sensor_id: str, num_channels: int) -> int:
    """
    Consistent hash: same sensor_id always → same channel index.
    Uses MD5 for speed (not security). Could use xxhash in prod.
    """
    hash_int = int(hashlib.md5(sensor_id.encode()).hexdigest(), 16)
    return hash_int % num_channels


# ---------------------------------------------------------------------------
# Single channel — owns its own offset counter (monotonic, crash-safe)
# ---------------------------------------------------------------------------
class SensorChannel:
    """
    One channel = one ordered write stream for a subset of sensor_ids.
    Offset is a monotonic int recovered from Snowflake on restart.
    """

    def __init__(
        self,
        client: SnowflakeStreamingIngestClient,
        config: SnowflakeConfig,
        channel_index: int,
    ):
        self._config = config
        self._name   = f"{config.channel_prefix}_{channel_index}"
        self._lock   = Lock()          # thread-safe offset increment

        self._channel = client.open_channel(
            name=self._name,
            database=config.database,
            schema=config.schema,
            table=config.table,
        )

        # Recover offset from Snowflake so restarts don't re-send duplicates
        self._offset = self._recover_offset()
        logger.info("Opened channel %s at offset %d", self._name, self._offset)

    def _recover_offset(self) -> int:
        """
        On restart: ask Snowflake what the last committed offset was.
        Resume from offset + 1 so we never re-insert committed batches.
        """
        try:
            last = self._channel.get_latest_committed_offset_token()
            if last is not None:
                recovered = int(last) + 1
                logger.info("Channel %s recovering from offset %d", self._name, recovered)
                return recovered
        except Exception as e:
            logger.warning("Could not recover offset for %s: %s. Starting at 0.", self._name, e)
        return 0

    def insert_rows(self, rows: list[dict]) -> None:
        if not rows:
            return

        with self._lock:
            current_offset = self._offset
            self._offset += 1              # increment before send (idempotent on retry with same token)

        response = self._channel.insert_rows(
            rows=rows,
            offset_token=str(current_offset),   # deterministic → safe to retry
        )

        if response.has_errors():
            for err in response.get_insert_errors():
                logger.error(
                    "Channel %s insert error row_index=%s: %s",
                    self._name, err.row_index, err.message,
                )
            raise RuntimeError(
                f"Channel {self._name} batch {current_offset} had errors"
            )

        logger.debug("Channel %s flushed %d rows at offset %d", self._name, len(rows), current_offset)

    @property
    def name(self) -> str:
        return self._name

    def close(self) -> None:
        self._channel.close()
        logger.info("Closed channel %s at offset %d", self._name, self._offset)


# ---------------------------------------------------------------------------
# Per-channel producer — buffer + flush + retry + DLQ
# ---------------------------------------------------------------------------
class ChannelProducer:
    """
    Each channel gets its own producer with its own buffer.
    Flushed independently — one slow/failing channel doesn't block others.
    """

    def __init__(self, channel: SensorChannel, config: SnowflakeConfig):
        self._channel    = channel
        self._config     = config
        self._buffer: list[dict] = []
        self._last_flush = time.monotonic()
        self._lock       = Lock()

    def enqueue(self, row: dict) -> None:
        with self._lock:
            self._buffer.append(row)
            should_flush = (
                len(self._buffer) >= self._config.batch_size
                or (time.monotonic() - self._last_flush) >= self._config.flush_interval
            )
        if should_flush:
            self.flush()

    def flush(self) -> None:
        with self._lock:
            if not self._buffer:
                return
            batch, self._buffer = self._buffer, []
            self._last_flush = time.monotonic()

        self._flush_with_retry(batch)

    def _flush_with_retry(self, batch: list[dict]) -> None:
        delay = 1.0
        for attempt in range(1, self._config.max_retries + 1):
            try:
                self._channel.insert_rows(batch)
                return
            except Exception as exc:
                logger.warning(
                    "Channel %s flush attempt %d/%d failed: %s",
                    self._channel.name, attempt, self._config.max_retries, exc,
                )
                if attempt == self._config.max_retries:
                    self._dead_letter(batch, exc)
                    return
                time.sleep(delay)
                delay *= self._config.retry_backoff

    def _dead_letter(self, batch: list[dict], exc: Exception) -> None:
        dlq_path = f"dlq_{self._channel.name}_{int(time.time())}.jsonl"
        with open(dlq_path, "w") as f:
            for row in batch:
                f.write(json.dumps(row) + "\n")
        logger.error(
            "Dead-lettered %d rows from channel %s → %s. Cause: %s",
            len(batch), self._channel.name, dlq_path, exc,
        )

    def close(self) -> None:
        self.flush()                 # drain buffer
        self._channel.close()


# ---------------------------------------------------------------------------
# Channel pool — routes readings to the right producer
# ---------------------------------------------------------------------------
class ChannelPool:
    """
    Manages N channels. Routes each SensorReading to exactly one channel
    based on sensor_id hash so:
      - Same sensor always lands in same channel (ordered per sensor)
      - Data arrives pre-partitioned, matching CLUSTER BY sensor_id
      - N channels = N parallel write streams = higher throughput

    Usage:
        with ChannelPool(client, config) as pool:
            pool.produce(reading)
    """

    def __init__(self, client: SnowflakeStreamingIngestClient, config: SnowflakeConfig):
        self._config    = config
        self._producers = [
            ChannelProducer(
                SensorChannel(client, config, i),
                config,
            )
            for i in range(config.num_channels)
        ]
        logger.info("ChannelPool ready with %d channels", config.num_channels)

    def produce(self, reading: SensorReading) -> None:
        idx     = route_to_channel(reading.sensor_id, self._config.num_channels)
        row     = to_snowflake_row(reading)
        self._producers[idx].enqueue(row)

    def flush_all(self) -> None:
        """Force-flush all channels — call before shutdown or at checkpoint."""
        for producer in self._producers:
            producer.flush()

    def close(self) -> None:
        for producer in self._producers:
            producer.close()
        logger.info("All channels closed")

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.flush_all()
        self.close()


# ---------------------------------------------------------------------------
# Snowflake client factory
# ---------------------------------------------------------------------------
@contextmanager
def snowflake_streaming_client(config: SnowflakeConfig):
    with open(config.private_key_path, "r") as f:
        private_key = f.read()

    client = SnowflakeStreamingIngestClient(
        name="iot_sensor_client",
        account=config.account,
        user=config.user,
        private_key=private_key,
        role=config.role,
        connect_string=f"jdbc:snowflake://{config.account}.snowflakecomputing.com",
    )
    try:
        yield client
    finally:
        client.close()
        logger.info("Snowflake streaming client closed")


# ---------------------------------------------------------------------------
# Simulator
# ---------------------------------------------------------------------------
def simulate_sensor_reading() -> SensorReading:
    reading_type = random.choice(["temperature", "humidity", "pressure"])
    value_range  = {
        "temperature": (15.0, 30.0),
        "humidity":    (30.0, 80.0),
        "pressure":    (990.0, 1030.0),
    }
    lo, hi = value_range[reading_type]
    return SensorReading(
        sensor_id=f"sensor_{random.randint(1, 100)}",
        location_id=f"location_{random.randint(1, 10)}",
        reading_type=reading_type,
        reading_value=round(random.uniform(lo, hi), 2),
        reading_timestamp=datetime.now(timezone.utc),
        metadata={
            "unit": {"temperature": "celsius", "humidity": "percent", "pressure": "hPa"}[reading_type],
            "firmware_version": "2.1.0",
        },
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    config = load_config()

    with snowflake_streaming_client(config) as client:
        with ChannelPool(client, config) as pool:
            logger.info("Starting multi-channel ingestion with %d channels", config.num_channels)

            # In prod: replace with Kafka consumer / MQTT subscriber
            for i in range(10_000):
                reading = simulate_sensor_reading()
                pool.produce(reading)       # auto-routed to correct channel

                if i % 1000 == 0:
                    logger.info("Produced %d readings", i)

            # flush_all + close happen automatically on context manager exit


if __name__ == "__main__":
    main()
    def __init__(self, client: SnowflakeStreamingIngestClient, config: SnowflakeConfig):
        self._config  = config
        self._channel = client.open_channel(
            name=config.channel_name,
            database=config.database,
            schema=config.schema,
            table=config.table,
        )
        logger.info("Opened channel: %s", config.channel_name)

    def insert_rows(self, rows: list[dict]) -> None:
        """
        Insert a batch of rows. Snowpipe Streaming buffers internally
        and commits to the table within seconds.
        """
        if not rows:
            return
        response = self._channel.insert_rows(
            rows=rows,
            offset_token=str(uuid.uuid4()),   # unique token per batch for dedup
        )
        if response.has_errors():
            # Log each failed row — don't silently drop
            for err in response.get_insert_errors():
                logger.error(
                    "Insert error row_index=%s message=%s",
                    err.row_index, err.message,
                )
            raise RuntimeError(f"Insert batch had {len(response.get_insert_errors())} errors")

        logger.info("Flushed %d rows via channel %s", len(rows), self._config.channel_name)

    def close(self) -> None:
        self._channel.close()
        logger.info("Closed channel: %s", self._config.channel_name)


# ---------------------------------------------------------------------------
# Producer — batches readings and flushes with retry
# ---------------------------------------------------------------------------
class SensorDataProducer:
    """
    Buffers SensorReading objects and flushes to Snowflake in batches.
    Call .produce() per reading, .flush() to force-send, or use as context manager.

    Industry pattern:
    - Buffer locally → flush on batch_size OR flush_interval, whichever hits first
    - Retry transient errors with exponential backoff
    - Dead-letter failed rows to a file/queue for reprocessing
    """

    def __init__(self, channel: SensorChannel, config: SnowflakeConfig):
        self._channel = channel
        self._config  = config
        self._buffer: list[dict] = []
        self._last_flush = time.monotonic()

    def produce(self, reading: SensorReading) -> None:
        self._buffer.append(to_snowflake_row(reading))
        should_flush = (
            len(self._buffer) >= self._config.batch_size
            or (time.monotonic() - self._last_flush) >= self._config.flush_interval
        )
        if should_flush:
            self.flush()

    def flush(self) -> None:
        if not self._buffer:
            return
        batch, self._buffer = self._buffer, []
        self._flush_with_retry(batch)
        self._last_flush = time.monotonic()

    def _flush_with_retry(self, batch: list[dict]) -> None:
        delay = 1.0
        for attempt in range(1, self._config.max_retries + 1):
            try:
                self._channel.insert_rows(batch)
                return
            except Exception as exc:
                logger.warning("Flush attempt %d/%d failed: %s", attempt, self._config.max_retries, exc)
                if attempt == self._config.max_retries:
                    self._dead_letter(batch, exc)
                    return
                time.sleep(delay)
                delay *= self._config.retry_backoff

    def _dead_letter(self, batch: list[dict], exc: Exception) -> None:
        """
        In prod: write to S3/GCS DLQ or a Kafka dead-letter topic.
        Here: write to local file for visibility.
        """
        import json
        dlq_path = f"dlq_{int(time.time())}.jsonl"
        with open(dlq_path, "w") as f:
            for row in batch:
                f.write(json.dumps(row) + "\n")
        logger.error("Dead-lettered %d rows to %s. Cause: %s", len(batch), dlq_path, exc)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.flush()
        self._channel.close()


# ---------------------------------------------------------------------------
# Snowflake client factory
# ---------------------------------------------------------------------------
@contextmanager
def snowflake_streaming_client(config: SnowflakeConfig):
    """Context manager — ensures client is always closed cleanly."""
    with open(config.private_key_path, "r") as f:
        private_key = f.read()

    client = SnowflakeStreamingIngestClient(
        name="iot_sensor_client",
        account=config.account,
        user=config.user,
        private_key=private_key,
        role=config.role,
        # Connection pool — reuse for multiple channels
        connect_string=f"jdbc:snowflake://{config.account}.snowflakecomputing.com",
    )
    try:
        yield client
    finally:
        client.close()
        logger.info("Snowflake streaming client closed")


# ---------------------------------------------------------------------------
# Sensor simulator — stands in for real IoT source (Kafka, MQTT, etc.)
# ---------------------------------------------------------------------------
def simulate_sensor_reading() -> SensorReading:
    reading_type = random.choice(["temperature", "humidity", "pressure"])
    value_range = {
        "temperature": (15.0, 30.0),
        "humidity":    (30.0, 80.0),
        "pressure":    (990.0, 1030.0),
    }
    lo, hi = value_range[reading_type]
    return SensorReading(
        sensor_id=f"sensor_{random.randint(1, 100)}",
        location_id=f"location_{random.randint(1, 10)}",
        reading_type=reading_type,
        reading_value=round(random.uniform(lo, hi), 2),
        reading_timestamp=datetime.now(timezone.utc),
        metadata={
            "unit": {"temperature": "celsius", "humidity": "percent", "pressure": "hPa"}[reading_type],
            "firmware_version": "2.1.0",
        },
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    config = load_config()

    with snowflake_streaming_client(config) as client:
        channel = SensorChannel(client, config)

        with SensorDataProducer(channel, config) as producer:
            logger.info("Starting sensor data ingestion...")

            # In prod: replace this loop with your Kafka consumer / MQTT subscriber
            for i in range(1000):
                reading = simulate_sensor_reading()
                producer.produce(reading)

                if i % 100 == 0:
                    logger.info("Produced %d readings", i)

            # Final flush happens automatically on context manager exit
            logger.info("Done. Final flush on exit.")


if __name__ == "__main__":
    main()
