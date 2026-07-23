# Content Publication Plan — Existing Blog Drafts & LinkedIn Posts

## 1. Existing Blog Assets

### Blog markdown drafts

1. `blog/databricks-de-associate-journey.md` — **Canonical** Databricks certification guide (84 lines, strongest content).
2. `blog/databricks-data-engineer-associate-journey.md` — **Deprecated / duplicate** (41 lines, older wording). Use `databricks-de-associate-journey.md` instead; delete or redirect this one.
3. `blog/kafka-pyspark-delta-pipeline.md` — Production streaming pipeline deep-dive.
4. `blog/rag-fastapi-chromadb.md` — RAG Document QA system deep-dive.
5. `blog/data-platform-engineering-roadmap.html` — Generated HTML only; back it with an `.md` source later.

### LinkedIn post drafts

- `linkedin_posts.md` contains 10 ready-to-post technical posts.

---

## 2. Blog Publication Plan

### P0: Databricks certification guide

- **File:** `blog/databricks-de-associate-journey.md`
- **Primary platform:** LinkedIn Article (native), then Medium
- **SEO title:** *How I Passed the Databricks Data Engineer Associate Exam: A 3-Week Study Plan*
- **Tags / hashtags:** #Databricks #DataEngineering #PySpark #DeltaLake #Lakehouse #Certification #CareerGrowth
- **Publish:** Week 1, Tuesday 9:00 AM IST
- **Cross-post:** Medium, Dev.to (re-published after 24 hours to avoid duplicate-penalty)
- **CTA:** "If you are preparing for the same exam, connect with me or drop your questions in the comments."

### P1: Kafka → PySpark → Delta Lake pipeline

- **File:** `blog/kafka-pyspark-delta-pipeline.md`
- **Primary platform:** Hashnode / Medium
- **SEO title:** *Building a Production-Style Kafka → PySpark → Delta Lake Pipeline on a Laptop*
- **Tags:** #ApacheKafka #PySpark #DeltaLake #Databricks #StreamingData #DataEngineering #AWS #Terraform
- **Publish:** Week 1, Thursday 9:00 AM IST
- **Cross-post:** LinkedIn Article (condensed to 3-minute read), Dev.to
- **CTA:** "Repository link in the comments. Let me know if you want a follow-up on AWS MSK + EMR Serverless deployment."

### P2: RAG Document QA

- **File:** `blog/rag-fastapi-chromadb.md`
- **Primary platform:** Medium
- **SEO title:** *Building a Private RAG Document QA Chatbot with FastAPI, ChromaDB, and Ollama*
- **Tags:** #RAG #LLM #ChromaDB #FastAPI #Streamlit #Ollama #OpenAI #VectorDB #AIEngineering
- **Publish:** Week 2, Tuesday 9:00 AM IST
- **Cross-post:** LinkedIn Article, Dev.to
- **CTA:** "Want the full repo and a Streamlit demo? Link in comments."

### P3: Data platform engineering roadmap

- **File:** `blog/data-platform-engineering-roadmap.html` (no MD source yet)
- **Action:** Create `blog/data-platform-engineering-roadmap.md` from the HTML content, then publish.
- **SEO title:** *A 12-Week Roadmap to Become a Data Platform Engineer in 2025*
- **Tags:** #DataPlatform #DataEngineering #CareerRoadmap #PySpark #Kafka #DeltaLake
- **Publish:** Week 3, Wednesday 9:00 AM IST
- **Cross-post:** LinkedIn Article, Medium
- **CTA:** "Which topic should I cover first — streaming, lakehouse, or CI/CD for data pipelines?"

---

## 3. LinkedIn Publication Calendar

### Week 1 — Cert credibility + streaming project

| Day | Time | Post | Goal |
|---|---|---|---|
| Tue | 9:00 AM IST | Post 1 — Production PySpark + Kafka at Accenture | Establish credibility |
| Thu | 9:00 AM IST | Post 4 — Databricks DE Associate exam notes | Certification signal |
| Sun | 10:00 AM IST | Post 2 — Kafka → PySpark → Delta pipeline | Project showcase |

### Week 2 — Cloud platform + AI / RAG

| Day | Time | Post | Goal |
|---|---|---|---|
| Tue | 9:00 AM IST | Post 5 — Cloud-Native Streaming Data Platform | Cloud + Terraform depth |
| Thu | 9:00 AM IST | Post 3 — RAG with FastAPI/ChromaDB | AI / data intersection |
| Sun | 10:00 AM IST | Post 8 — Building AI-Ready Data Systems | Thought leadership |

### Week 3 — Engineering discipline + open source

| Day | Time | Post | Goal |
|---|---|---|---|
| Tue | 9:00 AM IST | Post 6 — Test coverage in data engineering | Engineering maturity |
| Thu | 9:00 AM IST | Post 10 — 90+ production PySpark jobs | Senior experience |
| Sun | 10:00 AM IST | Post 9 — Open source is my portfolio | Portfolio signal |

### Week 4 — Career + community

| Day | Time | Post | Goal |
|---|---|---|---|
| Tue | 9:00 AM IST | Post 7 — From Data Engineer to Data Platform Engineer | Career narrative |

---

## 4. LinkedIn Engagement Strategy

### CTA templates per post type

1. **Credibility posts:** "If you are building similar platforms, what has worked for you?"
2. **Project posts:** "Repository link in the comments. Let me know if you want a deep-dive thread."
3. **Cert posts:** "If you are preparing for the same exam, connect with me or drop your questions below."
4. **Opinion posts:** "What would you add?"

### Best posting schedule

- **Tuesday / Thursday 9:00–10:00 AM IST** — highest recruiter and practitioner visibility.
- **Sunday 10:00 AM IST** — good for long-form project and career posts.
- Avoid posting after 7:00 PM IST; engagement drops sharply.

### Engagement protocol

1. Reply to every meaningful comment within the first 60 minutes.
2. Post the GitHub repo link as the first comment, not inside the post (algorithm favors it).
3. Tag nobody. Let organic reach carry it.
4. Reshare the most-engaged post 7 days later as a "ICYMI" follow-up.

---

## 5. Cross-Posting Rules

1. **LinkedIn** — always native first. Do not paste a Medium link as the primary post; summarize + link in comments.
2. **Medium** — canonical long-form home. Import from LinkedIn Article or publish original draft.
3. **Dev.to / Hashnode** — wait 24–48 hours after Medium to avoid duplicate-content penalties.
4. **Portfolio blog** — keep `blog/*.html` as the owned asset. Link back to portfolio from Medium and Dev.to.

---

## 6. Cleanup Actions Before Publishing

- [ ] Delete or redirect `blog/databricks-data-engineer-associate-journey.md` and its HTML.
- [ ] Regenerate `blog/*.html` from updated `*.md` files using `build_blog.py`.
- [ ] Add `og:title`, `og:description`, and `og:image` meta tags to `build_blog.py` template.
- [ ] Add a `Read more on my portfolio` link to the top and bottom of every article.
- [ ] Add `rel="canonical"` pointing to the portfolio HTML URL for each blog.
