---
tags:
- rlhf
- training
- alignment
- reward-modeling
- ppo
- dpo
- constitutional-ai
- fundamentals
source: https://x.com/itsreallyvivek/status/2063610589621219596
raw: '[[raw/itsreallyvivek_2063610589621219596]]'
date: 2026-06-07
author: Vivek (@itsreallyvivek)
type: bookmark
summary: 'RLHF explained from first principles: the three-phase pipeline (SFT → reward
  model → PPO loop), Bradley-Terry preference modeling, the KL penalty as a leash
  against reward hacking, and common failure modes (reward hacking, distributional
  shift, labeler bias). Covers post-RLHF developments: DPO, Constitutional AI, RLAIF.
  Core insight: measured preferences ≠ actual values ≠ what''s genuinely good.'
related:
- '[[automate-writing-llm-prompts-dspy]]'
description: 'RLHF explained from first principles: the three-phase pipeline (SFT
  → reward model → PPO loop), Bradley-Terry preference modeling, the KL penalty as
  a leash against reward hacking, and common failure modes (reward hacking, distributional
  shift, labeler bias). Covers post-RLHF developments: DPO, Constitutional AI, RLAIF.
  Core insight: measured preferences ≠ actual values ≠ what''s genuinely good.'
---

# What Every Programmer Should Know About RLHF

**Source:** Vivek (@itsreallyvivek). A ground-up guide to the algorithm that teaches language models what we actually want.

## The Problem

A base LM is expensive autocomplete — no concept of helpfulness. SFT with human examples helps but hits a wall: the model learns to look helpful, not be helpful.

## Three-Phase Pipeline

| Phase | What | Output |
|-------|------|--------|
| 1. SFT | Fine-tune on human-written prompt-response pairs | Brittle starting point that roughly knows "good" |
| 2. Reward Model | Train a separate network on human preference comparisons | Scalar reward signal for any response |
| 3. PPO Loop | RL fine-tune the LM against the reward model | Policy that generates higher-scoring outputs |

## Reward Model Math

**Bradley-Terry model:** `P(y_w ≻ y_l | x) = σ(r(x, y_w) − r(x, y_l))`

**Loss:** `L(r) = −E[log σ(r(x, y_w) − r(x, y_l))]`

One human comparison → one bit of information → one gradient signal. Over thousands of comparisons, the reward model builds taste. But noisy labels → confidently wrong reward model.

## The KL Leash

```
max_π  E[r_φ(x, y)] − β · KL[π_θ ‖ π_SFT]
```

Without the KL penalty, the model reward hacks — finds responses that score high but are bad. The KL term anchors the policy near the SFT model so the critic's opinion stays meaningful.

## Failure Modes

| Failure | Mechanism |
|---------|-----------|
| **Reward hacking** | Long responses, sycophancy, confident nonsense — raters prefer these superficially |
| **Distributional shift** | Policy generates OOD outputs → reward model confidently wrong → phantom reward chasing |
| **Labeler bias** | Demographic blind spots, tone preferences baked into the reward signal |

## Beyond RLHF

- **DPO:** No separate reward model needed. Fine-tune directly on preference pairs.
- **Constitutional AI:** Written principles replace human comparisons for scalability.
- **RLAIF:** Another LLM replaces human labelers — cheaper, but whose values?

## The Chain

Human preference → scalar → gradient → behavior you interact with every day. Each step has a gap. RLHF doesn't guarantee alignment with actual values — it guarantees alignment with measured preferences, which are an approximation at best.
