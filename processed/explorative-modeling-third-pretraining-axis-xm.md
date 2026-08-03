---
tags: ["training", "pretraining", "generative-models", "diffusion", "scaling-laws", "image-generation", "video-generation", "language-models", "robotics", "world-models", "efficiency", "papers"]
source: https://explorative-modeling.github.io/
date: 2026-08-03
type: paper
description: "Explorative Modeling (XM) factors training not generation — third pretraining axis (K-mode exploration) plus end-to-end gen matching diffusion at far fewer NFEs."
authors: ["Alexi Gladstone", "Heng Ji", "Yilun Du"]
summary: "Explorative Modeling (XM) factors training not generation — third pretraining axis (K-mode exploration) plus end-to-end gen matching diffusion at far fewer NFEs."
raw: "[[raw/explorative_modeling_project_page]]"
arxiv: "2607.27372"
code_url: "https://github.com/alexiglad/XM"
---

# Explorative Modeling (XM) — third pretraining axis

**Project:** https://explorative-modeling.github.io/  
**arXiv:** https://arxiv.org/abs/2607.27372  
**Code:** https://github.com/alexiglad/XM  
**Authors:** Alexi Gladstone, Heng Ji (UIUC); Yilun Du (Harvard)

## Key takeaways

- Generative models stayed **not** end-to-end because they factor **generation** (many steps) to handle multimodality.
- **Explorative Modeling** factors the **training loop** instead: explore **K** candidate generations, train on the best match to data → commit to modes rather than blur.
- Two uses:
  1. **Third pretraining axis** (with params + data) bolted onto existing generative models.
  2. **Standalone end-to-end** reconstructive generation (train ≈ sample).

## Third axis results (reported)

| Claim | Number |
|-------|--------|
| Sample efficiency | 6.2× |
| FLOP efficiency | 4.1× |
| Parameter efficiency | 47% better (Large+XM-5 beats larger no-XM) |
| Gains vs data scale | 7% → 36% |
| Gains vs model scale | 13% → 23% |
| ImageNet 256 no-guidance FID | **1.43** (XDiTDH-XL XM-2 vs RAE baseline 1.55) |
| Convergence vs SiT | ~300× faster (claimed) |

Monotonic gains with K across **image (FID), video (FVD), language (masked-diffusion LM)**. More end-to-end base models benefit more; exploration can **reduce** optimal generation steps.

Generalization: more exploration → less memorization on small video data (best FVD 30.0 at XM-12 vs 37.5 none).

## End-to-end control

- **Robotics (Robomimic):** Explorative Policy ≈ Diffusion Policy success, **1 NFE vs 100**.
- **Maze2D world model:** better avg score than Diffuser at **~2.3 vs ~192 steps** (up to **256×** fewer NFEs).

## Forward XM (recipe)

Best-of-K on reconstruction (or diffusion) loss:

```text
losses = []
for _ in range(K):
    y = model(sample_latent())   # or noise for diffusion
    losses.append(recon_loss(y, x))
min(losses).backward()
```

Works continuous and discrete; full code at `alexiglad/XM`.

## Why it matters

Frames **generative expressivity** as the bottleneck once params/data scale, and makes “how end-to-end” a **scalable** knob via training-time exploration rather than inference steps only.

## Related

- [[how-to-build-diffusion-language-model-kuleshov]]
- [[distillation-post-training-frontier-2026]]
- [[understanding-video-models-rl-post-training]]
- [[continuous-batching-grpo-trl]]
- [[looped-transformers-explained-neural-avb]]
- [[gpt2-to-kimik3-architecture-22580-waterloo]]

## Source

https://explorative-modeling.github.io/  
https://arxiv.org/abs/2607.27372
