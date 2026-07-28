---
title: "What are Looped Transformers? Explained clearly"
tags: [architecture, transformers, looped-transformers, recurrence, test-time-compute, training, inference, moe, universal-transformer, models, ml-research]
source: https://x.com/neural_avb/status/2081741935883223196
date: 2026-07-28
published: 2026-07-27
authors: ["@neural_avb"]
type: bookmark
description: "Looped Transformers reuse the same layers for iterative latent thinking — parameter savings with FLOPs similar to deeper stacks; UT→Huginn→MoR→Loopie lineage."
summary: "Looped Transformers reuse the same layers for iterative latent thinking — parameter savings with FLOPs similar to deeper stacks; UT→Huginn→MoR→Loopie lineage."
author: neural_avb
raw: "[[raw/neural_avb_2081741935883223196]]"
---

# What are Looped Transformers? Explained clearly

Clear explainer from @neural_avb (AVB / Neural Breakdown) on the third path beyond “more params” and “more train compute”: **reuse weights by looping** so the model iteratively refines latents (“think more”) without storing a deeper stack.

## Core idea

- Train e.g. 25 layers and loop them 4× instead of 100 unique layers.
- Forward latency / FLOPs stay in the same ballpark as a deeper model; **stored weights drop** (4× in the example).
- Weights become **polymorphic**: same parameters must refine their own prior outputs.
- Strong showings on reasoning, ICL, ARC-AGI / Sudoku-style tasks.

## Lineage

1. **Universal Transformer (ICLR 2018)** — Shared transition applied recurrently over depth steps (parallel across tokens), vs RNN looping over sequence positions. Ancestor idea; didn’t win the early scale era (parallel dense stacks, Kaplan-era “scale,” hard sequential depth).

2. **Modern decoder-only “latent thinking”** — Typical split:
   - **Prelude (P):** normal layers → latent space  
   - **Recurrent core (R):** looped shared block  
   - **Coda (C):** final layers + LM head  
   Training often uses **truncated BPTT**. Instead of UT’s ACT halting, many modern recipes **sample loop count r at train time** so inference can dial loops as a compute–quality knob.

3. **Recent papers called out**
   - **Huginn / Recurrent Depth** (Geiping et al.) — modern reference  
   - **MoEUT** — loop + MoE  
   - **Relaxed Recursive Transformers** — per-step LoRA adapters on top of weight tying  
   - **Mixture-of-Recursions (MoR)** — easy tokens fewer loops, hard tokens more  
   - **DeepLoop** — loop-aware DeepNorm-style scaling (standard DeepNorm assumes independent layers)  
   - **Loopie** — layer-loop (`A A A B B B C C C` not `A B C A B C…`) + MoE + reinvested compute; claims **beat compute-matched vanilla** Transformers, not just param-matched  

Author points readers to paperbreakdown.com (Recurrent Depth → Loopie).

## Why It Matters

Connects vault notes on looped Nanochat / Ouro TTT and the broader test-time compute story: depth-as-iteration is an **architectural** compute dial, not only CoT tokens. Complements Kimi-style hybrid recurrent memory maps (different axis: state reuse vs layer reuse).

## Skeptical read

Ends with paperbreakdown.com CTA (author’s product). Paper claims (esp. Loopie beating compute-matched baselines) need primary-source checks; arXiv IDs in raw for follow-up.

## Source

[What are Looped Transformers? Explained clearly — @neural_avb](https://x.com/neural_avb/status/2081741935883223196)

## Related

- [[looped-nanochat-two-pass-routing-kyleliang]]
- [[looped-ttt-test-time-training-looped-transformers-alvinzh]]
- [[gpt2-to-kimik3-architecture-22580-waterloo]]
- [[autodata-synthetic-data-generation-explained]]
- [[how-ai-models-learn-skills-behaviors-leerob]]
