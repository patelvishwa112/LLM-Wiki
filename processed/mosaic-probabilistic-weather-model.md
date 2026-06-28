---
tags:
- models
- weather
- probabilistic-modeling
- deepmind
- ensemble-methods
source: https://x.com/maxxxzdn/status/2057026766380659085
raw: '[[raw/maxxxzdn_2057026766380659085]]'
date: 2026-05-20
type: note
description: 'Mosaic: Probabilistic Weather Model'
---

# Mosaic: Probabilistic Weather Model

## Summary
Mosaic is a probabilistic weather model that shifts the Pareto frontier of ML weather forecasting. It matches state-of-the-art skill while generating a 24-member, 10-day global forecast in under 12 seconds on a single H100. Built on learned functional perturbations by Google DeepMind.

## Key Takeaways

### The Problem with Existing ML Weather Models
Large weather models match or exceed physics-based forecasts at lower cost, but degrade at fine scales — exactly where forecasts matter most (frontal zones, tropical cyclones). Three failure modes:
1. **Deterministic training** — produces smooth conditional means, not sharp realistic realizations
2. **Information bottleneck** from compressive encoding — coarse latent mesh can't represent fine-scale features, turning their energy into high-frequency artifacts
3. **Predicting tendencies** — amplifies errors at fine scales

### Mosaic's Solutions
- **Probabilistic** — produces ensembles where each member is a sharp, physically plausible realization (not a smoothed mean)
- **Native resolution interactions** — computes interactions at native resolution before coarsening, avoiding the information bottleneck

## Connections
- Builds on Google DeepMind's learned functional perturbations approach for probabilistic weather modeling
