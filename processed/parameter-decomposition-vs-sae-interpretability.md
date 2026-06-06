---
tags: ["interpretability", "models", "parameter-decomposition", "sae"]
source: https://x.com/BartBussmann/status/2051738729841041746
date: 2026-05-05
type: note
related: ["goodfire-parameter-decomposition-interpretability", "priests-of-agi-interpretability-crisis"]
---

# Parameter Decomposition vs SAEs for LLM Interpretability

## Summary
Community reaction to Goodfire AI's parameter decomposition breakthrough, which decomposes a language model's weights rather than its activations. The approach natively handles attention and behaves more like a generalizing algorithm than a lookup table — positioning it as a direct competitor to sparse autoencoders (SAEs).

## Key Takeaways
- **Paradigm shift:** Parameter decomposition has "just started working on LLMs" at meaningful scale
- **SAE comparison:** Unlike SAEs that decompose activations into sparse feature vectors, parameter decomposition operates directly on weights
- **Attention support:** Natively handles attention computations — a long-standing challenge for interpretability methods
- **Algorithmic behavior:** Behaves less like a lookup table and more like a generalizing algorithm
- **Community sentiment:** Strong enthusiasm, with some suggesting SAEs may be superseded

## Connections
- [[goodfire-parameter-decomposition-interpretability]] — the primary source with full findings
- [[priests-of-agi-interpretability-crisis]] — context on why new interpretability methods matter
