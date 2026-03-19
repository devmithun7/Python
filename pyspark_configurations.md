# PySpark Configuration Reference Guide

> A comprehensive guide to the most important Apache Spark / PySpark configuration parameters — what they are, what they do, and why you'd use them.

---

## Table of Contents

1. [SQL & Shuffle Configurations](#1-sql--shuffle-configurations)
2. [Memory Configurations](#2-memory-configurations)
3. [Executor & Core Configurations](#3-executor--core-configurations)
4. [Storage & Persistence Configurations](#4-storage--persistence-configurations)
5. [Adaptive Query Execution (AQE)](#5-adaptive-query-execution-aqe)
6. [Join Configurations](#6-join-configurations)
7. [Serialization Configurations](#7-serialization-configurations)
8. [Dynamic Allocation Configurations](#8-dynamic-allocation-configurations)
9. [I/O & File Format Configurations](#9-io--file-format-configurations)
10. [Logging & UI Configurations](#10-logging--ui-configurations)
11. [Network & RPC Configurations](#11-network--rpc-configurations)
12. [Arrow & Pandas Configurations](#12-arrow--pandas-configurations)

---

## How to Set Configurations

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.sql.shuffle.partitions", 200) \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# Or at runtime
spark.conf.set("spark.sql.shuffle.partitions", 100)

# Read a config value
value = spark.conf.get("spark.sql.shuffle.partitions")
```

---

## 1. SQL & Shuffle Configurations

---

### `spark.sql.shuffle.partitions`

| Property        | Value             |
|----------------|-------------------|
| **Default**    | `200`             |
| **Type**       | Integer           |

**What it is:**  
Controls the number of partitions used when shuffling data for joins and aggregations in Spark SQL / DataFrame operations.

**Why it's used:**  
- The default of `200` is often **too high** for small datasets (leads to tiny files and overhead) or **too low** for large datasets (causes OOM errors or slow performance).  
- Tune it based on the size of your data. A common rule of thumb: aim for partition sizes of **100MB–200MB**.  
- For small datasets, setting it to `4` or `8` can dramatically speed up jobs.

```python
spark.conf.set("spark.sql.shuffle.partitions", 50)
```

---

### `spark.default.parallelism`

| Property        | Value             |
|----------------|-------------------|
| **Default**    | Largest number of partitions in a parent RDD (for transformations), or `2 * number of cores` for others |
| **Type**       | Integer           |

**What it is:**  
Sets the default number of partitions for RDD operations like `reduceByKey`, `join`, `parallelize` when not explicitly set by the user.

**Why it's used:**  
- Affects low-level RDD API operations (not DataFrame/SQL which uses `spark.sql.shuffle.partitions`).
- Increasing it allows more parallelism and better resource utilization across the cluster.

```python
spark.conf.set("spark.default.parallelism", 100)
```

---

### `spark.sql.autoBroadcastJoinThreshold`

| Property        | Value              |
|----------------|--------------------|
| **Default**    | `10485760` (10 MB) |
| **Type**       | Long (bytes)       |

**What it is:**  
Configures the maximum size in bytes of a table that will be broadcast to all worker nodes when performing a join. Set to `-1` to disable broadcasting.

**Why it's used:**  
- **Broadcast joins** avoid shuffling the large table by sending the smaller table to every executor.
- Very effective when one side of the join is small (e.g., a lookup/dimension table).
- Increases the threshold if you have small-ish tables that are still above 10MB but safe to broadcast.

```python
# Allow tables up to 50MB to be broadcast
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 50 * 1024 * 1024)

# Disable broadcasting entirely
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)
```

---

### `spark.sql.files.maxPartitionBytes`

| Property        | Value                        |
|----------------|------------------------------|
| **Default**    | `134217728` (128 MB)         |
| **Type**       | Long (bytes)                 |

**What it is:**  
The maximum number of bytes to pack into a single partition when reading files.

**Why it's used:**  
- Controls the granularity of file reads. A smaller value creates more partitions (more parallelism), a larger value creates fewer.
- Useful to tune when working with large Parquet/ORC files to control task sizes.

```python
spark.conf.set("spark.sql.files.maxPartitionBytes", 256 * 1024 * 1024)  # 256 MB
```

---

### `spark.sql.files.openCostInBytes`

| Property        | Value                  |
|----------------|------------------------|
| **Default**    | `4194304` (4 MB)       |
| **Type**       | Long (bytes)           |

**What it is:**  
The estimated cost to open a file, measured in bytes. Used to pack multiple small files into the same partition.

**Why it's used:**  
- Helps avoid the **small files problem**. If you have thousands of small files, Spark can merge them into fewer partitions based on this cost estimate.
- Increase this value to encourage Spark to merge more small files together.

```python
spark.conf.set("spark.sql.files.openCostInBytes", 8 * 1024 * 1024)  # 8 MB
```

---

## 2. Memory Configurations

---

### `spark.executor.memory`

| Property        | Value   |
|----------------|---------|
| **Default**    | `1g`    |
| **Type**       | String  |

**What it is:**  
Amount of memory to use per executor process (e.g., `2g`, `4g`, `8g`).

**Why it's used:**  
- One of the most critical configs. Insufficient executor memory leads to OOM (Out of Memory) errors and excessive disk spills.
- Should be sized based on the data volume each executor handles.

```python
# Set at SparkSession creation
spark = SparkSession.builder.config("spark.executor.memory", "4g").getOrCreate()
```

---

### `spark.driver.memory`

| Property        | Value   |
|----------------|---------|
| **Default**    | `1g`    |
| **Type**       | String  |

**What it is:**  
Amount of memory to allocate for the Spark driver process.

**Why it's used:**  
- The driver collects results from executors. If you do `.collect()` or use large broadcast variables, the driver needs enough memory.
- Increase this when you are pulling large datasets back to the driver or using `toPandas()`.

```python
spark = SparkSession.builder.config("spark.driver.memory", "4g").getOrCreate()
```

---

### `spark.memory.fraction`

| Property        | Value   |
|----------------|---------|
| **Default**    | `0.6`   |
| **Type**       | Double  |

**What it is:**  
Fraction of the total JVM heap space that is used for Spark execution and storage. The rest is reserved for user data structures, internal Spark metadata, and safeguarding against OOM errors.

**Why it's used:**  
- Controls how much of executor heap Spark can use for caching and computation.
- Decreasing it leaves more memory for your own UDFs or Java objects but may cause more disk spills.

```python
spark.conf.set("spark.memory.fraction", 0.7)
```

---

### `spark.memory.storageFraction`

| Property        | Value   |
|----------------|---------|
| **Default**    | `0.5`   |
| **Type**       | Double  |

**What it is:**  
Within `spark.memory.fraction`, this is the fraction dedicated to **storage (caching)**. The remainder is for execution (shuffles, sorts, joins).

**Why it's used:**  
- If your job caches a lot of data, increase this to protect cached data from being evicted.
- If your job is computation-heavy (lots of joins/aggregations) with little caching, reduce it to give more space to execution.

```python
spark.conf.set("spark.memory.storageFraction", 0.4)
```

---

### `spark.executor.memoryOverhead`

| Property        | Value                                      |
|----------------|--------------------------------------------|
| **Default**    | `executorMemory * 0.1`, minimum `384 MB`   |
| **Type**       | Long (MB)                                  |

**What it is:**  
Amount of off-heap memory (in MB) to be allocated per executor. This is for JVM overhead, interned strings, native libraries, etc.

**Why it's used:**  
- When running PySpark (Python processes), or using native libraries, or doing very large shuffles, the off-heap memory can be exhausted, killing the container.
- Always increase this when you see `Container killed by YARN for exceeding memory limits` errors.

```python
spark.conf.set("spark.executor.memoryOverhead", "1g")
```

---

### `spark.driver.memoryOverhead`

| Property        | Value                                    |
|----------------|------------------------------------------|
| **Default**    | `driverMemory * 0.1`, minimum `384 MB`   |
| **Type**       | Long (MB)                                |

**What it is:**  
Off-heap memory allocated to the driver process.

**Why it's used:**  
- Same as executor overhead but for the driver. Increase when the driver is doing heavy Python-side operations.

```python
spark.conf.set("spark.driver.memoryOverhead", "512m")
```

---

## 3. Executor & Core Configurations

---

### `spark.executor.cores`

| Property        | Value   |
|----------------|---------|
| **Default**    | `1` (YARN/K8s), all available (Standalone) |
| **Type**       | Integer |

**What it is:**  
Number of CPU cores to use for each executor.

**Why it's used:**  
- More cores = more tasks run concurrently per executor.
- Recommended sweet spot is **4–5 cores per executor** to balance parallelism without too much HDFS contention.
- Too many cores per executor (e.g., 10+) can cause HDFS throughput issues.

```python
spark = SparkSession.builder.config("spark.executor.cores", 4).getOrCreate()
```

---

### `spark.executor.instances`

| Property        | Value   |
|----------------|---------|
| **Default**    | `2`     |
| **Type**       | Integer |

**What it is:**  
Number of executor instances to launch (only relevant when dynamic allocation is disabled).

**Why it's used:**  
- Fixed number of executors for your application.
- More executors = more parallelism = faster jobs (up to a point).
- Balance with available cluster resources.

```python
spark = SparkSession.builder.config("spark.executor.instances", 10).getOrCreate()
```

---

### `spark.driver.cores`

| Property        | Value   |
|----------------|---------|
| **Default**    | `1`     |
| **Type**       | Integer |

**What it is:**  
Number of CPU cores to use for the driver process.

**Why it's used:**  
- Needed when the driver has to handle heavy parallel work (e.g., `collect()` on a large DataFrame, complex Python post-processing).

```python
spark = SparkSession.builder.config("spark.driver.cores", 2).getOrCreate()
```

---

## 4. Storage & Persistence Configurations

---

### `spark.storage.level` *(set per RDD/DataFrame, not globally)*

**What it is:**  
Defines how a cached RDD or DataFrame is stored. Common values:

| Level                    | Meaning                                  |
|--------------------------|------------------------------------------|
| `MEMORY_ONLY`            | Store as deserialized Java objects in JVM heap |
| `MEMORY_AND_DISK`        | Spill to disk if not enough memory       |
| `MEMORY_ONLY_SER`        | Serialized Java objects (more space-efficient) |
| `MEMORY_AND_DISK_SER`    | Serialized, spills to disk if needed     |
| `DISK_ONLY`              | Store only on disk                       |
| `MEMORY_ONLY_2`          | Replicated on 2 nodes                   |

**Why it's used:**  
- Choose based on memory availability and how expensive it is to recompute the dataset.
- `MEMORY_AND_DISK` is the safest default for large datasets.

```python
from pyspark import StorageLevel

df.persist(StorageLevel.MEMORY_AND_DISK)
```

---

### `spark.local.dir`

| Property        | Value          |
|----------------|----------------|
| **Default**    | `/tmp`         |
| **Type**       | String (path)  |

**What it is:**  
Directory to use for "scratch" space in Spark — shuffle maps, intermediate results, and spills to disk.

**Why it's used:**  
- `/tmp` is often on the root disk which may be small. Point this to a faster or larger disk to avoid disk I/O bottlenecks during heavy shuffles.

```python
spark = SparkSession.builder.config("spark.local.dir", "/data/spark-tmp").getOrCreate()
```

---

## 5. Adaptive Query Execution (AQE)

> AQE is available from Spark 3.0+ and can dynamically optimize query plans at runtime.

---

### `spark.sql.adaptive.enabled`

| Property        | Value    |
|----------------|----------|
| **Default**    | `true` (Spark 3.2+), `false` (Spark 3.0–3.1) |
| **Type**       | Boolean  |

**What it is:**  
Enables **Adaptive Query Execution**, which re-optimizes the query plan based on runtime statistics.

**Why it's used:**  
- Automatically handles skewed joins, coalesces small shuffle partitions, and picks better join strategies at runtime.
- **Should almost always be enabled** in Spark 3+.

```python
spark.conf.set("spark.sql.adaptive.enabled", True)
```

---

### `spark.sql.adaptive.coalescePartitions.enabled`

| Property        | Value   |
|----------------|---------|
| **Default**    | `true`  |
| **Type**       | Boolean |

**What it is:**  
When AQE is enabled, this automatically coalesces small shuffle partitions into larger ones after the shuffle.

**Why it's used:**  
- Avoids the issue of having thousands of tiny shuffle partitions when `spark.sql.shuffle.partitions` is set high.
- Reduces task scheduling overhead and improves performance.

```python
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", True)
```

---

### `spark.sql.adaptive.coalescePartitions.minPartitionSize`

| Property        | Value                  |
|----------------|------------------------|
| **Default**    | `1048576` (1 MB)       |
| **Type**       | Long (bytes)           |

**What it is:**  
The minimum size of a coalesced partition when using AQE partition coalescing.

**Why it's used:**  
- Prevents AQE from creating partitions that are too small.
- Increase this if you still see too many small tasks after coalescing.

```python
spark.conf.set("spark.sql.adaptive.coalescePartitions.minPartitionSize", "20mb")
```

---

### `spark.sql.adaptive.advisoryPartitionSizeInBytes`

| Property        | Value                   |
|----------------|-------------------------|
| **Default**    | `67108864` (64 MB)      |
| **Type**       | Long (bytes)            |

**What it is:**  
The advisory size (target size) for each partition when AQE coalesces shuffle partitions or splits skewed partitions.

**Why it's used:**  
- AQE tries to make partitions approximately this size.
- Increase for larger clusters or larger datasets for more efficient processing.

```python
spark.conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes", "128mb")
```

---

### `spark.sql.adaptive.skewJoin.enabled`

| Property        | Value   |
|----------------|---------|
| **Default**    | `true`  |
| **Type**       | Boolean |

**What it is:**  
Enables automatic handling of **skewed joins** in AQE by splitting skewed partitions into smaller sub-partitions.

**Why it's used:**  
- Data skew is one of the most common causes of slow Spark jobs (one task taking 100x longer than others).
- With this enabled, Spark auto-detects and mitigates skew at runtime without any manual intervention.

```python
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", True)
```

---

### `spark.sql.adaptive.skewJoin.skewedPartitionFactor`

| Property        | Value   |
|----------------|---------|
| **Default**    | `5`     |
| **Type**       | Double  |

**What it is:**  
A partition is considered skewed if its size is larger than this factor multiplied by the median partition size.

**Why it's used:**  
- Lower the value to be more aggressive in treating partitions as skewed.
- Raise it if AQE is splitting too many partitions unnecessarily.

```python
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionFactor", 3)
```

---

## 6. Join Configurations

---

### `spark.sql.join.preferSortMergeJoin`

| Property        | Value   |
|----------------|---------|
| **Default**    | `true`  |
| **Type**       : Boolean |

**What it is:**  
Prefers sort-merge join over shuffle-hash join when applicable.

**Why it's used:**  
- Sort-merge join is more memory-stable for very large datasets.
- Disable it to allow Spark to choose shuffle-hash joins for medium-sized tables (can be faster when data fits in memory).

```python
spark.conf.set("spark.sql.join.preferSortMergeJoin", False)
```

---

### `spark.sql.broadcastTimeout`

| Property        | Value     |
|----------------|-----------|
| **Default**    | `300` (seconds) |
| **Type**       | Long      |

**What it is:**  
Timeout in seconds for the broadcast wait time in broadcast joins.

**Why it's used:**  
- If broadcasting a large table takes too long, Spark times out and fails the query.
- Increase this on slow networks or when broadcasting larger-than-default tables.

```python
spark.conf.set("spark.sql.broadcastTimeout", 600)
```

---

## 7. Serialization Configurations

---

### `spark.serializer`

| Property        | Value                                              |
|----------------|----------------------------------------------------|
| **Default**    | `org.apache.spark.serializer.JavaSerializer`       |
| **Type**       | String (class name)                                |

**What it is:**  
The serializer used for shuffling data between nodes and for caching RDDs.

**Why it's used:**  
- The default Java serializer is slow and produces large output.
- **Kryo serializer** (`org.apache.spark.serializer.KryoSerializer`) is significantly faster and more compact.
- Always set to Kryo for production jobs.

```python
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

---

### `spark.kryo.registrationRequired`

| Property        | Value   |
|----------------|---------|
| **Default**    | `false` |
| **Type**       | Boolean |

**What it is:**  
If set to `true`, Kryo will throw an error when encountering an unregistered class.

**Why it's used:**  
- Registering classes with Kryo gives better performance than relying on dynamic class detection.
- Set to `true` in performance-critical production environments to enforce registration.

```python
spark.conf.set("spark.kryo.registrationRequired", True)
```

---

### `spark.kryoserializer.buffer.max`

| Property        | Value   |
|----------------|---------|
| **Default**    | `64m`   |
| **Type**       | String  |

**What it is:**  
Maximum allowable size of Kryo serialization buffer. Must be larger than the largest object you need to serialize.

**Why it's used:**  
- Increase this if you get `Buffer overflow` errors from Kryo when serializing large objects.

```python
spark.conf.set("spark.kryoserializer.buffer.max", "256m")
```

---

## 8. Dynamic Allocation Configurations

---

### `spark.dynamicAllocation.enabled`

| Property        | Value   |
|----------------|---------|
| **Default**    | `false` |
| **Type**       | Boolean |

**What it is:**  
Enables dynamic allocation of executors — Spark automatically scales the number of executors up and down based on workload.

**Why it's used:**  
- Prevents resource waste in a shared cluster. Executors are added when the queue of pending tasks grows and removed when idle.
- Ideal for long-running Spark applications with varying workloads.

```python
spark.conf.set("spark.dynamicAllocation.enabled", True)
```

---

### `spark.dynamicAllocation.minExecutors`

| Property        | Value   |
|----------------|---------|
| **Default**    | `0`     |
| **Type**       | Integer |

**What it is:**  
Minimum number of executors to keep alive when dynamic allocation is enabled.

**Why it's used:**  
- Ensures there are always some executors ready to avoid cold-start latency.

```python
spark.conf.set("spark.dynamicAllocation.minExecutors", 2)
```

---

### `spark.dynamicAllocation.maxExecutors`

| Property        | Value      |
|----------------|------------|
| **Default**    | `infinity` |
| **Type**       | Integer    |

**What it is:**  
Maximum number of executors to allocate when dynamic allocation is enabled.

**Why it's used:**  
- Caps resource usage to prevent a single job from monopolizing the cluster.

```python
spark.conf.set("spark.dynamicAllocation.maxExecutors", 50)
```

---

### `spark.dynamicAllocation.executorIdleTimeout`

| Property        | Value   |
|----------------|---------|
| **Default**    | `60s`   |
| **Type**       | String  |

**What it is:**  
Duration for which an executor can be idle before it is removed.

**Why it's used:**  
- Frees up cluster resources when executors are no longer needed.
- Decrease for aggressive resource release; increase for workloads with frequent bursts.

```python
spark.conf.set("spark.dynamicAllocation.executorIdleTimeout", "120s")
```

---

## 9. I/O & File Format Configurations

---

### `spark.sql.parquet.compression.codec`

| Property        | Value     |
|----------------|-----------|
| **Default**    | `snappy`  |
| **Type**       | String    |

**What it is:**  
Compression codec to use when writing Parquet files. Options: `none`, `snappy`, `gzip`, `lzo`, `brotli`, `lz4`, `zstd`.

**Why it's used:**  
- `snappy` is fast but less compressed.
- `gzip` gives better compression but is slower.
- `zstd` is the best balance of speed and compression ratio (recommended for modern setups).

```python
spark.conf.set("spark.sql.parquet.compression.codec", "zstd")
```

---

### `spark.sql.parquet.mergeSchema`

| Property        | Value   |
|----------------|---------|
| **Default**    | `false` |
| **Type**       | Boolean |

**What it is:**  
When `true`, Spark merges schemas collected from all Parquet files in a directory.

**Why it's used:**  
- Useful when reading Parquet files that were written at different times and may have evolved schemas (new columns added over time).
- Keep it `false` unless needed, as it adds overhead (requires reading all file footers).

```python
spark.conf.set("spark.sql.parquet.mergeSchema", True)
```

---

### `spark.sql.orc.compression.codec`

| Property        | Value     |
|----------------|-----------|
| **Default**    | `snappy`  |
| **Type**       | String    |

**What it is:**  
Compression codec used when writing ORC files. Options: `none`, `snappy`, `zlib`, `lzo`, `zstd`.

**Why it's used:**  
- Same reasoning as Parquet compression. ORC is commonly used in Hive-based ecosystems.

```python
spark.conf.set("spark.sql.orc.compression.codec", "zstd")
```

---

### `spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version`

| Property        | Value   |
|----------------|---------|
| **Default**    | `1`     |
| **Type**       | Integer |

**What it is:**  
Algorithm version for the Hadoop file output committer. Version `2` is faster as it moves individual task outputs directly to the final location rather than staging everything first.

**Why it's used:**  
- Version `2` significantly reduces the time to commit large jobs with many output files.
- Use `2` unless you need the safer commit semantics of version `1`.

```python
spark.conf.set("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
```

---

## 10. Logging & UI Configurations

---

### `spark.eventLog.enabled`

| Property        | Value   |
|----------------|---------|
| **Default**    | `false` |
| **Type**       | Boolean |

**What it is:**  
Enables logging of Spark events to a directory, which can be replayed in the Spark History Server.

**Why it's used:**  
- Critical for post-mortem debugging and performance analysis after a job finishes.
- Without it, the Spark UI disappears when the application ends.

```python
spark.conf.set("spark.eventLog.enabled", True)
spark.conf.set("spark.eventLog.dir", "hdfs:///spark-logs")
```

---

### `spark.ui.port`

| Property        | Value   |
|----------------|---------|
| **Default**    | `4040`  |
| **Type**       | Integer |

**What it is:**  
Port on which the Spark Web UI is served.

**Why it's used:**  
- Change when port `4040` is already in use (Spark auto-increments to `4041`, `4042`, etc. but you can fix it explicitly).

```python
spark.conf.set("spark.ui.port", 4050)
```

---

### `spark.ui.showConsoleProgress`

| Property        | Value   |
|----------------|---------|
| **Default**    | `true`  |
| **Type**       | Boolean |

**What it is:**  
Shows a progress bar in the console for each stage.

**Why it's used:**  
- Disable in production logs to reduce noise.

```python
spark.conf.set("spark.ui.showConsoleProgress", False)
```

---

## 11. Network & RPC Configurations

---

### `spark.network.timeout`

| Property        | Value   |
|----------------|---------|
| **Default**    | `120s`  |
| **Type**       | String  |

**What it is:**  
Default timeout for all network interactions (fetch retries, heartbeats, etc.).

**Why it's used:**  
- Increase this for jobs on slow networks or when executors do GC pauses that cause missed heartbeats.
- Helps prevent jobs from failing due to transient network issues.

```python
spark.conf.set("spark.network.timeout", "600s")
```

---

### `spark.rpc.message.maxSize`

| Property        | Value   |
|----------------|---------|
| **Default**    | `128` (MB) |
| **Type**       | Integer |

**What it is:**  
Maximum message size (in MB) to allow in "control plane" communication. Large broadcast variables or task results can exceed the default.

**Why it's used:**  
- Increase if you get `RPC message too large` errors, often caused by sending large broadcast variables or large task result objects.

```python
spark.conf.set("spark.rpc.message.maxSize", 512)
```

---

### `spark.task.maxFailures`

| Property        | Value   |
|----------------|---------|
| **Default**    | `4`     |
| **Type**       | Integer |

**What it is:**  
Number of times to retry a task before giving up and failing the job.

**Why it's used:**  
- Increases fault tolerance for flaky nodes or transient errors.
- For very large long-running jobs, increase this to avoid the entire job failing due to a single bad node.

```python
spark.conf.set("spark.task.maxFailures", 8)
```

---

## 12. Arrow & Pandas Configurations

---

### `spark.sql.execution.arrow.pyspark.enabled`

| Property        | Value   |
|----------------|---------|
| **Default**    | `false` |
| **Type**       | Boolean |

**What it is:**  
Enables Apache Arrow for data transfers between JVM (Spark) and Python (Pandas). Used by `toPandas()` and `createDataFrame()` from Pandas.

**Why it's used:**  
- **Massively speeds up** `toPandas()` and `createDataFrame()` conversions — often 10–100x faster than the default row-by-row serialization.
- Always enable this in PySpark workloads where you convert between Spark DataFrames and Pandas DataFrames.

```python
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", True)
```

---

### `spark.sql.execution.arrow.pyspark.fallback.enabled`

| Property        | Value   |
|----------------|---------|
| **Default**    | `true`  |
| **Type**       | Boolean |

**What it is:**  
If Arrow conversion fails (e.g., due to unsupported data types), fall back to the default non-Arrow method.

**Why it's used:**  
- Provides safety net when using Arrow. If you encounter Arrow errors, Spark silently falls back rather than failing.
- Set to `false` in strict environments where you want to catch Arrow incompatibilities explicitly.

```python
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled", True)
```

---

### `spark.sql.execution.arrow.maxRecordsPerBatch`

| Property        | Value   |
|----------------|---------|
| **Default**    | `10000` |
| **Type**       | Integer |

**What it is:**  
Maximum number of records per Arrow batch when converting Spark DataFrames to Pandas.

**Why it's used:**  
- Controls the memory footprint of Arrow batches.
- Reduce this if you hit OOM errors during `toPandas()` conversions.
- Increase for throughput on large, memory-safe environments.

```python
spark.conf.set("spark.sql.execution.arrow.maxRecordsPerBatch", 50000)
```

---

## Quick Reference Summary Table

| Configuration | Default | Key Use Case |
|---|---|---|
| `spark.sql.shuffle.partitions` | `200` | Tune partition count for shuffles |
| `spark.default.parallelism` | 2x cores | RDD-level parallelism |
| `spark.executor.memory` | `1g` | Executor heap memory |
| `spark.driver.memory` | `1g` | Driver heap memory |
| `spark.executor.cores` | `1` | CPU cores per executor |
| `spark.executor.instances` | `2` | Fixed executor count |
| `spark.executor.memoryOverhead` | 10% | Off-heap / Python overhead |
| `spark.sql.autoBroadcastJoinThreshold` | `10MB` | Broadcast join threshold |
| `spark.sql.adaptive.enabled` | `true` (3.2+) | Enable AQE |
| `spark.sql.adaptive.skewJoin.enabled` | `true` | Auto handle data skew |
| `spark.serializer` | Java | Use Kryo for speed |
| `spark.dynamicAllocation.enabled` | `false` | Auto-scale executors |
| `spark.sql.parquet.compression.codec` | `snappy` | Parquet compression |
| `spark.sql.execution.arrow.pyspark.enabled` | `false` | Fast Pandas conversion |
| `spark.network.timeout` | `120s` | Prevent timeout failures |
| `spark.local.dir` | `/tmp` | Scratch disk location |

---

*Generated for Apache Spark 3.x / PySpark. Some defaults may vary across Spark versions and cluster managers (YARN, Kubernetes, Standalone).*
