---
tags: ["rl", "mcts", "alphago", "llm-training", "credit-assignment", "autoresearch"]
source: https://x.com/dwarkesh_sp/status/2055324348332871779
date: 2026-05-15
type: note
related: ["sutton-barto-rl-notes", "fast-slow-training-continual-llm-adaptation", "rl-environments-guide-llm", "recursive-self-improvement-2028-prediction"]
---

# AlphaGo, MCTS, and LLM RL — Dwarkesh Patel with Eric Jang

## Summary
Dwarkesh Patel hosts Eric Jang for a blackboard lecture walking through how to build AlphaGo from scratch using modern AI tools. The conversation bridges AlphaGo's architecture to modern LLM training, revealing why naive policy gradient RL struggles with credit assignment in language models.

## Key Takeaways

### AlphaGo as the Cleanest Intelligence Primitive
- AlphaGo remains the cleanest worked example of intelligence primitives: search, learning from experience, and self-play
- Understanding 2017-era systems gives insight into how more general future AIs might learn

### Why RL in LLMs Struggles (vs AlphaGo's MCTS)
- Naive policy gradient RL must figure out which of 100k+ tokens in a trajectory actually produced the right answer
- AlphaGo's MCTS suggests a strictly better action every single move, providing a training target that sidesteps the credit assignment problem
- Human learning is likely closer to MCTS-style than naive policy gradient

### Automated AI Research
- LLMs can already automate: implementing/running experiments, optimizing hyperparameters
- LLMs still struggle with: choosing the right question to investigate, escaping research dead ends
- Relevant to intelligence explosion timing and what it would look like from the inside

## Lecture Timestamps
- 0:00:00 – Basics of Go
- 0:08:06 – Monte Carlo Tree Search
- 0:31:53 – What the neural network does
- 1:00:22 – Self-play
- 1:25:27 – Alternative RL approaches
- 1:45:36 – Why doesn't MCTS work for LLMs
- 2:00:58 – Off-policy training
- 2:11:51 – RL is even more information inefficient than you thought
- 2:22:05 – Automated AI researchers

## Connections
- [[sutton-barto-rl-notes]] — foundational RL theory
- [[fast-slow-training-continual-llm-adaptation]] — alternative to pure RL for LLM adaptation
- [[recursive-self-improvement-2028-prediction]] — automated AI research and recursive self-improvement
