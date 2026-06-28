---
tags:
- rl
- agents
- prompt-engineering
- training
source: https://x.com/_avichawla/status/2049037299334472015
raw: '[[raw/_avichawla_2049037299334472015]]'
date: 2026-04-28
type: processed-note
related:
- '[[policy-gradients-timeline-reinforce-to-grpo]]'
description: RL Agents Using System Prompt as Reward Function
---

# RL Agents Using System Prompt as Reward Function

## Summary
Top AI labs (Anthropic, OpenAI, DeepSeek) are converging on using the system prompt as the reward function for reinforcement learning agents. This builds on Karpathy's system prompt learning idea. The evolution traces from RLHF to RULER. The OpenPipe ART repository provides a concrete implementation.

## Key Takeaways
- System prompts are being repurposed as reward functions for RL agents — a convergence across major labs
- The approach builds on Karpathy's idea of learning system prompts through optimization
- The evolution path: RLHF → RULER (using system prompt as reward)
- Reference implementation available at [OpenPipe/ART](https://github.com/OpenPipe/ART)

## Connections
- [[policy-gradients-timeline-reinforce-to-grpo]] — the policy gradient algorithms that underpin this RL
- [[claude-code-slm-training-bootstrap]] — related teacher-student RL training pattern using Claude Code
