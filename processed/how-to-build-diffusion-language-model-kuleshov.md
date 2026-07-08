---
tags:
  - training
  - llm
  - diffusion
  - dllm
  - masked-diffusion
  - architecture
  - inference
  - scaling-laws
  - transformers
  - tutorial
source: https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/
date: 2026-01-01
type: bookmark
author: Kuleshov Group
description: "Tutorial on diffusion LLMs — masked/uniform diffusion, remasking, block diffusion, distillation, post-training; Mercury 2, Gemma Diffusion, Nemotron; parallel inference scaling thesis."
raw: "[[raw/kuleshov_how-to-build-diffusion-language-model_2026]]"
---

# How to Build a Diffusion Language Model

**Source:** [Kuleshov Group blog](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) (ICLR 2026 / MLSS 2026 material)

## AR vs diffusion for text

Autoregressive LMs: left-to-right, no revision, causal attention, latency ∝ sequence length. **Diffusion LLMs (dLLMs):** start from noisy/full draft, **refine all positions in parallel** over steps — bidirectional context, built-in error correction, speed/quality knob via step count.

## Building blocks (survey)

- **Masked diffusion (MDLM):** forward masks tokens; reverse unmasks; simple but errors can stick.
- **Remasking (ReMDM):** re-mask subset of committed tokens → predictor–corrector; inference-time compute scaling toward AR quality.
- **Uniform-state diffusion:** random token corruption; any position editable each step.
- **Block diffusion:** flexible-length generation.
- **Architectures:** encoder / decoder / encoder–decoder variants for dLLMs.
- **Distillation:** faster sampling.
- **Controllable generation** and **post-training** recipes.
- **Production examples (2026):** Mercury 2, Gemma Diffusion, Nemotron Diffusion; also biological/scientific domains.

## Scaling-laws framing (closing thesis)

Pre-training scaled via **parallel transformer** vs sequential RNNs. Post-2024 gains increasingly from post-training + **inference-time compute**, still bottlenecked by sequential AR decoding. Authors argue diffusion could make **inference fully parallel** — analogous to transformer’s role for pre-training — improving FLOPs/s utilization up to ~100B-parameter experiments cited.

## Why it matters

Canonical open tutorial for **non-AR language modeling** — connects to vault training roadmaps, GPU parallelism notes, and text-diffusion experiments (e.g. from-scratch lesson threads).

## Related

- [[training-llm-from-scratch-5-lessons]]
- [[llm-engineering-projects-roadmap-2026]]
- [[how-to-build-your-own-llm-from-scratch-5-stage-pipeline]]
- [[how-gpu-executes-code-first-principles]]
- [[rlhf-from-first-principles]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]