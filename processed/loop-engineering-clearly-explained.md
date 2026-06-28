---
tags:
- loop-engineering
- agents
- agent-harness
- context-engineering
- claude-code
- prompt-engineering
- production
- evals
source: https://x.com/akshay_pachaar/status/2069118430582866051
date: 2026-06-23
type: bookmark
author: akshay_pachaar
summary: 'Accessible loop-engineering primer: the while-loop is solved; value is harness
  + brakes (completion checks, context rot, idempotent tools, critic). Boris Cherny
  builds loops, not prompts; same model + better loop can jump benchmark ranks.'
raw: '[[raw/akshay_pachaar_2069118430582866051]]'
description: 'Accessible loop-engineering primer: the while-loop is solved; value
  is harness + brakes (completion checks, context rot, idempotent tools, critic).
  Boris Cherny builds loops, not prompts; same model + better loop can jump benchmark
  ranks.'
---

# Loop Engineering Clearly Explained

Akshay Pachaar’s explainer on the shift from **prompt steering** to **loop design**, anchored on Boris Cherny (Claude Code): *“I don't prompt Claude anymore. I have loops that are running.”*

## Stack of Layers

| Layer | What you engineer |
|-------|-------------------|
| Prompt | Words sent to the model |
| Context | Full observable state (not just instructions) |
| Harness | Tool execution, state, errors |
| Loop | Autonomous cycle toward a goal |

**Agent = Model + Harness** (LangChain framing). Teams have held the model fixed and moved benchmark rank purely by harness/loop changes.

## The Trivial Core Loop

`model → tools → context → repeat` until no tool calls. Frameworks converge on ~6 lines; competition is everything *around* the `while`.

## Four Hard Parts (Where Loops Break)

1. **Stop conditions** — End of turn ≠ task done. Layer max iterations, budgets, no-progress detection, and **machine-checkable completion** (tests pass, not “agent feels done”).
2. **Context rot / doom loop** — Long runs degrade decisions. Treat context as budget: compaction, offload large outputs, sub-agents return summaries only.
3. **Tool design** — Few non-overlapping tools; **idempotent writes** for retries; errors written as *next-step instructions for the LLM*.
4. **Critic** — Separate maker from checker; worker must not grade its own homework.

## Mindset Shift

Design **goal (checkable success criteria)**, **loop (brakes)**, and **verifier** — then step back (Karpathy-style overnight research loops).

## Why It Matters

Pedagogical companion to deeper loop roadmaps in the vault; emphasizes production failure modes (turn vs task, self-approval) that pure prompt guides skip.

## Related

- [[wtf-is-a-loop]]
- [[loop-engineering-technical-roadmap-h100envy]]
- [[loop-engineering-14-step-roadmap]]
- [[agent-harness-should-repair-itself]]
- [[harness-is-the-product-context-aware-agents]]
- [[feedback-loops-claude-code-less-babysitting]]