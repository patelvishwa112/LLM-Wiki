---
tags: ["rl", "training", "post-training", "agents", "open-source", "glm", "megatron", "sglang", "slime"]
source: https://x.com/DailyDoseOfDS_/status/2083123018914746803
date: 2026-08-01
type: bookmark
description: "Open-source slime RL stack behind GLM-5.2 keeps one fixed learning kernel and pushes task variety into data generation."
author: DailyDoseOfDS_
summary: "Open-source slime RL stack behind GLM-5.2 keeps one fixed learning kernel and pushes task variety into data generation."
raw: "[[raw/DailyDoseOfDS__2083123018914746803]]"
---

# slime — open-source RL kernel behind GLM-5.2

## Key Takeaways

- Full post-training of GLM-5.2 ran on **slime** (~two days); same stack behind GLM 4.5 → 5.1.
- Core bet: **one stable RL learning kernel**; all task diversity lives in **experience generation**.
- Split: generation (model + scorer/env/tools) vs learning (samples → loss → optimizer). Learning stays mechanical and identical across math, multi-turn agents, sandboxes, verifiers.
- Stack: **Megatron** training + **SGLang** rollouts + **Data Buffer** owning prompts/custom data/generation logic.
- Supports Qwen3, DeepSeek V3, Llama 3; ecosystem builds (Dressage, Miles, vime, Relax, OpenClaw-RL, P1, TritonForge) without forking the loop.
- Engineering posture: explicit dataflow, CI, reproducibility, fault tolerance — RL bugs are silent.
- Repo: https://github.com/THUDM/slime
- Post quotes @akshay_pachaar “How to Fine-Tune LLMs in 2026” (GRPO / RULER / ART).

## Why it matters

Most RL stacks sprawl into disconnected trainers, rollout services, and agent frameworks. slime’s hard line (kernel vs data-gen) is a production-grade answer to that sprawl and pairs cleanly with modern agent RFT (GRPO + LLM judges).

## Related

- [[how-to-fine-tune-llms-2026-grpo-ruler-art-akshay]]
- [[continuous-batching-grpo-trl]]
- [[grpo-trl-training-agents-class3-sergiopaniego]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
