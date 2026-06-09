---
tags: ["interpretability", "models", "parameter-decomposition", "sae", "causal-ablation"]
source: https://x.com/leedsharkey/status/2051717264286609516
raw: "[[raw/leedsharkey_2051717264286609516]]"
date: 2026-05-05
type: note
related: ["parameter-decomposition-vs-sae-interpretability", "priests-of-agi-interpretability-crisis", "anthropic-natural-language-autoencoders"]
---

# Goodfire: Parameter Decomposition for Model Interpretability

## Summary
Goodfire AI introduces a new approach to mechanistic interpretability: decomposing a language model's weights instead of its activations. This represents a paradigm shift from sparse autoencoders (SAEs) and transcoders, operating on parameters rather than activations.

## Key Findings
1. **Sparse parameter usage:** Networks don't use all their parameters on a given input. Causal ablations identify which parameter subsets are active, revealing components that play individual computational roles (e.g., emoticon prediction, gender identification)
2. **Scaling up:** Now works on meaningful model sizes (4-layer LMs), positioning parameter decomposition as a genuine competitor to SAEs and transcoders
3. **Attention decomposition:** First satisfying solution in ~3 years for decomposing attention computations, even when distributed across attention heads
4. **Attribution graphs:** Parameter components enable tracing information flow through the model, building causal attribution graphs

## Connections
- [[parameter-decomposition-vs-sae-interpretability]] — community reaction to this breakthrough
- [[priests-of-agi-interpretability-crisis]] — broader context of interpretability challenges
- [[anthropic-natural-language-autoencoders]] — complementary approach using activation-based autoencoders
