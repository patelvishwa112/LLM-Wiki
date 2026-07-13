---
tags: ["hermes", "agents", "cronjob", "agent-memory", "trading", "crypto", "onchain", "research", "agent-ops", "productivity"]
source: https://x.com/0xjeff/status/2076631167152042204
date: 2026-07-13
type: bookmark
description: "0xJeff's production Hermes workflows: daily analyst trackers + bookmark triage + Top 10 alpha synthesis with rotating contrarian sources, plus onchain forensics cross-checked against X sentiment."
author: 0xJeff
summary: "0xJeff's production Hermes workflows: daily analyst trackers + bookmark triage + Top 10 alpha synthesis with rotating contrarian sources, plus onchain forensics cross-checked against X sentiment."
raw: "[[raw/0xjeff_2076631167152042204]]"
---

# 2 Hermes Workflows I can't live without — @0xJeff

Four months of daily Hermes use for research & investment (equities, crypto, prediction markets). Pattern: define skills/tools → let Hermes research → human cross-check. Continuous improvement via champion loop + feedback sweep loop.

## Workflow 1 — Daily Grok Alpha Trackers + X Bookmarks + Top 10 Synthesis

Three coupled cron-style jobs:

1. **Analyst trackers** — 11+ macro/equities/crypto accounts; daily summaries with links delivered to Discord, tailored to portfolio/strategies.
2. **Bookmark triage** — 5–15 bookmarks/day ranked high/medium/low importance and summarized.
3. **Top 10 alpha synthesis** — Analyst outputs + bookmarks + **rotating external sources** (Mon–Sun cycle: arxiv, HF letters, onchain flows, derivatives, etc.) → one brief; Top 10 items ingested into **Hindsight** (external memory) to improve next-day context.

Echo-chamber defense is explicit: contrarian/external sources rotate so the agent (and operator) stay grounded.

**Requirements:** Grok or X Premium (`x_search`); X API v2 for bookmarks; synthesis model (author uses DeepSeek v4 Pro); external memory (Hindsight).

## Workflow 2 — Onchain Forensics

For fair-launched / launchpad tokens, Hermes inspects a contract for:

- Top holder concentration
- Buy/sell/transfer patterns over time
- Whale moves and recurring behavior
- Daily/weekly holder-change summaries
- Cross-check vs X sentiment (Cookie MCP)

Divergence heuristics:

- Onchain dump + bullish X → investigate (possible narrative trap)
- Negative X + onchain inflows → possible silent accumulation

**Stack:** x402 via AgentCash & BlockRun; Nansen, BlockRun SQL, Surf, Base RPC; Cookie MCP for sentiment.

## Bonus monitors

- **Exa Monitors** — daily “search radar” across broader sources
- **Firecrawl monitors** — finer cadence (hourly/custom) when needed

## Why it matters

Concrete Hermes ops template for market research: scheduled multi-source ingestion, tiered prioritization, synthesis into a short brief, memory write-back, and dual-channel (onchain + social) verification. Augments judgment rather than replacing it. Title says “2 workflows”; body frames alpha stack as three coupled jobs plus a separate onchain track.

## Related

- [[hermes-goal-mode-guide]]
- [[hermes-seven-skills-cobi-bean]]
- [[hermes-agent-10x-faster-vault-index]]
- [[living-wiki-second-brain-hermes-leopardracer]]
- [[agent-memory-four-layer-stack-matthew-gunnin]]
- [[4-agent-trading-desk]]
- [[hermes-kanban-mission-control]]
