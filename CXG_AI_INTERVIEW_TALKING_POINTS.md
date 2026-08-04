# CXG AI Interview — Talking Points

## Introduction (30 seconds)
"I am Sasidhar Mopuru, a Data & AI Platform Engineer at Accenture with 2+ years building production PySpark ETL pipelines, streaming data platforms, and Python automation tools. I am Databricks and Microsoft Fabric certified, and I have recently built web-scraping and data-extraction projects end-to-end. I am applying for the Data Engineer — Web Scraping role because it matches my Python, data extraction, and automation strengths."

## Web Scraping / Data Extraction (1–2 minutes)
- Explain recent projects: PDF bank statement extractor, open-source exam scraper, macOS email profile scraper.
- Tools used: `pdfplumber`, `pytesseract`, `Playwright`, `requests`, `BeautifulSoup`, `pandas`, `openpyxl`.
- Handling mixed layouts: use table extraction first, then regex/text heuristics, then OCR fallback for scanned pages.
- Accuracy: validate dates, amounts, balances; write reconciliation checks; produce structured outputs.

## Data Engineering Experience (1–2 minutes)
- 90+ PySpark ETL jobs supporting 67 source and 120+ core data products.
- Kafka → Stage → Raw → HAST/CDP pipeline design and validation.
- 99.5% uptime, 95%+ test coverage, 40% faster deployments through reusable Python utilities.

## Problem-Solving / Project Example (1 minute)
Pick the PDF bank-statement project:
"I needed to convert mixed-layout PDFs into Excel. Some pages were text, some scanned. I built a Python converter that tries table extraction first, falls back to OCR, then uses regex to find dates and amounts. It writes one sheet per statement and a consolidated summary."

## Why CXG / This Role (30 seconds)
"CXG's focus on AI-supported data and web scraping aligns with my recent projects and my goal of building production-grade data extraction systems. I want to contribute to a team that values structured data and automation."

## Questions to Ask
1. What are the primary sources and volumes of data the scraping pipeline will target?
2. Is there an existing data platform I would integrate with?
3. What does success look like in the first 30 days?
