---
tags:
  - applied-ai
  - career
  - evals
  - agent-harness
  - harness-engineering
  - agents
  - distributed-systems
  - trajectory-grading
source: https://x.com/eyad_khrais/status/2074519552277336571
date: 2026-07-07
type: bookmark
author: eyad_khrais
description: "Eyad Khrais — SWE→applied AI path: probabilistic systems, outcome+trajectory evals, harness layers, multi-agent as distributed systems (single-writer, idempotency, preconditions)."
raw: "[[raw/eyad_khrais_2074519552277336571]]"
---

# How to become an applied AI engineer

**Source:** [X Article @eyad_khrais](https://x.com/eyad_khrais/status/2074519552277336571) (Varick Agents)

## Shift

Applied AI extends SWE with **probabilistic** systems: you engineer confidence via measurement, not only logic. Core stack: **evals → harness → multi-agent coordination**.

## Evals (measurement layer)

- **Outcome:** did the task end state match spec?
- **Trajectory:** was the tool path safe? (correct answer + forbidden writes = production failure)
- Split scores; deterministic guards for safety, judge+rubric for quality.

## Harness (operating layer)

Tool execution bridge, context window policy, external state/memory, guardrails, iterative agent loop. Most day-to-day applied AI work lives here — not prompting the model in isolation.

## Multi-agent (coordination layer)

Second agent turns design into **distributed systems**: single-writer state, idempotent mutating tools, conditional writes against stale views, orchestrated typed hand-offs.

## Why it matters

Practical onboarding map aligned with vault themes (trace/eval loops, harness engineering, production agent ops) — bridges traditional engineering hiring profile to agent reliability work.

## Related

- [[learn-harness-engineering]]
- [[writing-good-skills-measured-rulebook-aparna]]
- [[improving-agents-data-mining-traces]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[making-ai-agent-production-ready-sarthakrastogi]]
- [[5-ai-skills-six-figures-2027]]