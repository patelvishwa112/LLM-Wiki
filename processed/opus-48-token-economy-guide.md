---
title: "Opus 4.8 Token Economy — Stop Burning Your Daily Limit in 30 Minutes"
tags: ["claude", "claude-code", "opus", "token-economy", "prompt-engineering", "skills", "productivity"]
source: https://x.com/0x_kaize/status/2061475678143365248
date: 2026-06-02
published: 2026-06-01
authors: ["kaize (@0x_kaize)"]
type: bookmark
raw: "[[raw/0x_kaize_2061475678143365248]]"
related: "[[colleague-skill-dot-skill]]"
---

# Opus 4.8 Token Economy Guide

Practical configuration guide by kaize on how to stop burning through Claude Opus 4.8 tokens without losing performance.

## Key Takeaways

- **Effort routing is the #1 savings lever.** Route per task: Low (~$0.005/answer) for small stuff, High (~$0.05) for daily work, Max (~$0.20-0.40) ONLY for hardest problems. Leaving everything on one level is the difference between 30 minutes and all day.
- **Fast mode is now 3x cheaper.** Used to be 6x the standard rate, now only 2x for 2.5x speed. Use for bulk work (refactors, tests, docs), avoid for debugging/architecture/security.
- **Dynamic Workflows = power tool, not default.** Can spawn up to 1,000 agents via JS orchestration script running in background. Only the final answer hits your context. But dozens of parallel context windows burn tokens fast — scope carefully, test on one folder first.
- **Skill files are the content secret weapon.** Paste a markdown file with your writing rules, tone, post formulas, and examples at the start of every session. Without it, no AI produces good writing.
- **Safe permissions save tokens too.** Block reading .env/SSH keys, rm -rf, sudo, git push. One misconfigured agent run = re-running the whole task = double tokens.
- **Daily rhythm:** /effort low for startup/config, /effort high for daily work, /effort max only for hard problems, /compact regularly.

## Why Tokens Disappear

Three mistakes almost everyone makes:
1. Using Max thinking on questions that need none
2. Cranking everything to Max "to be safe"
3. Never compacting — every message re-reads the entire history

Rate is identical at every effort level ($5/$25 per 1M tokens). You don't pay more per token for thinking harder — you pay because the model generates more tokens.

## Effort Control Reference

| Level (App) | Level (CLI) | Cost/Answer |
|-------------|-------------|-------------|
| Low | low | ~$0.005 |
| Medium | medium | — |
| High | high | ~$0.05 |
| Extra | xhigh | — |
| Max | max | ~$0.20-0.40 |

## Fast Mode Decision Matrix

**Use for:** large multi-file refactors, code generation from spec, docs/test generation — anything where the model knows what to do and just needs speed.

**Avoid for:** complex debugging, architecture decisions, security review.

**Combo:** fast mode for bulk + standard High for thinking work.

## Dynamic Workflows (/effort ultracode)

Writes a JS orchestration script, runs subagents in background. Only the final answer returns to your session.

**Cost control:** scope the task, run on one folder first, count subagents, calibrate from there.

## Content & Marketing Workflows

1. **Content:** Skill file with writing rules → draft → edit → final. Never post raw output.
2. **Contract review:** AI for simple contracts, saves $1000+ in legal fees. Real lawyers for complex ones.
3. **Project due diligence:** Verify projects before partnerships — reputation insurance.
4. **KOL management:** Merge spreadsheets, filter by quality metrics — a week of manual work becomes minutes.

## Config (Quick Reference)

Env vars: `ANTHROPIC_MODEL`, `ANTHROPIC_SMALL_FAST_MODEL`, `CLAUDE_CODE_EFFORT`

Safe permissions: allow read/edit/test/commit, block .env reading, SSH key access, rm -rf, sudo, git push.

## Relevance

Practical token management for anyone using Claude heavily. The effort routing pattern applies to any LLM usage. The skill file approach for content generation is essentially what Hermes already does with its persona and skill system. The safe permissions pattern is worth reviewing against Hermes's tool access controls.
