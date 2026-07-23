# Sasidhar Mopuru — Interview Prep & Story Notes

> Read this before an interview, not during. Use it to remember the *story* behind every line on your resume. Speak in your own words. Numbers are real, so own them.

---

## 1. My 30-second intro (use this everywhere)

"Hi, I'm Sasidhar. I'm a Data & AI Platform Engineer at Accenture with a little over two years of experience building configuration-driven PySpark data products. At work I run a Core Data Product platform that covers 90+ production ETL jobs across 67 source data products and 120+ core data products. I deal with PySpark, Docker, GitLab CI/CD, Kafka, HashiCorp Vault for secrets, and I keep 95%+ unit-test coverage across the pipeline files. Outside of work I've built a RAG chatbot with FastAPI, Streamlit, ChromaDB and OpenAI, and a Kafka → PySpark → Delta Lake streaming pipeline with AWS and Terraform. I'm now looking for Data Platform Engineer, Cloud Data Engineer or AI/Data Engineer roles where I can own the full data lifecycle."

**Why it works:** It opens with role, company, scale, tech, and closes with what you want. Keep it under 30 seconds.

---

## 2. Resume bullets — how to explain each one

### Bullet: Built configuration-driven Core Data Product (CDP) platform

**What it means in plain English:**
Before my change, every PySpark job had hard-coded source, transformation, and target logic. Adding a new job meant copy-pasting an old one, editing code, and doing a full release. I moved the job definition into JSON configs and the reusable transformations into Python modules.

**Say it like this:**
"I led the design of a Core Data Product platform where a data product is defined by a JSON config — source, transformations, target, schedule, and ownership. The actual transformation logic lives in reusable Python modules. This meant a non-coder could create a new data product by editing a JSON file, and the CI/CD pipeline would test and deploy only that job. We went from copy-paste releases to config-driven releases."

**Numbers to drop:**
- 90+ production PySpark ETL jobs
- 67 source data products (SDPs)
- 120+ core data products (CDPs)
- 40% faster deployments at the resume level; 70% in some README/project descriptions
- 99.5% pipeline uptime

**Deep-dive questions you might get:**

*Q: What did the JSON config look like?*
"It had sections like `source`, `transformations`, `target`, `schedule`, and `owner`. The `transformations` block referenced named Python functions rather than inline code. This kept the config declarative."

*Q: How did you keep the Python modules reusable?*
"Every transform was a pure function that took a Spark DataFrame and a config dict and returned a DataFrame. No side effects, no hard-coded table names. That made unit testing trivial."

*Q: What was the business impact?*
"New data products went from a couple of days to a few hours. Deployment time dropped by 40-70%, and we had fewer failed releases because each job was tested and deployed independently."

---

### Bullet: End-to-End Data Engineering

**What it means in plain English:**
I don't just write a script and hand it off. I design the full data flow — source ingestion, intermediate processing, final core product, and the data quality checks that keep it reliable.

**Say it like this:**
"I built the end-to-end flow from source systems into what we call Source Data Products, and from there into Core Data Products. That means I handled ingestion, transformation, schema validation, data quality, and the orchestration that runs it all. We delivered 5+ enterprise data products across both batch and streaming."

**Numbers to drop:**
- 5+ enterprise data products
- 90+ production jobs
- 67 SDPs, 120+ CDPs

**Deep-dive question:**

*Q: What's the difference between an SDP and a CDP?*
"An SDP is a cleaned, standardized version of a source system — close to the raw data. A CDP is a business-ready product built by joining and enriching SDPs. Think of SDP as the raw material, CDP as the finished good."

---

### Bullet: PySpark Pipeline Development

**What it means in plain English:**
I write modular Spark jobs in Python. I build error handling, retries, schema validation, and logging so jobs don't break silently.

**Say it like this:**
"I build PySpark pipelines as small, reusable functions. Each function does one thing — clean, enrich, validate, write. I add retries for transient failures like S3 or DB timeouts, schema validation so bad data fails fast, and comprehensive logging so we can debug quickly. This modular approach is what let us hit 99.5% uptime."

**Technical terms to own:**
- **Schema validation:** Check that input data has expected columns and types before processing.
- **Retry mechanism:** Re-run failed steps with delays for transient errors.
- **Lazy evaluation:** Spark builds a plan but doesn't execute until you call an action like `show()` or `write()`.
- **Catalyst optimizer:** Spark's engine that rewrites your logical plan into an efficient physical plan.

*Q: How do you handle schema drift?*
"We maintain a config registry of required vs optional fields. Required fields must be present; new optional fields are accepted as nullable columns. Events that fail required validation go to a quarantine path, and we alert on the quarantine volume."

---

### Bullet: Containerization & CI/CD

**What it means in plain English:**
I package Spark jobs in Docker so they run the same way on my laptop, in staging, and in production. I use GitLab CI/CD to test and deploy automatically across dev, sit, perf, and prod.

**Say it like this:**
"I containerized our Spark jobs using a custom Docker image based on `harbor.dell.com/customer-lakehouse/spark-py:3.5.5-v14-python3.12`. This fixed the classic problem where 'it works on my machine' breaks in production. Then I set up parent-child GitLab CI/CD pipelines: the parent pipeline reads the config and spawns child pipelines per job, so we can test and deploy each job independently across dev, sit, perf, and prod."

**Numbers to drop:**
- 60% less manual deployment effort
- 40-70% faster deployments
- Multi-environment: dev, sit, perf, prod

**Technical terms to own:**
- **Docker image:** A snapshot of code + dependencies + runtime.
- **Parent-child pipeline:** A CI pipeline that triggers smaller pipelines; keeps the blast radius small.
- **Dev / SIT / Perf / Prod:** Development, System Integration Test, Performance, Production.
- **Artifact promotion:** Tested code/image moves from one environment to the next, not rebuilt.

*Q: How do you roll back?*
"We tag Docker images and config versions. If a release breaks, we redeploy the previous tag. The rollback is just a config or image swap, not a rebuild."

---

### Bullet: Streaming Integration

**What it means in plain English:**
I connect real-time event sources like Kafka to Spark streaming jobs and write reliable output to Delta Lake.

**Say it like this:**
"I integrated Kafka and S3A-compatible object storage into our PySpark Structured Streaming jobs. The streaming job reads from Kafka, validates schema, drops duplicates using a watermark on event time, and writes append-only output to Delta Lake. Checkpointing is on S3 or ADLS so the job can recover exactly where it left off."

**Numbers to drop:**
- 31k–45k rows/sec on a 4-core laptop
- 1M+ events/hour in the AWS Kafka demo

**Technical terms to own:**
- **Exactly-once semantics:** Output is produced once even if the job restarts. Achieved with idempotent writes + checkpointing.
- **Watermark:** A moving time threshold that tells Spark when it can safely drop old state for late-arriving events.
- **Checkpointing:** Saving the stream state periodically so you can resume after a failure.
- **Idempotent sink:** Writing with the same data and identifier produces the same result, so duplicates don't matter.
- **dropDuplicates:** Spark function to remove duplicates based on one or more columns.

*Q: How do you guarantee exactly-once?*
"Spark tracks offsets in the checkpoint. Delta Lake is an idempotent sink because writes are transactional and you can deduplicate by a unique key. So even if the job reprocesses a batch, the same rows with the same keys won't be duplicated."

---

### Bullet: Security & Quality

**What it means in plain English:**
I keep credentials out of code using Vault, and I make sure critical pipeline files have unit tests.

**Say it like this:**
"I implemented secure credential management with HashiCorp Vault and enterprise certificate stores, so secrets are never hard-coded in repositories. We also enforce environment-driven config. For quality, I wrote unittest scripts across all critical pipeline files and hit 95%+ coverage. That means regressions get caught in CI, not in production."

**Technical terms to own:**
- **HashiCorp Vault:** A secrets manager. You request credentials at runtime; they expire and rotate.
- **Enterprise certificate stores:** Central stores for TLS/SSL certs used for encrypted connections.
- **Environment-driven config:** Same code, different configs for dev/sit/prod. No if-else on environment names in code.
- **unittest / pytest:** Python testing frameworks. We use unittest scripts and pytest runners.
- **Mocking:** Replace real external services with fake ones in tests so tests run fast and offline.

*Q: Why unittest and not only pytest?*
"The team standard was a mix. unittest is in the standard library, so no extra dependency. pytest gives better fixtures and reporting. I wrote the tests using unittest classes and ran them with pytest."

---

### Bullet: Performance Optimization

**What it means in plain English:**
I made pipelines faster by fixing partitioning, caching, and filtering issues.

**Say it like this:**
"I profiled slow jobs and found the usual suspects — too many small files, skewed partitions, repeated reads, and missing filters. I added `repartition` on `event_date`, cached intermediate DataFrames where reuse was high, and pushed filters closer to the source. That reduced data processing latency by 30%."

**Technical terms to own:**
- **Partitioning:** Split data by a key so queries read only relevant slices.
- **Adaptive Query Execution (AQE):** Spark's runtime optimizer that can change joins and partitions based on real statistics.
- **Caching:** Persist a DataFrame in memory to reuse it without recomputing.
- **Predicate pushdown:** Apply filters at the source (e.g., Parquet file) so less data is read.

---

### Bullet: Infrastructure as Code

**What it means in plain English:**
I version-controlled pipeline configs and database schemas with Git, and used Terraform for cloud resources.

**Say it like this:**
"I treat data pipeline configs and schemas as code. Everything is in Git with proper branching and PR reviews. For the AWS streaming demo I also used Terraform so the entire Kafka/PySpark/Delta Lake stack could be recreated in minutes with the same configuration."

**Technical terms to own:**
- **Git version control:** Tracks changes and enables rollbacks.
- **DDL scripts:** SQL that defines tables and schemas.
- **Terraform:** Declarative IaC tool. You describe resources, Terraform creates them.
- **State file:** Tracks what Terraform has deployed.

---

## 3. Project deep dives (pick 2-3 based on the role)

### Project 1 — Cloud-Native Streaming Data Platform

**One-liner:**
A streaming ingestion + lakehouse platform on Azure using Event Hubs, Databricks, ADLS Gen2, and Terraform.

**Why this matters:**
It shows cloud platform thinking: managed streaming, lakehouse storage, IaC, and CI/CD.

**Architecture in plain English:**
- Events are published to **Azure Event Hubs** (like Kafka-as-a-service).
- **Databricks** runs a PySpark Structured Streaming job that reads those events.
- The job validates the JSON schema, drops duplicates with a watermark, and appends to **Delta Lake** on **ADLS Gen2**.
- **Terraform** provisions Event Hubs, Databricks workspace, storage, and IAM for dev and prod.
- **GitHub Actions** runs tests and deployment automatically.

**Tradeoffs to know:**
- **Event Hubs vs Kafka:** Event Hubs removes broker management, IAM is native to Azure, and auto-scaling is built in. Kafka gives more tuning knobs but more operational burden.
- **Delta Lake vs Parquet:** Delta gives ACID transactions, time travel, schema enforcement, and merge/upsert. Parquet is just a columnar format with no transaction guarantees.
- **Databricks vs EMR:** Databricks manages the Spark runtime and cluster for you. EMR Serverless is closer to raw Spark with less management.

**Numbers:**
- 99.9% data accuracy
- 50% faster infrastructure setup with Terraform modules
- Multi-environment (dev/prod)

**Questions you'll get:**

*Q: How do you scale the streaming job?*
"Scale Event Hubs partitions and Databricks workers. Spark parallelism is tied to Kafka/Event Hubs partitions, so add partitions before adding workers."

*Q: What happens if the stream is down?*
"The checkpoint preserves the last committed offsets. When the job restarts it picks up from there. Event Hubs retains events for a configurable time, so we don't lose data."

---

### Project 2 — RAG Document QA Chatbot

**One-liner:**
A local-first retrieval-augmented generation chatbot that answers questions over uploaded PDFs, DOCX, and TXT files.

**Why this matters:**
It shows you understand the data foundation for AI: embeddings, vector search, and LLM orchestration.

**Architecture in plain English:**
- User uploads a document via a **Streamlit** UI.
- **FastAPI** backend ingests the file, extracts text, and splits it into chunks.
- **sentence-transformers** (all-MiniLM-L6-v2) turns each chunk into a vector embedding.
- **ChromaDB** stores the vectors and runs similarity search.
- The query vector retrieves the top-k relevant chunks.
- An LLM (OpenAI or local **Ollama**/**LLaMA**) generates an answer grounded in the retrieved chunks.

**Tradeoffs to know:**
- **ChromaDB vs Pinecone:** ChromaDB is local-first, zero setup, great for demos. Pinecone is managed, scalable, better for production.
- **OpenAI vs local LLM:** OpenAI is more capable but sends data out. Local LLMs keep documents private but need more hardware.
- **Chunking:** Recursive splitting with overlap preserves sentence context. Chunk size 512 tokens with 64-token overlap is common. Too small loses context; too large dilutes relevance.
- **Caching:** We cache query embeddings and final answers by a hash of the question. Updates to documents invalidate the cache.

**Numbers:**
- 85% retrieval accuracy on test documents
- 70% fewer API calls through caching
- PDF, DOCX, and TXT ingestion support

**Questions you'll get:**

*Q: What is RAG?*
"RAG means Retrieval-Augmented Generation. Instead of asking an LLM to answer from its training data, we retrieve relevant documents first and feed those as context. That reduces hallucinations and keeps answers grounded."

*Q: How do you prevent hallucinations?*
"We ground the answer in retrieved chunks. The prompt explicitly says 'answer only from the provided context.' We also test on documents where we know the right answer."

---

### Project 3 — Production-Style Kafka → PySpark → Delta Pipeline

**One-liner:**
A real-time streaming pipeline that ingests from Apache Kafka, processes with PySpark, and writes to Delta Lake, deployed on AWS with Terraform.

**Why this matters:**
It shows streaming fundamentals plus cloud/DevOps skills.

**Architecture in plain English:**
- **Apache Kafka** accepts JSON events from producers.
- **PySpark Structured Streaming** reads from Kafka, validates JSON schema, applies watermarks, and deduplicates by `event_id`.
- Output is written to **Delta Lake** in append mode with checkpointing.
- For the AWS version: **MSK Serverless** for Kafka, **EMR Serverless** for Spark, **S3** for storage and checkpoints, **Terraform** for IaC, **CloudWatch** and **SNS** for monitoring and alerts.

**Tradeoffs to know:**
- **MSK Serverless vs self-managed Kafka:** No broker provisioning, auto-scales, IAM auth. More expensive per message at low scale.
- **EMR Serverless vs Databricks:** EMR is cheaper for raw Spark but you manage more. Databricks adds Delta and governance.
- **Exactly-once with Delta + Kafka:** Use `foreachBatch` or `writeStream` with idempotent `MERGE` on `event_id`, plus checkpointing.

**Numbers:**
- 31k–45k rows/sec on a 4-core laptop
- 1M+ events/hour
- 90%+ pytest coverage in the project

**Questions you'll get:**

*Q: How did you benchmark?*
"I generated 100k to 1M JSON events with a Python script, wrote them to Kafka, and measured rows processed per second from the streaming query console. I ran it on my 4-core laptop."

*Q: How do you handle late data?*
"A 10-minute watermark with `dropDuplicates` on `event_id`. Late events within the watermark are processed; older ones are ignored. For very late data we have a separate catch-up batch job."

---

## 4. Tech glossary — how to explain every term on your resume

Use the pattern: **Term:** one sentence definition + why it matters.

### Programming & Data

**Python:** My main language. I use it for data pipelines, FastAPI backends, testing, and automation.

**SQL:** For querying relational databases, writing DDL, and doing lightweight analytics validation.

**PySpark:** Python API for Apache Spark. I use it for distributed data processing on large datasets.

**Apache Spark:** A distributed engine that processes data across a cluster. It uses RDDs/DataFrames and a Catalyst optimizer to build an efficient physical plan.

**DataFrame:** A distributed table. Operations on it are lazy and optimized.

**Lazy evaluation:** Spark doesn't run transformations until you call an action. This lets it optimize the full plan.

**Schema validation:** Ensuring input data has the expected columns, types, and constraints before processing.

**Data quality:** Checks for nulls, duplicates, format errors, out-of-range values, and referential integrity.

**CDC (Change Data Capture):** Capturing changes (inserts/updates/deletes) from source systems so downstream can stay in sync.

**ETL vs ELT:** ETL transforms before loading; ELT loads raw then transforms in the target. I use ELT for data lakes and ETL for curated products.

**Data modeling:** Designing how data is stored and related so queries are fast and understandable.

### Streaming

**Apache Kafka:** A distributed event log. Producers write to topics; consumers read at their own pace.

**Kafka topic:** A logical stream of events. Partitions let it scale horizontally.

**Kafka partition:** A split of a topic. More partitions = more parallelism.

**Azure Event Hubs:** Kafka-compatible managed event streaming service in Azure.

**PySpark Structured Streaming:** A micro-batch stream processing engine in Spark. It looks like batch code but runs continuously.

**Watermark:** A threshold on event time. Spark keeps state for late data up to the watermark, then drops it.

**Exactly-once:** Output is produced one time even if the job restarts. Done with idempotent sinks + checkpointing.

**At-least-once:** Messages are never lost but may be duplicated.

**Checkpointing:** Saving the stream state and offsets so a failed job can resume from where it stopped.

**Offset:** The position of a consumer in a Kafka partition.

### Storage & Lakehouse

**Delta Lake:** An open storage layer over Parquet that adds ACID transactions, time travel, schema enforcement, and merge/upsert.

**Parquet:** A columnar file format. Good compression and fast for analytical queries.

**ACID:** Atomicity, Consistency, Isolation, Durability. Guarantees reliable transactions.

**Time travel:** Querying an older version of a Delta table using a version number or timestamp.

**Schema enforcement:** Delta rejects writes that don't match the table's schema unless schema evolution is enabled.

**Schema evolution:** Allowing new nullable columns in Delta tables over time.

**ADLS Gen2:** Azure Data Lake Storage. Scalable cloud object storage with hierarchical file system support.

**AWS S3:** Object storage in AWS. Cheap and durable. Used for data lakes and checkpoints.

**Databricks:** A managed Spark and lakehouse platform. It adds Delta Lake, job scheduling, and governance.

**Microsoft Fabric:** A unified analytics platform from Microsoft that combines data engineering, data science, and BI. DP-700 validated my skills on the data engineering side.

**SingleStore:** A distributed SQL database that can handle both transactional and analytical workloads.

**MongoDB:** A document NoSQL database. Good for flexible, nested data.

**PostgreSQL / MySQL:** Relational databases. Used for structured transactional data.

### DevOps & Cloud

**Docker:** Packages code + dependencies into a container so it runs the same everywhere.

**Kubernetes:** Orchestrates containers at scale. I know the basics but still learning production operations.

**Terraform:** Declarative infrastructure-as-code tool. Define resources in HCL, Terraform creates and manages them.

**Ansible:** Configuration management tool for automating server setup.

**CI/CD:** Continuous Integration (test and build on every change) and Continuous Deployment (release automatically after tests pass).

**GitLab CI/CD:** GitLab's built-in CI/CD. I used it for parent-child pipelines.

**GitHub Actions:** GitHub's CI/CD. I used it for the open-source projects.

**HashiCorp Vault:** Secrets management tool. I used it to keep credentials out of code and config.

**AWS Lambda:** Serverless function service. Run code in response to events without managing servers.

**AWS EC2:** Virtual machines in AWS.

**GCP BigQuery:** Serverless analytical data warehouse in Google Cloud.

**GCP GKE:** Managed Kubernetes service in Google Cloud.

### AI / LLM

**RAG (Retrieval-Augmented Generation):** Retrieve relevant documents first, then ask the LLM to generate an answer based on that context.

**LLM (Large Language Model):** A model trained on large text corpora that can generate or summarize text.

**Vector database:** A database optimized for storing and searching embeddings by similarity.

**ChromaDB:** An open-source vector database. Easy to run locally.

**sentence-transformers:** Library to convert text into dense vector embeddings.

**Embedding:** A numerical vector that represents the meaning of text. Similar texts have similar vectors.

**FastAPI:** A modern Python web framework for building APIs. Async-friendly and auto-generates OpenAPI docs.

**Streamlit:** A Python library for quickly building data apps and UIs.

**OpenAI API:** Access to models like GPT-4.

**Ollama:** Tool to run open-source LLMs locally.

### Testing & Quality

**pytest:** A Python testing framework with fixtures, parametrization, and plugins.

**unittest:** Python's built-in testing framework. I used it for the pipeline test classes.

**Mocking:** Replacing real dependencies with fake ones in tests.

**Fixture:** Reusable test setup, like an in-memory SparkSession.

**Code coverage:** Percentage of code exercised by tests. We target 95%+.

**Integration test:** Tests that multiple components work together.

**Unit test:** Tests a single function or class in isolation.

---

## 5. Certifications — how to talk about them

### DP-700: Implementing Data Engineering Solutions using Microsoft Fabric
- **What it proves:** I can use Microsoft Fabric for data engineering — notebooks, pipelines, Lakehouses, and dataflows.
- **Say:** "I passed DP-700, which validated my ability to build lakehouse and data pipeline workloads in Microsoft Fabric. It's useful for roles in Microsoft-heavy environments."
- **Month/year:** Dec 2025

### Databricks Certified Data Engineer Associate
- **What it proves:** Lakehouse platform, Delta Lake, ETL with Apache Spark, and Databricks job orchestration.
- **Say:** "This certification gave me a strong foundation in Delta Lake, Spark, and Databricks workspace operations. I applied it directly to my work."
- **Month/year:** Dec 2024

### Databricks PySpark Streaming Training (8 Weeks)
- **What it proves:** Hands-on training with PySpark Structured Streaming.
- **Say:** "I completed an 8-week Accenture training on PySpark streaming. It deepened my understanding of watermarks, checkpointing, and exactly-once."
- **Period:** Dec 2023 – Feb 2024

### Google Data Analytics Professional Certificate
- **What it proves:** Data cleaning, SQL, R, and visualization.
- **Say:** "This was my early certificate. It solidified my data cleaning, SQL, and storytelling skills."
- **Year:** 2023

### NPTEL Management Information System
- **What it proves:** Understanding of management information systems.
- **Say:** "I completed an NPTEL course on Management Information Systems with Elite status and 73% score. It helped me understand how data systems support business decisions."
- **Period:** Jul – Oct 2022

---

## 6. Common interview questions — short answers

### Behavioral

**Q: Tell me about yourself.**
"I'm Sasidhar, a Data & AI Platform Engineer at Accenture. For two years I've been building a configuration-driven PySpark CDP platform covering 90+ production jobs, 67 SDPs, and 120+ CDPs. I work with Spark, Docker, GitLab CI/CD, Kafka, and Vault. On the side I've built a RAG chatbot and a Kafka → PySpark → Delta Lake streaming pipeline with AWS and Terraform. I'm looking for a Data Platform Engineer role where I can own the full lifecycle."

**Q: Why data engineering?**
"I like the intersection of software engineering and business impact. A well-built data platform makes every downstream analyst, ML engineer, and product manager faster. That's visible impact."

**Q: Why are you leaving Accenture?**
"I'm grateful for the scale and learning at Accenture, but I want to work in a product company where I can own a narrower, deeper data platform and ship at a faster pace."

**Q: Tell me about a failure.**
"Early on, I assumed a schema was stable and didn't add graceful handling for new fields. When upstream added a field, the job failed. I added permissive schema validation and a quarantine path. Now schema changes don't cause outages."

**Q: Tell me about a time you influenced someone.**
"I had to convince the team to move from copy-paste notebooks to a config-driven platform. I ran a two-week pilot, measured deployment time and defect rate, and showed the improvement. After that, the team adopted it."

**Q: Where do you see yourself in 3-5 years?**
"I want to become a Senior Data Platform Engineer or Staff Engineer who can design the architecture, mentor a team, and influence the data platform roadmap."

### Technical

**Q: How do you test Spark jobs?**
"I create an in-memory SparkSession with `local[*]`, then write unittest classes. I use mocking for external services and write pure functions for transformations so I can test them in isolation. We keep 95%+ coverage."

**Q: What's the difference between Kafka and Azure Event Hubs?**
"Kafka is open-source and self-managed or managed by Confluent. Event Hubs is Azure-managed, Kafka-compatible, and auto-scales. Both are distributed logs. I pick Event Hubs for Azure-native projects and Kafka for open stacks."

**Q: Delta Lake vs Parquet?**
"Parquet is a columnar file format. Delta Lake is Parquet plus a transaction log that gives ACID, time travel, and schema enforcement. For production lakehouses, I choose Delta."

**Q: How do you handle secrets?**
"I store secrets in HashiCorp Vault. At runtime the job requests a credential with a short-lived lease. Nothing is hard-coded in code or Git."

**Q: What's the difference between ETL and ELT?**
"ETL transforms before loading; ELT loads raw then transforms. ELT is common in data lakes because storage is cheap and transformations can be SQL-based later. ETL is useful when data must be clean before it reaches the target."

**Q: What is a lakehouse?**
"A lakehouse combines the low cost and flexibility of a data lake with the reliability and performance of a data warehouse. Delta Lake is the key technology."

**Q: What is RAG?**
"Retrieval-Augmented Generation. Retrieve relevant documents, feed them as context to an LLM, then generate an answer. It reduces hallucinations and keeps answers current."

**Q: How do you monitor pipelines?**
"I look at job duration, row counts, late/missing data, error rates, and quarantine volume. I set CloudWatch or GitLab alerts so the team knows before business users."

### Situational

**Q: A pipeline is slow. Walk me through debugging.**
"First I check the Spark UI for stages that take the most time. Then I look for skew, too many small files, or repeated reads. I add partitioning, caching, or predicate pushdown. I rerun with a subset of data to measure improvement."

**Q: A job starts failing after months of running fine.**
"I check recent changes — code, config, schema, and source volume. I look at logs for the exact error. If it's a schema change, I update the validation or quarantine logic. If it's data volume, I tune partitioning."

**Q: The business wants a new metric by tomorrow.**
"I check if the required source data already exists. If yes, I add a transformation in the config-driven pipeline and run tests. If not, I explain the dependencies and timeline. I never release untested code to production."

---

## 7. Behavioral STAR stories (keep to 90-120 seconds)

### Story 1 — Config-driven CDP platform (leadership + impact)
- **Situation:** 90+ hard-coded PySpark jobs, slow releases.
- **Task:** Build a config-driven platform.
- **Action:** JSON configs, reusable Python modules, parent-child GitLab CI/CD, Vault for secrets, unittest coverage.
- **Result:** 40-70% faster deployments, 99.5% uptime, 5+ enterprise products.

### Story 2 — 99.5% uptime (reliability)
- **Situation:** Downstream dashboards break when pipelines fail.
- **Task:** Keep 90+ jobs reliable.
- **Action:** Standardized logging, retries, checkpointing, runbooks, unit tests, monitoring.
- **Result:** 99.5% uptime, 60% fewer incidents, MTTR under 30 minutes.

### Story 3 — 95%+ unit-test coverage (quality)
- **Situation:** Spark testing was seen as too hard.
- **Task:** Make tests fast and reliable.
- **Action:** In-memory Spark fixtures, pure functions, mocks for Kafka/Delta/API, GitLab CI gates.
- **Result:** 95%+ coverage, 60+ test suites, CI under 5 minutes, fewer production bugs.

### Story 4 — Cloud migration with Terraform (DevOps)
- **Situation:** Local streaming pipeline needed cloud deployment.
- **Task:** Deploy Kafka → PySpark → Delta on AWS.
- **Action:** Terraform for MSK Serverless, EMR Serverless, S3, IAM, CloudWatch, SNS; GitHub Actions for CI.
- **Result:** Reproducible infrastructure, monitoring before first run, clear cost guardrails.

### Story 5 — RAG chatbot (AI + privacy)
- **Situation:** Answer questions over private docs without sending data to OpenAI.
- **Task:** Build local-first RAG.
- **Action:** FastAPI, ChromaDB, sentence-transformers, OpenAI/Ollama swap, caching.
- **Result:** 85% retrieval accuracy, 70% fewer API calls, documents stay local.

### Story 6 — Schema drift (problem solving)
- **Situation:** Upstream added fields, parser broke.
- **Task:** Make pipeline resilient.
- **Action:** Permissive schema with required subset, quarantine path, schema registry in config, alerts on quarantine volume.
- **Result:** Zero data loss, downstream consumers shielded.

---

## 8. Questions to ask the interviewer

1. What does the day-to-day of this role look like?
2. What is the biggest data platform challenge the team is solving right now?
3. How do you test Spark / data pipelines here?
4. What's the current lakehouse or warehouse stack?
5. How do data engineers work with ML / AI teams?
6. What does success look like in the first 90 days?
7. Is there an on-call rotation?
8. What are the next hiring priorities for the team?

---

## 9. Final reminders before every interview

- **Quantify:** 90+ jobs, 99.5% uptime, 95%+ coverage, 67/120+ SDPs/CDPs, 40-70% faster deployments.
- **Own the story:** Don't say "we" for everything. Say what *you* did, where appropriate.
- **Pause and clarify:** If you don't understand a question, ask for clarification. Better than guessing.
- **Be honest about what you built vs what the team built.** Don't over-claim.
- **Keep answers to 90-120 seconds.** Let the interviewer dig deeper.
- **Use these notes, don't memorize them.** Sound natural.

---

**Last updated:** July 2026
