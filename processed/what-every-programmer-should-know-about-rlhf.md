---
tags:
- rlhf
- dpo
- constitutional-ai
- reward-model
- alignment
- training
source: https://x.com/itsreallyvivek/status/2063610589621219596
date: 2026-06-07
type: bookmark
author: itsreallyvivek
summary: 'Clear explanation of the RLHF pipeline: SFT → reward model (Bradley-Terry
  on preference pairs) → PPO with KL penalty to prevent reward hacking. Covers failure
  modes (reward hacking, distributional shift, labeler bias) and post-RLHF methods
  (DPO, Constitutional AI, RLAIF). Emphasizes that measured preferences ≠ actual values.'
raw: '[[raw/itsreallyvivek_2063610589621219596]]'
description: 'Clear explanation of the RLHF pipeline: SFT → reward model (Bradley-Terry
  on preference pairs) → PPO with KL penalty to prevent reward hacking. Covers failure
  modes (reward hacking, distributional shift, labeler bias) and post-RLHF methods
  (DPO, Constitutional AI, RLAIF). Emphasizes that measured preferences ≠ actual values.'
---

# What Every Programmer Should Know About RLHF

vivek's ground-up guide to the algorithm behind modern aligned models.

## The Three-Phase Pipeline
1. **Supervised Fine-Tuning (SFT)**: Start with base model, fine-tune on high-quality human prompt-response pairs.
2. **Reward Model Training**: Humans compare pairs of responses; train a model to predict preferences using Bradley-Terry model.
3. **RL Fine-Tuning (PPO)**: Use reward model as environment; optimize policy with KL penalty to stay close to SFT model.

## Key Insights
- The reward model is the most important (and most skipped) part.
- KL penalty prevents reward hacking and over-optimization.
- Failure modes: reward hacking, distributional shift, labeler bias.
- Post-RLHF methods (DPO, Constitutional AI, RLAIF) remove or reduce the need for a separate reward model.

Relevant to alignment, post-training, and understanding why models behave the way they do.