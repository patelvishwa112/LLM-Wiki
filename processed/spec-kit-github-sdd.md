---
tags:
- spec-driven-development
- agents
- claude-code
- skills
- templates
- presets
- extensions
- github
- coding-tools
- workflows
source: https://github.com/github/spec-kit
raw: '[[raw/github_spec-kit]]'
date: 2026-06-06
type: bookmark
author: github
summary: 'GitHub''s open-source Spec-Driven Development toolkit. Flips development
  so specifications become executable, generating implementations. 109k stars. 9 slash
  commands (constitution → specify → clarify → plan → tasks → analyze → implement).
  4-layer extensibility: project overrides > presets > extensions > core. Supports
  30+ AI coding agents. Extension vs preset distinction maps cleanly to Hermes skill
  vs preset model.'
description: 'GitHub''s open-source Spec-Driven Development toolkit. Flips development
  so specifications become executable, generating implementations. 109k stars. 9 slash
  commands (constitution → specify → clarify → plan → tasks → analyze → implement).
  4-layer extensibility: project overrides > presets > extensions > core. Supports
  30+ AI coding agents. Extension vs preset distinction maps cleanly to Hermes skill
  vs preset model.'
---

# Spec Kit — GitHub's Spec-Driven Development Toolkit

**109k stars | 9.7k forks | MIT | github/spec-kit**

## Core Idea

Spec-Driven Development flips the traditional model: specifications become executable, directly generating working implementations. Intent-driven — define *what* before *how*. Multi-step refinement, not one-shot generation.

## The 7-Step Workflow

```
/speckit.constitution  → Project principles and dev guidelines
/speckit.specify       → Define what to build (requirements, user stories)
/speckit.clarify       → [Optional] Clarify underspecified areas
/speckit.plan          → Technical plan with chosen tech stack
/speckit.tasks         → Actionable task list from plan
/speckit.analyze       → [Optional] Cross-artifact consistency check
/speckit.checklist     → [Optional] Quality checklists ("unit tests for English")
/speckit.implement     → Execute all tasks
/speckit.taskstoissues → Convert tasks to GitHub issues
```

## Extensibility Model (4-layer priority stack)

| Priority | Layer | Purpose |
|----------|-------|---------|
| 1 (highest) | Project-local overrides | One-off template tweaks |
| 2 | Presets | Change *how* it works — enforce standards, adapt methodology |
| 3 | Extensions | Add *new capabilities* — new commands, tool integrations |
| 4 | Core | Built-in SDD commands & templates |

Templates resolve at runtime (top-down, first match). Extension/preset commands install at init time.

**Extension vs Preset distinction:**
- Extension = new commands/workflows (expand *what*)
- Preset = customize templates/format (change *how*)
- This maps cleanly to Hermes Agent's skill vs preset model

## CLI

```bash
specify init my-project --integration copilot
specify self upgrade
specify extension search / add / remove
specify preset search / add / remove
specify integration list  # 30+ supported agents
```

## Why It Matters

GitHub's bet on post-vibe-coding workflow. The `/speckit.analyze` cross-artifact consistency check is the standout feature — validates tasks cover the plan, plan covers the spec, before any code is written. Rich extensibility with community extensions and presets. Runs on Claude Code, Codex, Cursor, Copilot, Gemini CLI, and 25+ others.

## Related

- [[colleague-skill-dot-skill]]
- [[problem-first-skill-invert-bad-ideas]]
- [[gstack-garry-tan-claude-code-skills]]
- [[Dynamic Workflows in Claude Code]]
