---
tags: ["foundation-models", "architecture", "vlm", "vla", "world-models", "video-generation", "image-generation", "biological-models", "mixture-of-transformers", "alphafold", "diffusion", "flow-matching", "encoders", "interaction-models", "realtime"]
source: https://x.com/bqbrady/status/2064055370809778371
date: 2026-06-08
type: bookmark
author: bqbrady
title: "Notes on Foundation Models"
summary: "~10K-word survey of modern foundation model architectures: VLMs, encoders, Mixture of Transformers, interaction models, video/image generation, world models, VLAs, and biological models (AlphaFold, ESM, Evo2). With detailed glossary."
raw: "[[raw/bqbrady_2064055370809778371]]"
related: ["[[joint-embedding-predictive-architecture-jepa]]", "[[inference-engines-2026]]", "[[anthropic-recursive-self-improvement]]"]
---

# Notes on Foundation Models

## Key Takeaways

1. **The encoder debate is settling.** SigLIP-2 is the default ViT for open VLMs. Counterintuitively, brute-force grid patching (16×16 non-overlapping) works. Trend toward minimal preprocessing (Gemma 4B, Thinking Machines) — less opinionated encoders trained end-to-end.

2. **Mixture of Transformers (MoT) solves multimodal crowding.** Split transformer body into per-modality weight stacks with shared global attention. No routing — deterministic per modality. Applied in both VLMs and VLAs (Cosmos 3).

3. **VLAs converge on diffusion heads.** Autoregressive token prediction is awkward for spatial coordinates. Modern VLAs use diffusion/flow-matching action heads. Long-term coherence solved by two-layer systems (MEM) with compressed memory.

4. **World models are the new robotics frontier.** F(Previous Frame, Action) → Current Frame. Latent-space prediction (JEPA) vs pixel-space reconstruction debate. MCTS planning over world model trajectories.

5. **Biological models enforce strong structural priors.** AlphaFold's EvoFormer enforces triangle inequality and co-evolution. Unlike LLMs which learn everything from data, bio models bake in geometric invariants.

6. **The interaction model pattern:** latency-sensitive model on top of powerful VLM. Async tool calling with oracle streams. Thinking Machines' native (video, audio, text) → (audio, text) with minimal preprocessing.

## Architecture Reference

| Domain | Default Architecture | Key Innovation |
|--------|---------------------|----------------|
| VLMs | SigLIP-2 ViT + Projector + LLM | Patch-based encoding |
| Video | DiT + 3D flow-matching blocks | 16×16×4 frame patches |
| Audio | AuT + Whisper-style mel-spectrograms | Discrete 80ms tokens (Moshi) |
| VLAs | VLM backbone + Diffusion Action Head | Two-tower MoT (Cosmos 3) |
| World Models | DiT flow-matching or JEPA latent | Action-conditioned frame prediction |
| Proteins | AlphaFold EvoFormer/PairFormer | MSA co-evolution + geometric invariants |
| DNA | Evo2 hybrid conv + attention | 1M context, 4-token vocabulary |

## Blog Post

Full version at: https://www.benedict.dev/foundation-models
