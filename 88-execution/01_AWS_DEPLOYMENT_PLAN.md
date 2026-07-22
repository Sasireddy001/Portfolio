# Phase 1 — Live AWS Deployment Execution Plan

**Project:** Kafka → PySpark → Delta Lake Pipeline  
**Goal:** Produce real AWS evidence (screenshots, CloudWatch metrics, S3 data) that recruiters and hiring managers can verify in one minute.

---

## 1. Services to deploy

| Service | Purpose | Estimated monthly cost (dev, 4h/day) |
|---|---|---|
| Amazon MSK Serverless | Kafka broker | ~$50–$80 |
| Amazon EMR Serverless | Spark compute | ~$30–$60 |
| Amazon S3 | Delta Lake data + checkpoints + job artifact | ~$5 |
| Amazon CloudWatch | Logs, alarms, dashboard | ~$5 |
| Amazon SNS | Alarm notifications | ~$0–$2 |
| VPC / subnets / security groups | Network isolation | ~$0 (no NAT Gateway) |
| IAM | Least-privilege roles | ~$0 |

**Expected dev total: ~$120–$200 for a 2-week evidence run, ~$50/week if destroyed daily.**

---

## 2. Minimal cost architecture

```text
Producer (local Python or AWS CLI) 
    → Internet Gateway
    → Public subnet
    → MSK Serverless (IAM auth, port 9098)
    
EMR Serverless (Spark job)
    → VPC endpoint / public subnet
    → reads from MSK
    → writes to S3 Delta path
    
CloudWatch
    → EMR job logs
    → custom dashboard
    → alarm on job failure / MSK lag / S3 4xx
```

**Cost controls**
- Public subnets only for dev (avoid NAT Gateway).
- MSK Serverless scales to zero.
- EMR Serverless jobs billed by worker second; auto-stop after 1 minute idle.
- Use S3 Lifecycle to move checkpoints to Glacier after 7 days.
- Run `terraform destroy` every evening until you capture evidence.

---

## 3. Deployment sequence

```bash
# 1. Configure AWS credentials and region
aws configure

# 2. Prepare terraform variables
cd deploy/aws
cp terraform.tfvars.example terraform.tfvars
# edit: environment = "dev", alert_email = "you@example.com"

# 3. Initialize and validate
terraform init
terraform fmt -check
terraform validate

# 4. Plan (review the resources and cost)
terraform plan -out=tfplan

# 5. Apply (provisions MSK, EMR, S3, IAM, CloudWatch)
terraform apply tfplan

# 6. Capture key outputs
terraform output -raw msk_bootstrap_brokers
terraform output -raw s3_bucket
terraform output -raw emr_application_id
terraform output -raw emr_execution_role_arn

# 7. Produce sample events
cd ../../
python scripts/generate_sample_events.py --topic events --count 10000
# This script publishes JSON events to the MSK topic.

# 8. Upload the streaming job to S3
aws s3 cp src/pipeline/streaming_job.py s3://$(terraform -chdir=deploy/aws output -raw s3_bucket)/jobs/streaming_job.py

# 9. Submit the EMR Serverless job
aws emr-serverless start-job-run \
  --application-id $(terraform -chdir=deploy/aws output -raw emr_application_id) \
  --execution-role-arn $(terraform -chdir=deploy/aws output -raw emr_execution_role_arn) \
  --job-driver '{
    "sparkSubmit": {
      "entryPoint": "s3://<BUCKET>/jobs/streaming_job.py",
      "entryPointArguments": [],
      "sparkSubmitParameters": "--conf spark.jars.packages=org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,io.delta:delta-core_2.12:2.4.0 --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
    }
  }'

# 10. Verify Delta data in S3
aws s3 ls s3://<BUCKET>/delta/events/
aws s3 ls s3://<BUCKET>/delta/events/_delta_log/

# 11. Stop / destroy when evidence is captured
terraform destroy
```

---

## 4. Terraform execution order

1. `terraform init` — download AWS provider and modules.
2. `terraform validate` — syntax and dependency checks.
3. `terraform plan` — preview resources and IAM; fix any issues.
4. `terraform apply` — create VPC, subnets, MSK, S3, IAM, EMR, CloudWatch.
5. `terraform output` — retrieve IDs and ARNs for job submission.
6. `terraform destroy` — tear down dev stack after evidence capture.

**Dependencies to respect**
- `aws_vpc` → `aws_subnet` → `aws_msk_serverless_cluster` + `aws_emrserverless_application`.
- `aws_s3_bucket` → `aws_s3_object` job upload.
- `aws_iam_role` → `aws_iam_role_policy` → `aws_emrserverless_application`.
- `aws_sns_topic` → `aws_cloudwatch_metric_alarm`.

---

## 5. Monitoring setup

- **CloudWatch Log Group:** `/aws/emr-serverless/{application-id}/streaming`
- **Alarms:**
  - `JobsFailed > 0` on EMR Serverless (immediate email/SMS if `alert_email` set).
  - `SumOffsetLag > 1000` on MSK for 10 minutes.
  - `4xxErrors > 0` on the S3 data bucket.
- **Dashboard widgets:**
  - EMR: `JobsRunning`, `JobsFailed`, `JobsSubmitted`
  - MSK: `MessagesInPerSec`, `SumOffsetLag`
  - S3: `BucketSizeBytes`, `NumberOfObjects`
  - Logs: `ERROR` count in the last hour

---

## 6. Screenshot / demo checklist

### AWS Console evidence
- [ ] MSK Serverless cluster overview (cluster name, status `Available`, IAM auth).
- [ ] MSK client information showing bootstrap brokers (mask broker names if sensitive).
- [ ] EMR Serverless application `Running`.
- [ ] EMR job run `Success` with duration.
- [ ] S3 bucket with `delta/events/` prefix and `_delta_log/`.
- [ ] CloudWatch Logs for the job run showing `INFO` and checkpoint commits.
- [ ] CloudWatch Alarms list showing green `OK` for all three alarms.
- [ ] CloudWatch Dashboard with throughput/lag/failure widgets.
- [ ] IAM role policy showing least-privilege S3 and MSK access.
- [ ] Terraform `apply` output terminal with `Apply complete!`.

### CLI / code evidence
- [ ] `aws kafka get-bootstrap-brokers` output.
- [ ] `aws emr-serverless start-job-run` command and job-run-id.
- [ ] `aws s3 ls` of the Delta Lake table.
- [ ] `python scripts/generate_sample_events.py` running.
- [ ] GitHub Actions `workflow_dispatch` AWS Deploy run with green `validate` and `apply`.

---

## 7. Expected results

- 100k events processed in ~3–5 minutes.
- S3 `s3://<bucket>/delta/events/` contains Parquet files.
- `_delta_log/` shows Delta transaction JSON files.
- CloudWatch logs show checkpoint commits.
- All CloudWatch alarms remain `OK`.

---

## 8. Safety rules

- Never commit `terraform.tfvars` or AWS credentials.
- Use `terraform destroy` after each evidence capture session.
- Set AWS billing alerts at $20 and $50.
- Use a dedicated `dev` account or cost center.
