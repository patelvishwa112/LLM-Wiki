---
tags: [quant, jim-simons, medallion, renaissance-technologies, trading, markov-chains, kelly-criterion, hurst-exponent, factor-model, neural-network, execution, signal-detection, regime-detection, finance]
source: https://x.com/ritonchain/status/2063308228323328247
type: article
author: venus (@RitOnchain)
date: 2026-06-06
---

# Jim Simons' Medallion Fund: The Exact Quant Framework

**183 bookmarks, ~50K views.** Jim Simons fired all the traders in 1988 and replaced them with signal detectors. Medallion Fund: $60B in fees, 39% annual returns (after 44% performance fee), zero losing years in 34 attempts.

## The 5-Layer Pipeline

```
Raw Market Data
      ↓
[L1] Signal Detection   → Hurst · ACF · Z-score
      ↓
[L2] Factor Model       → α extraction · β exposure
      ↓
[L3] Markov Regime      → Bull · Bear · Stagnant
      ↓
[L4] Neural Net Edge    → Long · Short · Flat
      ↓
[L5] Kelly + Execution  → Position Size · Cost Filter · Entry
      ↓
    Trade / No Trade
```

## Layer 1: Signal Detection Engine

Extracts patterns from price data. Three signals:
- **Autocorrelation:** is today's return predictive of tomorrow's?
- **Z-score:** deviation from rolling mean
- **Hurst exponent:** <0.45 = mean-reverting (fades work), >0.55 = trending (momentum works)

Medallion switches strategies based on regime detection.

## Layer 2: Factor Model

Decomposes returns into factors via linear regression. Public version = Fama-French 5-factor. Renaissance's private version = 200+ factors.

Data sources: options chains, order-book depth, fundamentals, news sentiment, social media, satellite imagery, credit card transactions, web traffic, shipping containers.

**High alpha + low R² = edge not explained by known factors. Medallion territory.**

## Layer 3: Markov Chain Regime Machine

3 states: Bull / Bear / Stagnant. Transition matrix estimated from historical data. Computes probability distribution over states after N steps. If 76% probability of remaining Bear over next 5 periods → don't go long.

## Layer 4: Neural Network Edge Extractor

Architecture: 50 → 128 → ReLU → Dropout(0.2) → 64 → ReLU → 3 → Softmax. Outputs [long, short, flat] probabilities.

Feature vector: last 20 returns + factor exposures + regime probabilities + hurst + z-score.

**You're not predicting price. You're predicting probability of direction. 52% accuracy with proper Kelly sizing prints money.**

## Layer 5: Execution (Where 80% of Quants Bleed Out)

- **Half-Kelly** position sizing with 2% max risk hard cap
- Calculate execution costs (spread + market impact)
- Only trade if edge > 1.5× execution cost

## Why Medallion Survives

1. Never show full system to outsiders → alpha preservation
2. Closed to outside money → capacity preservation
3. Half-Kelly → survives drawdowns that kill over-levered
4. Every signal out-of-sample tested → no data leakage

## The Real Secret

Renaissance has ~400 people (~200 on models). Every other fund has thousands with competing strategies. **Renaissance has one model everyone works on together.** The edge isn't any single formula — it's the pipeline where each layer filters noise until only statistical certainty remains.