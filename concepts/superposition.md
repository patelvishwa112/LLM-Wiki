---
title: Superposition
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [interpretability, superposition, features]
sources: [raw/papers/tcircuits-toy_model-index.md, raw/papers/arxiv-2211.00593.md]
confidence: high
---

# Superposition

Superposition is the phenomenon in which a neural network represents more
features than it has neurons by storing them as overlapping linear combinations.
Demonstrating and characterizing superposition is what motivated the
[[sparse-autoencoders|sparse-autoencoder]] line of interpretability research.

## What the sources say

- [[tcircuits-toy_model-index]] — "Toy Models of Superposition" (2022):
  the foundational paper that exhibits superposition cleanly in small,
  controlled models and predicts its appearance at scale
- [[arxiv-2211.00593]] — "Interpretability in the Wild: A Circuit for IOI
  in GPT-2": shows interpretable circuits coexisting with superposed
  features in a real model

## Related

- [[mechanistic-interpretability]]
- [[sparse-autoencoders]]
- [[induction-heads]]
- [[transformer-circuits-thread]]
