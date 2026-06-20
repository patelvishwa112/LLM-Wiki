---
tags: [on-policy-distillation, self-distillation, hallucination, ood-generalization, rlvr, reasoning-models, qwen, distillation, epistemic-verbalization]
source: https://x.com/rish2k1/status/2068414528598286485
type: concept
ingested: 2026-06-20
related: [[rlm-agents-structured-outputs], [agents], [agent-harness]]
---

# Why On-Policy Distillation Works and Naive Self-Distillation Doesn't

**Source:** [X Post by @rish2k1](https://x.com/rish2k1/status/2068414528598286485)

## Summary

Rishabh Tiwari provides a clear mechanistic explanation for why **on-policy distillation** succeeds while **naive self-distillation** fails in reasoning models.

**On-policy distillation** works when the teacher is both better on reward *and* close to the student. It delivers a dense token-by-token signal equivalent to KL-regularized RL toward a reward-tilted policy — highly sample- and compute-efficient when the teacher (larger model or RL expert) puts more probability mass on high-reward trajectories.

**Naive self-distillation** (student distills from itself using privileged information at training time, then runs without it at inference) fails because the “teacher” is not a good reward-tilted target. It teaches the model to mimic the *appearance* of having privileged information rather than actually producing higher-reward outputs.

## Failure Modes Observed (Qwen3-8B reasoning models on chemistry, tool-use, Polaris math)

- **Hallucination**: 96–100% in-distribution, 80–98% OOD — model fabricates references/solutions/feedback it never received.
- **Collapsed epistemic verbalization**: Hedging/backtracking tokens drop from ~86 to <10 per response. Produces overconfident, non-exploratory outputs.
- **Poor OOD generalization**: 6–25 point drop vs. pure RL despite competitive IID accuracy.

Prompt engineering and hybrid losses helped only by *reducing* the distillation term's influence. Pure RL remained strongest for robust reasoning.

## Why It Matters

This is high-signal mechanistic insight into training dynamics for reasoning agents. Directly relevant to RLVR, agent training loops, hallucination mitigation, and the limits of distillation. Explains why certain “self-improvement” distillation approaches degrade exploration and OOD performance. Strong connection to agent-harness engineering and structured output work.

## Key Metrics to Track
- Hallucination rate
- Epistemic verbalization count
- OOD generalization (not just IID accuracy)

## Related
- [[rlm-agents-structured-outputs]]
- FST / GEPA fast-weight approaches
- RLVR and on-policy methods in the vault