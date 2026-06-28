---
tags:
- claude-code
- slash-commands
- skills
- productivity
- coding-tools
- templates
source: https://x.com/0x_rody/status/2063549084695158936
raw: '[[raw/0x_rody_2063549084695158936]]'
date: 2026-06-07
author: rody (@0x_rody)
type: bookmark
summary: 'Claude Code slash commands are saved prompts in Markdown files. Subfolders
  create namespaces. Template: YAML frontmatter (description, argument-hint, allowed-tools,
  model) + prompt body with $ARGUMENTS. Includes 7 ready-to-ship commands: /review,
  /test, /migrate, /audit, /doc, /triage, /refactor. Build one a day for a week to
  handle 80% of routine work.'
related:
- '[[15-claude-skills-that-stuck-vaibhav-sisinty]]'
- '[[problem-first-skill-invert-bad-ideas]]'
description: 'Claude Code slash commands are saved prompts in Markdown files. Subfolders
  create namespaces. Template: YAML frontmatter (description, argument-hint, allowed-tools,
  model) + prompt body with $ARGUMENTS. Includes 7 ready-to-ship commands: /review,
  /test, /migrate, /audit, /doc, /triage, /refactor. Build one a day for a week to
  handle 80% of routine work.'
---

# Claude Code Slash Command Library

**Source:** rody (@0x_rody). A slash command is a saved prompt in a single Markdown file — no plugins, no build step, no registry.

## Locations

- `~/.claude/commands/` — global, every project
- `.claude/commands/` — per-project, commit to git

Filename = command name. Subfolders create namespaces (`team/review.md` → `/team:review`).

## Template Structure

```yaml
---
description: One-line summary (shows in /help and / menu)
argument-hint: <what-arguments-look-like>
allowed-tools: Read, Grep, Glob, Bash  # tighter = faster + safer
model: sonnet  # haiku=routine, sonnet=most, opus=security
---

Prompt body. $ARGUMENTS = full string, $1/$2/$3 = positional.
```

## The 7 Commands

| Command | Model | Purpose |
|---------|-------|---------|
| `/review` | sonnet | Diff review: bugs, security, perf, breaking changes |
| `/test` | sonnet | Write tests for file/function: edge cases > error paths > happy path |
| `/migrate` | sonnet | Pattern/library migration: one file at a time, test after each |
| `/audit` | opus | Security audit: secrets, injection, auth bypass, IDOR |
| `/doc` | haiku | Update docs to match code changes only |
| `/triage` | sonnet | Bug triage: root cause, severity, fix approach (no code) |
| `/refactor` | sonnet | Safety-first: plan first, baseline tests, stop on any break |

## Common Mistakes

1. Vague description — "Review code" → "Review diff for bugs, security, style"
2. allowed-tools too loose — scope tight for sensitive commands
3. `$1` instead of `$ARGUMENTS` — $1 = first token only
4. Wrong location — project vs global
5. Not committing to git — teammates lose shortcuts

## Build Cadence

One command a day for a week = 7 commands covering 80% of routine work. Each takes ~5 minutes: pick template → tweak for stack → save → test on real task.
