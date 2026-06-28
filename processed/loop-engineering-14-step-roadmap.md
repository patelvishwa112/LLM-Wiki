---
tags:
- agents
- claude-code
- loop-engineering
- automation
- mcp
- skills
- worktrees
- sub-agents
source: https://x.com/0xCodez/status/2064374643729773029
date: 2026-06-09
type: bookmark
author: 0xCodez
title: 'Loop engineering: the 14-step roadmap from prompter to loop designer'
summary: A 14-step framework for moving from manual prompting to designing autonomous
  agent loops, covering the 4-condition test, five building blocks (automations, worktrees,
  skills, connectors, sub-agents), state management, verification gates, and common
  failure modes.
raw: '[[raw/0xcodez_2064374643729773029]]'
description: A 14-step framework for moving from manual prompting to designing autonomous
  agent loops, covering the 4-condition test, five building blocks (automations, worktrees,
  skills, connectors, sub-agents), state management, verification gates, and common
  failure modes.
---

## Key Takeaways

**The shift:** Loop engineering replaces the human as the prompter. Instead of typing prompts repeatedly, you design a system that discovers work, delegates to agents, verifies results, maintains state, and decides next steps autonomously.

**The 4-condition test (mandatory before building):**
1. Task repeats at least weekly
2. Automated verification exists (tests, linter, build)
3. Token budget can absorb waste from retries/re-reads
4. Agent has senior-engineer tools (logs, reproduction env, ability to run its own code)

**Five building blocks:**
- **Automations** (/loop + /goal in Claude Code; scheduled tasks in Codex)
- **Worktrees** (parallel isolated checkouts to prevent file collisions)
- **Skills** (SKILL.md files that persist project context across runs)
- **Connectors** (MCP integrations: GitHub, Linear, Slack, Sentry)
- **Sub-agents** (maker/checker split; evaluator-optimizer pattern)

**Minimum viable loop:** One automation + one skill + one state file (STATE.md) + one objective gate.

**Failure modes to avoid:**
- Ralph Wiggum loops (soft completion conditions cause early exit on half-done work)
- Comprehension debt (shipping faster than you can read/understand)
- Cognitive surrender (stopping critical judgment)
- Security tax (unreviewed code, credential leaks, permission creep)
- Self-preferential bias (maker grading its own homework)

**Economics note:** Loops favor teams with repetitive, machine-checkable work and generous token budgets. Solo builders on consumer plans often lose money on token costs before seeing gains.

**Related concepts in vault:** [[claude-code-routines]], [[agent-harness]], [[mcp-connectors]], [[skills-as-compound-interest]]
