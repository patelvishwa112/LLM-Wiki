---
tags:
- jepa
- i-jepa
- v-jepa
- yann-lecun
- meta
- self-supervised-learning
- embeddings
- world-models
- representation-learning
- contrastive-learning
- vision-transformer
- computer-vision
- energy-based-models
- autonomous-machine-intelligence
source: https://outcomeschool.com/blog/joint-embedding-predictive-architecture-jepa
raw: '[[raw/outcomeschool_jepa]]'
type: article
author: Amit Shekhar (Outcome School)
date: 2026-06-06
description: Joint Embedding Predictive Architecture (JEPA)
---

# Joint Embedding Predictive Architecture (JEPA)

**Core idea:** Predict the gist of the hidden part, not every exact pixel. JEPA predicts summaries in embedding space instead of redrawing raw pixels — efficient, clean, and grounded in how humans learn by observation.

## Origin

Yann LeCun's 2022 paper "A Path Towards Autonomous Machine Intelligence" — a vision for machines that learn a model of the world by observation (like a baby) and can then imagine outcomes and plan toward goals. JEPA is the core building block.

## The Analogy

Looking at a photo: left half visible (dog, grass, tree), right half covered. We guess "more grass, a tail, a bit of tree" — the gist, not exact pixels. JEPA works the same way.

## JEPA vs. Alternatives

| Approach | What it predicts | Problem |
|----------|-----------------|---------|
| **Generative models** | Raw pixels (redraw hidden half) | Wastes effort on unpredictable detail |
| **Contrastive learning** | Similarity (push/pull pairs) | Needs many negative examples + hand-made augmentations |
| **JEPA** | Summary in embedding space | Clean, efficient, no negatives needed |

## Architecture

- **x-encoder:** visible context → summary s_x
- **y-encoder:** hidden target → summary s_y
- **Predictor:** takes s_x + position (+ latent z) → predicted s_y-hat
- **Energy =** gap between s_y-hat and s_y (low = good match)

## I-JEPA (Image, Meta 2023)

- Cuts image into patches, processed by Vision Transformer
- Context encoder (visible block) → predictor guesses target summaries
- Target encoder sees full image, summaries for target blocks selected after encoding
- **Collapse avoidance:** context encoder learns normally; target encoder follows via EMA + stop-gradient (acts as fixed answer key). No negative examples needed.
- Trained on ImageNet: 16 GPUs, <72 hours

## V-JEPA (Video, Meta 2024) → V-JEPA 2 (2025)

Same idea extended to video. V-JEPA 2 moves toward **world models** — internal sense of how the world behaves. A robot version controlled a real arm to pick and place objects in new labs just by being given a goal image, planning steps by imagining outcomes in embedding space.

## Why JEPA Matters

1. **Meaning over detail** — skips impossible pixel prediction
2. **Efficient** — summaries lighter than pixels, trains faster/cheaper
3. **Clean** — no negative examples, no hand-made augmentations
4. **Complementary to LLMs** — LLMs lack physical intuition; JEPA learns it by watching
5. **Toward common sense** — step toward machines that imagine, plan, and act