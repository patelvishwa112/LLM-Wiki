---
title: Persona Vectors
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [interpretability, persona-vectors, alignment]
sources: [raw/articles/anthropic-research-persona-vectors.md, raw/articles/anthropic-research-persona-selection-model.md]
confidence: high
---

# Persona Vectors

Persona vectors are activation-space directions that correspond to character
traits a language model expresses (e.g., helpfulness, deceptiveness,
harmfulness). They are extracted via [[sparse-autoencoders|feature-style]]
methods and can be used to monitor — or steer — the model's persona at
inference time.

## What the sources say

- [[anthropic-research-persona-vectors]] — Original work: identifying
  persona directions and monitoring/controlling them
- [[anthropic-research-persona-selection-model]] — Treats persona choice
  as a learned selection process inside the model

## Related

- [[mechanistic-interpretability]]
- [[sparse-autoencoders]]
- [[claude-values-and-character]]
- [[model-welfare]]
