---
tags:
  - multimodal
  - vision
  - vlm
  - glm
  - post-training
  - sft
  - rl
  - training
  - models
  - projector
  - grokking
source: https://x.com/part_harry_/status/2077610277571637435
date: 2026-07-15
type: bookmark
description: "Harry Partridge — add vision to GLM 5.2 via 50M MLP projector on Kimi tower; MMMU-Pro ~Haiku; SFT then RL grokking; frozen LLM."
author: part_harry_
summary: "Harry Partridge — add vision to GLM 5.2 via 50M MLP projector on Kimi tower; MMMU-Pro ~Haiku; SFT then RL grokking; frozen LLM."
raw: "[[raw/part_harry__2077610277571637435]]"
---

# GLM 5.2 With Vision

@part_harry_ (Harry Partridge) — retrofit **image inputs** onto text-only **GLM 5.2** without hurting pure-text behavior.

## Result

- Train only a **2-layer MLP projector** (~**50M** params)  
- Freeze the LLM backbone  
- Vision ≈ **Claude 4.5 Haiku** on **MMMU-Pro (~55%)**  
- Additive: no image → original text-only model  
- Strong generalization: names people **absent** from the 66k alignment set (e.g. Hawking ~26% correct; common confusions Einstein / Feynman / Oppenheimer)

## How open VLMs “see”

Vision towers are small vs the LM (Kimi K2.6 tower ~**466M**, ~0.04% of full Kimi). Typical stack:

1. **Preprocess** — conv patches → token sequence  
2. **Encoder** — full (non-causal) attention  
3. **Projector** — map into LM embedding space  

Moonshot path for Kimi: continual pretrain of SigLIP-SO-400M (Google 2023). This project **reuses Kimi’s public tower** (good Megatron/vLLM/SGLang/TRT-LLM support) and trains **only the projector** into GLM space.

## Grokking in SFT

Random projector init. **2 epochs SFT** on **66k** public image Q&A pairs; batch 64; LR **5e-4**. ~**900 steps** (epoch ≈ 1035) → sharp loss drop = projector aligns vision features to GLM latents.

**Recipe detail:** keep SFT as **short Q/A**, not long captions. Hypothesis: long descriptions are **off-policy** for the LM and dominate loss even when vision is aligned — prevents clean alignment signal.

## Grokking in RL

SFT model doesn’t reason over images (no CoT in data). **RL on projector only** restores visual reasoning:

- First 4 batches of 512: **0** reasoning traces  
- Batch 5: one reasoning trace → policy shifts hard; reward climbs toward **~0.8**

## Why it matters

Efficient **multimodal retrofit** pattern: frozen strong text model + frozen/public tower + tiny projector + short SFT then RL for CoT. Generalization beyond the alignment set is the striking empirical claim.

## Related

- [[portal-portable-task-adapters-llms]]
- [[inkling-ear-7-9m-lookup-table-huckiyang]]
- [[distillation-post-training-frontier-2026]]
- [[aiedge-glm-5.2-guide]]
- [[joint-embedding-predictive-architecture-jepa]]
