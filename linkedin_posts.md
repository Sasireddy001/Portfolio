# LinkedIn Technical Posts — Sasidhar Mopuru

Copy and paste these posts directly into LinkedIn. Schedule them across 2–3 weeks for consistent visibility.

---

## Post 1 — Production PySpark + Kafka at Accenture

Just wrapped up another quarter operating a configuration-driven Core Data Product (CDP) platform at Accenture.

What that means in numbers:
- 90+ production PySpark ETL jobs
- 67 Source Data Products (SDPs) and 120+ Core Data Products (CDPs)
- 95%+ test coverage across 60+ pytest suites
- 99.5% pipeline uptime
- 40% faster deployments after moving to JSON-based job definitions and parent-child GitLab CI/CD pipelines

The biggest lesson? Production data engineering is not just about writing PySpark. It is about modular Python utilities, schema validation, retry logic, secrets management with HashiCorp Vault, and testing discipline.

If you are building data platforms, I would love to hear what has worked for you.

#DataEngineering #PySpark #Kafka #DeltaLake #Databricks #DataPlatform #ETL #CI/CD #Accenture

---

## Post 2 — Kafka → PySpark → Delta Lake Pipeline

I open-sourced a production-style streaming data pipeline: Kafka → PySpark → Delta Lake.

What it includes:
- JSON schema enforcement and validation
- Watermark-based deduplication with exactly-once semantics
- Checkpointing and Delta Lake idempotent writes
- Environment-driven configuration for Databricks / local / EMR Serverless
- 95%+ pytest coverage with an in-memory Spark fixture
- Throughput benchmark: 31k–45k rows/sec on a 4-core laptop

I also added an AWS deployment using MSK Serverless + EMR Serverless + S3, fully managed with Terraform and GitHub Actions.

Repository link in the comments. Let me know if you want a deep-dive thread.

#ApacheKafka #PySpark #DeltaLake #Databricks #StreamingData #DataEngineering #AWS #Terraform

---

## Post 3 — RAG with FastAPI, ChromaDB, and Ollama

I built a RAG Document QA chatbot that answers questions over your own documents.

Stack:
- FastAPI for the backend
- Streamlit for the UI
- ChromaDB for vector storage
- Sentence-Transformers for embeddings
- Ollama or OpenAI for the LLM

Why this matters: instead of sending private documents to a third-party API, you can run the embedding model and LLM locally, keep data in-house, and still get grounded answers.

The repo is open-source. I documented the architecture and system design decisions, and I added pytest tests with mocked LLM/embedding calls to keep CI fast.

If you are exploring RAG or LLM data systems, I would love to connect.

#RAG #LLM #ChromaDB #FastAPI #Streamlit #Ollama #OpenAI #VectorDB #AIEngineering

---

## Post 4 — Databricks Data Engineer Associate — My Notes

I passed the Databricks Data Engineer Associate exam last year. Here is what actually helped:

1. Spend time in a real Databricks workspace, not just reading docs.
2. Understand Delta Lake `OPTIMIZE`, `VACUUM`, `MERGE`, and time travel cold.
3. Know the difference between `append`, `complete`, and `update` output modes in Structured Streaming.
4. Review Unity Catalog vs. Hive metastore grants and securables.
5. Do practice tests, then review every wrong answer.

The exam is scenario-based. It tests whether you can pick the right tool for the problem, not whether you can memorize syntax.

I wrote a full study guide with my week-by-week plan. Link in comments.

#Databricks #DataEngineering #PySpark #DeltaLake #Certification #Lakehouse #CareerGrowth

---

## Post 5 — Cloud-Native Streaming Data Platform on Azure

I built a cloud-native streaming data platform using Azure Event Hubs, Databricks, ADLS Gen2, Delta Lake, and Terraform.

Key features:
- Multi-environment Terraform modules (dev/prod)
- PySpark Structured Streaming with watermark-based deduplication
- Delta Lake checkpointing and exactly-once writes
- GitHub Actions CI/CD for infrastructure and application code
- 99.9% data accuracy target

The goal was to demonstrate how to move a local streaming pipeline into a real cloud environment without losing reliability.

If you are designing similar systems, what is your go-to stack?

#Azure #Databricks #DeltaLake #Terraform #DataPlatform #CloudEngineering #GitHubActions

---

## Post 6 — Why I Care About Test Coverage in Data Engineering

In a typical ETL project, failures show up late: stale dashboards, bad reports, angry stakeholders.

I have been pushing for **pytest + mocking** for data pipelines at Accenture. The result:
- 60+ unit test suites
- 95%+ overall coverage
- 60% fewer production incidents

Mocks let you test Spark transformations without a real cluster. CI catches regressions before they reach production.

Data engineering deserves the same testing discipline as backend engineering.

#DataEngineering #PyTest #DataQuality #Testing #ETL #PySpark #DataPlatform

---

## Post 7 — From Data Engineer to Data Platform Engineer

Two years ago I was writing SQL and Python scripts. Today I operate a configuration-driven CDP platform with PySpark, Kafka, Delta Lake, GitLab CI/CD, and HashiCorp Vault.

The shift from "building one pipeline" to "building a system that builds pipelines" changes how you think about:
- Reusable modules and JSON-based job definitions
- Environment-driven configuration
- Automated testing at scale
- Secrets management and governance

The title changed, but the real change was moving from task execution to platform thinking.

#DataPlatform #DataEngineering #CareerGrowth #PySpark #DataArchitecture #PlatformEngineering

---

## Post 8 — Building AI-Ready Data Systems

AI does not fix bad data. It exposes it.

Every RAG chatbot, LLM agent, and ML model is downstream of a data pipeline. If the pipeline is slow, inconsistent, or untested, the AI layer will fail.

That is why I focus on:
- Exactly-once streaming with Kafka and Delta Lake
- Schema enforcement at ingestion
- Partitioning and caching for query speed
- CI/CD and testing for data products

Clean, well-modeled, and well-tested data is the real AI infrastructure.

#AI #LLM #RAG #DataEngineering #DataPlatform #MLOps #DataQuality #PySpark

---

## Post 9 — Open Source Is My Portfolio

I used to think a portfolio was a website. Now I believe a portfolio is public, versioned work.

My GitHub repos include:
- Kafka → PySpark → Delta Lake pipeline with architecture and system design docs
- Cloud-native streaming platform on Azure with Terraform
- RAG QA chatbot with FastAPI, ChromaDB, and Ollama

Each one has:
- README with architecture diagrams
- ARCHITECTURE.md and SYSTEM_DESIGN.md
- CI/CD with GitHub Actions
- pytest suites

It is not perfect, but it is honest, documented, and reproducible.

#OpenSource #GitHub #DataEngineering #DataPlatform #Portfolio #AI #PySpark

---

## Post 10 — What I Learned From 90+ Production PySpark Jobs

After operating 90+ production PySpark jobs, here are 5 things I wish I knew earlier:

1. **Configuration beats code.** JSON-based job definitions let you add pipelines without releases.
2. **Test your transforms, not just the end-to-end job.** Unit tests with mocked Spark are fast and reliable.
3. **Partition by business time, not ingestion time.** Your future self will thank you when queries are 10x faster.
4. **Secrets belong in Vault, not in notebooks or env files.** Security is part of platform engineering.
5. **Observability is non-negotiable.** Logs, metrics, and checkpointing are as important as the DAG.

What would you add?

#PySpark #DataEngineering #DataPlatform #ETL #ProductionEngineering #DataOps
