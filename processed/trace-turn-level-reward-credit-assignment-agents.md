---
tags: ["rl", "training", "agents", "credit-assignment", "rlvr", "grpo", "post-training", "tool-use", "qwen", "microsoft-research", "long-horizon", "browsecomp"]
source: https://x.com/sharonyixuanli/status/2078854876084502825
date: 2026-07-20
type: bookmark
author: SharonYixuanLi
title: "TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents"
description: "TRACE densifies outcome RL for long-horizon tool agents: frozen ref model scores gold-answer predictability per prefix; TD deltas become turn rewards (no critic, process labels, MC rollouts, or LLM judge). BrowseComp-Plus big gains; beats GRPO/GSPO/GiGPO."
summary: "TRACE densifies outcome RL for long-horizon tool agents: frozen ref model scores gold-answer predictability per prefix; TD deltas become turn rewards (no critic, process labels, MC rollouts, or LLM judge). BrowseComp-Plus big gains; beats GRPO/GSPO/GiGPO."
raw: "[[raw/sharonyixuanli_2078854876084502825]]"
paper: https://arxiv.org/abs/2607.13988
---

# TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents

## Why it matters

Thesis: **scaling outcome-only RL is not enough** for long-horizon agentic work. With tens–hundreds of tool calls, a single terminal reward is sparse and noisy — the bottleneck is **credit assignment**, so **turn-level reward is inevitable**. TRACE is a practical way to get dense turn rewards without the usual expensive machinery.

Paper: https://arxiv.org/abs/2607.13988 (led by @LeitianT; Sharon Yixuan Li + Microsoft Research collab).

## Method (TRACE)

- Credit at **tool-call boundaries**.
- For each trajectory **prefix**, a **frozen reference model** measures how much more **predictable the gold answer** became.
- Convert to a **state value**; **temporal-difference** changes become per-turn rewards:
  - **+** closer to answer
  - **~0** redundant
  - **−** moves away
- Global objective stays **probability of predicting the final answer**; turn rewards only attribute contribution.
- **No** trained critic, process/supervisory labels, Monte Carlo continuations, or strong LLM judge.

## Formulation properties

- Rewards **telescope** — repeating searches / reopening the same evidence cannot stack fake one-step credit.
- **Delayed credit** can propagate backward (search finds page + later `open` reveals key fact → both get localized credit).

## Results (as claimed)

Pure RL (no cold-start SFT, no agentic mid-training, no live-web training data):

| Model | BrowseComp-Plus |
|-------|-----------------|
| Qwen3-4B | 7.2 → **35.6** |
| Qwen3-30B-A3B | 8.4 → **42.6** (≈ Tongyi-DeepResearch-30B-A3B) |

Controlled same-setup comparisons: **outperforms GRPO, GSPO, GiGPO** at both scales.

## Skeptical read / open issues (from thread + framing)

- Needs a **gold / reference answer** to score answer-predictability — reply thread flags similarity to IGPO and asks whether this is “distillation-shaped” vs expanding the frontier beyond known solutions.
- Not a free lunch for open-ended agents without verifiable terminal answers (ties to the verifiability constraint cluster).
- BrowseComp-Plus is a search/browse benchmark; transfer to coding/ops agents is unshown in the thread.

## Key takeaways

- Long-horizon agent RL fails first as **attribution**, not only as “not enough outcome signal volume.”
- Dense rewards from **answer-predictability TD** are a middle path between pure outcome RL and labeled process supervision.
- Compare against the vault’s GRPO/policy-gradient and RLVR notes when designing agent post-training stacks.

## Related

- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[rlhf-from-first-principles]]
- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[continuous-batching-grpo-trl]]
- [[learning-from-experience-noise-oaklab-handsdiff]]
- [[openthoughts-agent-data-recipes-agentic-models]]
- [[distillation-post-training-frontier-2026]]
- [[controlling-reasoning-effort-in-llms]]
- [[understanding-video-models-rl-post-training]]
- [[reward-hacking-and-tampering]]
