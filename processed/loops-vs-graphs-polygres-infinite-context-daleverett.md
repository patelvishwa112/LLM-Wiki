---
tags: ["agents", "loop-engineering", "multi-agent", "orchestration", "agent-memory", "langgraph", "postgres", "polygres", "context-management", "agent-harness", "harness-engineering", "knowledge-graph"]
source: https://x.com/daleverett/status/2078969402046009374
date: 2026-07-20
type: bookmark
author: daleverett
title: "Loops vs graphs — control, execution, data graphs and Infinite Context (Polygres)"
description: "Dale Everett on Steinberger loops-vs-graphs: a loop is a degenerate graph; transcript-as-string is a bad DB. Distinguish control/execution/data graphs; Polygres stores all on Postgres so execution joins the data graph (Infinite Context)."
summary: "Dale Everett on Steinberger loops-vs-graphs: a loop is a degenerate graph; transcript-as-string is a bad DB. Distinguish control/execution/data graphs; Polygres stores all on Postgres so execution joins the data graph (Infinite Context)."
raw: "[[raw/daleverett_2078969402046009374]]"
---

# Loops vs graphs — control, execution, data graphs and Infinite Context (Polygres)

## Why it matters

Direct answer to the viral “still loops or graphs?” meme. Pairs cleanly with the vault’s Claude Code **graph-engineering / loop-engineering** cluster and LangGraph notes — but the valuable cut is **three different graphs people conflate**, plus the claim that they need not be three products.

Prior thin note on same product line: [[daleverett-polygress-agent-era]].

## Core claims

- **Loop = simplest / shittiest graph** — Think → Act → Observe cycle; easy because you postpone structure.
- Loops rot when **plan, dependencies, rejected alternatives, and old facts** all live only in the **transcript** (“a database implemented as a string”).
- **Graphs are not automatically better** — don’t draw 87 boxes for email summarize; short improvised tasks still want a simple loop.
- Three graphs:
  1. **Control** — possible steps / branches / pauses / failure paths (LangGraph-class engines).
  2. **Execution** — what this run actually did.
  3. **Data** — entities and relationships in the world the agent acts on.
- **Polygres** pitch: ordinary **PostgreSQL tables** hold world state *and* runs/tasks/tool calls/approvals/artifacts — execution graph becomes part of data graph and steers later control.
- **Infinite Context Window** — model window stays finite; **queryable graph context** grows. Loop still runs; graph grows; still a loop.

## Skeptical read

- Product CTA (polygres.com free signup, pgGraph repo). Substance is the taxonomy more than the product.
- “Infinite context” is marketing for **structured external memory + retrieval**, not a literal context-window breakthrough.
- Does not detail consistency, schema evolution, or when graph writes become the new bottleneck.

## Key takeaways

- Diagnose agent mid-ness as **lossy string memory**, not only weak models.
- Before “graphify everything,” name whether you mean **control**, **trace**, or **world knowledge**.
- Strong systems may keep a loop at the edge while growing a durable graph underneath.

## Related

- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[loop-engineering-14-step-roadmap]]
- [[daleverett-polygress-agent-era]]
- [[langchain-langgraph-101-repo]]
- [[fault-tolerance-langgraph-retries-timeouts]]
- [[agent-memory-landscape-2026]]
- [[gbrain-markdown-git-brain-mem0]]
- [[graphiti-knowledge-graph-agent-memory]]
- [[open-knowledge-format-okf-google]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
