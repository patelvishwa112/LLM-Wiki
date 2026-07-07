---
tags:
  - fable-5
  - agents
  - multi-agent
  - orchestration
  - subagents
  - devin
  - agent-harness
  - verification
  - production
  - migration
  - human-in-the-loop
source: https://x.com/ryancarson/status/2074093250399330418
date: 2026-07-06
type: bookmark
author: ryancarson
description: "Ryan Carson — Fable/Devin parent + 40 children for 834-file migration (prod data + schema); manifest, risk waves, gates, ~$1.1K, zero incidents."
raw: "[[raw/ryancarson_2074093250399330418]]"
---

# Fable orchestrator: huge migration with 40 sub-agents

**Source:** [X Article @ryancarson](https://x.com/ryancarson/status/2074093250399330418) (Hello Untangle)

## What happened

Largest/riskiest engineering program: **834 files**, production data + schema changes, **31 PRs**, weekend timeline, **zero prod incidents** — one **parent orchestrator** (Fable on Devin Ultra), ~**40 child sessions**, parent wrote no code.

## Why it worked

| Pattern | Role |
|---------|------|
| Committed audit manifest | Single scope truth; UNKNOWN → human ruling |
| Risk-ordered waves | Irreversible prod/schema only after code paths verified |
| Disjoint file boundaries | Safe parallel children |
| Gate sessions | Regression, backups, dry-runs between waves |
| Inventory approval | Approve exact rows/actions, not intent |
| Parent escalation | No child scope improvisation |
| Post-ship doc/skills update | AGENTS.md + agent KB reflect new architecture |

**Cost signal:** ~$1.15K total; audits <$90; expensive lines = entanglement + regression gates; **$15** prod mutation after gates — program management as product, not raw codegen volume.

## Why it matters

Concrete field report for **product-loop / software-factory** orchestration: pairs with loop taxonomies, distributed-systems agent patterns, and Hermes-style kanban/delegation — steal patterns regardless of Devin/Fable tooling.

## Related

- [[how-to-automate-disaster-recovery-with-agents]]
- [[designing-loops-with-fable-5]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[how-to-become-applied-ai-engineer-eyad-khrais]]
- [[claude-fable-map-territory-unknowns-trq212]]
- [[addy-osmani-agent-autonomy-ladder-six-levels]]