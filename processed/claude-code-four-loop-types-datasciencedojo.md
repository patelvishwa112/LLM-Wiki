---
tags: ["loop-engineering", "claude-code", "agents", "agent-harness", "goal", "cronjob", "automation"]
source: https://x.com/datasciencedojo/status/2075671400900157670
date: 2026-07-11
type: bookmark
author: datasciencedojo
description: "Data Science Dojo maps four Claude Code loops by what starts and stops them: turn, /goal, /loop-/schedule, proactive."
summary: "Data Science Dojo maps four Claude Code loops by what starts and stops them: turn, /goal, /loop-/schedule, proactive."
raw: "[[raw/datasciencedojo_2075671400900157670]]"
---

# Claude Code Four Loop Types

**Source:** [X @DataScienceDojo](https://x.com/datasciencedojo/status/2075671400900157670) · [blog](https://datasciencedojo.com/blog/ai-agent-loop-types/) (raw via Playwright MCP)

## Summary

Four productized Claude loops, distinguished by **what starts the cycle** and **what stops it**:

1. **Turn-based** — user prompt → act/self-check → return. Default under almost every chat message.
2. **Goal-based (`/goal`)** — measurable finish line; evaluator model reopens work until condition clears. Only as good as measurability.
3. **Time-based (`/loop`, `/schedule`)** — timer replaces prompt; `/loop` local (dies with machine), `/schedule` cloud (session-independent).
4. **Proactive** — `/schedule` + `/goal` + workflow, event-triggered with no live prompter; each item resolves on its own goal until disabled. Easiest to get wrong at scale—pilot on few cases first.

**Default bias:** prefer turn-based unless the task has a real finish line or is genuinely ongoing. Match primitive to nature of work, not “most advanced.”

## Why it matters

Compact product map of Claude Code loop primitives; bridges vault’s abstract loop taxonomy (Aparna, Steinberger/Cherny) to concrete slash commands.

## Related

- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[wtf-is-a-loop]]
- [[how-to-create-loops-claude-code-sairahul1]]
- [[human-in-the-loop-agent-loops]]
- [[loop-engineering-clearly-explained]]
