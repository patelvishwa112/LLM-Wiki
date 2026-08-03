---
source_url: https://explorative-modeling.github.io/
ingested: 2026-08-03
author: alexiglad
title: "Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation"
paper_url: https://arxiv.org/abs/2607.27372
code_url: https://github.com/alexiglad/XM
blog_url: https://alexiglad.github.io/blog/2026/explorative_modeling/
note: Firecrawl credits exhausted; body via Playwright main.innerText from project page
sha256: fe56f03a932e6cb501a02efff36ed3dd59491f82b6f25ad20f9b0d26ea05bc26
---

# Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

Alexi Gladstone (UIUC), Heng Ji (UIUC), Yilun Du (Harvard)

Project page: https://explorative-modeling.github.io/
Paper PDF: https://explorative-modeling.github.io/static/pdfs/paper.pdf
arXiv: https://arxiv.org/abs/2607.27372
Code: https://github.com/alexiglad/XM
Blog: https://alexiglad.github.io/blog/2026/explorative_modeling/
HF: https://huggingface.co/papers/2607.27372
Tweet: https://x.com/AlexiGlad/status/2083230922196107288

## TL;DR

We introduce Explorative Modeling, a new paradigm for generative modeling that acts as a third pretraining axis when added to existing generative models, and also enables end-to-end generation. Increasing exploration monotonically improves existing models across images, video, and language, and the gains grow with scale (7%→36% with data, 13%→23% with parameters). Concretely, Explorative Models (XMs) reach 6.2× sample efficiency, 4.1× FLOP efficiency, and 47% better parameter efficiency. Exploration also enables scaling generalization, and scaling how end-to-end existing models are. As end-to-end generative models, XMs match diffusion on control tasks with up to 256× less inference compute.

## Abstract

The deep learning revolution, kicked off by AlexNet, taught us that end-to-end training beats decomposing a problem into hand-designed stages. Generative modeling, however, has remained the exception — despite generative models being remarkably capable, they are still not trained end-to-end. This is because, at its core, generative modeling is about handling multimodal distributions, and existing scalable approaches handle this multimodality the same way, by factoring the generation procedure, which prevents end-to-end generation. In this work, we introduce Explorative Modeling, a new paradigm that instead factors the training loop, exploring K candidate matches between model generations and data, and training on the best, so predictions commit to modes rather than blurring them. We find Explorative Models (XMs) useful in two settings. First, increasing exploration adds a third pretraining axis beyond parameters and data for existing generative models — where scaling exploration monotonically improves performance across both continuous and discrete domains (images, video, and language). Notably, gains from exploration increase with scale, climbing from 7% to 36% as data scales and from 13% to 23% as models grow, with efficiency gains more than doubling at 3× the compute. Concretely, exploration improves FLOP efficiency by 4.1×, sample efficiency by 6.2×, parameter efficiency by 47%, lifts the strongest of image-generation recipes to a near-state-of-the-art 1.43 FID on ImageNet without guidance, enables scaling how end-to-end existing models are, and unlocks scaling generalization. Second, XMs enable end-to-end reconstructive generative modeling, matching diffusion on control tasks with 16–256× fewer inference steps. Together, these results establish XMs as both a new pretraining axis for existing generative models and a standalone end-to-end generative modeling paradigm.

## The Idea: Factor Training, Not Generation

A generative model can break two things into pieces: how it generates, or how it trains. Today's models break up generation into hundreds of small steps, which works but prevents end-to-end generation. Explorative Models (XMs) break up training instead, through exploration. Because of this, for existing generative models, XMs unlock a third pretraining axis beyond parameters and data. XMs also enable end-to-end generative modeling, where sampling during training and inference are identical.

Increasing exploration (K) lets a model capture more modes instead of averaging them.

## Exploration as a Third Pretraining Axis

We add exploration to RAE, a near-SOTA image-generation recipe. Without any hyperparameter tuning, simply adding XM gives 6.2× better data efficiency and 4.1× better FLOP efficiency. The compute-optimal amount of exploration also keeps growing the longer you train.

The same holds for model size: a Large model that explores 5 modes outscales an XLarge model with 47% more parameters and no exploration.

With the model fixed, increasing exploration alone monotonically improves performance across images (FID), video (FVD), and language (a masked-diffusion LM). Some models gain over 20%, and the gains have not stopped at the highest exploration levels we test.

A generative model's performance is limited by three capacities: parameters restrict what it can represent, data restricts what it can learn, and generative expressivity restricts what it can generate. Scaling parameters and data relieves the first two, but generative expressivity is set by the training objective itself, so as models and data grow it increasingly becomes the bottleneck. Exploration raises generative expressivity directly, and its gains grow with scale — rising from 13% to 23% as models scale and from 7% to 36% as data scales.

Because exploration commits to real modes instead of a blurry average, there's less of an artifact to memorize, so models generalize better. On a small video dataset, more exploration overfits less and reaches a better best FVD (30.0 vs 37.5).

Exploration also lifts the strongest recipes. Added to RAE, it reaches a near-best 1.43 FID without guidance and converges ~300× faster than the standard SiT recipe.

Method (ImageNet 256×256, no guidance) | gFID ↓ | FDr6 ↓ | IS ↑
REPA-E (VAE latent diffusion) | 1.70 | – | 217.3
DiTDH-XL (RAE baseline) | 1.55 | 4.42 | 237.3
XDiTDH-XL, XM-2 Ours | 1.43 | 3.91 | 240.3

Exploration helped every model family tested, but models that are more end-to-end benefit most. Factoring training can substitute for factoring generation: as exploration increases, the best-performing models become increasingly end-to-end.

## End-to-End Generation

Taken to its limit, exploration handles multimodality during training, so the model generates end-to-end in one step (or a few) instead of hundreds.

### Behavior Cloning (robot manipulation)

Method | Steps | Lift | Can | Square | Transport | Tool Hang
Diffusion Policy | 100 | 100% | 100% | 94% | 72% | 86%
Explorative Policy Ours | 1 | 100% | 100% | 96% | 74% | 86%

### Goal-Conditioned World Modeling (Maze2D)

Diffuser avg score 127.2 at ~192 steps; Explorative World Model avg 130.0 at ~2.3 steps (16–256× fewer NFEs).

## Getting Started (Forward XM pseudocode)

Before exploration — one generation per step:
y = model(sample_latent())
loss = recon_loss(y, x)
loss.backward()

After exploration — explore K, keep the best:
losses = []
for _ in range(K):
    y = model(sample_latent())
    losses.append(recon_loss(y, x))
min(losses).backward()

Same recipe for diffusion/flow (explore over noises) and discrete masked-diffusion LMs.

Code: https://github.com/alexiglad/XM

## BibTeX

@misc{gladstone2026explorativemodelingunlockingpretraining,
      title={Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation},
      author={Alexi Gladstone and Heng Ji and Yilun Du},
      year={2026},
      eprint={2607.27372},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2607.27372},
}

Source extracted via Playwright from project page 2026-08-03.
