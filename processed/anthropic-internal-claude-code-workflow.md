---
title: Anthropic's Internal Claude Code Workflow (Boris Cherny)
tags:
- claude-code
- agents
- agent-ops
- anthropic
- claude
- coding-agents
source: https://x.com/polydao/status/2060810164068856130
raw: '[[raw/polydao_2060810164068856130]]'
date: 2026-05-30
published: 2026-05-30
authors:
- Mr. Buzzoni (@polydao)
- Boris Cherny (Anthropic)
type: article
description: Anthropic's Internal Claude Code Workflow
---

# Anthropic's Internal Claude Code Workflow

## Key Takeaways

- 80% of Anthropic engineers use Claude Code daily
- Give Claude access to run unit tests → rewrites code until tests pass, no human intervention
- Pipe massive GCP logs or git status via SDK with `-p` flag, process output as JSON
- Ctrl+R shows the exact context window the model currently sees
- Git worktrees enable 5 parallel Claude sessions on the same repo
- Enterprise policy files pre-approve safe bash commands → no confirmation prompts
- `#` before a message saves it permanently to CLAUDE.md memory

## Why It Matters

This is how the team that built Claude uses Claude Code. Not as a chatbot — as an autonomous coding agent. The key shift: trust the agent with verification (tests), give it context (log pipes), let it run in parallel (worktrees), and eliminate friction (pre-approved commands, persistent memory).

## Related

- [[raw/polydao_2060810164068856130]]
- [[processed/voxyz-ai-10-lessons-agents-md]]
