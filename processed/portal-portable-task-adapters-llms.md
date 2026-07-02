---
tags:
  - lora
  - peft
  - training
  - fine-tuning
  - hypernetwork
  - portable-adaptation
  - qwen
  - gemma
  - slm
source: https://x.com/RampLabs/status/2072381992285647280
date: 2026-07-01
type: bookmark
author: ramplabs
description: "PorTAL (Ramp Labs): frozen task latent + shared LoRA hypernet core; refit thin per-base converter — ~98% of LoRA lift on unseen Qwen3-8B vs ~14% Cross-LoRA."
raw: "[[raw/ramplabs_2072381992285647280]]"
summary: "PorTAL (Ramp Labs): frozen task latent + shared LoRA hypernet core; refit thin per-base converter — ~98% of LoRA lift on unseen Qwen3-8B vs ~14% Cross-LoRA."
---

# PorTAL: Portable Task Adapters for LLMs

Ramp Labs research (Ben Geist) on **amortizing task-specific LoRA** across rotating base models.

## Problem

Each new foundation model forces a full per-task LoRA retrain. Release cadence is shortening; maintenance cost scales with portfolio size × model churn.

## Idea

Learn once:

1. **Task latent** `z_t` (base-agnostic)
2. **Shared hypernetwork core** emitting LoRA factors at a fixed core width
3. **Thin per-base converter** (layer embeddings + dimension aligners)

**Porting:** freeze latent + core; calibrate only the converter on a small per-task set (≤2k examples/task in their setup).

## Key numbers

| Setting | vs per-task LoRA lift |
|---------|------------------------|
| Same-family unseen Qwen3-8B (train on 1.7B+4B) | **~98%** |
| Cross-LoRA baseline on 8B | **~14%** |
| Cross-family Gemma-3-4B | **~94%** |
| Source Qwen3-4B hypernet vs per-task LoRA | **~94%** |

Also claims **~2× data efficiency** and **better calibration** (lower held-out log-loss) vs from-scratch LoRA when matching accuracy.

## Relation to prior art

Combines single-base LoRA hypernets (Text-to-LoRA), cross-architecture generation (LoRAGen), and cross-model transfer (Cross-LoRA, LoRA-X, CAST)—but emphasizes **refitting a converter** rather than one-shot adapter translation without calibration.

## Why it matters

Operational answer to **model upgrade paths** for specialized SLM/adapter portfolios—relevant alongside multi-LoRA serving and agent-training data pipelines.

**Source:** [Ramp Labs research](https://labs.ramp.com/research)

## Related

- [[multi-lora-training-osmosis]]
- [[training-agents-class-1-sft-by-agent]]
- [[autodata-synthetic-data-generation-explained]]