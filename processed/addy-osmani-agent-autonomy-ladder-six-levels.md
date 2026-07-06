---
tags: ["agents", "agent-harness", "claude-code", "codex", "orchestration", "verification", "loop-engineering", "agent-ops"]
source: https://x.com/addyosmani/status/2072885435312042327
date: 2026-07-03
type: bookmark
author: addyosmani
description: "Addy Osmani’s six-level agent autonomy ladder (assist → factory orchestration) splits agency vs orchestration, ties each rung to verification/evidence, and lists contracts, metrics, and anti-patterns."
summary: "Addy Osmani’s six-level agent autonomy ladder (assist → factory orchestration) splits agency vs orchestration, ties each rung to verification/evidence, and lists contracts, metrics, and anti-patterns."
raw: "[[raw/addyosmani_2072885435312042327]]"
---

# Agent autonomy ladder (six levels)

Addy Osmani long post: agentic engineering shifted from **prompting to operating**. Yegge’s single-axis ladder (Gas Town) measures **one agent’s trust**; multi-agent work needs **two axes**.

## Two axes

| Axis | Low | Mid | High |
|------|-----|-----|------|
| **Agency** | Suggest; human decides | Scoped task + evidence + steering | Goal-seeking; experiments; returns proof |
| **Orchestration** | One thread | Parallel worktrees, isolated goals | Queue-driven factory; **management by exception** |

Tooling map: Claude Code (`/goal`, `/loop`, `/background`, `/batch`, subagents, hooks, checkpoints); Codex (Goal mode, worktrees, Automations, Auto-review, sandbox).

## Six levels (summary)

- **0 Assist** — suggestions only; local verification.
- **1 Supervised** — acts with approval; approval fatigue; Codex Auto-review as reviewer agent.
- **2 Scoped delegation** — bounded task + definition of done; evidence shifts to tests, types, screenshots, repro.
- **3 Goal-driven** — measurable stop condition (not wooly goals); `/goal`, Goal mode, `/schedule`.
- **4 Parallel** — decomposition + isolation; failure = false parallelism, merge conflicts, orchestration tax.
- **5 Managed-by-exception** — manager agent on triggers; implementer/reviewer/QA/security separation; Symphony-style issue workspaces cited.

## High-autonomy gate (three questions)

1. How fast will we know we're wrong?
2. How cleanly can we undo?
3. What **independent** evidence proves we're right?

“Trust the summary” fails all three.

## Per-run contract

Goal, scope, non-goals, tools/permissions, stopping condition, **evidence**, escalation, budget (time/tokens/retries/parallelism).

## Anti-patterns

Autonomy as status · permission laundering · summary substitution · fleet cosplay.

## Metrics (examples)

MTBI, longest good unattended run, auto-approve vs reject, rework/defect escape, token cost per accepted change.

**Readiness:** autonomy level follows **verification + reversibility**, not task label — pairs with [[agent-workflows-silent-degradation-verification-vladic]].

## Related

- [[loop-engineering]]
- [[addy-osmani-agent-skills-open-source]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[hermes-goal-mode-guide]]
- [[agent-swarms-production-governance]]
- [[human-in-the-loop-agent-loops]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[feedback-loops-claude-code-less-babysitting]]