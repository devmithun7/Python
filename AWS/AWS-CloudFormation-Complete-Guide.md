# AWS CloudFormation - Complete Guide (All-in-One Markdown)

AWS CloudFormation is an **Infrastructure as Code (IaC)** service that lets you define, provision, and manage AWS infrastructure using **declarative templates** written in **YAML or JSON**. Instead of creating resources manually in the AWS Console, you describe the desired state of your infrastructure, and CloudFormation handles creation, updates, dependencies, and rollback.

---

## Why CloudFormation?

### Key Benefits
- **Consistency and repeatability** - Same template produces the same infrastructure every time
- **Version control** - Templates can be stored, reviewed, and versioned in Git
- **Automated dependency management** - Resources are created in the correct order
- **Safe updates** - Change Sets preview changes before they are applied
- **Automatic rollback** - Failed deployments can revert to the previous stable state
- **Drift detection** - Detects manual changes made outside CloudFormation

---

## Core Concepts

| Term | Meaning |
|----|----|
| Template | YAML/JSON file defining AWS resources |
| Stack | A deployed instance of a template |
| Change Set | Preview of changes before updating a stack |
| Drift | Difference between template and actual resources |
| Logical ID | Name used inside the template |
| Physical ID | Actual AWS resource ID |

---

## High-Level Template Structure

A CloudFormation template may contain the following top-level sections:

- `AWSTemplateFormatVersion` (optional)
- `Description` (optional)
- `Parameters` (optional)
- `Mappings` (optional)
- `Conditions` (optional)
- `Resources` (required)
- `Outputs` (optional)

---

## Complete Example Template (YAML)

This template provisions:
- A **secure S3 bucket** (optional versioning)
- An **IAM role** with scoped access to the bucket
- **Outputs** for cross-stack usage

Save as: `cloudformation-s3-iam-example.yaml`

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: >
  CloudFormation example that provisions an S3 bucket and
  an IAM role with restricted access to that bucket.

Parameters:
  EnvironmentName:
    Type: String
    Default: dev
    AllowedValues:
      - dev
      - prod
    Description: Deployment environment

  EnableVersioning:
    Type: String
    Default: "true"
    AllowedValues:
      - "true"
      - "false"
    Description: Enable S3 versioning

Conditions:
  IsProd: !Equals [!Ref EnvironmentName, prod]
  UseVersioning: !Equals [!Ref EnableVersioning, "true"]

Resources:
  AppBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "my-app-${EnvironmentName}-${AWS::AccountId}-${AWS::Region}"
      VersioningConfiguration:
        Status: !If [UseVersioning, Enabled, Suspended]
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        IgnorePublicAcls: true
        BlockPublicPolicy: true
        RestrictPublicBuckets: true
      Tags:
        - Key: environment
          Value: !Ref EnvironmentName

  AppRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub "my-app-role-${EnvironmentName}-${AWS::Region}"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Policies:
        - PolicyName: S3AccessPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Sid: ListBucket
                Effect: Allow
                Action:
                  - "s3:ListBucket"
                Resource:
                  - !GetAtt AppBucket.Arn
              - Sid: ReadWriteObjects
                Effect: Allow
                Action:
                  - "s3:GetObject"
                  - "s3:PutObject"
                  - "s3:DeleteObject"
                Resource:
                  - !Sub "${AppBucket.Arn}/*"

Outputs:
  BucketName:
    Description: Created S3 bucket name
    Value: !Ref AppBucket
    Export:
      Name: !Sub "my-app-bucket-${EnvironmentName}"

  RoleArn:
    Description: IAM Role ARN
    Value: !GetAtt AppRole.Arn
```

---

## Section-by-Section Explanation

---

## 1. AWSTemplateFormatVersion and Description

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation example template
```

**Explanation**

- Provides **informational metadata**
- Improves **readability and documentation**
- Helps teams understand template intent
- **Does not affect execution behavior**

---

## 2. Parameters (Runtime Inputs)

```yaml
Parameters:
  EnvironmentName:
    Type: String
    Default: dev
```

**Why parameters?**

- Same template works for `dev`, `staging`, `prod`
- Prevents hardcoding values
- Makes templates reusable and portable

**Common parameter types**

- `String`
- `Number`
- `List<String>`
- `AWS::EC2::KeyPair::KeyName`
- `AWS::SSM::Parameter::Value<String>`

Parameters are resolved **at stack create or update time**.

---

## 3. Conditions (If / Else Logic)

```yaml
Conditions:
  UseVersioning: !Equals [!Ref EnableVersioning, "true"]
```

Used later:

```yaml
Status: !If [UseVersioning, Enabled, Suspended]
```

**Conditions allow**

- Environment-specific behavior
- Optional resources
- Feature flags
- Cost optimization

Conditions are evaluated **before resource creation**.

---

## 4. Resources (Core of CloudFormation)

### Logical vs Physical IDs

```yaml
AppBucket:              # Logical ID
  Type: AWS::S3::Bucket # Physical resource type
```

- Logical ID is used inside the template
- Physical ID is the actual AWS resource created
- CloudFormation maps logical IDs to physical IDs

---

### S3 Bucket Resource

**Best practices included**

- Server-side encryption enabled
- Public access completely blocked
- Deterministic naming
- Environment tagging for governance and cost tracking

---

### IAM Role Resource

Two distinct policy types:

#### Trust Policy (`AssumeRolePolicyDocument`)

- Defines **who can assume** the role (for example, EC2)
- Uses `sts:AssumeRole` action

#### Permissions Policy (`Policies`)

- Defines **what the role can do**
- Scoped to the bucket and its objects

---

## 5. Outputs (Cross-Stack References)

```yaml
Outputs:
  BucketName:
    Value: !Ref AppBucket
    Export:
      Name: !Sub "my-app-bucket-${EnvironmentName}"
```

**Why outputs?**

- Share resource values across stacks
- Make values easy to discover and reuse
- Support cross-stack `ImportValue` usage

---

## 6. Mappings (Static Lookups)

```yaml
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-0abc123
    us-west-2:
      AMI: ami-0def456
```

**Use cases**

- Region-specific values
- Environment-specific defaults
- Static configuration tables

---

## 7. Intrinsic Functions (Essentials)

Common functions:

- `!Ref` - reference a parameter or resource
- `!Sub` - string interpolation
- `!GetAtt` - get resource attributes
- `!Join` - concatenate strings
- `!If`, `!Equals`, `!And`, `!Or`, `!Not` - condition logic
- `!ImportValue` - cross-stack references

Example:

```yaml
BucketName: !Sub "${ProjectName}-${AWS::Region}-${EnvironmentName}"
```

---

## 8. Pseudo Parameters

- `AWS::AccountId`
- `AWS::Region`
- `AWS::StackName`
- `AWS::Partition`

Example:

```yaml
Name: !Sub "${AWS::StackName}-role"
```

---

## 9. Change Sets (Safe Updates)

**Why use Change Sets?**

- Preview additions, modifications, deletions
- Understand replacement vs in-place changes
- Reduce deployment risk

Workflow:

1. Create Change Set
2. Review changes
3. Execute or discard

---

## 10. Stack Policies

Stack policies protect critical resources from updates:

```json
{
  "Statement" : [
    {
      "Effect" : "Deny",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "LogicalResourceId/ProductionDatabase"
    }
  ]
}
```

---

## 11. Drift Detection

**What it does**

- Detects manual changes outside CloudFormation
- Flags resources that are modified, deleted, or added

**Best practice**

- Run drift detection regularly in production
- Remediate by updating templates or reverting changes

---

## 12. Nested Stacks

Use `AWS::CloudFormation::Stack` to split large templates:

```yaml
Resources:
  NetworkStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/bucket/network.yaml
```

**Benefits**

- Reuse common building blocks
- Reduce template size and complexity
- Enable team ownership boundaries

---

## 13. StackSets (Multi-Account and Multi-Region)

Use StackSets to deploy stacks across accounts and regions:

- Centralized management
- Consistent infrastructure at scale
- Useful for security baselines and shared services

---

## 14. Template Validation

Validate before deploy:

```bash
aws cloudformation validate-template --template-body file://template.yaml
```

---

## 15. Common CloudFormation CLI Commands

```bash
# Create a stack
aws cloudformation create-stack \
  --stack-name my-stack \
  --template-body file://template.yaml \
  --parameters ParameterKey=EnvironmentName,ParameterValue=dev

# Update a stack
aws cloudformation update-stack \
  --stack-name my-stack \
  --template-body file://template.yaml \
  --parameters ParameterKey=EnvironmentName,ParameterValue=prod

# Create a change set
aws cloudformation create-change-set \
  --stack-name my-stack \
  --template-body file://template.yaml \
  --change-set-name preview-1

# Describe change set
aws cloudformation describe-change-set \
  --stack-name my-stack \
  --change-set-name preview-1

# Execute change set
aws cloudformation execute-change-set \
  --stack-name my-stack \
  --change-set-name preview-1
```

---

## 16. Best Practices

- Keep templates **small and modular** (use nested stacks)
- Use **parameters** for environment-specific values
- Apply **conditions** to avoid unnecessary resources
- Always use **Change Sets** for production updates
- Enable **termination protection** on critical stacks
- Use **stack policies** to protect key resources
- Store templates in **version control**
- Tag resources consistently

---

## 17. Troubleshooting Tips

- Check the **Events** tab in the CloudFormation console
- Use **stack rollback** to recover safely
- Inspect failed resources in the AWS service console
- Validate templates before deployment

---

## Quick Glossary

- **Template** - Blueprint describing resources
- **Stack** - A deployed instance of a template
- **Change Set** - A preview of updates
- **Drift** - Actual resources differ from template
- **Logical ID** - Template reference name
- **Physical ID** - Real AWS resource ID

---

## End

You now have a complete, single-file Markdown guide to AWS CloudFormation.
