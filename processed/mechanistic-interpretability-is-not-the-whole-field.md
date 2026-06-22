---
title: Mechanistic Interpretability Is Not the Whole Interpretability Field
created: 2026-06-22
updated: 2026-06-22
type: summary
tags: [interpretability, mechanistic-interpretability, faithfulness, probing, concept-bottleneck-models, feature-attribution, circuits, superposition, sparse-autoencoders]
sources: [raw/giangnguyen2412_2068743875527844200.md]
---

# Mechanistic Interpretability Is Not the Whole Interpretability Field

**Source:** X thread by @giangnguyen2412 (Guide Labs AI), June 21, 2026. [[raw/giangnguyen2412_2068743875527844200.md]]

## Summary

Many researchers entering interpretability today do so via **mechanistic interpretability** (circuits, superposition, SAEs) and treat it as the entire field. This is a mistake. Mech interp is a recent, powerful branch but sits within a much older, broader discipline that includes feature attribution, inherently interpretable models, probing, counterfactuals, and conceptual foundations. Ignoring this history risks rediscovering known failures (e.g., faithfulness issues), using mismatched validation methods, and limiting the available tools.

The thread provides a clear taxonomy:

- **Attribution methods** (Integrated Gradients, SHAP, LIME, Grad-CAM) — post-hoc input feature importance.
- **Probing** — testing what information representations encode.
- **Concept-based** (TCAV, Concept Bottleneck Models, ProtoPNet) — human-concept aligned or inherently interpretable.
- **Example-based** (influence functions, prototypes).
- **Counterfactual explanations**.
- **Mechanistic** (circuits, SAEs, patching/ablations) — reverse-engineering internal algorithms.

Key historical warnings come from the "faithfulness crisis" (Adebayo et al. 2018 sanity checks) and conceptual papers (Lipton 2016, Rudin 2019).

## Why It Matters

This directly supports the vault's [[interpretability]] domain and the owner's career transition target (AI interpretability/safety roles). Entering the field narrowly through SAEs/circuits without the broader context is a common trap. The note emphasizes choosing the right tool for the question rather than defaulting to circuits. It connects to existing notes on [[superposition]], [[sparse-autoencoders]], [[probing]], and [[circuits]] while expanding the taxonomy to include attribution and concept-based approaches that are often more appropriate for certain evaluation or high-stakes use cases.

Recommended reading from the thread aligns with vault goals: Saphra & Wiegreffe (2024) “Mechanistic?”, Adebayo sanity checks, and Lipton on the “mythos” of interpretability.

## Related

- [[superposition]]
- [[sparse-autoencoders]]
- [[probing]]
- [[circuits]]
- [[feature-attribution]] (new tag candidate)
- [[concept-bottleneck-models]] (new tag candidate)
- [[faithfulness]]

## References

- Olah et al. (2020) Circuits thread
- Elhage et al. (2022) Superposition
- Bricken et al. (2023) SAEs
- Adebayo et al. (2018) Sanity checks
- Sundararajan (2017) Integrated Gradients
- Lipton (2016), Rudin (2019), Saphra & Wiegreffe (2024)

---

*Ingested from X thread. No PII. Full visible thread text preserved in raw.*