---
tags: [agents, multi-agent, subagents, orchestration, agent-harness, governance, production, compression, coordination, hermes, cost-optimization]
source: https://x.com/nyk_builderz/status/2070346338269819043
date: 2026-06-26
type: bookmark
author: nyk_builderz
summary: "Nyk (@nyk_builderz): one agent doing research+code+review+orchestration blurs by week 4 — throughput is architecture (sub-agents for compression vs multi-agent only for coordination). Production org: worker sub-agents + coordinator; four governance controls (pretool guard, handoff artifact, controlled disagreement, completion gate). Claims ~1/3 token cost vs full multi-agent and LACP gate over 3k sessions."
raw: "[[raw/nyk_builderz_2070346338269819043]]"
---

# Agent Swarms That Don't Go Rogue

Field guide to **shape over IQ**: wide parallel work needs a grid, not one context walking 50 serial jobs.

## Single agent breaks on width

Series time ~50×; context forgets early findings; you become manual glue. Sharper models don't fix line-shaped work.

## Compression vs coordination

| Pattern | When |
|---------|------|
| **Sub-agents (compression)** | Independent parallel lanes, clean memory each (~1/3 token vs full multi-agent per author [E1]) |
| **Multi-agent (coordination)** | Lanes must negotiate one shared decision |

Don't use a committee when you needed fan-out.

## Org chart

**Workers:** one lane, memory, tools. **Coordinator:** split, plan review, merge only.

## Four production governance controls

1. **Pretool guard** — block destructive/exfil patterns before tools run  
2. **Handoff artifact** — session end state injected into next run (no blank slate)  
3. **Controlled disagreement** — competing plans scored before merge  
4. **Completion gate** — weighted rubric (completeness/honesty/deferral/evidence) blocks fake "done" [E2]

## Run checklist

Fit test → team-style brief → one-pass inputs → approve coordinator split → gate output before ship.

## Why it matters

Pairs with loop/async patterns: parallelism without gates is faster blast radius. Hermes-style delegation maps to worker/coordinator split.

## Related

- [[human-in-the-loop-agent-loops]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[agent-harness-engineering-agentforge]]
- [[hermes-kanban-mission-control]]