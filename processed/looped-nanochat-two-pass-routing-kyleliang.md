---
tags:
  - architecture
  - transformers
  - training
  - inference
  - looped-transformers
  - attention
  - nanochat
  - test-time-compute
  - ml-research
  - recurrence
source: https://x.com/kyleliang5/status/2078543088419840292
date: 2026-07-18
type: bookmark
author: kyleliang5
description: "Looped Nanochat: shared-weight two-pass Transformer with gated first-pass Q/K attention priors; +9–12% CORE, GSM8K relative +45% at ~2.4× train compute; K>2 untrained fails."
summary: "Looped Nanochat: shared-weight two-pass Transformer with gated first-pass Q/K attention priors; +9–12% CORE, GSM8K relative +45% at ~2.4× train compute; K>2 untrained fails."
raw: "[[raw/kyleliang5_2078543088419840292]]"
---

# Looped Nanochat — two-pass routing-loop Transformer

**@KyleLiang5** builds on Karpathy **nanochat**: same trunk **twice**, shared weights, with a learned **attention prior** from pass 1 into pass 2.

## Mechanism

1. **Pass 1:** ordinary causal stack; cache RoPE-normalized **(q₁, k₁)** at progressive source layers (d24: L12, L17, L23).  
2. **Pass 2:** restart from embeddings; each layer adds  
   `attn_logits = q₂k₂ᵀ/√D + g · (q₁k₁ᵀ/√D)`  
   with `g = softplus(gate)`.  
3. Implementation trick: concat heads to width **2D** so one FlexAttention equals the sum (no full N×N prior materialization). Extra params: per-layer gate + 2 pass embeddings (~same **1.38B** as baseline).

Routing (progressive): L0–7 ← L12; L8–15 ← L17; L16–23 ← L23. Gates **strong early** (~0.75–0.87), weak deep (~0.2) — first pass as rough plan for early second-pass reps.

## Results (matched data/tokens/schedule, 4×H100 d24)

| Metric | Baseline | Looped |
|--------|----------|--------|
| Base CORE | 0.2552 | 0.2783 (+9.0% rel) |
| ChatCORE | 0.2253 | 0.2521 (+11.9% rel) |
| ARC-E / ARC-C | 62.0 / 50.0 | 68.0 / 52.2 |
| MMLU | 37.1 | 38.0 |
| GSM8K | 2.9 | 4.2 (~+45% rel; still low abs) |
| HumanEval | 11.0 | 11.0 |

Cost: **~2.4× train time**, **~2× decode latency** — not free FLOPs. Iso-FLOP vs deeper/longer single-pass still open.

## Negative result (important)

Inference **K≠2** without training degrades val bpb. Looping ≠ automatic test-time scaling; needs variable-K training / curriculum / iterative objective.

## Why it matters

- Controlled alternative to “more params / data / tokens”: **same weights, richer compute graph** with depth feedback early layers normally cannot see.  
- Sits next to vault **looped-transformer / TTT** notes — different knobs (attention prior vs TTT adapters).  
- Honest efficiency caveats and failed multi-pass TTS make it citable, not hype-only.

Project / code: https://kyleliang919.github.io/looped_nanochat/ · github.com/kyleliang919/looped_nanochat

## Related

- [[looped-ttt-test-time-training-looped-transformers-alvinzh]]
- [[controlling-reasoning-effort-in-llms]]
- [[attention-qkv-math-amitiitbhu]]
- [[how-to-build-diffusion-language-model-kuleshov]]
- [[notes-on-foundation-models]]
- [[training-llm-from-scratch-5-lessons]]
- [[understanding-video-models-rl-post-training]]
