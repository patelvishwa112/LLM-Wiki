---
title: "Finetuning with Sampling: SFT Learns Better Than You Think"
type: bookmark
description: "Karan, Chen and Du keep the SFT loss and change the data instead: projection sampling uses an MCMC chain to rewrite off-policy expert traces into higher-likelihood, on-policy equivalents, and the resulting SFT beats OPSD, GRPO and UFT on new tasks while forgetting the least."
tags: [sft, post-training, sampling, mcmc, rl, distillation, forgetting]
source: https://x.com/aakaran31/status/2106037829059133903
date: 2026-10-02
author: Aayush Karan
summary: "Karan, Chen and Du keep the SFT loss and change the data instead: projection sampling uses an MCMC chain to rewrite off-policy expert traces into higher-likelihood, on-policy equivalents, and the resulting SFT beats OPSD, GRPO and UFT on new tasks while forgetting the least."
raw: "[[raw/aakaran31_2106037829059133903]]"
---

# Finetuning with Sampling: SFT Learns Better Than You Think

**Source:** Aayush Karan (@aakaran31), 2026-10-02. Announcement thread (1/n, rest as replies) for arXiv:2610.02140 with Sitan Chen and Yilun Du — sampling as an operator on post-training *data* rather than on the loss.

The paper takes the standard explanation of why RL generalizes and SFT does not — RL trains on its own samples, SFT trains on someone else's — seriously, and then removes the constraint that makes RL expensive. SFT gets to keep off-policy expert traces, which carry privileged information the model could never produce by sampling; RL gets on-policy traces, which keeps updates close to the base distribution but yields no gradient when the model cannot find a correct rollout at all. Projection sampling asks for the distribution that is simultaneously the closest to the base model and supported only on traces that are still correct: the information projection `p_C ∝ p(x)·1(x ∈ C)`, where `C` is the set of traces semantically equivalent to the expert one (same final answer, or same factual content under an LLM grader). SFT on samples from `p_C` is technically off-policy but distributionally near-on-policy, and nothing in the objective changes.

Because `p_C` is intractable to sample directly when the base model cannot solve the task, the paper runs Metropolis–Hastings on it: start from the expert trace, propose information-preserving mutations (a continuation prompt that must reach the same final answer), accept by likelihood ratio. The KL between the data-generation policy and the base model is provably non-increasing at every step, which is what separates this from "rewrite the data with a model once and hope" — the paper's own ablation shows a zero-th-order rewrite (rewrite SFT) lands between vanilla SFT and the full chain. For LLMs the chain is applied block-wise (B=32, T=1856, 10 MCMC steps per block, reusing the power-sampling implementation from the authors' prior work), with a cheaper swap rule that trades an exact acceptance test for a monotone-but-aggressive drift toward high-likelihood regions. Information preservation is verified rather than assumed: boosted datasets retain 93.9–95.9% of the original traces' accuracy across chemistry, math and medical.

The results are the kind that make the SFT-versus-RL argument concrete. On chemistry with Qwen2.5-7B-Instruct, sampling SFT reaches 0.660 against 0.618 for both vanilla SFT and OPSD, and it forgets least — a 1.10-point average drop across MMLU/GPQA/AMC/MATH500/GSM8K where vanilla SFT loses 7.7, with MMLU actually improving to 0.692. On math with Qwen2.5-3B it beats both RL baselines on the hardest split (0.495 vs GRPO 0.457, UFT 0.470) and reaches 0.582 on MATH500 versus a 0.245 base, and the checkpoint is a better RL initialization than the base — GRPO on top of it is the strongest model in the paper. Medical is the honest counterexample on the new task (0.458 vs OPSD's 0.466) where sampling SFT still wins on retention. Two controls sharpen the claim: boosted data is model-specific (Qwen trained on Olmo-boosted data falls to 0.5733, below vanilla SFT), and pass@k stays above the base model at high k, so the model is learning new behavior rather than re-weighting what it already had.

## Why it matters

This reframes a live budget decision. If most of the generalization benefit attributed to RL comes from on-policy-ness rather than from the reward signal, then much of it is purchasable with sampling compute instead of rollouts and reward infrastructure — and it composes with RL rather than replacing it, since sampling SFT is the better initialization. It also gives a cheap diagnostic for an underperforming fine-tune: check the likelihood of your training traces under the base model before blaming the data or the hyperparameters.

## Key points

- Target distribution is the information projection of the base model onto semantically-equivalent traces: `p_C ∝ p(x)·1(x ∈ C)` — closest to the base model while preserving the expert's information.
- Sampling is Metropolis–Hastings with information-preserving proposals; KL(data policy ‖ base) is non-increasing every step (Proposition 3).
- LLM implementation: block-wise projection sampling, B=32, max length T=1856, N_MCMC=10; a higher-likelihood swap rule avoids the second forward pass per iteration.
- Chemistry (Qwen2.5-7B-Instruct): 0.660 vs base 0.343, vanilla SFT 0.618, OPSD 0.618, rewrite-SFT 0.613 — +31.7 over base, +4.2 over OPSD.
- Forgetting on that run: −1.10 average across five prior benchmarks (MMLU 0.692 vs base 0.687) versus −7.7 for vanilla SFT.
- Math (Qwen2.5-3B): 0.495 on MATH(3,4,5) vs GRPO 0.457 and UFT 0.470; MATH500 0.582 vs base 0.245; GRPO initialized from the sampling checkpoint gets 0.545 / 0.652 / 0.830 (MATH345 / MATH500 / GSM8K).
- Medical (Qwen2.5-7B-Instruct): 0.458 vs OPSD 0.466 on the new task, but it recovers 16.3 points of the 24.4-point prior-capability loss that vanilla SFT takes.
- Boosted data does not transfer across base models: Qwen trained on Olmo-boosted chemistry data scores 0.5733, below vanilla SFT's 0.618; a 50/50 mix lands at 0.6214.
- Information preservation measured, not assumed: 94.33%/93.94% chemistry (Qwen/Olmo), 95.33% math, 95.86% medical.

## Related

- [[opsd-off-policy-self-distillation]]
- [[why-on-policy-distillation-works]]
- [[distillation-post-training-frontier-2026]]
- [[on-policy-distillation-aha-neural-avb]]
- [[how-to-fine-tune-llms-2026-grpo-ruler-art-akshay]]
