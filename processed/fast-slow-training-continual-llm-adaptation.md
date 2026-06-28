---
tags:
- training
- rl
- continual-learning
- models
- fast-slow-training
source: https://x.com/KushaSareen/status/2054586907904901245
raw: '[[raw/KushaSareen_2054586907904901245]]'
date: 2026-05-13
type: note
description: Fast-Slow Training for Continual LLM Adaptation
---

# Fast-Slow Training for Continual LLM Adaptation

## Summary
Fast-Slow Training (FST) is a technique that pairs "slow" model weights with "fast" context, inspired by classic ML and neuroscience. It addresses the core challenge of adapting LLMs continually without catastrophically losing base skills — something pure RL approaches struggle with.

## Key Takeaways
- **FST vs RL:** FST achieves 3x more sample efficiency, higher performance ceilings, and less KL drift (better plasticity)
- **Continual learning advantage:** FST checkpoints remain amenable to future RL training; heavy RL on a narrow domain makes continued training difficult when tasks change
- **How it works:** Context is treated as "fast weights" and model parameters as "slow weights," using co-evolving prompt optimization instead of reward signals
- **OOD performance:** Equal or better out-of-distribution performance compared to RL
- **Core insight:** RL forces adaptation through rewards; FST leverages strong in-context learning capabilities already present in modern LLMs

## Connections
- [[on-policy-distillation-resources-2026]] — related distillation-based training approaches
- [[alphago-mcts-llm-rl-dwarkesh-eric-jang]] — explores why RL struggles with credit assignment in LLMs
- [[rl-environments-guide-llm]] — infrastructure matters for RL at scale
