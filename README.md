<div align="center">



# Sasidhar Mopuru



### Python | Automation | Data Engineering | System Integration



[![Live Portfolio](https://img.shields.io/badge/Live%20Portfolio-sasireddy001.github.io%2FPortfolio-4ade80?logo=githubpages&logoColor=white)](https://sasireddy001.github.io/Portfolio)

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org)

[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org)

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white)](https://databricks.com)

[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org)

[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-00ADD8?logo=delta&logoColor=white)](https://delta.io)

[![GitHub  Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)

[![Resume](https://img.shields.io/badge/Resume-View-2563EB)](https://sasireddy001.github.io/Portfolio/SASIDHAR_RESUME.html)



</div>



## Latest Updates



- **Cloud-ready deployment guide** added to the Kafka → PySpark → Delta Lake pipeline (local + Databricks).
- **Architecture and System Design docs** published for all major projects with Mermaid diagrams, scalability, fault tolerance, and tradeoff analysis.
- **New technical blog articles** on Kafka/PySpark/Delta Lake, RAG with FastAPI/ChromaDB, and the Databricks DE Associate journey.
- **10 ready-to-post LinkedIn technical posts** and a public cloud-native project roadmap.
- **One-page impact-driven HTML resume** with live certification verification links.

## About Me



I am a **Software Engineer** with experience in Python development, automation, data engineering, API integrations, ETL workflows, and enterprise platform support. I specialize in building automation solutions, developer tools, data validation frameworks, and integration systems.



- **Real-time pipelines:** Kafka → PySpark → Delta Lake with exactly-once processing

- **Cloud & Lakehouse platforms:** Databricks, Apache Spark, schema enforcement, data quality

- **AI-ready data engineering:** Evaluation systems, RAG data foundations, and agentic pipelines

- **Production discipline:** CI/CD, automated testing, modular configuration-driven code



I am actively expanding into **Cloud, DevOps, Platform Engineering, and AI/LLM systems** — roles where strong data-engineering fundamentals are a force multiplier.



## What I Build



End-to-end streaming data platforms that feed analytics, ML, and generative AI applications — with the reliability, testability, and observability production systems demand.

## Knowledge Base

I maintain [engineering-vault](https://github.com/Sasireddy001/engineering-vault-), a comprehensive knowledge management system that captures and organizes technical knowledge, patterns, and learnings across data engineering, AI/RAG, OSS research, technical writing, architecture patterns, certifications, and career development.

This serves as my second brain for systematic learning and knowledge preservation.



## Target Roles

Python Developer · Automation Engineer · Data Engineer · Backend Engineer · Platform Engineer · Full Stack Developer



## Professional Experience

### Data Engineer, Management & Governance Analyst — Accenture

*Feb 2024 – Present (Associate → Analyst, Feb 2026 (effective March 2026))*

- Delivered numerous production ETL jobs across multiple business domains through Python development, JSON configuration, and DDL development.
- Led change requests across data products and completed validations by comparing design documents, source messages, and data across multiple environments.
- Worked in cross-functional data engineering teams covering multiple business domains; owned data pipeline domains while supporting live monitoring.
- Managed full lifecycle of data products: PySpark/Python main scripts, JSON configs, unit tests, production database tables, Delta Lake lakehouse tables, enterprise scheduling tools, job orchestration platforms, and monitoring solutions across multiple environments.
- Improved deployment efficiency by developing configuration-driven pipeline definitions and reusable Python utilities used by the data platform and consumed by existing CI/CD workflows.
- Maintained high pipeline availability through modular PySpark pipelines with error handling, retry logic, schema validation, and data quality checks.
- Achieved comprehensive test coverage across pytest suites with mocked components and integration patterns.
- Optimized pipeline performance through partitioning, caching, and performance tuning strategies.
- Owned end-to-end data quality and platform validation for sprint releases, validating schemas, tags, record counts, primary keys, business hash keys, and duplicate records across data layers, and prepared SQL-based reconciliation evidence for clean production sign-off.
- Developed Kafka consumer and validation workflows, DDL scripts, and validation/reconciliation queries for real-time data processing, and monitored/troubleshot production pipelines.
- Developed data products from design documents and built downstream datasets based on source schemas, applying transformation queries when multiple source data products feed a single dataset; maintained per-schema exception tables to capture invalid records with target table reference, error log, and timestamp.

## Selected Projects

### DataOps Toolkit

*Aug 2026*

- Built an enterprise-grade CLI toolkit for SQL validation, lineage analysis, schema comparison, data quality auditing, and reporting.
- Implemented multi-dialect SQL parsing, column-level lineage analysis, Hive partition auditing, metadata profiling, and HTML report generation.
- Created comprehensive test suite with 23 tests, CLI interface with Typer, and rich terminal output with Rich library.
- Published to GitHub with B+ grade after maintainer audit focusing on code quality, documentation, and best practices.

**Links:** [Repository](https://github.com/Sasireddy001/dataops-toolkit)

### Dagster OSS Contribution

*Aug 2026*

- Fixed critical bug in Dagster's AssetNode parent_keys handling, improving data pipeline reliability for thousands of users.
- Added regression tests to prevent future issues and scoped warning suppression for async test execution.
- Submitted PR #34143 to the Dagster repository, demonstrating ability to work with large-scale open-source codebases.
- Followed contribution guidelines, wrote clear commit messages, and engaged with maintainers in code review process.

**Links:** [Pull Request](https://github.com/dagster-io/dagster/pull/34143)



### RAG Document QA Chatbot

*Jul 2026*



- Built a retrieval-augmented generation (RAG) application with **FastAPI**, **Streamlit**, **ChromaDB**, and local or OpenAI LLMs.

- Implemented document ingestion, text chunking, sentence-transformer embeddings, dense retrieval, and LLM answer generation.

- Designed an environment-driven, modular architecture with separate ingest, embed, vector-store, LLM, and query components.

- Created a pytest test suite with mocked embeddings and LLM calls, GitHub Actions CI, and architecture documentation.



**Links:** [Repository](https://github.com/Sasireddy001/rag-document-qa)



### Production-Style Kafka PySpark Delta Pipeline

*Jul 2026*



- Built a production-style streaming data pipeline that ingests JSON events from Apache Kafka, transforms them with PySpark Structured Streaming, and writes the results to Delta Lake.

- Implemented environment-driven configuration, JSON schema enforcement, checkpointing with exactly-once semantics, and watermark-based deduplication.

- Created a pytest unit-test suite with an in-memory Spark fixture, GitHub Actions CI, a sample data generator, and a throughput benchmark.

- Designed to run on Databricks, a Spark cluster, or locally for development.



**Links:** [Repository](https://github.com/Sasireddy001/Kafka-pyspark-delta-pipeline)



### Cloud-Native Streaming Data Platform

*Jul 2026*



- Designed and implemented a cloud-native streaming data platform using Azure Event Hubs, Databricks, ADLS Gen2, and Delta Lake.

- Created Terraform modules for infrastructure as code with multi-environment support (dev/prod), demonstrating cloud automation skills.

- Implemented a production-style PySpark streaming job with Azure Event Hubs integration, watermark-based deduplication, and Delta Lake checkpointing.

- Demonstrated cloud skills, platform engineering, and infrastructure automation capabilities for high-value data platform roles.



**Links:** [Repository](https://github.com/Sasireddy001/Cloud-data-platform)



## Open Source Contributions

**14+ Public Pull Requests** across major open-source projects including Dagster, urllib3, axios, fastify, strapi, tRPC, vitest, and jsdoc.

### Merged

| PR | Description | Merged |
|---|---|---|
| [dagster/dagster#34143](https://github.com/dagster-io/dagster/pull/34143) | fix: AssetNode parent_keys mutation bug | 2026-08-19 |
| [fastify/fastify#6880](https://github.com/fastify/fastify/pull/6880) | docs: update TypeScript docs to reference Fastify 5.x | 2026-07-29 |
| [axios/axios#11113](https://github.com/axios/axios/pull/11113) | docs: add missing `fs` import to README stream example | 2026-07-29 |
| [Topicspot/skillfrisk#9](https://github.com/Topicspot/skillfrisk/pull/9) | Add `--min-severity` flag to control which findings appear in reports | 2026-07-31 |

### Active

| PR | Description |
|---|---|
| [trpc/trpc#7452](https://github.com/trpc/trpc/pull/7452) | docs: add secure error reporting section |
| [jsdoc/jsdoc#2176](https://github.com/jsdoc/jsdoc/pull/2176) | docs: align README Node.js requirement with package.json |
| [xxnjms1-code/kickama-prize-lab#33](https://github.com/xxnjms1-code/kickama-prize-lab/pull/33) | [$35 BOUNTY] Coordinate auth token refresh across tabs |

### Reviews

- [axios/axios#11115](https://github.com/axios/axios/pull/11115) — maintainer-style review of a documentation/bug fix.

## Certifications



| Certification | Issuer |

|---|---|

| [DP-700: Implementing Data Engineering Solutions using Microsoft Fabric](https://learn.microsoft.com/api/credentials/share/en-us/MopuruSasidhar-4473/13AA53E82F21D70C?sharingId=57F4CD5FCA3B941E) | Microsoft |

| [Databricks Certified Data Engineer Associate](https://www.credly.com/users/sasidhar-mopuru) | Databricks |

| Databricks PySpark Streaming Training – 8 Weeks | Accenture |

| [Google Data Analytics Professional Certificate](https://www.coursera.org/account/accomplishments/specialization/DAZFH4EUB7LG?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Ds12n) | Coursera |

| [NPTEL Management Information System (MIS)](https://nptel.ac.in/noc/E_Certificate/NPTEL22MG100S5435012910114355) | Elite · 73% · IIT Kharagpur · Jul–Oct 2022 |



## Technical Skills

- **Programming:** Python, SQL, PySpark, TypeScript
- **Data Engineering:** Apache Kafka, PySpark Streaming, ETL/ELT Pipelines, Data Ingestion, Data Transformation, Batch & Streaming Processing, Microsoft Fabric
- **AI / LLM / App Development:** RAG, LLM, FastAPI, Streamlit, ChromaDB, Vector Databases, GenAI, AI Agents
- **Data Platforms:** Databricks, Apache Spark, Delta Lake, Relational Databases
- **Quality & Testing:** Pytest, Unittest, Mocking, Data Validation, Schema Validation
- **DevOps & Tools:** Git, CI/CD Pipelines, Docker, Terraform, Jira, Agile Scrum
- **Architecture:** Object-Oriented Programming, Modular Coding, YAML/JSON, Logging, Exception Handling, System Design
- **Open Source & Collaboration:** GitHub REST API, Open Source Contribution Workflow, Code Review, Maintainer-Style Reviews
- **Building Toward:** Cloud (Azure), Kubernetes, Platform Engineering, Observability

## Education & Achievements

- B.Tech in Computer Science and Engineering – CGPA 7.99
- JEE Mains – 94.14 Percentile
- Enterprise Data Engineer at Accenture

### OSS Achievements

- Merged documentation PRs in `fastify/fastify#6880` and `axios/axios#11113` (2026-07-29)
- Merged feature PR `Topicspot/skillfrisk#9` — `--min-severity` flag (2026-07-31)
- Active upstream PRs: `trpc/trpc#7452`, `jsdoc/jsdoc#2176`, `xxnjms1-code/kickama-prize-lab#33` ($35 bounty)
- Maintainer-style review of `axios/axios#11115`

## GitHub Stats



<div align="center">



![GitHub stats](https://github-readme-stats.vercel.app/api?username=Sasireddy001&show_icons=true&theme=default)

![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Sasireddy001&layout=compact)



</div>



## Contact



- Portfolio: [sasireddy001.github.io/Portfolio](https://sasireddy001.github.io/Portfolio)

- Resume: [HTML Resume](https://sasireddy001.github.io/Portfolio/SASIDHAR_RESUME.html)

- Email: [sasidharmopuru@gmail.com](mailto:sasidharmopuru@gmail.com)

- GitHub: [@Sasireddy001](https://github.com/Sasireddy001)

- LinkedIn: [linkedin.com/in/sasidhar-mopuru-417a03233](https://www.linkedin.com/in/sasidhar-mopuru-417a03233)

- Location: India

- Open to global remote Python, Automation, Data Engineering, and System Integration roles

## Blog

- [My Databricks Data Engineer Associate Journey](https://sasireddy001.github.io/Portfolio/blog/databricks-data-engineer-associate-journey.html) — Certification notes, resources, and preparation strategy.

