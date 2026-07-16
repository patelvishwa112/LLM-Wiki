---
tags:
  - continual-learning
  - training
  - rl
  - credit-assignment
  - agents
  - agent-memory
  - jepa
  - oak-lab
  - sutton
  - online-learning
  - sgd
source: https://x.com/handsdiff/status/2077392432505708714
date: 2026-07-15
type: bookmark
description: "handsdiff + Oak Lab — SGD assumes all data is to learn; IDBD/NetworkIDBD filter noise; agents wrongly treat context as pure signal."
author: handsdiff
summary: "handsdiff + Oak Lab — SGD assumes all data is to learn; IDBD/NetworkIDBD filter noise; agents wrongly treat context as pure signal."
raw: "[[raw/handsdiff_2077392432505708714]]"
---

# Learning from experience requires handling noise

@handsdiff flags first Oak Lab (@oaklab_ai, Sutton-linked) post: **learning from experience ≠ learning from curated datasets**. Dominant algorithms assume all data should be learned. Connects to **JEPA** (embeddings trained to filter noise) and argues multi-agent + memory systems often fail because agents treat **context = truth** (data = signal).

Linked post: https://oaklab.ai/posts/learning-from-experience-instead-of-curated-datasets.html (July 13, 2026)

## Oak Lab core argument

Human-curated datasets are cleaned so almost everything is learnable. **Experience** mixes predictable associations with unlearnable noise in inputs and targets. Modern deep learning mostly optimized for curated data → little pressure for unfiltered stream learners.

### Linear demos

Build a stream where one rare Bernoulli feature (1%) equals the target. SGD can learn weight 1. Then:

1. Rare ±1 target noise → only some targets predictable  
2. Heavy Gaussian target noise  
3. **4095** extra useless Bernoulli features  

**SGD / Adam / RMSProp** still try to fit every error → noise absorbed into weights. No selective credit; all non-zero-gradient params get blamed.

**IDBD** (Sutton 1992) learns *per-signal* credit and can **withhold** credit when targets aren’t predictable → recovers only the learnable component.

### NetworkIDBD + NoisyMNIST

Digit in center of noisy 64×64 canvas; target odd/even when digit present, else 0 + Gaussian noise. After training, large weights: **SGD** pumps all inputs (noise forwarded to hidden); **NetworkIDBD** concentrates on the center 28×28 digit region.

## Implication for online / continual learning

Mini-batch IID / replay averages away noise but is a poor fit for **online continual** streams. Thesis: need algorithms that **learn credit assignment** (NetworkIDBD as one instance), not just lower every residual.

## Agent takeaway (handsdiff)

If multi-agent stacks and memory files assume every token in context is trustworthy signal, they inherit the same bug as SGD-on-noise — related to “context-trust” pretrain biases and continual-learning amnesia discussions in the vault.

## Why it matters

Clean conceptual bridge: **Sutton-style credit assignment**, **JEPA-style noise filtering**, and **agent memory/context hygiene** as one problem family — not three separate fads.

## Related

- [[joint-embedding-predictive-architecture-jepa]]
- [[trying-to-actually-define-continual-learning-oneill]]
- [[what-if-harness-comes-before-pretraining-lihanc02]]
- [[continual-learning-replit-agent-vibench]]
- [[sutton-barto-rl-notes]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
