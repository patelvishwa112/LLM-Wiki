---
tags:
- polymarket
- markov-chains
- quant
- trading
- monte-carlo
- kelly-criterion
- prediction-markets
- longshot-bias
source: https://x.com/de1lymoon/status/2059275498660757727
raw: '[[raw/de1lymoon_2059275498660757727]]'
date: 2026-05-28
type: bookmark
author: de1lymoon
description: Markov Chains for Polymarket Trading
---

# Markov Chains for Polymarket Trading

By Alex (@de1lymoon) | 1M views | 2.2K bookmarks

## Key Takeaways

- **Most traders ask the wrong question.** "Will this resolve YES?" is a coin flip framed as a hot take. The real question: given current price, what's the full spread of next moves and how often does each happen?
- **Markov Chains model price as states, not trends.** Discretize into 10 price buckets and build a transition matrix from historical data. The next move depends only on current state.
- **Longshot bias is massive and data-backed.** Becker's 72.1M trade study: 1¢ contracts win 0.43% of the time, not 1%. Calibrate or bleed.
- **Execution is worth more than the model.** Maker = +1.12%, Taker = -1.12%. Never cross the spread unless edge is enormous.
- **Quarter-Kelly is the professional standard.** Full Kelly maximizes growth on paper. Quarter-Kelly survives.
- **NO outperforms YES at 69/99 price levels.** Below 30¢, buy NO — you're riding the crowd's YES bias.

## Summary

Alex presents a complete 5-step quant framework for Polymarket trading using Markov Chains. The system models price as a sequence of states where transition probabilities depend only on current state (Markov property). A transition matrix built from 30-60 days of price history drives 10K Monte Carlo simulations. Raw probabilities are calibrated against Becker's empirical longshot bias data (72.1M trades analyzed). Position sizing uses quarter-Kelly. Execution mandates limit orders — the maker-taker gap of 2.24pp is worth more than most models.

## Source

https://x.com/de1lymoon/status/2059275498660757727

## Related

- [[polymarket]] — Querying Polymarket markets and data
- [[ghost-in-residual-stream-experiment]] — Our probing/patching experiment
