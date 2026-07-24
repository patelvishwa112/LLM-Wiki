---
tags: ["agents", "graph-engineering", "multi-agent", "loop-engineering", "trading", "quant", "finance", "factor-model", "slate", "orchestration", "verification", "agent-harness", "harness-engineering", "prediction-markets"]
source: https://x.com/rohonchain/status/2080296261576687751
date: 2026-07-23
type: bookmark
description: "RohOnChain maps prompts→loops→swarms→graphs to an 11-node Fama-French/Carhart multi-factor alpha Program on Slate (7 parallel factors + validator/HMM/portfolio/risk)."
author: RohOnChain
summary: "RohOnChain maps prompts→loops→swarms→graphs to an 11-node Fama-French/Carhart multi-factor alpha Program on Slate (7 parallel factors + validator/HMM/portfolio/risk)."
raw: "[[raw/rohonchain_2080296261576687751]]"
---

# Graph engineering → multi-factor alpha model (RohOnChain)

**@RohOnChain (Roan)** X Article: hedge-fund-style **multi-factor alpha** as a self-running **graph** on **Slate** (Random Labs), for solo builders who cannot staff factor/stat/portfolio/risk teams.

## Progression (named stages)

1. **Prompts** — human is the loop; nothing survives laptop close.
2. **Loops** — scheduled single-agent jobs with state.
3. **Swarms** — specialized agents in parallel; hand-written Python glue.
4. **Graphs** — nodes = agents, edges = data handoffs; runtime owns parallel/wait/retry/escalate.

**Why graphs:** scripts die on waits, multi-cycle state, and multi-model parallel. Node-scoped failure + plain-English patch beats whole-pipeline crashes (author’s profitability agent / rate-limit story).

## Runtime: Slate Programs

- Terminal runtime from **@wearerandomlabs** / randomlabs.ai; uses existing model subscriptions.
- **Program** = JS graph that runs continuously (vs one-shot prompt).
- Describe intent in English → Slate drafts diagram → Q&A → save/run; failures patched via chat.
- Warm-ups: **`/goal`** (maker-checker until verified done) and **`/deepresearch`** (parallel research fanout → orchestrator) — pattern for 7 parallel factor agents.

## Eleven-node multi-factor graph

**Seven parallel construction nodes (classic stack):** Market beta (60m), SMB, HML, MOM (12-1), RMW, CMA, low vol (60d).

**Four sequential coordination nodes:**

| Node | Job |
|------|-----|
| Validator | Newey-West t-stats; 10k bootstrap; kill >30% IS/OOS degradation; stronger model (maker ≠ checker) |
| Regime auditor | 3-state HMM on vol/returns; kill single-regime “alpha” |
| Portfolio constructor | Risk-parity long/short; sector/beta/dollar neutrality |
| Risk decomposer | Residual α after style/macro; trade only if residual t > ~2.5 |

Daily loop (~3am): parallel factors → hard gates (author claims ~80% of pretty backtests die at validator) → Slack signal or documented no-signal day.

## Build / ops notes from the piece

- Tiered models: Sonnet-class for factor nodes; Opus-class for validator/regime/portfolio/risk.
- Suggested **$30/run** budget — Slate flagged enforcement as **advisory** (self-reported spend), not hard realtime kill; honesty as trust signal.
- Debug examples: FX-normalize non-US books; widen MOM lookback in hostile regimes; project sector neutrality.
- Blueprint: progression → 7 factors → draw 11 nodes first → tier models → hard stats gates → warm-up Programs → compound over months.

## Why it matters

Connects the vault’s **graph-engineering / loop-engineering** thread to a concrete **quant factor-model** graph: parallel research fanout + sequential verification gates + residual-alpha honesty. Same maker-checker and parallel-then-sync pattern as coding graphs, applied to Fama-French/Carhart-style research ops.

## Skeptical read

Product narrative around Slate + “first 20 architecture reviews” CTA. Factor construction described at textbook level; live data, costs, slippage, and true hard budget/kill switches are the hard parts. Residual-α and regime gates are the real intellectual core — treat runtime claims as demo until reproduced.

## Related

- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[graph-engineering-dynamic-workflows-fleet-0xcodila]]
- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[loop-engineering-14-step-roadmap]]
- [[4-agent-trading-desk]]
- [[jim-simons-medallion-quant-framework]]
- [[hermes-alpha-trackers-onchain-forensics-0xjeff]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
