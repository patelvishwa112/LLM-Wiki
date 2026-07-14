---
tags: ["agents", "multi-agent", "orchestration", "loop-engineering", "verification", "agent-harness", "conductor", "harness-engineering"]
source: https://x.com/leanxbt/status/2076679468186513600
date: 2026-07-13
type: bookmark
description: "leanxbt conductor build: decompose with mandatory checks, sequential dispatch, disk-materialized integration + seam tests, conductor-run oracles, multi-agent brakes and attribution."
author: leanxbt
summary: "leanxbt conductor build: decompose with mandatory checks, sequential dispatch, disk-materialized integration + seam tests, conductor-run oracles, multi-agent brakes and attribution."
raw: "[[raw/leanxbt_2076679468186513600]]"
---

# How to Build a Conductor — Multi-Agent Loops from Scratch (@leanxbt)

Single-agent loops hit a **context ceiling** on migrations, cross-system features, large repos. The fix is not a smarter worker — it is a **conductor**: pure coordinator (split, assign, order, merge, stop), domain-dumb, coordination-disciplined. Separate roles physically (different prompts / model calls).

## Strict build order

| Stage | Job | Failure if skipped |
|-------|-----|--------------------|
| **1. Decomposition** | Goal → subtasks with `id`, `desc`, **required `check`**, `depends_on` | Uncheckable work → self-kind “done” |
| **2. Dispatch** | Ready = deps closed; pick max-`unblocks`; **sequential first** | Parallel before seams work → races |
| **3. Integration** | Materialize on disk; conductor reads traces; **integration tests on seams** | Green parts, red whole (interface mismatch) |
| **4. Verification** | Conductor runs each check + end-to-end acceptance | Trust worker reports; dummy subtask gaming |
| **5. Brakes** | Step/budget/heartbeat + **per-subtask timeout**, **round cap** → human | Hang / endless argument melts budget |

Replan when all subtasks closed but acceptance red. Deadlock if work remains but nothing ready.

## Design principles

- **Checks are sacred** — defined at decompose time; worker cannot grade itself.
- **Facts on disk** — not summaries in the conductor’s head.
- **Attribution in state** — who did what + **evidence** (oracle exit) for 3am debugging.
- **Scale honestly** — first conductor = 3–4 workers on one boring large task, not a 100-agent fleet story.

## Why it matters

Executable skeleton for multi-agent harnesses (Python sketches included). Aligns with verification-first loop engineering, ADK isolation, and swarm roadmaps — with sharper anti-patterns (skip checks, parallelize early, believe “done”).

## Related

- [[orchestrating-agents-adk-fhinkel]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[addy-osmani-agent-autonomy-ladder-six-levels]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[how-to-create-loops-claude-code-sairahul1]]
- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
- [[wtf-is-a-loop]]
