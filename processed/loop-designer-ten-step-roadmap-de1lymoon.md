---
tags: ["agents", "claude-code", "loop-engineering", "agent-harness", "skills", "automation", "verification"]
source: https://x.com/de1lymoon/status/2069726411724673077
date: 2026-06-24
type: bookmark
author: de1lymoon
title: "Ten moves from prompter to loop designer (Claude Code)"
summary: "A three-tier roadmap (see, build, compound) for turning manual Claude Code prompting into self-scheduled loops with independent graders, state memory, skill distillation, and fail-safe hooks."
raw: "[[raw/de1lymoon_2069726411724673077]]"
---

## Key takeaways

**Framing:** A *prompter* optimizes one message; a *loop designer* optimizes the cycle — prompt, run, check against goal, repeat until done.

**Tier 1 — See the loop:** (1) Loop = prompt on a timer / while-loop around the model. (2) Harness first — reliable single run with `CLAUDE.md`, verification target, and tools before automating. (3) Improvement is systemic (memory, skills, grader), not weight updates.

**Tier 2 — Build:** (4) Explicit goal + stop condition. (5) Maker/checker split with fresh context for the judge. (6) `/loop` then cloud routines. (7) Workflows for fan-out, adversarial verify, loop-until-stop.

**Tier 3 — Compound:** (8) State file read at start / written at end. (9) Promote durable lessons from state into skills. (10) Hooks/guardrails, model routing by cost, block irreversible unattended actions.

**Failure modes called out:** thin harness, self-grading, no stop condition, no memory, permissions too broad, Opus on every iteration.

## Why it matters

Complements longer loop-engineering roadmaps with a compact Claude Code–native checklist (timer, cloud, `/loop`, skills, hooks) aimed at practitioners who already use the tool but still babysit each turn.

## Related

- [[loop-engineering-14-step-roadmap]]
- [[loop-engineering-clearly-explained]]
- [[wtf-is-a-loop]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[harness-is-the-product-context-aware-agents]]