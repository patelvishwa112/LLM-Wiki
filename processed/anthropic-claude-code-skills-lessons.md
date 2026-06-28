---
tags:
- claude-code
- skills
- anthropic
- agent-engineering
- productivity
- hooks
- progressive-disclosure
source: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
raw: '[[raw/anthropic-claude-code-skills-lessons]]'
date: 2026-06-03
author: Thariq Shihipar (Anthropic, Claude Code team)
type: bookmark
summary: 'Anthropic''s internal playbook for Claude Code skills: 9 categories (library
  reference, product verification, data analysis, business automation, scaffolding,
  code review, CI/CD, runbooks, infra ops), plus tips on gotchas sections, progressive
  disclosure, model-oriented descriptions, on-demand hooks, persistent memory via
  log files, and skill distribution via repo or marketplace. Verification skills had
  the most measurable impact on output quality.'
related:
- '[[claude-code-slash-command-library]]'
- '[[15-claude-skills-that-stuck-vaibhav-sisinty]]'
- '[[anthropic-self-service-analytics-claude]]'
description: 'Anthropic''s internal playbook for Claude Code skills: 9 categories
  (library reference, product verification, data analysis, business automation, scaffolding,
  code review, CI/CD, runbooks, infra ops), plus tips on gotchas sections, progressive
  disclosure, model-oriented descriptions, on-demand hooks, persistent memory via
  log files, and skill distribution via repo or marketplace. Verification skills had
  the most measurable impact on output quality.'
---

# Lessons from Building Claude Code: How Anthropic Uses Skills

**Source:** Thariq Shihipar, Anthropic Claude Code team. Hundreds of skills in active use internally.

## 9 Skill Categories

| # | Category | Purpose |
|---|----------|---------|
| 1 | **Library/API Reference** | Explain correct usage of libraries, CLIs, SDKs with gotchas |
| 2 | **Product Verification** | Test/verify code works — had the most measurable quality impact |
| 3 | **Data Fetching & Analysis** | Connect to data/monitoring stacks with common workflows |
| 4 | **Business Process Automation** | Automate repetitive workflows (standup, tickets, recaps) |
| 5 | **Code Scaffolding & Templates** | Generate framework boilerplate with org conventions |
| 6 | **Code Quality & Review** | Enforce code quality, adversarial review, testing practices |
| 7 | **CI/CD & Deployment** | Fetch, push, deploy — babysit PRs, gradual rollout, cherry-pick |
| 8 | **Runbooks** | Symptom → multi-tool investigation → structured report |
| 9 | **Infrastructure Operations** | Routine maintenance with guardrails for destructive actions |

## Key Design Tips

- **Gotchas section is highest-signal content** — build from real failure points
- **Skills are folders, not just markdown** — progressive disclosure: SKILL.md → references/api.md → assets/templates
- **Descriptions are for the model, not humans** — they're trigger descriptions Claude scans to decide "is there a skill for this?"
- **Don't state the obvious** — Claude already knows how to code
- **Store persistent state** — append-only log files, JSON configs. Use `${CLAUDE_PLUGIN_DATA}` for stable storage
- **On-demand hooks** — `/careful` blocks destructive commands, `/freeze` locks edits to specific directories
- **Think through setup** — config.json + AskUserQuestion for structured onboarding

## Distribution

- Small teams: check into `./.claude/skills` in repo
- At scale: internal plugin marketplace, sandbox folder → Slack traction → marketplace PR
- No centralized team — organic discovery and promotion

## Measurement

PreToolUse hook logs skill usage. Find popular skills and undertriggering ones vs expectations.
