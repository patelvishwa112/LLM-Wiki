---
title: "Knowledge System That Compounds — Painn's Obsidian + Vellum Workflow"
tags: ["obsidian", "second-brain", "knowledge-management", "vellum", "workflows", "n8n", "compounding"]
source: https://x.com/_0xpainn/status/2061014710984511916
date: 2026-06-02
published: 2026-05-31
authors: ["painn (@_0xpainn)"]
type: bookmark
raw: "[[raw/0xpainn_2061014710984511916]]"
---

# Knowledge System That Compounds

A complete Obsidian-based knowledge capture and synthesis system using four tools. The core insight: organize by note TYPE, not topic — this forces cross-domain connections that topic-based folders would hide.

## Key Takeaways

- **Organize by type, not topic.** The most consequential architectural decision. A crypto insight and a behavioral psychology observation both land in `patterns/` — and the intelligence layer finds the bridge between them. Topic-based folders silo; type-based folders connect.
- **Four tools, zero overlap.** Obsidian (vault), Vellum (intelligence/synthesis layer), Readwise (capture highlights automatically), N8N (automation glue).
- **The VELLUM.md file is the most important file.** It gives the AI identity context, current projects, what matters — makes every session start with context instead of cold.
- **Four workflows cover everything.** Process Inbox (daily), Daily Brief (6am auto), Weekly Connections (Sunday), Deep Research (on-demand). Each saved as markdown, called by name.
- **Daily ritual: 15 minutes.** 5 min raw capture → 5 min process inbox → 5 min read daily brief. Execution happens after, not during.
- **Close the loop for compounding.** When a thesis plays out, record the outcome. Over months, the system knows not just what you think but what thinking has been right for you.
- **30/90/180 day progression:** Useful → knows things you don't remember → complete record of every belief evolution.

## Vault Architecture

```
00-INBOX/          — Raw landing ground. Speed > structure at capture.
01-CAPTURES/       — Organized by type (articles/, patterns/, questions/, data/)
02-CONNECTIONS/    — Emergent synthesized insights
03-PROJECTS/       — One subfolder per active project
04-VELLUM/         — AI working directory (VELLUM.md + workflows/)
```

## The Four Workflows

| Workflow | Frequency | Purpose |
|----------|-----------|---------|
| Process Inbox | Daily | Sort, sharpen, move captures to 01-CAPTURES |
| Daily Brief | 6am auto | 3 connections, 1 pattern, 1 question |
| Weekly Connections | Sunday | Cross-folder synthesis, 3-5 surprise connections |
| Deep Research | On-demand | Full vault scan on topic: beliefs, contradictions, gaps, unasked questions |

### Connection Types
- **Type A:** Same principle in two different domains
- **Type B:** Contradiction between two notes
- **Type C:** Pattern across 3+ notes → unnamed insight
- **Type D:** Question from one note answered by another

## Monthly Synthesis Prompt

"Read everything added in last 30 days. Tell me: what beliefs am I forming that I haven't stated yet? What pattern keeps appearing across domains? What is the single highest-leverage thing I could be thinking about? What am I clearly not reading that gaps suggest?"
