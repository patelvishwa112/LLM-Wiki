<!-- sha256: af83fb4e06b2d857 -->
# RL ALGO — Comprehensive Q&A

**Source:** https://www.k-a.in/rl-algo.html
**Date:** 2026-06-08
**Note:** Answers to RL interview questions compiled by Xiuyu Li (@sheriyuo)

---

## Q: Why Actor-Critic instead of pure Critic?

Pure critic (DQN) needs argmax over actions — impossible for LLMs with vocab-sized action spaces. Actor-critic handles continuous actions naturally and has lower variance than pure policy gradient (REINFORCE). The critic serves as a baseline to kill variance and enables bootstrapping.

In LLM RL, the actor-critic argument is weaker — value functions over token sequences are hard to learn well. That's exactly why GRPO throws the critic away and uses a group mean as baseline.

## Q: KL divergence, cross entropy, and MLE relationship?

KL(P|Q) = H(P,Q) − H(P). When P (data distribution) is fixed, minimizing KL(P_data|Q_θ) = minimizing cross-entropy H(P_data, Q_θ) = MLE.

RLHF KL penalty is reverse KL (model seeking behavior) — why RL'd models lose diversity. DPO inherits this behavior.

## Q: Reward design in different RL scenarios?

- Verifiable correctness (math/code): clean unit tests, symbolic checks
- LLM-as-judge: noisy, gameable, prone to reward hacking
- Format rewards: should decay once format is learned
- Outcome vs Process rewards: ORMs reward final correctness, PRMs reward intermediate steps. Most LLM RL uses ORMs at scale.

## Q: Importance sampling, rejection sampling, and Monte Carlo in RL?

- IS: reweights off-policy data with ratio ρ = π_θ(a|s) / β(a|s). PPO clips it. GRPO uses IS implicitly. High variance when policies diverge.
- Rejection Sampling: filtering (best-of-N), ReST-style (sample, keep good, refit)

## Q: Advantage computation in PPO and GRPO?

**PPO (GAE):** A_GAE = Σ(γλ)^l δ_{t+l}, requires learned value function. Typically whitened per minibatch.

**GRPO:** A_i = (r_i − mean(r_j)) / std(r_j). Pure group-normalized reward, no critic, no reward model.

**Why subtract baseline?** Doesn't bias gradient (E[∇logπ·b] = 0) but dramatically reduces variance.

**Is std normalization necessary?** Helps stabilize but distorts advantage when group has near-zero variance (all right or all wrong). Dr.GRPO and DAPO clip/skip such groups.

## Q: RL training vs test-time scaling exploration?

RL training: learning — reshapes weights via stochastic sampling during rollouts.
Test-time scaling: exploration/search — uses fixed policy more extensively (best-of-N, beam search, MCTS) without modifying weights.

## Q: PPO clipping — why min? What happens without? CISPO difference?

L_CLIP = E[min(r_t·A_t, clip(r_t, 1−ε, 1+ε)·A_t)]

When A_t > 0: clip prevents overconfident updates.
When A_t < 0: clip prevents escaping punishment.
The min ensures we don't take steps too large in either direction.

Without clipping: pure IS-weighted gradient, ratio can become arbitrarily large → catastrophic gradient steps → policy collapse.

**CISPO:** Clips IS ratio in gradient computation but not loss value — preserves gradient flow for clipped samples (avoids PPO's flat gradient problem).

## Q: GRPO KL penalty — why? How computed? Why do DAPO/GSPO remove it?

Per-token KL between current policy and frozen reference. Prevents policy drift and reward hacking. Requires reference forward pass.

In RLVR (verifiable rewards): the verifier self-insures against hacking, making KL's protective job redundant. KL becomes pure drag — stops you moving far enough to learn the new domain. DAPO/GSPO drops it; clipping already bounds step size.

## Q: AllReduce accidentally applied multiple times during LLM training?

Gradient scaled by k → effectively k× learning rate → gradient explosion/overflow in BF16/FP16 → loss spikes or NaNs. Hard to spot — extra reduce sneaks in from gradient hooks or wrong pipeline placement.

## Q: DPO reward function? Can reward hacking occur? Mitigations?

Implicit reward: r(x,y) = β log(π*(y|x)/π_ref(y|x)) + β log Z(x)

Can exploit: length bias, surface features, degenerate solutions. Mitigations: IPO, length regularization, SFT warmup, iterative/online DPO (regenerate preference pairs from current policy).

## Q: Train-inference mismatch in MoE models?

Routing differs between training (auxiliary loss enforces uniform expert utilization) and inference (some experts overloaded, some idle).

Methods: Expert Choice routing (experts choose tokens — guarantees load balance but causes inference mismatch), auxiliary load-balancing losses, shared experts (dense), fine-grained expert segmentation, inference-time load balancing (vLLM/SGLang EP with work stealing).

## Q: Hyperparameter selection for RL training?

- **Group size G (GRPO):** 8-16 common. Too small = noisy advantages. Diminishing returns beyond 32.
- **Learning rate:** 1e-6 to 5e-6 for 7B models. More conservative than SFT (sparse, noisy reward signal).
- **PPO epochs:** 1-4. DeepSeek-R1 used 1. Beyond 4 often hurts (IS ratio drifts outside clip).
- **Generation length:** Adaptive (generate until EOS within max) > fixed-length. Long-CoT: 4K-32K tokens with careful memory management.

## Q: GRPO variants — Dr.GRPO, DAPO, GSPO, CISPO, SAPO, DPPO, MaxRL, SimKO?

- **Dr.GRPO:** Removes std normalization when group has zero variance. Question-level filtering.
- **DAPO:** Removes token-level KL. Clip-higher (higher upper clip for exploration). Dynamic sampling.
- **GSPO:** Sequence-level IS ratio constraint instead of token-level. Better aligned with sequence rewards.
- **CISPO:** Clips IS ratio in gradient, not objective. Preserves gradient flow.
- **SAPO:** Sequence-coherent + token-adaptive. Soft gating for continuous trust region.
- **DPPO:** Direct policy divergence estimate (TV or KL) instead of heuristic clipping.
- **MaxRL:** Sampling-based framework converging to max-likelihood in infinite-compute limit.
- **SimKO:** Asymmetric top-K boosting for correct responses, top-1 penalty for incorrect. Mitigates over-concentration.

## Q: TRPO, DPPO, AReaL trust-region enforcement?

- **TRPO:** Hard KL constraint, conjugate gradient + line search. Accurate but doesn't scale to LLMs.
- **DPPO:** Direct policy divergence estimate replacing heuristic clipping.
- **AReaL:** Importance sampling with staleness correction — drops/downweights rollouts past staleness threshold.

## Q: Can RL expand LLM capability frontier?

RL expands reliable use of existing capabilities and improves test-time search. Fundamental knowledge frontier is set by pretraining. Whether RL can push beyond remains open. See: "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"

## Q: ProRL — scaling RL training boundaries?

Builds on GRPO + DAPO enhancements: decoupled clipping (ε_low=0.2, ε_high=0.4), dynamic sampling, KL regularization with periodic reference policy reset + optimizer reinit. 136K problems across math, code, STEM, logic, instruction following. Sustains 2,000+ training steps.

## Q: OPD improvements over RL and SFT?

Dense credit assignment: every token gets a meaningful reward. On-policy training: student generates its own trajectories, receives teacher supervision on those. Consistently outperforms SFT. Applications: multi-task capability merging, strong-to-weak distillation, budget-controlled reasoning.

## Q: When does reasoning ability emerge?

Pretraining: foundational pattern matching. SFT: teaches structured expression. RL on verifiable tasks: amplifies and refines — teaches search for correct paths, not just imitation.

DeepSeek-R1 showed: SFT gives the format, RL gives the strategy.

## Q: DeepSeek R1 → V3.2 → V4 RL evolution?

- **R1:** GRPO, no critic, verifiable rewards, multi-stage pipeline
- **V3.2:** Single mixed RL stage (reasoning + agent + alignment), GRPO stabilization, unbiased KL, Off-Policy Sequence Masking for MoE, generative reward model with per-prompt rubrics
- **V4:** OPD replaces mixed RL, multi-teacher distillation, full-vocab logit distillation, Generative Reward Model (actor as judge), FP4 quantized rollouts, million-token-context RL, DSec sandbox

**Full arc:** PPO → GRPO (R1) → unified mixed-RL (V3.2) → specialist GRPO + OPD merge (V4)

**RL in MoE differences:** Routing makes gradients spiky, load balancing fights policy gradient, expert parallelism spreads rollouts, reference model for KL doubles expert memory.
