---
type: bookmark
description: "Vasuman (Varick Agents) for enterprise CFOs: horizontal copilots and point SaaS fail; win with background agents inside existing ERP tools, ~85% deterministic code + 15% LLM judgment, process mapping, confidence gates, evals — claimed close 12→5 days."
tags: ["agents", "enterprise", "finance", "agent-ops", "evals", "agent-harness", "cost-optimization", "workflow", "varick", "background-agents"]
source: https://x.com/vasuman/status/2077156239059107867
date: 2026-07-15
author: vasuman
summary: "Vasuman (Varick Agents) for enterprise CFOs: horizontal copilots and point SaaS fail; win with background agents inside existing ERP tools, ~85% deterministic code + 15% LLM judgment, process mapping, confidence gates, evals — claimed close 12→5 days."
raw: "[[raw/vasuman_2077156239059107867]]"
---

# AI for Enterprise Finance & How to Do It Right

Long-form by **vas** (@vasuman), CEO of **Varick Agents** (ex-Meta AI), aimed at CFOs at $1B+ companies. Finance-domain product narrative with a clear agent-architecture thesis.

## Diagnosis

### Two failed default paths
1. **Horizontal assistants** (Copilot, Claude Cowork, etc.): every employee spins up agents; no interop; huge token bills (example $3M); ~80% agents defunct/breaking — tech debt with no owner.
2. **Point solutions** (generic AP/close/expense agents): ignore company-specific process depth (e.g. 7-step AP + Brittany-style under-$500 exceptions); low adoption; ROI often <15%; more logins, not less.

Industry stats cited: Gartner 84% plan/use AI but 7% high impact; MIT NANDA 95% pilots no P&L return; high cancel risk for agentic projects; ~2/3 invoices need human touch; $12.42 manual invoice cost; 14% exception rate as the key “your exceptions ≠ theirs” wedge.

### Why copilots alone fail in finance
Frontier models on real finance tasks ~52–66% accuracy (Vals AI / DualEntry cited). Hallucinations = money + SOX/audit failure. Need **guardrails, permissions, deterministic path** so models only decide judgment slices; traces for auditors.

## What works (philosophy)

**One agent layer on top of systems of record** (NetSuite, Workday, SAP, Bill, BlackLine…) — not a new pane of glass. Agents **do the glue work** (copy, match, chase, escalate), not another dashboard.

Examples: invoice lands → PO match or Slack human with two candidates; overnight bank tie-out; W-9/payment chase; PBC list prep.

## Implementation playbook (5 always)

1. **Forward-deployed process mapping** — sit with ICs; SOPs lie; capture Brittany rules.
2. **Build inside existing tools** — same screens/APIs as new hire.
3. **Agents do work, not dashboards** — KPIs follow actions.
4. **Confidence gates + human feedback** — clear 70–85% pattern matching; approvals train system weekly.
5. **Design for whole department day one** — avoid siloed vibe-coded agent islands.

## Cost & accuracy stack

- **~85% plain code / ~15% LLM** (judgment only: messy extract, exception bucket, draft note).
- **Three layers:** deterministic code (auditable) → path+answer **evals** → human feedback loops (e.g. GL coding 85% → 97%).
- Contrast: full-stochastic “every action is an LLM” stacks (e.g. generic Cowork) burn tokens and resist audit.

## Results claimed (case-style)

- Close 12 days → 5; exceptions 130h/mo → 20h; invoice 20 min → <1 min avg.
- One client ~$45M annual value (time/money + revenue + risk).
- Author claim: 100% of Varick finance deployments to production; avg ROI ~5.5x.

Value buckets for any AI finance program: **save time/money · increase revenue · reduce risk**.

## Skeptical read

Strong services/product pitch for Varick (scarcity + fall cohort). Vendor-reported ROI and “100% production” not third-party audited. Architecture lessons (code-heavy agents, process mapping, department-wide design) transfer even if specific numbers do not.

## Related

- [[anthropic-finance-claude-cowork]]
- [[sierra-pinecone-singular-company-agent]]
- [[glean-coding-harness-programmatic-tool-calling]]
- [[making-ai-agent-production-ready-sarthakrastogi]]
- [[anthropic-self-service-analytics-claude]]
- [[the-untrainable]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[the-great-flattening-tokenmaxx-vorflux-myprasanna]]
