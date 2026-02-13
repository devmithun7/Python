# AWS CloudTrail - Complete Guide (Governance Focus)

AWS CloudTrail is a **governance, risk, and compliance** service that records API activity across your AWS account. It captures who did what, when, from where, and with which parameters, enabling auditing, security analysis, and operational troubleshooting.

---

## What CloudTrail Records

CloudTrail records **API calls** and **console actions** made by users, roles, and AWS services. Events are grouped into categories:

- **Management events**: Control-plane operations for AWS resources
- **Data events**: Data-plane operations on resources like S3 objects or Lambda invocations
- **Insight events**: Unusual activity patterns based on baseline behavior

---

## CloudTrail Lake (From Slide)

### What It Is
CloudTrail Lake is a **managed data lake** for AWS user and API activity. It stores events in a queryable form so you can run SQL-like queries directly on CloudTrail data.

### Lake Channels (From Slide)
**Flow**
```
External sources
  -> Lake channel (integration)
      -> CloudTrail Lake event store

AWS services
  -> Service-linked channel
      -> CloudTrail Lake event store
```

**Explanation**
- **Integration with outside sources**: Lake channels can ingest events from external sources.
- **Service-linked channels**: AWS services create channels to send CloudTrail events to the lake.

---

## CloudTrail Extras (From Slide)

- CloudTrail enables **deep analysis** of event data (for example, over long time ranges).
- You can create **EventBridge rules** on CloudTrail events when you need real-time automation.

---

## Management Events (Control Plane)
Management events track operations that **configure** or **manage** AWS resources.

### 10 Management Event Examples
1. **CreateUser** - create an IAM user
2. **AttachRolePolicy** - attach a policy to an IAM role
3. **CreateBucket** - create an S3 bucket
4. **PutBucketPolicy** - update S3 bucket policy
5. **RunInstances** - launch EC2 instances
6. **TerminateInstances** - terminate EC2 instances
7. **CreateDBInstance** - create an RDS instance
8. **ModifyDBInstance** - change RDS instance settings
9. **CreateStack** - create a CloudFormation stack
10. **UpdateFunctionConfiguration** - update Lambda function config

**Why it matters**: These operations change infrastructure and security posture, which is critical for audits and incident response.

---

## Data Events (Data Plane)
Data events record **access to data** within resources. These are higher volume and often disabled by default.

### 10 Data Event Examples
1. **GetObject** - read an S3 object
2. **PutObject** - write an S3 object
3. **DeleteObject** - delete an S3 object
4. **ListObjectsV2** - list objects in an S3 bucket
5. **Invoke** - invoke a Lambda function
6. **GetItem** - read a DynamoDB item
7. **PutItem** - write a DynamoDB item
8. **DeleteItem** - delete a DynamoDB item
9. **Query** - query a DynamoDB table
10. **Scan** - scan a DynamoDB table

**Why it matters**: These operations are the direct evidence of data access and data movement.

---

## Insight Events
Insight events detect **unusual activity patterns** by comparing API usage to historical baselines.

### 10 Insight Event Examples
1. **Unusual API call rate** for `RunInstances`
2. **Sudden spike in CreateUser** calls
3. **Unexpected increase in AssumeRole** activity
4. **Burst of DeleteBucket** operations
5. **High volume of PutBucketPolicy** changes
6. **Anomalous ListBuckets frequency**
7. **Unusual number of StopInstances** calls
8. **Spike in UpdateFunctionCode** calls
9. **Unexpected CreateSecurityGroup pattern**
10. **Abnormal ModifyDBInstance activity**

**Why it matters**: These indicate potential compromised credentials or automation gone wrong.

---

## Trail Types

### 1) Multi-Region Trail
Records events from **all regions** in an account and stores them in a central S3 bucket.

**Use case**: Centralized auditing across a global footprint.

### 2) Single-Region Trail
Records events from **one region only**.

**Use case**: Lower cost or regulatory separation for specific regions.

### 3) Organization Trail
Records events from **all accounts in AWS Organizations**.

**Use case**: Enterprise-wide governance and compliance.

---

## Real-World Use Cases (Data Engineering Focus)

- **Who deleted a production table?**
  - Check `DeleteTable` data events in DynamoDB.
- **Why did a dataset disappear from S3?**
  - Check `DeleteObject` events by bucket and prefix.
- **Pipeline failed after config change**
  - Check management events for `UpdateJob` or `UpdateFunctionConfiguration`.
- **Detect unusual credential behavior**
  - Use insight events for spikes in API calls.

---

## CloudTrail + EventBridge (Automation)

CloudTrail can send events to EventBridge, enabling real-time automation.

**Example pattern**: Alert when a new IAM user is created.

```json
{
  "source": ["aws.iam"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventName": ["CreateUser"]
  }
}
```

**Target examples**
- Send notifications via SNS
- Trigger a Lambda for auto-remediation
- Log to CloudWatch Logs for audit

---

## Best Practices

- Enable **multi-region trails** for full coverage.
- Store logs in **centralized S3 buckets** with strict access controls.
- Enable **log file validation** for integrity.
- Turn on **data events** for sensitive buckets and tables.
- Use **CloudTrail Lake** for long-term analytics.
- Integrate with **EventBridge** for real-time alerting.

---

## End

This guide provides an in-depth CloudTrail overview with governance, trail types, and detailed examples for management, data, and insight events.
