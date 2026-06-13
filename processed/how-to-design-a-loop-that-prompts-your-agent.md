---
tags: ["loops", "agent-orchestration", "claude-code", "prompt-engineering", "skills"]
source: https://x.com/amitiitbhu/status/2063983640535847093
date: 2026-06-08
type: bookmark
author: amitiitbhu
summary: "Detailed blueprint for designing loops that prompt agents: 5 parts (define done, build context from state, act & capture, feedback, stop conditions). Full code pattern + common mistakes. The loop is the strategy; a prompt is just one move."
raw: "[[raw/amitiitbhu_2063983640535847093]]"
---

# How to design a loop that prompts your agent?

Amit Shekhar's complete guide to the five parts of a production loop.

## The Five Parts
1. Define "done" (the check that tells the loop when to stop)
2. Build the context from state (not hand-written instructions)
3. Let the agent act and capture everything (diff, logs, errors)
4. Close the loop with feedback (turn failure into the next prompt)
5. Set stop conditions (max turns, cost cap, human checkpoints)

## Key Insight
A prompt is a single move. A loop is the strategy that plays the full game.

Relevant to Hermes /goal and agent loop design.