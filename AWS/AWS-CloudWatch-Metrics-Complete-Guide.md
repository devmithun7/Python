# AWS CloudWatch Metrics - Complete Guide (Data Engineer Focus)

AWS CloudWatch Metrics is a time-series monitoring service that collects, stores, and visualizes metric data from AWS services, applications, and custom sources. It enables operational visibility, alerting, and near real-time analytics for infrastructure and data pipelines.

---

## What CloudWatch Metrics Provides

- **Time-series storage** for metrics from AWS services and custom applications
- **Aggregation** across dimensions (for example, by cluster, service, or job)
- **Alarms** and **automated actions** based on thresholds or expressions
- **Streaming** metrics to AWS and third-party destinations via Metric Streams

---

## Core Concepts

### Namespaces
A **namespace** is a logical container for metrics. It can represent:
- An **individual AWS service** (for example, `AWS/EC2`, `AWS/Glue`)
- A **collection of related metrics** (for example, `Custom/DataPipelines`)

**Best practice**: Use clear custom namespaces for your own metrics to avoid collision with AWS namespaces.

### Metrics, Timestamps, and Resolution
- **Metric**: A single time-series (for example, `CPUUtilization`)
- **Timestamp**: The time a metric datapoint represents
- **Resolution**:
  - **Standard**: 60-second granularity
  - **High-resolution**: 1-second granularity (use for rapid changes)

### Dimensions
**Dimensions** are key-value pairs that identify a time-series more precisely.

Examples:
- `ClusterName=etl-prod`
- `JobName=orders_daily`
- `ExecutorId=7`

A metric with different dimension values becomes **distinct time-series**.

### Period
The **period** is the time window (in seconds) used to aggregate datapoints.

Common values:
- `60` (1 minute)
- `300` (5 minutes)
- `900` (15 minutes)

### Statistics
Statistics define how datapoints are aggregated:
- `Average`
- `Sum`
- `Minimum`
- `Maximum`
- `SampleCount`
- `p90`, `p95`, `p99` (percentiles)

---

## Data Engineer Focus: Key Metrics and Definitions

### ETL and Data Movement Metrics
- **BytesProcessed / BytesRead / BytesWritten**: Volume of data read/written during ETL.
- **DataShuffleBytes**: Total bytes exchanged between executors or stages.
- **RecordsProcessed / RecordsPerSecond**: Throughput of pipeline processing.
- **JobDuration / StageDuration**: Time spent in ETL job or specific stage.

### Compute and Resource Metrics
- **CPUUtilization**: Percentage CPU used on workers.
- **MemoryUtilization**: Memory usage across executors.
- **DiskIOPS / DiskThroughput**: Disk read/write rates.
- **NetworkIn / NetworkOut**: Data transferred over the network.

### Reliability and Quality Metrics
- **FailedRecords / ErrorCount**: Number of errors or failed records.
- **RetryCount**: How many retries occurred during processing.
- **QueueDepth / Backlog**: Pending work or queued tasks.
- **Lag / Freshness**: Delay between source data and processed output.

### Query and Warehouse Metrics (Common for Data Platforms)
- **QueryLatency**: Time taken per query.
- **QueryFailures**: Failed queries in analytics workloads.
- **Concurrency / ActiveSessions**: Workload pressure on engines.

---

## Metric Streams

### What It Is
**CloudWatch Metric Streams** continuously stream metrics **near real time** to AWS and third-party destinations.

### Why It Matters
- Low-latency monitoring
- Centralized observability
- Integration with external tooling

### Destinations
- **Amazon Kinesis Data Firehose**
- **Amazon Kinesis Data Streams**
- **Amazon S3**
- **Amazon Redshift**
- **Amazon OpenSearch Service**

#### What Is Amazon OpenSearch Service?
A fully managed service for **search, log analytics, and real-time observability** based on the OpenSearch engine. It is commonly used for indexing and querying large volumes of metrics and logs.

---

## CloudWatch Alarms

### Alarm Types
- **Metric Alarm**: Monitors a single metric (or a math expression on metrics).
- **Composite Alarm**: Monitors the **state of other alarms**.

### Alarm States
- **OK**: The metric or expression is within threshold.
- **ALARM**: The metric or expression is outside threshold.
- **INSUFFICIENT_DATA**: Not enough data to determine state.

### Alarm Actions
- **Amazon SNS**: Send notifications to topics (email, SMS, webhooks).
- **EC2 Actions**: Stop, reboot, or terminate instances.
- **Auto Scaling**: Adjust instance count based on load.
- **Lambda**: Execute a function for automated remediation.
- **Incident Management**: Create high-urgency requests (for example, via AWS Systems Manager Incident Manager).

---

## How to Create a CloudWatch Alarm (Typical Workflow)

### Step 1 - Specify Metric and Condition
- Select **metric name** and **namespace**
- Apply **dimensions** (for example, `WorkGroup`, `QueryState`)
- Choose **statistic** (for example, `Average` or `Sum`)
- Set **period** (for example, 5 minutes)
- Define **threshold** and **comparison**

### Step 2 - Configure Actions
- Select an **SNS topic** or create a new one
- Add **email endpoints** or other subscribers
- Optionally add **Auto Scaling** or **EC2 actions**

### Step 3 - Name and Describe
- Provide **alarm name** and **description**
- Review **preview** and create the alarm

---

## Image-Based Flows (From Slides)

### 1) CloudWatch Logs - High-Level Purpose
**Flow**
```
AWS services and apps
  -> CloudWatch Logs
      -> Centralized logging in one place
      -> Near real-time monitoring of log data
```

**Explanation**: CloudWatch Logs collects and consolidates logs from multiple sources so you can monitor them in one location.

---

### 2) CloudWatch Logs - Core Concepts
**Flow**
```
Log group
  -> contains log streams
      -> each stream is a sequence of log events from one source
          -> each event is a single log record with timestamp/message
```

**Key points**
- **Log groups**: logical containers for related log streams.
- **Log streams**: ordered events from a single source (for example, one instance).
- **Log events**: individual log records.
- **Retention policy**: controls how long logs are stored.
- **Logs Insights**: interactive query and visualization tool.
- **Exports**: send logs to S3, Kinesis Data Streams/Firehose, or Lambda.

---

### 3) Log Filtering and Subscription
**Flow**
```
CloudWatch Logs
  -> Metric filter (extract patterns -> custom metrics)
  -> Subscription filter (near real-time streaming)
      -> Kinesis Data Streams or Kinesis Data Firehose
```

**Explanation**
- **Metric filter**: extracts data from logs to create custom metrics.
- **Subscription filter**: streams matching log events to other services.

---

### 4) Cross-Account Access for Log Streaming
**Flow**
```
Source account
  CloudWatch Logs
    -> Subscription filter
        -> Assume role in destination account
            -> Kinesis Data Streams (destination)
                -> Data consumers
```

**Steps**
1. Create Kinesis Data Stream in the destination account.
2. Create an IAM role + trust policy in the destination account.
3. Create the subscription filter in the source account.

---

### 5) CloudWatch Logs Agent (Why and When)
**Flow**
```
EC2 or on-prem server
  -> CloudWatch Logs agent
      -> CloudWatch Logs
```

**Explanation**: EC2 or on-prem servers do not send logs automatically. The agent collects and streams logs in near real time.

---

### 6) Agent Types (Legacy vs Unified)
**Flow**
```
Logs Agent (legacy)
  -> collects logs only

Unified CloudWatch Agent (recommended)
  -> collects logs + system metrics
      (CPU, RAM, disk, network, swap)
```

**Note**: AWS generally recommends the **Unified CloudWatch Agent** for broader telemetry.

---

## Additional Notes and Best Practices

- Prefer **standard resolution** unless you need sub-minute visibility.
- Use **dimensions** to isolate specific jobs, clusters, or stages.
- Keep **period** aligned with data freshness requirements.
- Use **composite alarms** for noisy environments.
- Stream metrics to **OpenSearch** or **S3** for long-term analytics.
- Document metric definitions in a shared catalog.

---

## Quick Glossary

- **Namespace**: Logical container for metrics
- **Dimension**: Key-value identifier that defines a unique time-series
- **Resolution**: Granularity of metric datapoints
- **Period**: Aggregation window for statistics
- **Statistic**: Aggregation method (average, sum, etc.)
- **Alarm**: Rule that changes state and triggers actions

---

## End

This guide summarizes CloudWatch Metrics with a data engineering lens, including streams, alarms, and operational best practices.
