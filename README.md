<div align="center">

# Sasidhar Mopuru

### Data & AI Platform Engineer | Databricks Certified | Kafka · PySpark · Delta Lake · Python

[![Live Portfolio](https://img.shields.io/badge/Live%20Portfolio-sasireddy001.github.io%2FPortfolio-4ade80?logo=githubpages&logoColor=white)](https://sasireddy001.github.io/Portfolio)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org)
[![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white)](https://databricks.com)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-00ADD8?logo=delta&logoColor=white)](https://delta.io)
[![GitHub  Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Resume](https://img.shields.io/badge/Resume-PDF-critical?logo=adobeacrobatreader&logoColor=white)](https://sasireddy001.github.io/Portfolio/SASIDHAR_RESUME.pdf)

</div>

## About Me

I am a **Data & AI Platform Engineer** with 2+ years of experience building production-grade streaming data products and lakehouse systems at Accenture. I specialize in turning high-velocity event data into reliable, AI-ready data platforms.

Currently, I build and operate a configuration-driven **Core Data Product (CDP) platform** across 4 E2E supply-chain sub-domains (site, supplier, item, product). My work spans **90+ production PySpark ETL jobs** supporting **67 Source Data Products (SDPs)** and **120+ Core Data Products (CDPs)**, dynamic CI/CD generation, enterprise secrets management with HashiCorp Vault, and automated testing that reaches **95%+ overall code coverage** across 60+ test suites.

- **Configuration-driven platforms:** YAML-based job definitions, dynamic GitLab CI/CD generators, multi-environment deployments
- **Real-time pipelines:** Kafka → PySpark → Delta Lake with exactly-once processing
- **Cloud & Lakehouse platforms:** Databricks, Apache Spark, schema enforcement, data quality
- **AI-ready data engineering:** Evaluation systems, RAG data foundations, and agentic pipelines
- **Production discipline:** CI/CD, automated testing, modular configuration-driven code, enterprise security

I am actively expanding into **Cloud, DevOps, Platform Engineering, and AI/LLM systems** — roles where strong data-engineering fundamentals are a force multiplier.

## What I Build

End-to-end streaming data platforms that feed analytics, ML, and generative AI applications — with the reliability, testability, and observability production systems demand.

## Target Roles

Cloud Data Engineer · Data Platform Engineer · AI Engineer · Solutions Architect · DevOps Engineer (data-platform focus)

## Professional Experience

### Data Engineer – Accenture
*Feb 2024 – Present*

- Built configuration-driven Core Data Product (CDP) platform reducing deployment time by **70%**.
- Designed end-to-end data flows from source systems to SDP and CDP layers for **90+ production PySpark ETL jobs** across 4 E2E supply-chain sub-domains, supporting **67 SDPs and 120+ CDPs**.
- Developed PySpark pipelines with JSON-based job definitions achieving **99.5% pipeline uptime**.
- Containerized Spark jobs with Docker and deployed through GitLab CI/CD across dev, sit, perf, prod environments.
- Integrated Kafka eventing and S3A-compatible object storage into pipeline workflows.
- Managed secrets and credentials securely using HashiCorp Vault and enterprise certificate stores.
- Built Kafka-based JSON ingestion pipelines into a lakehouse architecture.
- Implemented comprehensive testing strategy with **60+ unit test suites** achieving **95%+ overall code coverage**.
- Created DDL scripts and configuration-driven workflows using Git.
- Performed data validation, debugging, and performance optimization reducing latency by 30%.
- Worked under strict NDA and enterprise data governance standards.

## Selected Projects

### Enterprise Configuration-Driven Data Platform
*Feb 2024 – Present*

- Built and operated enterprise-grade configuration-driven data platform with **90+ production PySpark ETL jobs** across 4 E2E supply-chain sub-domains (site, supplier, item, product), supporting **67 Source Data Products (SDPs)** and **120+ Core Data Products (CDPs)**. Implemented STG, Active, and Historical job patterns for physical data products and view-based CDPs, with Kafka-driven streaming ingestion for SDP stage jobs. Collaborated with a 10+ person cross-functional team (Accenture and client).
- Designed dynamic CI/CD configuration generator with **YAML-based job definitions** enabling non-technical users to configure data pipelines without code changes.
- Implemented parent-child **GitLab CI/CD pipeline architecture** with dynamic child pipeline generation for scalable deployment orchestration.
- Integrated **HashiCorp Vault** for enterprise secrets management and implemented secure logging decorators with sensitive data sanitization.
- Created comprehensive testing strategy with **60+ unit test suites** achieving **95%+ overall code coverage** on pipeline components.
- Achieved **99.5% deployment success rate** and **99.5% pipeline uptime** across 4 environments (dev, sit, perf, prod).
- Reduced pipeline configuration time by **70%** and production incidents by **60%** through automation and comprehensive testing.

**Technologies:** PySpark, GitLab CI/CD, Docker, YAML, Python, HashiCorp Vault, pytest, Configuration-Driven Design

### RAG Document QA Chatbot
*Jul 2026*

- Built a retrieval-augmented generation (RAG) app with **FastAPI**, **Streamlit**, **ChromaDB**, and OpenAI/local LLMs.
- Implemented document ingestion, chunking, sentence-transformer embeddings, dense retrieval, and LLM answer generation.
- Achieved **85% retrieval accuracy**, reduced API calls by **70%** through caching, and built a **85% coverage** pytest suite with mocked LLM/embeddings components.
- Deployed with GitHub Actions CI and modular, environment-driven architecture.

**Links:** [Repository](https://github.com/Sasireddy001/rag-document-qa)

### Production-Style Kafka PySpark Delta Pipeline
*Jul 2026*

- Built a production-style streaming pipeline ingesting JSON events from **Apache Kafka**, transforming them with **PySpark Structured Streaming**, and writing to **Delta Lake**.
- Enforced JSON schemas, watermark-based deduplication, and exactly-once semantics with checkpointing.
- Benchmarked at **31k–45k rows/sec** on a 4-core laptop; achieved **90% pytest coverage** with in-memory Spark fixture, sample data generator, and GitHub Actions CI.
- Designed to run on Databricks, a Spark cluster, or locally.

**Links:** [Repository](https://github.com/Sasireddy001/Kafka-pyspark-delta-pipeline)

### Cloud-Native Streaming Data Platform
*Jul 2026*

- Designed a cloud-native streaming platform using **Azure Event Hubs**, **Databricks**, **ADLS Gen2**, and **Delta Lake**.
- Created **Terraform** modules for multi-environment IaC (dev/prod) and GitHub Actions CI for automated deployment.
- Implemented PySpark streaming with watermark-based deduplication, schema enforcement, and Delta Lake checkpointing.
- Demonstrated cloud data-platform engineering and infrastructure automation skills.

**Links:** [Repository](https://github.com/Sasireddy001/Cloud-data-platform)

## Certifications

| Certification | Issuer |
|---|---|
| DP-700: Implementing Data Engineering Solutions using Microsoft Fabric | Microsoft |
| Databricks Certified Data Engineer Associate | Databricks |
| Databricks PySpark Streaming Training – 8 Weeks | Accenture |
| Google Data Analytics Professional Certificate | Coursera |
| NPTEL MIS | IIT Madras |

## Technical Skills

- **Programming:** Python, SQL, PySpark
- **Data Engineering:** Apache Kafka, PySpark Streaming, ETL/ELT Pipelines, Data Ingestion, Data Transformation, Batch & Streaming Processing, Microsoft Fabric
- **AI / LLM / App Development:** RAG, LLM, FastAPI, Streamlit, ChromaDB, Vector Databases, GenAI, AI Agents
- **Data Platforms:** Databricks, Apache Spark, Delta Lake, SingleStore, Relational Databases
- **Quality & Testing:** Pytest, Unittest, Mocking, Data Validation, Schema Validation
- **DevOps & Tools:** Git, CI/CD Pipelines (GitHub Actions, GitLab CI), Docker, Kubernetes, Terraform, HashiCorp Vault, Jira, Agile Scrum
- **Architecture:** Object-Oriented Programming, Modular Coding, YAML/JSON, Logging, Exception Handling, System Design, Platform Engineering, Observability
- **Building Toward:** Cloud (AWS/Azure), Advanced Kubernetes, Production LLM Evaluation, AI Agents

## Education & Achievements

- B.Tech in Computer Science and Engineering – CGPA 7.99
- JEE Mains – 94.14 Percentile
- **Enterprise Data Platform Engineer at Accenture:** Built and operated 90+ production PySpark ETL jobs supporting 67 SDPs and 120+ CDPs, achieved 95%+ overall test coverage, and reduced deployment time by 70% through dynamic CI/CD automation

## GitHub Stats

<div align="center">

![GitHub stats](https://github-readme-stats.vercel.app/api?username=Sasireddy001&show_icons=true&theme=default)
![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Sasireddy001&layout=compact)

</div>

## Contact

- Portfolio: [sasireddy001.github.io/Portfolio](https://sasireddy001.github.io/Portfolio)
- Resume: [PDF](https://sasireddy001.github.io/Portfolio/SASIDHAR_RESUME.pdf)
- Email: [sasidharmopuru@gmail.com](mailto:sasidharmopuru@gmail.com)
- GitHub: [@Sasireddy001](https://github.com/Sasireddy001)
- LinkedIn: [linkedin.com/in/sasidhar-mopuru-417a03233](https://www.linkedin.com/in/sasidhar-mopuru-417a03233)
- Location: India
- Open to global remote Data & AI roles
