---
title: Induction Heads
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [interpretability, induction-heads, circuits]
sources: [raw/papers/tcircuits-in-context-learning-and-induction-heads-index.md, raw/papers/arxiv-2202.07785.md, raw/papers/arxiv-2303.03846.md]
confidence: high
---

# Induction Heads

Induction heads are pairs of attention heads that implement a simple
copy-and-extend pattern: when the model sees `[A][B] ... [A]`, the second
head attends from the trailing `[A]` back to the first `[A]`, then promotes
`[B]` as the next-token prediction. They appear during training in a sharp
phase change that coincides with the emergence of in-context learning.

## What the sources say

- [[tcircuits-in-context-learning-and-induction-heads-index]] — The original
  Anthropic paper identifying induction heads and tying them to ICL emergence
- [[arxiv-2202.07785]] — "Predictability and Surprise in LLMs": broader
  context on capability emergence during training
- [[arxiv-2303.03846]] — "Larger language models do in-context learning
  differently": how ICL behavior changes with scale

## Related

- [[mechanistic-interpretability]]
- [[transformer-circuits-thread]]
- [[scaling-laws]]
- [[superposition]]
