"""
Snowpipe Streaming - IoT Sensor Data Ingestion
Industry-grade pattern: config, channel management, batching, retries, logging
"""

import logging
import time
import uuid
import random
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional
from contextlib import contextmanager

from snowflake.ingest import SnowflakeStreamingIngestClient
from snowflake.ingest.utils.datatypes import SnowflakeType

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("snowpipe_streaming")


# ---------------------------------------------------------------------------
# Config — in prod, load from env vars / Secrets Manager / Vault
# ---------------------------------------------------------------------------
@dataclass
class SnowflakeConfig:
    account:   str
    user:      str
    role:      str
    database:  str
    schema:    str
    table:     str
    warehouse: str
    private_key_path: str             # RSA private key (PEM), no password auth in prod
    channel_name: str = "sensor_channel_1"

    # Batching / retry knobs
    batch_size:      int   = 500      # rows per flush
    flush_interval:  float = 2.0      # seconds between flushes
    max_retries:     int   = 3
    retry_backoff:   float = 1.5      # exponential backoff multiplier


def load_config() -> SnowflakeConfig:
    """Load config from env in prod. Hardcoded here for clarity."""
    import os
    return SnowflakeConfig(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        role=os.environ.get("SNOWFLAKE_ROLE", "snowpipe_streaming_role"),
        database=os.environ.get("SNOWFLAKE_DATABASE", "iot_streaming"),
        schema=os.environ.get("SNOWFLAKE_SCHEMA", "sensor_data"),
        table=os.environ.get("SNOWFLAKE_TABLE", "sensor_readings"),
        warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "streaming_wh"),
        private_key_path=os.environ["SNOWFLAKE_PRIVATE_KEY_PATH"],
    )


# ---------------------------------------------------------------------------
# Row builder — maps your domain object → Snowflake row dict
# ---------------------------------------------------------------------------
@dataclass
class SensorReading:
    sensor_id:         str
    location_id:       str
    reading_type:      str       # temperature | humidity | pressure
    reading_value:     float
    reading_timestamp: datetime
    metadata:          dict = field(default_factory=dict)


def to_snowflake_row(reading: SensorReading) -> dict:
    """
    Convert domain object to the flat dict Snowpipe Streaming expects.
    Column names must match the target table exactly.
    VARIANT columns are passed as JSON strings.
    """
    import json
    return {
        "READING_ID":          str(uuid.uuid4()),
        "SENSOR_ID":           reading.sensor_id,
        "LOCATION_ID":         reading.location_id,
        "READING_TYPE":        reading.reading_type,
        "READING_VALUE":       reading.reading_value,
        "READING_TIMESTAMP":   reading.reading_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "INGESTION_TIMESTAMP": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "METADATA":            json.dumps(reading.metadata),   # VARIANT → JSON string
    }


# ---------------------------------------------------------------------------
# Channel manager — owns open/close and offset tracking
# ---------------------------------------------------------------------------
class SensorChannel:
    """
    Wraps a single Snowpipe Streaming channel.
    One channel = one ordered write stream into the table.
    For high throughput, run multiple channels in parallel.
    """

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
