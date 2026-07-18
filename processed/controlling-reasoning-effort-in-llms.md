---
tags:
  - training
  - rl
  - rlvr
  - reasoning
  - inference-scaling
  - post-training
  - qwen
  - models
  - sft
source: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
date: 2026-07-18
type: article
description: "Raschka explains how multi-level reasoning effort (low/medium/high) is trained via effort-conditioned RLVR length penalties, SFT, chat templates, and open-weight recipes (Qwen3, DeepSeek V4, Nemotron, Kimi, GLM-5, Inkling)."
author: Sebastian Raschka
summary: "Raschka explains how multi-level reasoning effort (low/medium/high) is trained via effort-conditioned RLVR length penalties, SFT, chat templates, and open-weight recipes (Qwen3, DeepSeek V4, Nemotron, Kimi, GLM-5, Inkling)."
raw: "[[raw/sebastianraschka_controlling-reasoning-effort-in-llms]]"
published: 2026-07-18
---

# Controlling Reasoning Effort in LLMs

Sebastian Raschka (Ahead of AI, Jul 18 2026) on how modern LLMs get user-selectable reasoning effort (GPT-5.6 Light to Ultra, gpt-oss low/medium/high, continuous Inkling effort), not only binary think on/off.

## Key takeaways

1. Reasoning model means intermediate reasoning trace before final answer (not literal human reasoning).
2. RLVR (DeepSeek-R1 style) uses verifiable 0/1 rewards on math/code; format rewards add think delimiters. Traces often ignored in the reward (PRMs still research).
3. Think tags are cosmetic for capability; they structure UI and training separation.
4. On/off hybrid (Qwen3): Thinking Mode Fusion SFT mixes think traces and empty think non-think answers; enable_thinking=False hard-prefills empty think block.
5. Effort levels at inference are usually system-prompt or chat-template labels on a single checkpoint trained to map label to length/quality tradeoff.
6. Two training levers: (a) effort-conditioned length penalty in RL; (b) SFT on short vs long target traces. Often both.
7. Inference scaling is not training scaling: model size menu vs effort slider are separate knobs; small plus high effort can match large plus low effort on cost-accuracy curves (diminishing returns at max effort).
8. Open-weight recipes differ: DeepSeek V4 specialists plus distillation; Nemotron medium-effort plus hard budgets/truncation SFT; Kimi Toggle budgeted or unconstrained RL; GLM-5 turn-level/interleaved thinking; Inkling continuous effort in RL.

## Shared framework (six flagships)

| Ingredient | Role |
|------------|------|
| SFT + chat template | Teach thinking vs non-thinking formats |
| Mode-conditioned RL | Context window / length penalty by effort |
| Budget robustness | Truncation SFT, forced stop, alternating budgeted RL |

## Why it matters

Explains product UX (effort sliders) as post-training design, not prompt magic. Useful when building hybrid reasoners, agent cost controls, or comparing open models thinking modes.

## Related

- [[distillation-post-training-frontier-2026]]
- [[rlhf-from-first-principles]]
- [[training-llm-from-scratch-5-lessons]]
- [[how-to-build-your-own-llm-from-scratch-5-stage-pipeline]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
