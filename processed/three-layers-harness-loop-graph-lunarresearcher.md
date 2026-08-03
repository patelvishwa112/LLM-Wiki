---
tags: ["agents", "agent-harness", "harness-engineering", "loop-engineering", "graph-engineering", "verification", "observability", "multi-agent", "production"]
source: https://x.com/lunarresearcher/status/2082076425465762082
date: 2026-07-28
type: bookmark
description: "Harness vs loop vs graph — environment, evidence-based feedback, and workflow topology as three distinct production agent layers."
author: lunarresearcher
summary: "Harness vs loop vs graph — environment, evidence-based feedback, and workflow topology as three distinct production agent layers."
raw: "[[raw/lunarresearcher_2082076425465762082]]"
---

# Three layers: harness, loop, graph (@lunarresearcher)

## Key takeaways

Production agents are **systems**, not “a model.” Three layers get mixed and mis-debugged:

| Layer | Job | Mental model |
|-------|-----|----------------|
| **Harness** | Environment around the model | OS: tools, memory, persistence, safety, observability |
| **Loop** | Repeated work + feedback | Cycle: goal, evidence, stop rules |
| **Graph** | Workflow topology | Flow: nodes, edges, gates, branches |

**Environment → Feedback → Flow**

### Harness

Context injection, action surfaces (APIs/browser/MCP), persistence, budgets/routing/approvals, least-privilege, traces/evals/cost.  
**Debug here when:** cannot operate, loses context, permissions, unauditable.

### Loop

Not prompt engineering. Design triggers, success criteria, state for next cycle, action policy, **evidence** (tests/validation/review — not confidence), compact feedback, stop rules (success/timeout/budget/retries/escalate).  
**Core:** loop on **evidence**, not confidence.

### Graph

Explicit nodes/edges, schemas, routing on evidence, concurrency, cycles/exits, checkpoints.  
**Use when:** branching, approvals, specialist handoffs, parallel work, recovery. Simple tool-using agent may only need harness + loops.

### Diagnosis

- Cannot operate → harness  
- Almost works, unreliable → loop  
- Complex paths/stakeholders → graph  

### Mistakes

Elaborate graphs before harness+loops work; same model writes and grades; “keep trying” loops; harness as junk drawer; blaming the model for orchestration failures.

## Why it matters

Clean diagnostic map that unifies the vault’s harness / loop / graph clusters (Marfin “master architecture,” ArchiveExplorer LOOP→GRAPH→HARNESS, Cyril three commitments, WinterArc/harness-hard essays).

## Related

- [[master-agent-architecture-harness-loop-graph-marfin]]
- [[loop-graph-harness-pipeline-archiveexplorer]]
- [[graph-engineering-three-commitments-cyrilxbt]]
- [[learn-harness-engineering]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[loop-engineering-clearly-explained]]
- [[wtf-is-a-loop]]
- [[eval-engineering-merge-gate-hanakoxbt]]

## Note on provenance

Playwright hit X “Something went wrong”; raw is x_search synthesis. Refresh if full article loads later.

## Source

https://x.com/lunarresearcher/status/2082076425465762082
