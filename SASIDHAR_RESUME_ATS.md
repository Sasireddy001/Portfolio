SASIDHAR MOPURU
Bengaluru, India | sasidharmopuru@gmail.com | +91-63029-60712
linkedin.com/in/sasidhar-mopuru-417a03233 | github.com/Sasireddy001 | sasireddy001.github.io/Portfolio


PROFESSIONAL SUMMARY
Data and AI Platform Engineer with 2+ years of experience building and validating production-grade streaming data pipelines and lakehouse systems at Accenture. Databricks Certified Data Engineer Associate and Microsoft DP-700. Core stack includes PySpark, Apache Spark, Delta Lake, Apache Kafka, Databricks, Microsoft Fabric, Python, and SQL. Delivered 90+ production PySpark ETL jobs, achieved 99.5% pipeline uptime, and reduced deployment time by 40% across 4 end-to-end supply chain sub-domains.


SKILLS
- Languages: Python, SQL
- Data Engineering: PySpark, Apache Spark, Delta Lake, Apache Kafka, ETL/ELT, Data Modeling, Data Quality, Schema Validation
- Cloud and Platforms: Databricks, Microsoft Fabric, Azure Event Hubs, ADLS Gen2, AWS (S3, EMR Serverless, MSK Serverless)
- DevOps: GitLab CI/CD, GitHub Actions, Docker, Terraform, Linux, pytest, Jira
- AI/LLM: RAG, OpenAI, ChromaDB, Vector Databases, Sentence-Transformers, FastAPI, Streamlit


PROFESSIONAL EXPERIENCE

Data Engineer, Management and Governance Analyst -- Accenture
Feb 2024 - Present (Associate to Analyst, Feb 2026, effective March 2026) | Bengaluru, India

- Delivered 90+ production PySpark ETL jobs across 4 end-to-end supply-chain sub-domains, supporting 67 SDPs and 120+ CDPs through Python development, JSON configuration, and DDL development.
- Led 12 change requests across 14 CDPs and completed tag validations for 40+ SDPs in a single day by comparing design documents, Kafka messages, and data across SDP STG -> ACTIVE -> HIST and SDP Active -> CDP STG -> ACTIVE -> HIST flows.
- Worked in a 7-member E2E supply-chain data engineering team (1 lead, 1 tester, 5 DEs) covering site, supplier, item, and product sub-domains; primarily owned site and supplier pipelines while supporting item and product live monitoring.
- Managed full lifecycle of each physical data product: PySpark/Python main scripts, JSON configs, unit tests, SingleStore tables, Delta Lake lakehouse tables (with catalog and schemas), Control-M scheduling, IOMate job orchestration, and Acceldata monitoring across DEV, SIT, and PROD.
- Reduced deployment time by 40% by developing configuration-driven pipeline definitions and reusable Python utilities used by the CDP/SDP platform and consumed by existing CI/CD workflows.
- Achieved 99.5% pipeline uptime through modular PySpark pipelines with error handling, retry logic, schema validation, and data quality checks.
- Maintained 95%+ overall test coverage across 60+ pytest suites with mocked components and integration patterns.
- Improved data processing latency by 30% through partitioning, caching, and performance tuning on production pipelines.
- Owned end-to-end data quality and platform validation for 3-4 sprint releases as the primary validation resource, validating schemas, tags, record counts, primary keys, business hash keys, and duplicate records across Kafka -> Stage -> Raw -> HAST/CDP layers, and preparing SQL-based reconciliation evidence for clean production sign-off.
- Developed Kafka consumer and validation workflows for real-time event processing, schema validation, and end-to-end data verification using Kafka topic messages.
- Developed DDL scripts, database object definitions, and validation queries for SDP/CDP layers using Python, SQL, and Git.
- Monitored and troubleshot production data pipelines, performing job monitoring, data-load validation, and production issue analysis.
- Used Jira dashboards to track sprint tasks, incidents, and maintenance activities for 90+ production data products.
- Developed SDPs from design documents and built CDPs based on SDP schemas, applying transformation queries when multiple source SDPs feed a single CDP; maintained per-schema exception tables to capture invalid records with target table reference, error log, and timestamp.


PROJECTS

Production-Style Kafka PySpark Delta Pipeline | github.com/Sasireddy001/Kafka-pyspark-delta-pipeline
- Ingested JSON events from Kafka, enforced schemas, and wrote exactly-once to Delta Lake using checkpointing and idempotent writes.
- Benchmarked 31k-45k rows/sec on a 4-core laptop for 100k-1M row workloads.
- Maintained pytest test coverage with an in-memory Spark fixture and continuous integration.
- Tech: Apache Kafka, PySpark, Delta Lake, Databricks, GitHub Actions

RAG Document QA Chatbot | github.com/Sasireddy001/rag-document-qa
- Built a retrieval-augmented generation application with document ingestion, chunking, dense vector retrieval, response caching, and LLM answer generation.
- Implemented response caching to reduce redundant LLM API calls and a configurable, environment-driven architecture.
- Shipped pytest tests with mocked LLM/embedding calls, FastAPI endpoints, and a Streamlit chat UI.
- Tech: FastAPI, Streamlit, ChromaDB, OpenAI, Sentence-Transformers

Cloud-Native Streaming Data Platform | github.com/Sasireddy001/Cloud-data-platform
- Designed modular Terraform templates for multi-environment (dev/prod) infrastructure and a PySpark Structured Streaming job that ingests Azure Event Hubs events, applies watermark-based deduplication, and writes to Delta Lake with checkpointing.
- Automated Terraform plan/apply pipelines through GitHub Actions for dev and prod environments.
- Tech: Azure Event Hubs, Databricks, ADLS Gen2, Delta Lake, Terraform, GitHub Actions


EDUCATION
B.Tech in Computer Science and Engineering -- Madanapalle Institute of Technology and Science, 2023
- CGPA: 7.99
- JEE Mains: 94.14 Percentile (Top 6% nationally)
- Graduated with Distinction


CERTIFICATIONS
- DP-700: Implementing Data Engineering Solutions using Microsoft Fabric -- Microsoft, Dec 2025
- Databricks Certified Data Engineer Associate -- Databricks, Dec 2024
- Databricks PySpark Streaming Training (8 Weeks) -- Accenture, Dec 2023 - Feb 2024
- Google Data Analytics Professional Certificate -- Coursera, 2023
- NPTEL Management Information System (MIS) -- Elite, 73% -- IIT Kharagpur, Jul-Oct 2022
