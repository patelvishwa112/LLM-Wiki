---
tags:
- training
- ml-research
- research-methodology
- experiments
- scaling-laws
- pretraining
- architecture
- agents
description: "Poolside-scale playbook for ML experiments — research questions, dated baselines, manual run logs, finish runs, and compute-efficiency gain via scaling laws."
summary: "Poolside-scale playbook for ML experiments — research questions, dated baselines, manual run logs, finish runs, and compute-efficiency gain via scaling laws."
source: https://x.com/iamgrigorev/status/2071688181628678468
date: 2026-06-29
type: bookmark
author: iamgrigorev
raw: "[[raw/iamgrigorev_2071688181628678468]]"
---

# How to design good ML experiments and actually learn from them

George Grigorev (Poolside architecture) describes running ~100 experiments/week with parallel agent sessions and a discipline stack aimed at **learning**, not just logging curves.

## Process pillars

1. **Explicit research question** before code — without it, results are ambiguous.
2. **Research taste** — prefer simple, cheap-to-test ideas; go **wide before deep**; avoid expensive exotic attention/SSM bets unless confidence is high.
3. **Compound failures** — e.g. Curse-of-Depth norm scaling → citation chase → **ProRes (Progressive Residual Warmup)**.
4. **Let runs finish** — early kills bias toward fast-looking wins and destroy evidence.
5. **Manual experiment table** (Google Sheet) for memory/accountability at high throughput.
6. **Config verification** before launch; **dated shared baseline** in main updated only with verified wins (4B + 17B MoE tiers, ~1-day turnaround).
7. **Stable evals** — likelihood benchmarks + averaged generation evals (e.g. GPQA); baselines for iteration, **scaling-law ladders** (7–20 runs) for scale confidence.
8. **Compute efficiency gain** = C_predicted / C_observed from baseline scaling law — turns tiny loss deltas into “how much compute saved.”

## Agent-era angle

High experiment volume is enabled by tooling (parallel agent sessions, paper/X feeds), but the bottleneck shifts to **experiment design and logging** — same theme as loop engineering for coding agents.

## Related

- [[how-to-be-good-at-research]]
- [[training-llm-from-scratch-5-lessons]]
- [[loop-engineering-quietly-ate-prompt-engineering]]