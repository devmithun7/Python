# AWS CloudWatch Logs - Complete Guide (Data Engineer Focus)

AWS CloudWatch Logs collects, stores, and analyzes log data from AWS services and applications. It helps you centralize troubleshooting, operational monitoring, security analysis, and data pipeline observability.

---

## Ways to View Logs

### 1) View Logs by Resource (Most Common)
**Example**: AWS Glue ETL job
- Open the Glue job in the console
- Go to **Runs**
- Select a run to view **continuous logs** or **driver/executor logs**

**Why it matters**: You see logs in the context of the specific job run. This is the fastest way to debug failures, executor issues, or performance bottlenecks.

### 2) View Logs by Log Group
- Go to CloudWatch Logs
- Browse **Log groups** and **Log streams**

**Use case**: When you want to inspect logs across multiple services or look at all runs of a workload in one view.

### 3) Log Insights (Query Logs)
CloudWatch Logs Insights provides SQL-like queries for searching and aggregating log data.

**Example use case**: Find the top 10 Glue errors in the last 2 hours.

```sql
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 10
```

### 4) Log Tail (Live Streaming)
**Log tail** lets you stream log events in near real time from a selected log group or log stream.

**Use case**: Watch a Glue job or Lambda function live during a deployment or test run to spot errors immediately.

---

## Core CloudWatch Logs Concepts

### Log Groups
Logical containers that hold related log streams.

**Example**: `/aws-glue/jobs/output` groups logs for Glue jobs.

**Typical design**: One log group per service and environment, such as:
- `/aws/glue/prod`
- `/aws/athena/query-events`

### Log Streams
Sequences of log events from a single source.

**Example**: A single Glue job run, a single Lambda invocation stream, or a single EC2 instance.

### Log Events
Individual log records with timestamp and message.

**Example**: `2026-02-08T12:01:43Z Job failed due to missing input data.`

### Retention Policy
Controls how long logs are stored before automatic deletion.

**Example**: Keep ETL logs for 30 days in dev, 180 days in prod to balance cost and audit needs.

### Log Insights
Query and visualize log data. It supports filters, parsing, stats, and time-based analysis.

**Example use cases**
- Count failed queries by workgroup
- Track long-running Spark stages
- Identify top error messages in the last 24 hours

### Log Anomalies
Detects unusual log patterns automatically using statistical baselines.

**Example**: A sudden spike in `OutOfMemoryError` or `ExecutorLostFailure` messages in Spark jobs.

---

## Log Filtering and Subscriptions

### Metric Filters
Extract metrics from log patterns.

**Use case**: Count `ERROR` lines per minute and create an alarm when error rate exceeds a threshold.

### Subscription Filters
Stream log events to other services in near real time.

**Use case**: Send ETL errors to Kinesis Data Firehose for long-term storage or to a SIEM pipeline.

---

## Athena Logs and EventBridge (Manual Setup)

Some services (for example, Athena) do not automatically push query logs to CloudWatch Logs. You can capture Athena events using EventBridge and route them to a CloudWatch Log Group.

### Step 1 - Create a Log Group
Create a log group such as: `/aws/athena/query-events`

### Step 2 - Create a New EventBridge Rule
- Go to **EventBridge**
- Create a **rule**
- Choose **Event pattern**
- Select **Service name** = `Athena`
- Choose an **event type** (see below)

### Athena Event Types (Common)
- **Query State Change**: `SUCCEEDED`, `FAILED`, `CANCELLED`, or `RUNNING`
- **Workgroup State Change**: when a workgroup is created, updated, or deleted

### Step 3 - Choose Target
Set target to the CloudWatch Log Group you created.

---

## Athena Event Patterns (Examples)

### 1) Failed Query Test (Simple)
```json
{
  "source": ["aws.athena"],
  "detail-type": ["Athena Query State Change"],
  "detail": {
    "state": ["FAILED"]
  }
}
```

**Use case**: Capture only failed queries for troubleshooting.

### 2) Data Engineer Pattern - Prod Workgroup Failures
```json
{
  "source": ["aws.athena"],
  "detail-type": ["Athena Query State Change"],
  "detail": {
    "state": ["FAILED"],
    "workGroupName": ["prod-etl"]
  }
}
```

**Use case**: Alert on failures in a production ETL workgroup.

### 3) Data Engineer Pattern - Expensive Queries
```json
{
  "source": ["aws.athena"],
  "detail-type": ["Athena Query State Change"],
  "detail": {
    "state": ["SUCCEEDED"],
    "statistics": {
      "dataScannedInBytes": [ { "numeric": [">", 100000000000] } ]
    }
  }
}
```

**Use case**: Detect queries that scan more than 100 GB.

**Note**: Adjust field names to match your account's event schema if needed.

---

## Image-Based Flows (From Slides)

### 1) CloudWatch Logs - Core Components
**Flow**
```
CloudWatch Logs
  -> Log groups (logical containers)
      -> Log streams (single source sequence)
          -> Log events (timestamp + message)
```

**What this means**
- **Log streams** are sequences of log events from a single source.
- **Log groups** are logical containers for related streams.
- **Log events** are individual records logged by applications.
- **Retention policy** defines how long logs stay in CloudWatch.
- **Log Insights** lets you query and visualize logs.
- Logs can be delivered to **S3**, **Kinesis Data Streams/Firehose**, or **Lambda**.

---

### 2) Log Filtering + Subscription
**Flow**
```
CloudWatch Logs
  -> Metric filter (extract fields -> custom metrics)
  -> Subscription filter (stream logs)
      -> Kinesis Data Streams
      -> Kinesis Data Firehose
```

**Explanation**
- Metric filters turn text logs into metrics you can alarm on.
- Subscription filters push logs to other services for processing or storage.

---

### 3) Cross-Account Log Streaming
**Flow**
```
Source account
  CloudWatch Logs
    -> Subscription filter
        -> Assume role in destination account
            -> Kinesis Data Streams (destination)
                -> Consumers / analytics
```

**Steps**
1. Create the destination Kinesis Data Stream in the target account.
2. Create IAM role + trust policy in the destination account to allow writes.
3. Create subscription filter in the source account pointing to the role and stream.

---

### 4) CloudWatch Logs Agent
**Flow**
```
EC2 / on-prem server
  -> CloudWatch Logs agent
      -> CloudWatch Logs
```

**Why it is needed**
EC2 and on-prem servers do not send logs by default. The agent collects and streams logs near real time.

---

### 5) Agent Types (Legacy vs Unified)
**Flow**
```
Logs Agent (legacy)
  -> collects logs only

Unified CloudWatch Agent (recommended)
  -> collects logs + system metrics
     (CPU, RAM, disk, network, swap)
```

**Note**: AWS generally recommends the **Unified CloudWatch Agent**.

---

## Example: End-to-End Log Flow for Data Engineering

```
ETL job (Glue/Spark/Airflow)
  -> CloudWatch Logs (log group + log streams)
      -> Log Insights (ad-hoc query and analysis)
      -> Metric filter (create error-count metric)
      -> Alarm (notify on errors)

Athena queries
  -> EventBridge rule
      -> CloudWatch Logs (athena query events)
          -> Log Insights (failed queries, long runtimes)
```

---

## Best Practices

- Use **clear log group naming** per service and environment.
- Set **retention policies** to control costs.
- Use **Log Insights** for fast ad-hoc debugging.
- Use **Metric filters** for error rates and thresholds.
- Route **Athena events** to Logs with EventBridge for auditing.
- Create **alarms** on derived metrics for SLAs.

---

## End

This guide documents CloudWatch Logs from a data engineering perspective, including log viewing paths, anomalies, Insights, and Athena EventBridge integration with example patterns.
