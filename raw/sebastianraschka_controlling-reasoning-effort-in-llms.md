---
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
ingested: 2026-07-18
author: Sebastian Raschka
title: Controlling Reasoning Effort in LLMs
sha256: 3188180d3beb6ad4cea5784f2b5763011611982ef56550cf03807a613b77ada1
note: Full article via Firecrawl markdown; structured full-article capture for vault
---

# Controlling Reasoning Effort in LLMs

### How LLMs Learn Low-, Medium-, and High-Effort Reasoning Modes

Sebastian Raschka, PhD — Jul 18, 2026
Source: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms

It has been almost two years since OpenAI released o1, a model that popularized the idea of LLM-based reasoning models. DeepSeek-R1 followed about four months later, together with details of a reinforcement learning with verifiable rewards (RLVR) recipe to train such reasoning models.

Last week, OpenAI released the GPT-5.6 model family. It comes in three sizes, each with roughly five or six reasoning-effort settings.

Reasoning models have become a standard part of modern model releases. This article explains how to develop a reasoning model that has multiple effort modes (low / medium / high), not only how to turn a conventional LLM into a reasoning model.

## 1. A brief definition of reasoning models

In LLM research, "reasoning model" means a model that outputs an intermediate reasoning trace — an intermediate response that works through a question or task step by step — before a final answer. It should not be taken as human-like reasoning.

## 2. Training and inference scaling

### 2.1 Training reasoning models

DeepSeek-R1 proposed training an LLM using RLVR: reward 0/1 for verifiable domains (math via symbolic checkers; code via tests/compilers). The intermediate reasoning trace itself was not used for the reward signal in R1 (process reward models remain active research). Format rewards encourage think-tag structure: R_total = R_accuracy + R_format.

### 2.2 Aha moments

Training on final-answer rewards alone was enough for models to learn intermediate explanations, backtracking, and self-correction ("aha" moments). DeepSeek-R1-Zero applied pure RLVR to a base model without SFT and showed RLVR alone can teach reasoning traces (weaker than full R1). Full R1 pipelines are multi-stage.

Related contemporaneous work: Kimi K1.5 (same arXiv day), Tulu 3 (coined RLVR earlier).

### 2.3 Inference scaling

Spending more compute at usage time: longer traces from RLVR models, self-consistency / majority vote, self-refinement (e.g. DeepSeekMath-V2). Reasoning effort settings further modulate output length.

## 3. Think tokens

Think open/close tags are cosmetic for capability: they mark where the reasoning trace begins/ends for training UI/hiding. Same performance possible without them. Implemented via format rewards during RLVR.

## 4. Reasoning mode on/off switches

First-gen models (DeepSeek-R1) were always-on verbose reasoners. Later hybrids (Qwen3) support thinking on/off.

Qwen3: tokenizer enable_thinking True/False. False force-adds empty think block at assistant start (hard switch). Soft switch via /think and /no_think in SFT Thinking Mode Fusion stage after long-CoT SFT + reasoning RL; general RL reinforces mode following.

## 5. How reasoning effort settings work

### 5.1 Effort, length, quality

OpenAI gpt-oss exposes effort via system prompt (Reasoning effort: low/medium/high) in the chat template. Effort correlates with response length and accuracy; returns diminish at highest levels (cost curves on Artificial Analysis Coding Agent Index for GPT-5.6). Inkling uses continuous effort 0.2-0.99 with similar length/score tradeoffs.

### 5.2 Possible training implementations

1. RLVR length penalties conditioned on effort labels in system prompts (high penalty for low effort).
2. Post-RLVR SFT on targets with different reasoning lengths paired with effort labels.
3. Combination of both (likely for gpt-oss / GPT-5.x).

Conceptual reward (Inkling-style): R(e) = R_task - lambda(e) * N_tokens with larger lambda for low effort.

### 5.3 Inkling case study

During large-scale RL: specify effort in system message; adjust per-token cost. Continuous e in [0,1]. Inference: Thinking effort level: 0.8.

### 5.4 Inference vs training scaling

Model menu (Luna/Terra/Sol) approximates different trained scales; effort slider is inference-time token budget on fixed weights. Smaller model + high effort can match larger model + low effort on some cost-accuracy curves.

## 6. Bonus: flagship open-weight recipes

### 6.1 DeepSeek V4 — separate effort specialists

Modes: Non-think, Think High, Think Max. Think Max uses special system instruction (Reasoning Effort: Absolute maximum...) plus different context window and length penalty during post-training. Specialists distilled into one checkpoint via on-policy distillation from a large teacher pool.

### 6.2 Nemotron 3 Ultra — learned modes + hard budgets

reasoning-off / regular / medium-effort via chat template (enable_thinking, medium_effort). Medium-effort from GPT-OSS-120B medium traces in SFT + about 2.5% of RLVR prompts. Hard budgets: truncate reasoning at token limit; SFT on randomly truncated traces with original answers; client may force-close think end tag.

### 6.3 Kimi K2.5 — Toggle (budgeted vs unconstrained RL)

Alternates budgeted RL (correct solutions within problem-specific token budgets) and unconstrained RL to avoid overfitting to short solutions. Budgets from percentiles of correct rollouts once accuracy threshold met. About 25-30% fewer tokens with little benchmark drop. Binary thinking/instant at inference separate from Toggle.

### 6.4 GLM-5 — turn-level / interleaved thinking via SFT

Interleaved thinking, preserved thinking across turns, turn-level on/off per request. Chat template prefills open or closed think tags. Multi-task SFT then reasoning/agentic/general RL + on-policy distillation.

### 6.5 Qwen3 — mode fusion + inference truncation

Long-CoT SFT, reasoning RL, Thinking Mode Fusion SFT, general RL. Hard thinking budget can stop reasoning span and insert stop-thinking instruction; partial-reasoning behavior emerged after fusion without explicit training.

### 6.6 Inkling — continuous effort in RL

Most post-training from async RL (more than 30M rollouts); effort in system message; lambda(e) token penalty during RL.

### 6.7 Shared framework

1. Introduce mode control via SFT + chat template (thinking vs non-thinking mixtures).
2. Mode-conditioned RL (context windows / length penalties vary by effort).
3. Robustness under budgets (random truncation, forced stop, alternating budgeted/unconstrained RL).

## 7. Conclusion

Similar UI labels can mean specialists, mixed SFT, mode-conditioned rewards, hard budgets, or combinations. No single best recipe; depends on product goals. Holy grail: automatic effort selection (GPT-5 Auto was imperfect and removed from UI). Future: cheap router chooses mode from request/tool state/budget with user override.

## Key papers / links referenced

- DeepSeek-R1 arXiv:2501.12948
- Kimi K1.5 arXiv:2501.12599
- Tulu 3 arXiv:2411.15124
- Qwen3 arXiv:2505.09388
- DeepSeekMath-V2 arXiv:2511.22570
- Kimi K2.5 arXiv:2602.02276
- GLM-5 arXiv:2602.15763
- Inkling: thinkingmachines.ai/news/introducing-inkling/
- gpt-oss model card / OpenAI effort via system prompt
