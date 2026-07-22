# Screenshot Plan — Recruiter Proof Package

Use this checklist after the live AWS deployment. Each screenshot should be high-resolution, clearly cropped, and recruiter-friendly. Store them in `docs/images/` in the Kafka repo and link them from the README and portfolio.

---

## 1. AWS Console — Big Picture

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 1.1 | AWS console home with recent services | `MSK`, `EMR Serverless`, `S3`, `CloudWatch` in the recently visited list | Shows active AWS usage |
| 1.2 | AWS region dropdown | Region set to `us-east-1` (or your chosen region) | Shows deliberate global deployment |
| 1.3 | AWS Billing → Cost Explorer | Current month spend for the dev run | Shows cost awareness |

---

## 2. Amazon MSK

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 2.1 | MSK Serverless clusters list | Cluster name, status `Active`, type `Serverless` | Managed Kafka |
| 2.2 | Cluster details | Cluster ARN, IAM authentication enabled, TLS enabled | Security model |
| 2.3 | Client information | Bootstrap brokers (partial / masked) | Connectivity |
| 2.4 | Topics tab | `events` topic listed | Real topic |
| 2.5 | Topic details | Partitions count, replication factor | Kafka depth |

---

## 3. Amazon S3

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 3.1 | S3 buckets list | Bucket name `kafka-pyspark-delta-dev-data-*` | Data lake storage |
| 3.2 | Bucket objects — `delta/events/` | Parquet files under date partitions | Delta Lake output |
| 3.3 | Bucket objects — `_delta_log/` | JSON transaction log files | Delta Lake ACID proof |
| 3.4 | Bucket properties | Versioning enabled, default encryption | Production hygiene |
| 3.5 | S3 upload of `streaming_job.py` | `jobs/streaming_job.py` in the bucket | Deployment artifact |

---

## 4. Amazon EMR Serverless

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 4.1 | EMR Serverless applications | Application name, state `Created` / `Started` | Spark runtime |
| 4.2 | Application details | Release label `emr-7.0.0-latest`, type `Spark` | Version and stack |
| 4.3 | Job runs list | Job run ID, status `Success`, runtime | Pipeline execution |
| 4.4 | Job run details | Spark version, execution role, network config | Engineering rigor |
| 4.5 | Job logs (CloudWatch) | First and last 20 lines of successful logs | It actually ran |

---

## 5. CloudWatch

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 5.1 | CloudWatch Log groups | `/aws/emr-serverless/{app-id}/streaming` | Observable logs |
| 5.2 | CloudWatch Logs — successful run | `INFO` lines and checkpoint commits | Streaming health |
| 5.3 | CloudWatch Alarms list | 3 alarms: EMR jobs failed, MSK lag, S3 4xx | Operational coverage |
| 5.4 | Alarm details — `emr-jobs-failed` | Threshold, dimensions, SNS action | Failure detection |
| 5.5 | CloudWatch Dashboard | Custom dashboard with throughput/lag/S3 metrics | Production monitoring |
| 5.6 | CloudWatch Metrics — `MessagesInPerSec` | MSK topic incoming message rate | Real throughput |

---

## 6. Terraform

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 6.1 | Terminal — `terraform init` | Provider downloaded, backend initialized | IaC readiness |
| 6.2 | Terminal — `terraform plan` | Plan summary: `Plan: X to add, 0 to change, 0 to destroy` | Reviewed plan |
| 6.3 | Terminal — `terraform apply` | `Apply complete! Resources: X added` | Successful deploy |
| 6.4 | Terminal — `terraform output` | `msk_bootstrap_brokers`, `s3_bucket`, `emr_application_id` | Verified outputs |

---

## 7. GitHub Actions

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 7.1 | Actions → AWS Deploy workflow | Triggered via `workflow_dispatch` with `apply: true` | CI/CD in action |
| 7.2 | Workflow summary | All jobs green: `validate` + `plan-and-apply` | Quality gates |
| 7.3 | Terraform Validate job | `terraform validate` success | No syntax errors |
| 7.4 | Terraform Apply job | `Apply complete!` in GitHub log | Automated deployment |

---

## 8. Pipeline Output

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 8.1 | Producer terminal | `python scripts/generate_sample_events.py` sending events | Data ingestion |
| 8.2 | EMR job log — `Streaming query started` | Query name and checkpoint path | Spark structured streaming |
| 8.3 | EMR job log — `Committed offsets` | Kafka offsets committed | Exactly-once semantics |
| 8.4 | S3 CLI listing | `aws s3 ls s3://<bucket>/delta/events/event_date=...` | Partitioned output |
| 8.5 | Delta Lake `_delta_log` files | Transaction log version files | ACID proof |

---

## 9. Delta Tables

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 9.1 | Databricks / Jupyter notebook | `spark.read.format("delta").load("s3://.../delta/events").show()` | Data is queryable |
| 9.2 | Databricks table schema | Columns: `event_id`, `event_type`, `event_timestamp`, `event_date`, `event_hour`, `ingested_at` | Schema evolution |
| 9.3 | Databricks — `DESCRIBE HISTORY` | Version 0, operation `WRITE` | Delta time travel |
| 9.4 | Databricks — `OPTIMIZE` / `VACUUM` run | Maintenance job output | Delta operations |

---

## 10. Monitoring Dashboard

| # | Screenshot | What to capture | Why it matters |
|---|---|---|---|
| 10.1 | Custom CloudWatch dashboard overview | All widgets visible | Unified observability |
| 10.2 | Throughput widget | `MessagesInPerSec` from MSK | Real-time metric |
| 10.3 | Lag widget | `SumOffsetLag` for consumer group | Consumer health |
| 10.4 | Job failure widget | `JobsFailed` from EMR Serverless | Reliability signal |
| 10.5 | Cost widget | Estimated month-to-date spend | Cost awareness |

---

## Naming and storage convention

Store screenshots as:

```
docs/images/aws/
  01-msk-cluster.png
  02-emr-application.png
  03-s3-delta-output.png
  04-cloudwatch-alarms.png
  05-cloudwatch-dashboard.png
  06-terraform-apply.png
  07-github-actions-success.png
  08-pipeline-output.png
  09-delta-table.png
  10-monitoring-dashboard.png
```

## Usage

1. Add a `## Live Deployment Gallery` section to `Kafka-pyspark-delta-pipeline/README.md`.
2. Insert the top 6 screenshots there with captions.
3. Add 2–3 screenshots to the portfolio project card for the Kafka pipeline.
4. Use 1–2 screenshots in LinkedIn posts and blog articles.
