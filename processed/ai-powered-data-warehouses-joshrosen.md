---
tags: ["data", "agents", "architecture", "evals"]
source: https://x.com/JoshARosen/status/2095488762532745712
date: 2026-09-03
type: bookmark
description: "Josh Rosen: seven warehouse-AI lessons — inference as operator, inferred transforms, semantic layer for agents, agent location, Flights, agent workload, AI lineage."
author: JoshARosen
summary: "Josh Rosen: seven warehouse-AI lessons — inference as operator, inferred transforms, semantic layer for agents, agent location, Flights, agent workload, AI lineage."
raw: "[[raw/JoshARosen_2095488762532745712]]"
---

# AI-Powered Data Warehouses: Architectural Lessons

Josh Rosen (@JoshARosen). Snowflake/Databricks/ClickHouse/BigQuery/MotherDuck/Redshift adding models to pre-LLM systems.

1. **Inference as operator** — LLM in SQL (filter/classify/extract); Snowflake AI-aware optimizer because LLM predicates have different costs.
2. **Transforms infer facts** — contract → obligations; call → objections. Columns mix source facts, deterministic calc, model judgments — all look like SQL data.
3. **Semantic layer as agent infra** — schema ≠ business model. Snowflake semantic views / Databricks Genie / Fabric Data Agent: metrics, filters, verified queries.
4. **Where the agent lives** — inside the warehouse vs MCP-outside; many vendors do both.
5. **Warehouse as execution env** — MotherDuck Flights (Python next to data); Databricks unified catalog/SQL/Python/Lakeflow/serving.
6. **Agents are a new DB workload** — bursty, iterative, concurrent; ClickHouse latency/concurrency; MotherDuck hypertenancy.
7. **AI-generated data needs lineage** — which model, prompt, transform version produced a "billing complaint" label.

Preview of production AI inside mature enterprise boundaries.

## Related

- [[llm-as-judge-architectures-runtime-joshrosen]]
- [[why-every-ai-accountant-fails-eya0]]
