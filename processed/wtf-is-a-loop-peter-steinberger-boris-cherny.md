---
tags:
- loops
- agent-orchestration
- skills
- verification
- claude-code
- hermes
source: https://x.com/mvanhorn/status/2063865685558903149
date: 2026-06-08
type: bookmark
author: mvanhorn
summary: 'Synthesis of the ''design loops that prompt your agents'' discourse: loops
  are cron + decision-maker; lineage ReAct → ralph → /goal → multi-agent supervision;
  the loop is only as good as its feedback/verification; the expensive resource shifted
  from tokens to loop management; reusable skills inside the loop are the real asset
  (not prompts).'
raw: '[[raw/mvanhorn_2063865685558903149]]'
description: 'Synthesis of the ''design loops that prompt your agents'' discourse:
  loops are cron + decision-maker; lineage ReAct → ralph → /goal → multi-agent supervision;
  the loop is only as good as its feedback/verification; the expensive resource shifted
  from tokens to loop management; reusable skills inside the loop are the real asset
  (not prompts).'
---

# WTF Is a Loop? Peter Steinberger vs. Boris Cherny

Matt Van Horn's research synthesis of the week-long "loops" discourse that hit 3.4M views.

## The Core Idea
Stop being the thing inside the loop typing prompts. Write the loop that prompts the agent, reads the result, decides whether it's done, and repeats. The model becomes a subroutine.

## Lineage
- ReAct (2022): single model, one loop, human watching
- AutoGPT (2023): goal + self-prompting, often spun forever
- ralph (2025): fixed context anchor files, cheap and disciplined
- /goal (2026): productized ralph with validator model
- Orchestration loops (now): multi-agent supervision, scheduling, durability, git-backed state

## Key Lessons
- The loop is only as good as its feedback (continuous review, verification gates, self-checks).
- The expensive part shifted from tokens to loop management (cap iterations, no-progress detection, dollar budgets).
- The reusable asset inside the loop is a **skill**, not a prompt. Loops that call sharp, named skills compound.

Directly relevant to Hermes /goal mode, skill authoring, and agent harness design.