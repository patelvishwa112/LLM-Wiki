---
title: Sparse Autoencoders (Dictionary Learning)
created: 2026-05-22
updated: 2026-05-22
type: concept
tags:
- interpretability
- sparse-autoencoders
- features
sources:
- raw/anthropic/papers/tcircuits-monosemantic-features-index.md
- raw/anthropic/papers/tcircuits-scaling-monosemanticity-index.md
- raw/anthropic/papers/arxiv-2406.04093.md
- raw/anthropic/articles/anthropic-research-mapping-mind-language-model.md
- raw/anthropic/articles/anthropic-research-natural-language-autoencoders.md
- raw/anthropic/papers/tcircuits-2026-nla.md
- raw/anthropic/articles/anthropic-research-evaluating-feature-steering.md
confidence: high
description: Sparse Autoencoders / Dictionary Learning
---

# Sparse Autoencoders / Dictionary Learning

Training a wide, sparse linear autoencoder on a language model's hidden
activations recovers a dictionary of human-interpretable features. This is
Anthropic's main technique for resolving [[superposition]] into discrete
concepts and is the empirical backbone of modern circuit-level interpretability.

## What the sources say

- [[tcircuits-monosemantic-features-index]] — "Towards Monosemanticity":
  the first demonstration at meaningful scale (Pythia-style models)
- [[tcircuits-scaling-monosemanticity-index]] — Extending the recipe to
  Claude 3 Sonnet
- [[arxiv-2406.04093]] — "Scaling and evaluating sparse autoencoders":
  systematic study of SAE quality vs. compute
- [[anthropic-research-mapping-mind-language-model]] — "Mapping the Mind
  of a Large Language Model": features extracted from production Claude
- [[anthropic-research-natural-language-autoencoders]] / [[tcircuits-2026-nla]]
  — Decoding feature directions into natural-language descriptions
- [[anthropic-research-evaluating-feature-steering]] — Using features to
  steer behavior, with a social-bias case study

## Related

- [[mechanistic-interpretability]]
- [[superposition]]
- [[transformer-circuits-thread]]
- [[persona-vectors]]
