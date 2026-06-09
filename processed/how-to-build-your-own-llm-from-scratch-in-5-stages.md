---
tags: ["llm", "training", "models", "pretraining", "post-training", "data"]
source: https://x.com/0xcodez/status/2058911661973454915
raw: "[[raw/0xcodez_2058911661973454915]]"
date: 2026-05-25
type: bookmark
---

# How to Build Your Own LLM From Scratch in 5 Stages

## Key Takeaways
- Architecture (transformers) matters least — data, evaluation, and systems make or break a model
- Data pipeline is the most secretive and important stage: Common Crawl → filter → deduplicate → classify → reweight
- Scaling laws let you predict performance before training — Chinchilla says ~20 tokens/param, but practical ratio is 150+ due to inference costs
- Post-training (SFT + RLHF) turns a text completer into an assistant that follows instructions
- The bitter lesson: don't over-complicate. Do simple things and scale them

## Summary
A compressed guide to the five-stage pipeline behind models like GPT and Claude: pretraining, data curation, scaling laws, post-training, and evaluation/systems. The core insight is that architecture is the commodity — the real moat is in data quality, compute-efficient scaling, and engineering that ships.

## Source
[https://x.com/0xcodez/status/2058911661973454915](https://x.com/0xcodez/status/2058911661973454915)
