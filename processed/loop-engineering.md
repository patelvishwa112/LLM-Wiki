---
tags:
- loop-engineering
- agent-orchestration
- skills
- worktrees
- sub-agents
- claude-code
- codex
source: https://x.com/addyosmani/status/2064127981161959567
date: 2026-06-08
type: bookmark
author: addyosmani
summary: 'Loop engineering = designing the system that prompts agents instead of prompting
  them yourself. Five building blocks: automations, worktrees, skills, plugins/connectors,
  sub-agents + external memory. Both Codex and Claude Code now ship all five. The
  expensive part moved from tokens to loop management and verification.'
raw: '[[raw/addyosmani_2064127981161959567]]'
description: 'Loop engineering = designing the system that prompts agents instead
  of prompting them yourself. Five building blocks: automations, worktrees, skills,
  plugins/connectors, sub-agents + external memory. Both Codex and Claude Code now
  ship all five. The expensive part moved from tokens to loop management and verification.'
---

# Loop Engineering

Addy Osmani's synthesis of the emerging discipline of designing loops that prompt agents.

## The Five Building Blocks
1. Automations (scheduled discovery & triage)
2. Worktrees (parallel isolation)
3. Skills (reusable project knowledge)
4. Plugins & connectors (MCP integration)
5. Sub-agents (maker/checker split)

+ External memory (markdown, Linear, etc.) so the loop survives restarts.

## The Shift
The new skill is not writing one perfect prompt. The new skill is building the system that keeps prompting the agent until the job is done.

Relevant to Hermes goal-execution and agent harness design.