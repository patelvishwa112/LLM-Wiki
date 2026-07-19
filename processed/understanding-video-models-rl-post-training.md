---
tags:
  - training
  - rl
  - rlhf
  - rlvr
  - dpo
  - grpo
  - video-generation
  - diffusion
  - flow-matching
  - post-training
  - reward-models
  - geometric-consistency
source: https://x.com/majumdar_ani/status/2078508177620926531
date: 2026-07-18
type: bookmark
author: majumdar_ani
description: "Majumdar Part III: RL post-training for video models — Flow-DPO/GRPO RLHF path plus sparse RLVR via epipolar/scene geometry (Epipolar-DPO, VideoGPA, VGGRPO)."
summary: "Majumdar Part III: RL post-training for video models — Flow-DPO/GRPO RLHF path plus sparse RLVR via epipolar/scene geometry (Epipolar-DPO, VideoGPA, VGGRPO)."
raw: "[[raw/majumdar_ani_2078508177620926531]]"
---

# Understanding Video Models: Part III — RL Post-Training

**@Majumdar_Ani** (Princeton / DeepMind) maps post-training for **video generators** onto the familiar LLM stack: maximize reward under a KL tether to a reference model, via **RLHF** and a thinner **RLVR** literature aimed mostly at **geometry**.

## Shared objective

Roughly: maximize E[r(v, c)] − β KL(pθ || pref) for video v given context c. Same shape as LLM RLHF/RLVR; the hard parts are **likelihoods under diffusion/flow**, **exploration in deterministic flow ODEs**, and **what “verifiable” means** for pixels over time.

## RLHF path

| Method | Idea |
|--------|------|
| **Diffusion-DPO** (Wallace 23) | DPO on diffusion; ELBO-style likelihood surrogate |
| **Flow-DPO** (Liu 25) | DPO via flow-matching link; beats Flow-RWR / Flow-NRG in their study |
| **Flow-DPO data** | **182K** multi-axis human prefs over **12** video models — main lever for quality jumps; used e.g. SkyReels-v2 motion |
| **Flow-GRPO / Dance-GRPO** | On-policy GRPO; ODE→SDE for exploration + KL; fewer train denoising steps, full steps at inference |
| **Reward models** | CLIP-style scores; VLM prefs (RewardDance “Yes” token probs + reasoning traces; VideoReward multi-axis) |

## RLVR path (nascent)

Objective rewards without human labels — mainly **multi-view / scene geometry**:

1. **Epipolar-DPO** — pairwise epipolar / Sampson error → preference pairs → Diffusion/Flow-DPO  
2. **VideoGPA** — foundation-model poses + aggregated point cloud, reproject for **scene-level** consistency prefs → DPO  
3. **VGGRPO** — dynamic scenes (static structure only in cloud); **latent adapter** so GRPO runs in video latent space (no full RGB decode for reward)

## Why it matters

- Documents that **video post-training is still mostly LLM-method porting** (DPO/PPO/GRPO), with RLVR far behind language.  
- Names the concrete **geometry-as-verifier** stack — useful contrast to math/code RLVR in language models.  
- Highlights **data** (182K prefs) and **flow-matching RL plumbing** (SDE relaxation) as the current bottlenecks more than novel algorithms.

## Related

- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[rlhf-from-first-principles]]
- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[continuous-batching-grpo-trl]]
- [[why-on-policy-distillation-works]]
- [[distillation-post-training-frontier-2026]]
- [[notes-on-foundation-models]]
- [[how-to-build-diffusion-language-model-kuleshov]]
- [[weight-synchronization-rl-post-training]]
