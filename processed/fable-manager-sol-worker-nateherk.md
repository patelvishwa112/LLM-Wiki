---
tags: ["fable-5", "models", "agents", "claude-code", "codex", "cost-optimization", "verification", "multi-agent", "harness-engineering"]
source: https://x.com/nateherk/status/2075394620536578128
date: 2026-07-11
type: bookmark
author: nateherk
description: "Nate Herk hands-on Fable 5 vs GPT-5.6 Sol: manager vs worker split, creative builds, API refusals, and cost/token efficiency."
summary: "Nate Herk hands-on Fable 5 vs GPT-5.6 Sol: manager vs worker split, creative builds, API refusals, and cost/token efficiency."
raw: "[[raw/nateherk_2075394620536578128]]"
---

# Fable Is the Manager, Sol Is the Worker

**Source:** [X Article @nateherk](https://x.com/nateherk/status/2075394620536578128) · [video walkthrough](https://www.youtube.com/watch?v=EthxaDswUFo)

## Summary

Blind creative agentic builds (Claude Code vs Codex) plus a batch of stateless API tasks:

| Build | Winner | Fable cost / tokens | Sol cost / tokens |
|-------|--------|---------------------|-------------------|
| Open-world bike game | Fable (quality) | $14.22 / ~90k out | $4.50 / ~31k out |
| Scroll-stop website | Fable (immersion) | $19.24 / ~80k | ~$1 / ~20k |
| Five visual worlds | Sol (idea spread) | ~$15 / ~65k | ~$1 / ~22k |

API round: **Sol 24 – Fable 3**, but most Fable losses were **guardrail refusals**. When both answered, capability was a tie (~0.98 vs 0.966). Batch spend: Sol $16 vs Fable $63.

**Role split:** Fable for creativity, writing, strategy, knowledge work, video; Sol for price, computer use, devil’s advocate, verification, speed. Dream setup: Fable orchestrating Sol workers. Ranking: GPT-5.5 ≈ Opus 4.8 < Sol << Fable Five. Sol sits near Opus pricing, not frontier Fable.

## Why it matters

Practical multi-model ops: match model tier to unit economics and role (judge/orchestrate vs ship/execute), not leaderboard slogans. Makes harness + skills choice load-bearing for which model “wins.”

## Related

- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
- [[hundred-x-agentic-engineer-preferences-systematicls]]
- [[claude-fable-map-territory-unknowns-trq212]]
- [[fable-5-self-improving-system-14-steps]]
- [[designing-loops-with-fable-5]]
