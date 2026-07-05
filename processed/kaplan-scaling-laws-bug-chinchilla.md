---
tags: ["training", "scaling-laws", "chinchilla", "pretraining", "ml-research", "openai", "deepmind"]
source: https://x.com/completeskeptic/status/2073442518117884197
date: 2026-07-04
type: bookmark
author: completeskeptic
description: "Former OpenAI researcher argues Kaplan et al. scaling laws were wrong due to fixed token budgets plus cosine LR decay to zero—not parameter counting alone—so the field over-sized models for years; Chinchilla is the right recipe."
summary: "Former OpenAI researcher argues Kaplan et al. scaling laws were wrong due to fixed token budgets plus cosine LR decay to zero—not parameter counting alone—so the field over-sized models for years; Chinchilla is the right recipe."
raw: "[[raw/completeskeptic_2073442518117884197]]"
---

# Kaplan scaling laws bug (CompleteSkeptic)

Diogo Almeida (ex–OpenAI, RLHF / early ChatGPT) argues the **Kaplan vs Chinchilla** gap is not mainly about how total parameters were counted (the story in Lilian Weng’s reconciliation post and follow-up papers). The Kaplan recipe was **wrong in practice** because of three stacked experimental choices:

1. **Fixed training tokens** for all model sizes (~same budget for tiny and giant models), so small models were relatively over-trained and large ones under-trained.
2. **Cosine learning rate decay to zero** at that fixed horizon, so curves **plateaued** and looked like “more data won’t help.”
3. **Claiming LR schedule barely mattered** within the fixed-token regime—true locally but misleading for the infinite-data limit scaling laws target.

**Upshot:** For years the field built **too-large, under-trained** models. Chinchilla’s smaller model with **>4×** more tokens only works when training is not artificially capped by LR hitting zero at ~300B tokens. Labs reportedly internalized this; the original paper was never publicly amended.

## Why it matters

- Reframes “scaling-pilled” history: compute allocation (tokens per parameter) matters as much as parameter scaling.
- Useful when reading older “just scale width” narratives or debugging why pretraining recipes feel Chinchilla-shaped today.
- Pairs with experiment-design hygiene (fixed budgets + schedulers that fake saturation).

## Related

- [[design-good-ml-experiments-grigorev]]
- [[training-llm-from-scratch-5-lessons]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]