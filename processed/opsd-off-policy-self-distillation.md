---
tags:
- rl
- off-policy
- self-distillation
- opsd
- opd
- training
- llm
- agents
- grpo
- distillation
- policy-optimization
source: https://x.com/ar0cket1/status/2054108160450064571
type: bookmark
summary: 'ar0cket1 shares early experimental results on Off-Policy Self-Distillation
  (OPSD). Goal: achieve RL-like performance upper bounds while retaining OPD''s sample
  efficiency and training stability. Work in progress after 1+ week of experiments,
  with results shared via X Article cover image.'
ingested: 2026-06-13
description: 'ar0cket1 shares early experimental results on Off-Policy Self-Distillation
  (OPSD). Goal: achieve RL-like performance upper bounds while retaining OPD''s sample
  efficiency and training stability. Work in progress after 1+ week of experiments,
  with results shared via X Article cover image.'
---

# Off-Policy Self-Distillation (OPSD)

**Source:** X post by @ar0cket1 (May 12, 2026) linking to personal X Article with experimental results.

## Key Claims & Goals
- **Objective:** Solve OPSD to get RL-level performance ceilings combined with off-policy distillation (OPD) sample efficiency and stability.
- **Status:** ~1 week+ of focused work; preliminary results shared (visuals in linked article).
- **Motivation:** Improve upon standard OPD by incorporating self-distillation elements for better policy optimization in LLM/agent training pipelines.

## Technical Context
- Aligns with broader interests in GRPO-style training, advantage computation from rollouts, reward modeling, and refitting generation backends.
- Related arXiv reference (nearby post): https://arxiv.org/abs/2604.13010 — OPD maintains proximity to SFT support, mitigating some off-policy distribution shift issues.
- User actively seeking compute resources for expanded OPSD experiments.

## Connections to Vault
- **RL/Training:** Extends discussions on policy optimization, off-policy methods, and hybrid RL-SFT approaches seen in other notes on GRPO, harness engineering, and agent training.
- **Agents & Harness:** Potential implications for agent training loops involving dataloaders, controllers, trajectory scoring, and iterative policy improvement.
- **Interpretability/Mechanistic:** Self-distillation may relate to understanding residual streams and value propagation in trained models.

## Open Questions
- What specific metrics (e.g., reward curves, sample efficiency gains, stability under distribution shift) are shown in the full article results?
- How does OPSD compare quantitatively to pure RL and standard OPD baselines?
- Integration points with existing frameworks like TRL, GRPO implementations, or custom harnesses?

**Raw Source:** [[raw/ar0cket1_2054108160450064571]]

*Note: Full X Article content inaccessible without authentication; synthesized from post text, metadata, and related activity.*

## Related

- [[rl-training-pipelines]]
- [[off-policy-rl]]
- [[grpo-advantages]]
- [[self-distillation]]
- [[ar0cket1]]
