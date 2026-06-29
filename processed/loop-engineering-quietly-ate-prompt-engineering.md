---
tags: ["loop-engineering", "agents", "agent-harness", "claude-code", "prompt-engineering", "skills", "verification", "automation"]
source: https://x.com/dunik_7/status/2071584492804784468
date: 2026-06-29
type: bookmark
author: dunik_7
description: "Field guide defining agent loops vs cron, five meanings of loop, verification brakes, skills as compounding assets, and a three-level build ladder."
summary: "Field guide defining agent loops vs cron, five meanings of loop, verification brakes, skills as compounding assets, and a three-level build ladder."
raw: "[[raw/dunik_7_2071584492804784468]]"
---

# Loop engineering: the skill that quietly ate prompt engineering

@dunik_7 synthesizes the post–Peter Steinberger / Boris Cherny discourse into a practical definition: **loop engineering** is designing stateful, decision-making cycles that prompt agents—not hand-typing each step.

## Core distinctions

- **Loop vs cron:** Cron repeats a fixed script; a loop **reads state each tick** and chooses the next action (fix tests, address review, stop when green).
- **Feedback is mandatory:** Without an external “no” (tests, types, linters), the loop is self-congratulation at scale.
- **Five “loops” people conflate:** ReAct, AutoGPT-style self-prompting, ralph bash loops, productized `/goal`, and multi-agent orchestration (e.g. Gas Town)—different architectures sharing one word.

## What makes a loop production-grade

- **Anchors:** VISION.md, CLAUDE.md, per-tick loop.md, plus a test suite as the honest judge.
- **Brakes:** Hard iteration cap, no-progress detection (same error twice → stop), and spend/token ceiling—Uber-style runaway spend is the cited cautionary tale ($1,500/person/month caps).
- **Skills over raw prompts:** Named, improving skills (code-review, fix-ci) are the compounding asset; bare prompts reset context every run.

## Build ladder (author)

| Level | Effort | Pattern |
|-------|--------|---------|
| 0 | ~15 min | Scheduled `/loop` on a bounded task (e.g. PR review) |
| 1 | ~1 hr | PROMPT.md + bash wrapper, MAX iterations + test gate (ralph with brakes) |
| 2 | Ongoing | Persistent loop + skills + cloud session + `/goal` for multi-hour unattended work |

**Reframe:** Prompt engineering “got promoted”—you design the loop (trigger, scope, brakes, verification) and work on *what* to build while it runs.

## Related

- [[wtf-is-a-loop]]
- [[loop-engineering-clearly-explained]]
- [[human-in-the-loop-agent-loops]]
- [[loop-engineering-14-step-roadmap]]