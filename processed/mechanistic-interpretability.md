---
title: Mechanistic Interpretability
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [interpretability, circuits, features, superposition]
sources: [raw/anthropic/articles/*, raw/anthropic/papers/*]
confidence: high
---

# Mechanistic Interpretability

The science of understanding how neural networks work internally — reverse-engineering
their computations at the level of circuits, features, and mechanisms.

## The Transformer Circuits Thread

Anthropic's dedicated publication venue for interpretability research:
[[transformer-circuits-thread]]

Key publications in order:
1. [[tcircuits-framework-index]] — A Mathematical Framework for Transformer Circuits
2. [[tcircuits-in-context-learning-and-induction-heads-index]] — In-context Learning and Induction Heads
3. [[tcircuits-toy_model-index]] — Toy Models of Superposition
4. [[tcircuits-monosemantic-features-index]] — Towards Monosemanticity
5. [[tcircuits-scaling-monosemanticity-index]] — Scaling Monosemanticity
6. [[tcircuits-2026-nla]] — Natural Language Autoencoders (2026)

## Major Discoveries

### Superposition
Neural networks represent more features than they have dimensions.
See [[superposition]] for a full synthesis.
[[tcircuits-toy_model-index]]

### Sparse Autoencoders / Dictionary Learning
Decomposing model activations into interpretable features.
See [[sparse-autoencoders]] for a full synthesis.
[[arxiv-2406.04093]]

### Mapping Claude's Mind
Direct visualization of features inside Claude 3 Sonnet.
[[anthropic-research-mapping-mind-language-model]]

### Natural Language Autoencoders
Training models to translate their internal representations into human-readable text.
[[anthropic-research-natural-language-autoencoders]]

## Key Techniques

- Circuit analysis
- Feature visualization
- Sparse autoencoding
- Activation patching
- Logit lens / tuned lens
