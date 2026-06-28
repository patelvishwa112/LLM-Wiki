---
tags:
- claude-code
- agents
- loop-engineering
- sub-agents
- hooks
- plan-mode
- claude-md
- review
- senior-engineer
- slash-commands
source: https://x.com/0xmortyx/status/2066469702075920794
date: 2026-06-15
type: bookmark
author: 0xMortyx
title: The 9-Step Loop That Turns Claude Code Into a Senior Engineer
summary: 'A 9-step senior-engineer workflow for Claude Code using plan mode, Explore
  subagent, CLAUDE.md, hooks, review subagents, and slash commands. Turns ad-hoc prompting
  into a repeatable disciplined loop: explore → plan → standards → build small → enforce
  with hooks → test → review → fix → ship via /ship command.'
raw: '[[raw/0xmortyx_2066469702075920794]]'
description: 'A 9-step senior-engineer workflow for Claude Code using plan mode, Explore
  subagent, CLAUDE.md, hooks, review subagents, and slash commands. Turns ad-hoc prompting
  into a repeatable disciplined loop: explore → plan → standards → build small → enforce
  with hooks → test → review → fix → ship via /ship command.'
---

## Key Takeaways

**The 9-step senior loop for Claude Code:**
1. **Explore** — Use Explore subagent first (read-only, isolated context) to map codebase before any edits.
2. **Plan** — Enter Plan mode; get full approach + risk list, review/approve before any code is written.
3. **CLAUDE.md** — Project constitution loaded every session (conventions, commands, rules). Advisory, not deterministic.
4. **Build small** — Implement approved plan in self-contained, reviewable pieces only.
5. **Hooks** — Deterministic PostToolUse hooks (lint + test after every Edit/Write). The non-negotiables that CLAUDE.md can't guarantee.
6. **Test** — Agent must write + run tests for the change; "done" = tests pass.
7. **Review subagent** — Fresh critic in clean context window; flags security, edge cases, CLAUDE.md violations (does not fix).
8. **Close the loop** — Fix reviewer issues, re-test, re-review until clean. Repeat until review passes.
9. **Ship via slash command** — Wrap entire loop in `.claude/commands/ship.md` so `/ship` triggers the full pipeline.

**Core insight:** The gap between junior-tier and senior-tier Claude Code usage isn't a better model — it's whether you've wired the existing primitives (plan mode, subagents, hooks, CLAUDE.md, slash commands) into a disciplined loop.

**Why it works:**
- Exploration prevents guessing
- Plan mode kills bad approaches before cost
- CLAUDE.md + hooks = standards loaded + critical rules enforced
- Tests + independent review = "done" is earned
- Slash command = setup once, run forever

**Related concepts in vault:** [[loop-engineering-14-step-roadmap]], [[claude-code-routines]], [[agent-harness]], [[skills-as-compound-interest]], [[sub-agents-are-a-promising-inference-time-scaling]]
