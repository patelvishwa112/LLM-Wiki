---
title: Training Thousands of LoRA Adapters Concurrently — Osmosis Multi-LoRA
tags:
- lora
- rl
- training
- fine-tuning
- qwen
- osmosis
- post-training
- slm
source: https://x.com/_weexiao/status/2061855508156563871
date: 2026-06-02
published: 2026-06-02
authors:
- Kasey Zhang (@_WEEXIAO)
type: bookmark
raw: '[[raw/weexiao_2061855508156563871]]'
description: Multi-LoRA Training at Scale
---

# Multi-LoRA Training at Scale

Osmosis extended Megatron-Bridge + Miles to load multiple LoRA adapters as a single matrix, enabling 1,536 concurrent LoRA adapter instances on Qwen3.6-35B-A3B with <3 min step time.

## Key Takeaways

- **Core innovation:** Modify Megatron-Bridge + Miles to load multiple LoRA adapters as a single matrix. One base model, many LoRA deltas in the same training step. No base model replication per policy.
- **Scale:** 1,536 concurrent LoRA adapter instances on Qwen3.6-35B-A3B + GSM8K. Step time under 3 minutes (inference ~2 min, training ~1 min).
- **No divergence:** Reference model and policy model show virtually no divergence — consistent with every policy being a small LoRA delta off the same shared base.
- **Beyond efficiency:** (1) Online loading/unloading bypasses cold-start time for cluster spin-up. (2) Fast scaling of post-trained expert models for on-policy distillation.
- **Vision:** Turn large-scale RL from "train many separate models" into "train many deltas around one base model."
