---
tags: ["rl", "training", "mechanistic-interpretability"]
source: https://x.com/neural_avb/status/2051536715983327563
date: 2026-05-04
type: processed-note
related:
  - "[[rl-agents-system-prompt-reward-function]]"
---

# Policy Gradients: From REINFORCE to GRPO

## Summary
A timeline tracing the evolution of policy gradient methods from the foundational REINFORCE algorithm through to modern techniques like PPO and GRPO. Each step addresses a weakness of the previous generation: REINFORCE's high variance → Actor-Critic's bias-variance tradeoff → A2C/A3C's advantage function → PPO's trust region → GRPO's latest innovations.

## Key Takeaways
- **REINFORCE**: The purest form — Monte Carlo rollout returns directly increase probability of actions in high-return trajectories. Unbiased but high variance. Baselines reduce variance without biasing the gradient
- **Actor-Critic**: Splits into critic (value function for state quality) and actor (action probabilities from critic estimates). Lower variance but biased — the critic proxies for real rollout scores
- **A2C/A3C**: Introduces advantage — measures how much better/worse an action is compared to the state's baseline. Prevents penalizing good actions taken in naturally low-value states
- **Variance-bias tradeoff**: REINFORCE = high variance, unbiased. Actor-Critic = lower variance, biased. Each generation navigates this tension
- **Related concept**: MC (Monte Carlo Sampling) vs 1-step TD (Temporal Difference Learning)

## Connections
- [[rl-agents-system-prompt-reward-function]] — modern application of these algorithms where system prompts serve as reward functions
