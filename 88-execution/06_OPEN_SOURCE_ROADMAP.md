# 60-Day Open Source Contribution Roadmap

**Goal:** Make a measurable, visible contribution to one or more Apache data ecosystem projects and add the result to your GitHub, LinkedIn, and portfolio.

**Time budget:** 1–2 hours per day, 5 days per week = 40–80 hours over 60 days.

---

## Target projects

| Project | Why it fits | Good first contribution | Expected recruiter impact |
|---|---|---|---|
| **Apache Spark (PySpark)** | Core to your resume and interviews | Doc fixes, small SQL test cases, error-message improvements | Very high |
| **Delta Lake** | Tied to Databricks certification and your data lakehouse work | Documentation, Python connector examples, bug reproduction | High |
| **Kafka (kafka-python / kafka-connect)** | You operate Kafka in production | README examples, bug reports, small fixes | Medium-High |
| **PySpark / pandas-on-Spark** | Aligns with your platform work | Good first issues, doc fixes | Medium |

**Primary target:** Apache Spark (biggest name, hardest to land, highest signal).  
**Backup target:** Delta Lake (most relevant to your day-to-day).

---

## 60-day plan

### Days 1–7: Set up and observe
- Fork Apache Spark, Delta Lake, and kafka-python repositories.
- Read `CONTRIBUTING.md` for each.
- Build Spark locally once (`./build/mvn -DskipTests clean package -pl sql/core -am`).
- Read 10 recent merged PRs to understand code style and review culture.
- Subscribe to dev mailing lists / GitHub notifications for `good first issue` labels.

### Days 8–14: First tiny contribution
- Pick one `good first issue` in Spark or Delta Lake.
- Good candidates:
  - Typo or grammar fix in docs.
  - Missing `__repr__` or `__str__`.
  - Improving an error message.
  - Adding a unit test for an edge case.
- Submit the PR. Keep the diff under 100 lines.
- Respond to review feedback quickly and respectfully.

### Days 15–30: Second, slightly larger contribution
- Pick an issue labeled `beginner` or `help wanted` that touches code you understand.
- Examples:
  - Spark: improve `DataFrame.show()` formatting or a SQL function doc.
  - Delta Lake: add an example to the Python docs or a `try-it` notebook.
  - kafka-python: update consumer/producer examples to modern Kafka APIs.
- Write a clean PR description with issue link and test evidence.

### Days 31–45: Third contribution + issue triage
- Submit a third PR or help review another beginner's PR.
- Open 2–3 high-quality bug reports with reproduction scripts.
- Answer one Stack Overflow or GitHub discussion question about PySpark/Delta.

### Days 46–60: Publicize and document
- Update your GitHub profile README with a "Open Source Contributions" section.
- Write a LinkedIn post about what you learned from contributing to Spark/Delta.
- Add the contribution links to your portfolio "Projects" or "Writing" section.
- Set a calendar reminder to continue one contribution per month.

---

## Beginner issue sources

### Apache Spark
- GitHub issues filter: `is:issue is:open label:"good first issue" language:Python`
- Search terms: `DataFrame`, `SQL`, `PySpark`, `documentation`, `error message`
- JIRA: `https://issues.apache.org/jira/browse/SPARK` (filter by `newbie`)

### Delta Lake
- GitHub: `delta-io/delta` issues with `good first issue` label
- Focus on `delta-core` Python examples and `kernel` documentation.

### Kafka (Python)
- `dpkp/kafka-python` repository, `good first issue` label
- `confluent-kafka-python` repository, `good first issue` label

### PySpark / pandas-on-Spark
- `apache/spark` with component `PySpark`
- `pyspark/sql`, `pyspark/pandas` modules are approachable.

---

## Potential first PR ideas

1. **Spark SQL function docs** — Add missing examples to `functions.py` docstrings.
2. **PySpark `DataFrame` error message** — Make a common error message more actionable.
3. **Delta Lake Python example** — Add a `merge` or `optimize` example to docs.
4. **kafka-python README** — Update outdated configuration examples for Kafka 3.x.
5. **Testing gap** — Add a unit test for a small edge case in PySpark SQL.
6. **Type hints** — Add `py.typed` or type stubs in a small module.
7. **Documentation diagram** — Improve an architecture diagram in the Delta Lake repo.

---

## Contribution workflow

```bash
# 1. Fork the repo on GitHub
# 2. Clone your fork
git clone https://github.com/Sasireddy001/spark.git
cd spark

# 3. Add upstream
git remote add upstream https://github.com/apache/spark.git

# 4. Create a branch
git checkout -b SPARK-XXXXX-fix-description

# 5. Make changes, run local tests for the module you touched
./python/run-tests --testnames pyspark.sql.tests.test_functions

# 6. Commit with a clear message
git commit -m "[SPARK-XXXXX][PYTHON] Fix typo in DataFrame.show docs"

# 7. Push and open PR
git push origin SPARK-XXXXX-fix-description
```

---

## Recruiter impact

| Signal | Value |
|---|---|
| Merged PR in Apache Spark | Strong evidence of technical depth; most candidates do not have this. |
| 3+ merged PRs across Spark/Delta/Kafka | Top-5% differentiator for a 2–3 year engineer. |
| Bug reports with reproduction scripts | Shows debugging and communication skills. |
| Review activity on other PRs | Shows collaboration and code-reading ability. |
| LinkedIn post about the contribution | Public proof of initiative and learning. |

**Expected profile score impact after 3 merged PRs and 2 LinkedIn posts:** +1.5 to +2 points.

---

## 30-minute daily routine

1. **Monday:** Search `good first issue` and pick one.
2. **Tuesday:** Reproduce the issue, read related code.
3. **Wednesday:** Write the fix and local tests.
4. **Thursday:** Submit PR and write a clean description.
5. **Friday:** Review others' PRs, answer questions, or read code.

---

## Common mistakes to avoid

- Do not submit a PR without running tests locally.
- Do not open giant PRs; keep changes focused.
- Do not argue with maintainers; ask questions instead.
- Do not ignore review comments for more than 48 hours.
- Do not pick `good first issue` topics you do not understand; doc fixes are valid.
