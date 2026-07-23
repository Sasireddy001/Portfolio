# SASIDHAR MOPURU

**Data & AI Platform Engineer | Databricks Certified | PySpark · Kafka · Delta Lake · Python | Building Real-Time Streaming & AI-Ready Data Systems**

Bengaluru, India | +91 63029 60712 | sasidharmopuru@gmail.com  
[LinkedIn](https://www.linkedin.com/in/sasidhar-mopuru-417a03233) | [GitHub](https://github.com/Sasireddy001) | [Portfolio](https://sasireddy001.github.io/Portfolio/)

---

## SUMMARY

Data & AI Platform Engineer with 2+ years of experience building production-grade data pipelines, streaming platforms, and lakehouse systems at Accenture. Proven track record delivering 90+ PySpark ETL jobs across 67 source data products and 120+ core data products, with 99.5% uptime and 95%+ test coverage. Databricks DE Associate and DP-700 (Microsoft Fabric) certified. Expanding into cloud-native data platforms, RAG/LLM applications, and platform engineering.

---

## EXPERIENCE

### **Data Engineer — Accenture** | *Feb 2024 – Present | Bengaluru, India*

- **Delivered** 90+ production PySpark ETL jobs across 4 end-to-end supply-chain sub-domains, supporting **67 SDPs** and **120+ CDPs** through Python development, JSON configuration, and DDL development.
- **Reduced deployment time by 40%** by developing configuration-driven pipeline definitions and reusable Python utilities used by the CDP/SDP platform and consumed by existing CI/CD workflows.
- **Achieved 99.5% pipeline uptime** through modular PySpark pipelines with error handling, retry logic, schema validation, and data quality checks.
- **Maintained 95%+ overall test coverage** across 60+ pytest suites with mocked components and integration patterns.
- **Improved data processing latency by 30%** through partitioning, caching, and performance tuning on production pipelines.
- **Owned end-to-end data quality and platform validation** for 3–4 sprint releases as the primary validation resource, validating schemas, tags, record counts, primary keys, business hash keys, and duplicate records across Kafka → Stage → Raw → HAST/CDP layers, and preparing SQL-based reconciliation evidence for clean production sign-off.
- **Developed Kafka consumer and validation workflows** for real-time event processing, schema validation, and end-to-end data verification using Kafka topic messages.
- **Developed DDL scripts, database object definitions, and validation queries** for SDP/CDP layers using Python, SQL, and Git.
- **Monitored and troubleshot production data pipelines**, performing job monitoring, data-load validation, and production issue analysis.

---

## PROJECTS

### **Cloud-Native Streaming Data Platform** | [GitHub](https://github.com/Sasireddy001/Cloud-data-platform)
*Azure Event Hubs · Databricks · ADLS Gen2 · Delta Lake · Terraform*

- **Designed** modular Terraform templates for multi-environment (dev/prod) infrastructure and a PySpark Structured Streaming job that ingests Azure Event Hubs events, applies watermark-based deduplication, and writes to Delta Lake with checkpointing.
- **Automated** Terraform plan/apply pipelines through GitHub Actions for dev and prod environments.
- **Validated** streaming output with schema checks and row-level data quality checks.

### **Production-Style Kafka PySpark Delta Pipeline** | [GitHub](https://github.com/Sasireddy001/Kafka-pyspark-delta-pipeline)
*Apache Kafka · PySpark · Delta Lake · Databricks · GitHub Actions*

- **Ingested** JSON events from Kafka, enforced schemas, and wrote exactly-once to Delta Lake using checkpointing and idempotent writes.
- **Benchmarked** 31k–45k rows/sec on a 4-core laptop for 100k–1M row workloads.
- **Maintained** pytest test coverage with an in-memory Spark fixture and continuous integration.

### **RAG Document QA Chatbot** | [GitHub](https://github.com/Sasireddy001/rag-document-qa)
*FastAPI · Streamlit · ChromaDB · OpenAI · Sentence-Transformers*

- **Built** a retrieval-augmented generation application with document ingestion, chunking, dense vector retrieval, response caching, and LLM answer generation.
- **Implemented** response caching to reduce redundant LLM API calls and a configurable, environment-driven architecture.
- **Shipped** pytest tests with mocked LLM/embedding calls, FastAPI endpoints, and a Streamlit chat UI.

---

## EDUCATION

**B.Tech in Computer Science and Engineering** — *CGPA 7.99*  
JEE Mains — **94.14 Percentile (Top 6% nationally)**

---

## CERTIFICATIONS

- [DP-700: Implementing Data Engineering Solutions using Microsoft Fabric](https://learn.microsoft.com/api/credentials/share/en-us/MopuruSasidhar-4473/13AA53E82F21D70C?sharingId=57F4CD5FCA3B941E) — Microsoft (Dec 2025)
- [Databricks Certified Data Engineer Associate](https://credentials.databricks.com/550e3234-a017-4afd-a236-5d695da5c212?utm_source=whatsapp&utm_medium=social) — Databricks (Dec 2024)
- Databricks PySpark Streaming Training (8 Weeks) — Accenture (Dec 2023 - Feb 2024)
- [Google Data Analytics Professional Certificate](https://www.coursera.org/account/accomplishments/specialization/DAZFH4EUB7LG?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Ds12n) — Coursera (2023)
- [NPTEL Management Information System (MIS)](https://nptel.ac.in/noc/E_Certificate/NPTEL22MG100S5435012910114355) — Elite · 73% · IIT Kharagpur (Jul–Oct 2022)

---

## SKILLS

- **Languages:** Python, SQL
- **Data Engineering:** PySpark, Apache Spark, Delta Lake, Apache Kafka, ETL/ELT, Data Modeling, Data Quality, Schema Validation
- **Cloud & Platforms:** Databricks, Microsoft Fabric, Azure Event Hubs, ADLS Gen2, AWS (S3, EMR Serverless, MSK Serverless)
- **DevOps:** GitLab CI/CD, GitHub Actions, Docker, Terraform, Linux
- **AI / LLM:** RAG, LLM, FastAPI, Streamlit, ChromaDB, Vector Databases, OpenAI, Sentence-Transformers
- **Testing:** pytest, unittest, mocking, test-driven development
