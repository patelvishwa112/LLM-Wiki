---
tags:
- claude-cowork
- anthropic
- productivity
- knowledge-work
- agents
- enterprise
source: https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork
raw: '[[raw/anthropic-claude-cowork-best-practices]]'
date: 2026-06-03
author: Austin Lau (Anthropic, Growth Marketing)
type: bookmark
summary: 'Austin Lau''s guide to Claude Cowork for knowledge workers: when to use
  Chat vs Cowork vs Code, the five ingredients of a Cowork-shaped task, concrete marketing
  workflows (daily briefing, budget pacing, weekly reporting), and a 10-minute getting-started
  recipe. Key habit: make Claude ask clarifying questions before starting.'
related:
- '[[claude-cowork-product-guide]]'
- '[[anthropic-gtm-claude-code-workflows]]'
description: 'Austin Lau''s guide to Claude Cowork for knowledge workers: when to
  use Chat vs Cowork vs Code, the five ingredients of a Cowork-shaped task, concrete
  marketing workflows (daily briefing, budget pacing, weekly reporting), and a 10-minute
  getting-started recipe. Key habit: make Claude ask clarifying questions before starting.'
---

# Claude Cowork Best Practices

**Source:** Austin Lau, Growth Marketing at Anthropic. 90% of his work now happens in Claude Cowork.

## Chat vs Claude Cowork vs Claude Code

| Workspace | For | Output |
|-----------|-----|--------|
| **Chat** | Questions, brainstorming, gut checks | A thought in your head |
| **Claude Cowork** | Multi-step deliverables, cross-app tasks | A file, deck, sheet, or report |
| **Claude Code** | Software development | Code and shipped features |

> All run the same Claude models underneath. The workspace is the difference.

## Decision Rule

- Use **Chat** if it fits in a few exchanges (question, explanation, brainstorm)
- Use **Claude Cowork** if it's a deliverable, touches >1 file/app, or is a task rather than a question

| Question/Task | Use |
|---------------|-----|
| "What should I cover in our QBR?" | Chat |
| "Read 3 months of meeting notes and build a QBR deck using our template." | Claude Cowork |
| "How do I VLOOKUP?" | Chat |
| "Go through all sheets and change VLOOKUP to INDEX MATCH." | Claude Cowork |

## Five Ingredients of a Cowork-Shaped Task

| # | Ingredient | Why It Matters |
|---|------------|----------------|
| 1 | **Multiple inputs** | >1 file, folder, or connector → beyond chat's sweet spot |
| 2 | **File output** | A deliverable to share, present, or repurpose |
| 3 | **Recurring** | One-offs are fine, but recurring tasks are the sweet spot — schedule them |
| 4 | **You know what good looks like** | Can judge output quality in 15 seconds |
| 5 | **Boring middle** | Extract, compile, reconcile, reformat — the part you hand off |

## Real Workflows

### Daily Briefing
- Runs every morning at 6am
- Connects to Slack + Gmail, sorts messages into buckets, flags product incidents
- TLDR report before the workday starts

### Budget Pacing
- Connects to Google Ads + Meta Ads via connectors
- Live HTML artifact (dashboard) pulls daily spend, calculates pacing
- Replaces manual export/copy-paste or paid ETL tools

### Weekly Reporting
- Connects to Google Search Console
- Pulls queries/countries/pages, reconciles into single sheet
- Compares last 7 days vs prior 7, flags meaningful changes
- 30 min → 5 min; scheduled to run automatically

## Getting Started (10 Minutes)

1. Open Claude desktop app → Claude Cowork tab
2. Drop in files, point at a folder, or connect an app (Slack, Gmail, Notion, CRM)
3. Describe the outcome you want
4. Start with a task you already know well
5. **Critical habit:** prompt Claude to ask clarifying questions before starting: "Repeat my ask back to me, then ask as many clarifying questions as you have."

## Key Insight

> The difference between mediocre and great Claude Cowork output is almost never your prompt — it's whether you're providing enough rich context.
