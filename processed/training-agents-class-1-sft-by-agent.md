---
tags: ["sft", "training", "agents", "lora", "gemma", "codex", "huggingface", "agent-traces", "distillation", "trl"]
source: https://x.com/sergiopaniego/status/2069369115630870771
date: 2026-06-23
type: bookmark
author: sergiopaniego
summary: "HF live class recap: one Codex prompt ran full SFT (data, train, Trackio, evals, model card) to teach Gemma 4 2B agent format from pi coding-agent traces; human keeps goal, constraints, and artifact verification."
raw: "[[raw/sergiopaniego_2069369115630870771]]"
---

# Training Agents Class 1 — SFT Run by an Agent

Sergio Paniego (Hugging Face) recaps a **live experiment**: a single prompt to **Codex** executed the entire supervised fine-tuning pipeline—no hand-written training code.

## Three-Agent Story

| Role | What it is |
|------|------------|
| **Builder** | Codex (or similar) does ML engineering |
| **Student** | Gemma 4 **2B** LoRA-tuned to mimic agent behavior |
| **Teacher (data)** | **pi** coding agent — real session traces (`pi-mono` dataset) |

## Why Small + Trace SFT

- Cheap, private, customizable coding agents vs frontier closed APIs.
- First milestone is **agent shape** (tool calls, multi-turn loop), not SOTA coding IQ.
- 2B + one SFT pass = visible limits; reproducible, auditable pipeline.

## Human vs Agent Split

Agent: resolve model, prep data, train, track (Trackio), eval (Inspect AI, vLLM), model card.  
Human: goal, constraints, pre-fixed selection rules, verify artifacts are real.

## Open Artifacts

- Stream: https://www.youtube.com/watch?v=rNgUoH7Wbv8
- Repo: https://github.com/burtenshaw/training-agents
- Dataset: https://huggingface.co/datasets/badlogicgames/pi-mono
- Example trace bucket: HF `burtenshaw/sft-on-traces`

## Why It Matters

Concrete **loop-engineering meets MLOps** pattern: an agent runs the training loop; real agent traces as curriculum for small open student models.

## Related

- [[loop-engineering-clearly-explained]]
- [[multi-lora-training-osmosis]]
- [[training-llm-from-scratch-5-lessons]]
- [[how-to-build-your-own-llm-from-scratch-5-stage-pipeline]]