# Top 10 Interview Stories — STAR + Technical Deep Dive

Use these for behavioral rounds, hiring-manager conversations, and technical deep-dives. Each story is 90–120 seconds spoken.

---

## 1. Built a Configuration-Driven Core Data Product Platform

### Situation
At Accenture, my team managed 90+ production PySpark ETL jobs across 67 source and 120+ core data products. Jobs were hard-coded, duplicated, and slow to release.

### Task
Design a configuration-driven Core Data Product (CDP) platform so new pipelines could be added without code changes.

### Action
- Introduced JSON-based job definitions that defined source, transformations, target, and schedule.
- Built reusable Python modules for common transforms, secrets injection, and logging.
- Implemented parent-child GitLab CI/CD pipelines so each job could be tested and deployed independently.
- Added `pytest` suites with 95%+ coverage using in-memory Spark fixtures and mocks for external systems.
- Stored secrets in HashiCorp Vault and enforced environment-driven config.

### Result
- 70% faster deployment time for new jobs.
- 99.5% pipeline uptime.
- 60+ pytest suites with 95%+ coverage.
- Team could onboard a new data product in hours instead of days.

### Technical deep dive
- How would you extend this to support streaming? Replace batch JSON with streaming configs, use PySpark Structured Streaming `trigger(once=True)` for batch parity, then `trigger(processingTime='5 minutes')`.
- How did you handle schema changes? Schema was versioned in the config; the transform layer validated `event_type` against a registry; invalid rows were quarantined.
- CI/CD strategy? Parent pipeline parsed job configs and spawned child pipelines per job, parallelizing tests and limiting blast radius.

### Leadership angle
I convinced the team to move from copy-paste notebooks to a modular platform by showing the deployment-time reduction in a two-week pilot.

---

## 2. Operated 90+ Production PySpark Jobs with High Uptime

### Situation
The data platform I supported was critical to downstream reporting. Any job failure cascaded into stale dashboards and delayed decisions.

### Task
Keep 90+ PySpark ETL jobs reliable and observable with minimal on-call burden.

### Action
- Standardized logging, retries, and checkpointing across all jobs.
- Added Airflow/GitLab scheduling with alerting on failure.
- Created runbooks for common failure patterns (schema drift, cluster timeouts, partition skew).
- Built unit and integration tests so most issues were caught in CI.
- Monitored job duration and row counts to detect silent data drift.

### Result
- 99.5% uptime across the pipeline estate.
- 60% fewer production incidents compared to the previous quarter.
- Mean time to recovery (MTTR) dropped to under 30 minutes.

### Technical deep dive
- How did you detect data drift? Compared daily row counts, column null percentages, and key cardinality against historical baselines; alerts triggered on >2-sigma deviations.
- Retry logic? Exponential backoff for transient S3/DB errors, capped at 3 retries, with dead-letter paths for poison records.
- Partition skew? Added adaptive query execution hints and `repartition` by `event_date` before aggregations.

### Leadership angle
I treated operational reliability as a product feature and made the team accountable for clean runbooks and test coverage.

---

## 3. Achieved 95%+ Test Coverage on Data Pipelines

### Situation
Data engineering teams often skip testing because Spark jobs are hard to unit-test. We had flaky integration tests and slow feedback loops.

### Task
Introduce fast, reliable testing for PySpark transformations and pipeline orchestration.

### Action
- Created an in-memory Spark fixture using `pytest` and `SparkSession.builder.master("local[*]")`.
- Migrated Kafka, Delta, and API calls to mocked interfaces.
- Refactored transforms into pure functions that took DataFrames and returned DataFrames.
- Added property-based tests for critical deduplication and enrichment logic.
- Enforced 95%+ coverage gates in GitLab CI.

### Result
- 60+ pytest suites with 95%+ coverage.
- CI time stayed under 5 minutes per job because tests ran in memory.
- 60% fewer production bugs attributed to transform logic.

### Technical deep dive
- How do you test a Kafka stream? Use `readStream` with `.format("rate")` or a mocked Kafka source; assert on the output DataFrame or a `MemorySink`.
- Delta Lake testing? Use a temporary `spark.sql.warehouse.dir` in `/tmp` and clean up after each test.
- Pure functions in Spark? Each transform accepts `DataFrame, config` and returns `DataFrame` — no side effects, easy to test.

### Leadership angle
I pushed testing as a team norm by proving it saved time in incident response, not just by writing rules.

---

## 4. Designed and Deployed a Kafka → PySpark → Delta Lake Pipeline

### Situation
We needed a streaming ingestion layer for JSON events that could also serve batch analytics without reprocessing.

### Task
Build a production-style pipeline that reads from Kafka, validates schema, deduplicates, and writes to Delta Lake with exactly-once semantics.

### Action
- Used PySpark `readStream` with Kafka source and `kafka.bootstrap.servers` from config.
- Enforced a strict JSON schema before parsing to fail fast on bad data.
- Used `withWatermark` and `dropDuplicates("event_id")` to handle late-arriving events.
- Wrote output with `.format("delta")`, `.outputMode("append")`, and checkpointing on S3/ADLS.
- Benchmarked 31k–45k rows/sec on a 4-core laptop.

### Result
- Streaming ingestion with exactly-once processing.
- Schema validation prevented corrupt events from entering the Delta table.
- Partitioned by `event_date` and `event_hour` for fast downstream queries.

### Technical deep dive
- Exactly-once in Spark? Checkpoint + idempotent sink. For Kafka, offsets are tracked in the checkpoint; replays use the same checkpoint, so Delta’s idempotent writes avoid duplicates.
- Watermark choice? 10-minute watermark bounded state for `dropDuplicates` while still handling late data.
- Why Delta Lake? ACID transactions, time travel, and schema enforcement make it the right sink for both streaming and batch.

### Leadership angle
I owned the end-to-end design and defended the choice of Delta over plain Parquet by benchmarking throughput and recovery time.

---

## 5. Migrated Streaming Pipeline to the Cloud with Terraform

### Situation
The local Kafka/PySpark/Delta pipeline needed to run in the cloud for production use.

### Task
Deploy the same pipeline on AWS using managed services and infrastructure as code.

### Action
- Chose MSK Serverless for Kafka, EMR Serverless for Spark, and S3 for Delta Lake and checkpoints.
- Wrote Terraform modules for VPC, subnets, IAM, MSK, EMR, S3, CloudWatch, and SNS.
- Added a GitHub Actions workflow for `terraform fmt`, `validate`, and `apply` on manual trigger.
- Created CloudWatch alarms for EMR job failures, MSK consumer lag, and S3 4xx errors.
- Documented cost estimates and a production checklist.

### Result
- A fully codified cloud deployment that can be destroyed and rebuilt in minutes.
- Monitoring and alerting in place before the first job ran.
- Clear cost guardrails to avoid runaway spend.

### Technical deep dive
- Why MSK Serverless? Removes broker management, scales automatically, and uses IAM auth over TLS for security.
- Why EMR Serverless? No cluster to manage; pay per worker second; good fit for batch/streaming Spark jobs.
- Terraform state? Use a remote S3 backend with DynamoDB locking for team safety.

### Leadership angle
I made infrastructure reviewable and reproducible, reducing the risk of hand-rolled cloud setups.

---

## 6. Built a RAG Document QA Chatbot with FastAPI and ChromaDB

### Situation
There was a need to answer questions over private documents without sending sensitive data to third-party APIs.

### Task
Build a retrieval-augmented generation (RAG) chatbot that runs locally or with an optional cloud LLM.

### Action
- Implemented FastAPI endpoints for document ingestion and question answering.
- Used ChromaDB with `sentence-transformers` all-MiniLM-L6-v2 for embeddings.
- Added a provider abstraction to swap between Ollama (local) and OpenAI (cloud).
- Built a Streamlit UI for non-technical users.
- Wrote `pytest` tests with mocked embeddings and LLM calls.

### Result
- 85% retrieval accuracy on test documents.
- 70% reduction in API calls through response caching.
- Clean separation between retrieval and generation, making provider swaps trivial.

### Technical deep dive
- Chunking strategy? Recursive text splitting with overlap to preserve sentence context; chunk size 512 tokens, overlap 64.
- Why ChromaDB? Local-first, zero setup, easy to persist and query; for production I would evaluate Pinecone or pgvector.
- Caching? Cached query embeddings and final answers keyed by a hash of the question; invalidation on document update.

### Leadership angle
I identified privacy as the key constraint and designed a solution that kept sensitive documents in-house by default.

---

## 7. Passed the Databricks Data Engineer Associate Exam

### Situation
I was working heavily with Databricks, Delta Lake, and PySpark and wanted a credential that validated those skills.

### Task
Pass the Databricks Data Engineer Associate exam within three weeks while working full-time.

### Action
- Week 1: Lakehouse platform + Delta Lake theory using Databricks Academy free content.
- Week 2: PySpark transformations, Delta CRUD, time travel, `MERGE`, `OPTIMIZE`, `VACUUM`.
- Week 3: Structured Streaming, Auto Loader, practice exams, and weak-topic review.
- Ran hands-on labs in a Databricks community workspace.
- Reviewed every wrong answer from practice tests.

### Result
- Passed on the first attempt.
- Applied the learnings immediately to a Databricks project at work.
- Wrote a study guide to help others preparing for the same exam.

### Technical deep dive
- Delta Lake `VACUUM` vs `OPTIMIZE`? `OPTIMIZE` compacts small files; `VACUUM` removes old files no longer referenced by the Delta log.
- Structured Streaming output modes? `append` for new rows only; `complete` for aggregations; `update` for changed rows.
- Unity Catalog vs. Hive metastore? Unity Catalog provides cross-workspace governance, fine-grained access control, and audit logging.

### Leadership angle
I used the certification to accelerate a team standard around Delta Lake governance and structured streaming best practices.

---

## 8. Reduced Deployment Time by 70% with Modular CI/CD

### Situation
Each new PySpark job required a full release cycle, including manual notebook promotion and hand-edited cluster configs.

### Task
Shorten the time from development to production for data products.

### Action
- Split monolithic CI into reusable GitLab templates.
- Used parent-child pipelines: one pipeline per job config, triggered from a central orchestrator.
- Standardized Docker images and dependency management.
- Added `pytest` and `flake8` stages before any deployment.
- Promoted artifacts through dev, staging, and prod with environment-specific configs.

### Result
- 70% faster deployments.
- Fewer failed production releases because changes were tested in isolation.
- New team members could add a job by editing a JSON file and opening a PR.

### Technical deep dive
- Parent-child pipeline trigger? `trigger: include: path/to/child-pipeline.yml` with `strategy: depend`.
- How did you handle secrets? `CI/CD variables` per environment plus HashiCorp Vault for dynamic DB/API credentials.
- Rollback? Tagged Docker images and config versions; rollback by redeploying a previous artifact tag.

### Leadership angle
I made the case to management by measuring deployment time and incidents before and after the migration.

---

## 9. Handled Schema Drift in a Streaming Pipeline

### Situation
Upstream producers started adding new fields to JSON events. The streaming job broke because the schema was hard-coded and the parser rejected unknown fields.

### Task
Make the streaming pipeline resilient to schema additions without losing data.

### Action
- Switched from a strict `from_json` schema to a permissive schema that allowed extra fields but enforced a required subset.
- Added a quarantine path for events that failed required-field validation.
- Implemented schema registration in the config so each job could declare expected and optional fields.
- Monitored the quarantine table and alerted on spikes.

### Result
- Zero data loss from schema additions.
- Downstream consumers were shielded from raw changes.
- Quarantine table gave us visibility into bad data within minutes.

### Technical deep dive
- How did you validate? `json_schema` defined required fields; Spark parsed the JSON, selected required fields, and checked for nulls; failures were written to a `quarantine` Delta path.
- Evolution strategy? New optional fields were added as nullable columns; downstream jobs could adopt them on their own schedule.
- Monitoring? `quarantine` row count per hour; alarm if >1% of events failed validation.

### Leadership angle
I balanced strictness and flexibility: the pipeline became more tolerant without becoming unsafe.

---

## 10. Mentored a Junior Engineer on Spark and Testing

### Situation
A junior teammate was struggling with PySpark syntax and had no experience writing unit tests for data pipelines.

### Task
Get them productive on the team within four weeks.

### Action
- Pair-programmed on their first Spark transform, explaining the Catalyst execution model and lazy evaluation.
- Set up a `pytest` fixture and showed them how to write a test for a pure DataFrame function.
- Reviewed their PRs within 24 hours with specific, actionable feedback.
- Recommended documentation and small Spark coding challenges.
- Gave them ownership of a low-risk job after two weeks.

### Result
- They merged their first PR in week 2.
- By week 4, they independently added a new data product to the CDP platform.
- Their test coverage on the module was 90%+.

### Technical deep dive
- What did you teach first? Reading `explain()` to understand the physical plan and why `groupBy` operations shuffle.
- Testing pattern? Pure function transforms + in-memory `SparkSession` + `chispa` for DataFrame assertions.
- Code review focus? Correctness, test coverage, and config-driven design before style nits.

### Leadership angle
I measured success by their independence, not by my own output. Their first fully owned job release was a bigger win than any PR I could have written.

---

## Quick interview tips

- **STAR length:** 60% Action, 20% Result, 10% Situation, 10% Task.
- **Quantify:** Use the real numbers from your resume (90+ jobs, 95% coverage, 99.5% uptime, 70% faster deployments).
- **Pivot to architecture:** When asked a behavioral question, explicitly mention the design tradeoffs you made.
- **Leadership stories:** Use #10 and #1 for “Tell me about a time you influenced someone.”
- **Failure stories:** If asked, adapt #9 and frame the initial outage as the trigger that led to a more resilient design.
