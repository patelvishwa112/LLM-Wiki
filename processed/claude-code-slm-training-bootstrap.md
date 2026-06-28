---
tags:
- claude-code
- slm
- training
- rl
- synthetic-data
- agents
source: https://x.com/neural_avb/status/2057201992666411518
raw: '[[raw/neural_avb_2057201992666411518]]'
date: 2026-05-20
type: processed-note
related:
- '[[coding-agent-harness-eight-pillars]]'
- '[[rl-agents-system-prompt-reward-function]]'
description: Bootstrapping Claude Code to Train a Small Language Model
---

# Bootstrapping Claude Code to Train a Small Language Model

## Summary
A system where Claude Code acts as a teacher to design synthetic data, environments, and reward functions for post-training a smaller student model. The teacher reads the student's failure traces from real datasets and generates targeted synthetic data where the student is weakest, implementing a classical active learning loop with an RLVR (RL with Verifiable Rewards) twist.

## Key Takeaways
- Claude Code serves as the teacher agent, designing and writing synthetic data, environments, and reward functions
- The student model (SLM) is post-trained on real data, evaluated, and probed for weaknesses
- Failure traces from the student are fed back to the teacher, which generates new synthetic data targeting those weak spots
- This is an active learning loop: train on small bursts, evaluate, add data where the model is most confused
- The open-source implementation: `/synthetic-self-improve-rl` — a Claude Code skill

## Connections
- [[coding-agent-harness-eight-pillars]] — the agent harness architecture that could host this teacher-student pattern
- [[rl-agents-system-prompt-reward-function]] — the RL techniques (RLVR) used in the student training phase
