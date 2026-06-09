---
tags:
  - rl
  - rlhf
  - training
  - interview-answers
  - ppo
  - grpo
  - infrastructure
  - async-rl
  - moe
source: https://x.com/vivek_2332/status/2063566811749331353
raw: "[[raw/vivek_2332_2063566811749331353]]"
date: 2026-06-07
author: Vivek (@vivek_2332)
type: bookmark
summary: "Answers to Xiuyu Li's RL Interview Questions 2026. Covers 15+ algorithm questions (Actor-Critic, PPO/GRPO variants, DPO reward hacking, train-inference mismatch, KL penalty removal, OPD) and 13 infrastructure questions (model copies in GRPO, KV cache, FP8/INT8, async frameworks, Expert Parallelism, staleness, FSDP vs Megatron). Recommends PrimeIntellect over VeRL/TRL/Unsloth/AReaL/slime."
related:
  - "[[rl-interview-questions-2026]]"
  - "[[rlhf-from-first-principles]]"
---

# RL Interview Answers 2026

**Source:** Vivek (@vivek_2332). Answers to [[rl-interview-questions-2026]].

## Algorithm Answers

| # | Topic | Key Answer |
|---|-------|-----------|
| 1 | Actor-Critic vs pure Critic | Value-based: no large/continuous action spaces, greedy only. Policy gradient: high variance. Actor-critic: best of both. |
| 2 | CE / KL / MLE | CE(p,q) = KL(p,q) + entropy(p). Minimizing any → same place. MLE = KL(data, model). |
| 3 | Reward design | Verifiable (math/code) easier than non-verifiable (writing). Prevent reward hacking paths. Data + rewards written carefully. |
| 4 | MC methods in RL | Importance sampling: reuse off-policy samples in async RL. Rejection sampling: filter SFT/rollout data. |
| 5 | PPO vs GRPO advantage | PPO: critic + reward model. GRPO: multiple rollouts → mean as baseline → zero-sum within group. Std norm not necessary (Dr.GRPO). |
| 6 | RL vs test-time scaling | RL embeds domain intelligence into weights. Test-time scaling spends inference budget finding best paths. |
| 7 | PPO clipping | Prevents abrupt policy turns. Min from TRPO trust-region. CISPO clips importance weight instead of whole objective → more signal. |
| 8 | KL in GRPO | KL prevents drifting from good base model. Removed in DAPO/GSPO because it blocks learning new domains. Helps stability in RLVR. |
| 10 | DPO reward | Implicit reward baked in dataset. Reward hacking still happens — catch via sudden reward jumps or rollout length blowups. |
| 11 | MoE train-inference mismatch | Different engine/expert/kernel/quantization. Fix: replay expert selection, compute logprobs on trainer side. |
| 12 | Hyperparameters | Group: 8/16. LR: 1e-6 range. PPO epochs: 1 (more = off-policy, destabilizing). Gen length: task-dependent. |
| 13 | GRPO variants | Dr.GRPO: remove std. DAPO: clip-higher, dynamic sampling, token-level loss. GSPO: sequence-level IS (better for MoE). CISPO: clip weight. MaxRL: diversity collapse. |
| 14 | Trust-region | TRPO: constrained optimization. PPO: approximate with clip. AReaL: bounds staleness instead of hard KL. |
| 15 | RL capability frontier | Papers suggest RL sharpens existing abilities rather than forming new ones. Exploration + diversity might change this. |
| 17 | OPD | Combines RL's on-policy exploration with SFT's dense signal. Teacher scores student's own rollouts. Cheap capability transfer. |
| 18 | Reasoning emergence | CoT plays big part. Pre-training for baseline, post-training amplifies via reasoning + test-time compute. |

## Infrastructure Answers

| # | Topic | Key Answer |
|---|-------|-----------|
| 1 | Model copies in GRPO | Training policy + ref policy (KL) + inference model. Drop KL to remove ref. NVFP4 quantization, FSDP/EP/TP for distribution. |
| 2 | KV cache transfer | NVLink or layer-wise overlapped transfer. TP helps. Keep heavy KV movement within node. |
| 3 | FP8 vs INT8 | FP8: more exponent bits → training. INT8: more precision in fixed range → inference serving. |
| 4 | Long-tail rollouts | PipelineRL, continuous batching, early truncation. Mostly async setups. |
| 5 | Continuous batching in RL | vLLM: paged-attention. SGLang: RadixAttention (prefix sharing). Challenge: aligning trajectories/logprobs at different finish times. |
| 6 | Utilization metrics | Throughput (tok/s), KV cache occupancy, GPU util. Low GPU = waiting on rollout sync or CPU. |
| 7 | Backprop in multi-node | FSDP, EP, TP. CP for long context. Avoid PP — complex, unnecessary at most scales. |
| 8 | Async RL frameworks | Prime-RL, VeRL, TRL. Bottleneck: staleness, train-inference mismatch, token-in token-out. |
| 10 | Expert Parallelism | Experts placed per node/GPU set. Raises throughput via parallel FFNs but adds all-to-all comms. Gain = overlap + load balance. |
| 11 | FSDP vs Megatron | FSDP: shards grads/params/optim, gathers on demand, simpler. Megatron: DP+PP+TP (3D) with explicit comms. |
| 14 | Staleness | Gap between rollout policy and training policy. 1-4 steps typical. More = instability in importance sampling ratios. |
| 16 | Framework choice | None — use PrimeIntellect. |

## Key Insight

RL interview prep requires full-stack understanding — algo and infra are inseparable in modern RL roles. See the full question list in [[rl-interview-questions-2026]].
