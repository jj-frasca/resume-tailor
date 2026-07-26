# Role playbooks — how to weight the resume per archetype

Pick the archetype from the job posting and apply the matching block. These are strategy
patterns for selecting and framing the user's OWN facts — they are never a source of
facts. If the user lacks what an archetype wants, report the gap; don't manufacture it.

## Cross-archetype rules
- **Lead with the target framing, reframe — never relabel.** Put the target role's framing
  up top; never claim a title the user didn't hold.
- **Match the level.** If the posting is Senior/Staff or wants more years than the user
  has, warn them — under-leveled candidates are often auto-filtered. Prefer IC / "II" /
  early-career reqs when that fits.
- **Keyword mirroring:** use the posting's exact terms (spell-out + acronym once), each
  backed by a real bullet. ~70–80% of hard requirements should map to a real line. No stuffing.
- Promote relevant side-projects to first-class entries with links when the role is AI/FDE
  and the user has them.

## Forward Deployed Engineer (FDE)
- **What it screens for:** customer-facing, end-to-end shipping under ambiguity, glue /
  full-stack code, deployment, stakeholder communication. Messy-data-at-scale experience
  is a moat (deployments are mostly data wrangling), not a liability.
- **Lead with:** built-and-shipped-to-users stories; user-facing scale; human-in-the-loop
  and explainable systems; 0→1 ownership.
- **Bullet shape:** scope + named baseline + metric delta + trade-off. Production / cost /
  latency metrics beat model-accuracy, which beats framework name-drops.
- **Frontier-lab vocabulary:** when the posting names things like agents, evals, deployment
  at scale, mirror the exact terms and exact service names — but only if the user has real
  backing.
- **Variants:** startups → emphasize ambiguity-handling, roadmap-driving, breadth.
  Integration-heavy shops → emphasize data integration + customer deployment.

## AI Engineer
- **What it is (today):** ships LLM/agent *products* — RAG, agents, evals, orchestration,
  productionizing models. Distinguish this from ML research.
- **#1 silent killer:** research-flavored bullets ("trained a transformer, improved F1")
  read as ML researcher = wrong role. Use product-builder framing ("shipped a RAG/agent
  feature to prod, cost/doc $0.18→$0.024").
- **Evals are the credibility gate:** foreground eval work (hand-written evals, LLM-as-
  judge, hill-climbing) if the user has it. Its absence signals "ships unevaluated features."
- **Keywords:** RAG, agents, evals/LLM-as-judge, prompt engineering, vector/retrieval,
  orchestration, latency/cost optimization, and the specific model APIs the posting names.

## Data Engineer
- **Lead with the strongest artifact-backed pipeline wins** (scale/ownership, dashboard or
  query optimization, migrations, backfills, on-call root-causes) — don't bury them behind
  side-projects.
- **Signal seniority via reliability vocabulary, not tool lists:** SLOs with named
  ownership + error budgets, data-quality SLIs (null-rate, reconciliation), observability
  (freshness/volume/schema/distribution/lineage), idempotency/backfills.
- **Level reality:** "Senior DE" usually gates at ~5–8 yrs; apply at mid / DE-II unless the
  user is genuinely senior. Flag Senior DE postings.
- **Keywords:** Spark, Airflow, dbt, the posting's warehouse (BigQuery/Snowflake/
  Databricks/Redshift), streaming (Kafka/Flink), data modeling, ETL/ELT, lineage.

## Trading-firm Data Engineer (distinct from generic DE)
These firms do NOT reward scale-bragging, AI/LLM work, or infra-architecting. Read the
posting literally; the throughline is usually:
- **Detective instinct / data investigation** (often the #1 screened trait): finding
  anomalies in derived datasets and tracing issues back to their source; deductive
  reasoning; communicating with stakeholders. Lead with the user's best debugging /
  root-cause story.
- Messy real-world data → reliable input (judgment on data, not volume); reconciliation /
  validation / quality checks.
- **Demote hard:** AI agents, hackathons, scale-brags — they read as "wrong hire" here.
- **Skills mirror the exact named stack:** Python, SQL, pandas/Polars, PostgreSQL, Linux
  command line, ETL. Financial-data experience is often "a plus"; don't fabricate vendor
  exposure (Bloomberg/Refinitiv/etc.) the user lacks.

## Software Engineer (backend/general)
- **Framing:** "systems that scale without burning money." Lead with throughput + uptime +
  infra cost on a named system ("event-driven pipeline, 12K req/s, 99.95%, $4K/mo").
  Architecture/cost numbers differentiate; task-list resumes lose.
- Surface CS fundamentals, languages matching the posting, and the most systems-heavy work.
- Match level precisely and mirror the posting's exact stack.

## Quant / trading developer
- **Pitch:** strong analytical/engineering background + a serious quantitative project is a
  genuine quant story. Translate adjacent-domain skills into quant terms (numerical methods,
  simulation, signal processing → time-series/backtesting) only where real.
- **Centerpiece:** a validation-heavy quant project (backtesting, walk-forward, risk,
  reproducibility, property tests) if the user has one.
- **Gate:** pure HFT wants deep C++ (memory model, lock-free, kernel bypass, Linux perf).
  Confirm the user's real C++ depth before claiming it; don't overstate. Many profiles fit
  quant-dev / trading-data-infra better than low-latency HFT.

## Aerospace / defense
- **Surface the relevant degree + controls/systems projects high up** if the user has them
  — it's a real differentiator. Pull controls coursework/projects and relevant hardware or
  systems work.
- **Bridge framing:** "domain engineer who became a production software/data engineer" —
  domain credibility + shipping ability.
