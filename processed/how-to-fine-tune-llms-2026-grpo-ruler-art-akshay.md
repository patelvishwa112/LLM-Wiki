---
tags: ["rl", "training", "fine-tuning", "grpo", "agents", "evals", "openpipe", "art", "ruler", "lora", "post-training"]
source: https://x.com/akshay_pachaar/status/2029212227438518406
date: 2026-08-01
type: bookmark
description: "2026 agent fine-tuning path: GRPO + RULER LLM judges + OpenPipe ART for multi-turn tool agents without hand-written rewards."
author: akshay_pachaar
summary: "2026 agent fine-tuning path: GRPO + RULER LLM judges + OpenPipe ART for multi-turn tool agents without hand-written rewards."
raw: "[[raw/akshay_pachaar_2029212227438518406]]"
---

# How to Fine-Tune LLMs in 2026 (GRPO + RULER + ART)

## Key Takeaways

- Prompting/few-shot still fails ~30–40% and never learns from mistakes; shared frontier APIs give no moat.
- Small open models fine-tuned on *your* tasks can beat 10–100× larger general models on narrow domains (cost + latency).
- **SFT** = imitate pairs (textbook). **RFT** = trial/error with rewards (on-the-job) — required for multi-step tool agents.
- **GRPO** (DeepSeek-R1 lineage): sample N completions, score, normalize *within group*, reinforce above-average. Needs relative rankings only.
- **RULER** (Relative Universal LLM-Elicited Rewards): LLM judge compares trajectories (“which best achieved the goal?”) instead of brittle absolute 0–10 scores or hand-built reward functions. Works with cheap/local judges for many tasks.
- **ART** (OpenPipe Agent Reinforcement Trainer): open-source client/backend for real agents — tool calls, multi-turn, LangGraph/CrewAI/ADK; backend = vLLM + Unsloth GRPO; auto-load new LoRA after each step.
- Practical path: MCP server URL → auto task gen → RULER eval → GRPO on ~3B model (notebook pattern in article).

## Why it matters

Turns “reward engineering” into comparative prompt design and makes agent self-improvement accessible outside frontier labs. Pairs with production RL kernels like slime (fixed learning loop, variety in generation).

## Related

- [[slime-open-source-rl-kernel-glm-dailydose]]
- [[continuous-batching-grpo-trl]]
- [[grpo-trl-training-agents-class3-sergiopaniego]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[build-claude-code-harness-crewai-akshay]]
