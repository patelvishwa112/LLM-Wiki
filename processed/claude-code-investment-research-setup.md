---
tags: [claude-code, investment-research, obsidian, knowledge-management, finance, workflow-automation, playwright, firecrawl]
source: https://x.com/leopardracer/status/2058949350315667829
author: "@leopardracer"
date: 2026-05-25
scraped: 2026-05-26
---

# How I Set Up Claude Code as My Investment Research Analyst

A finance professional's 60-day experience running their entire investment research workflow through Claude Code + Obsidian + Playwright + Firecrawl.

## Core Thesis

> Claude Code is Claude with hands. A chatbot helps with one step. Claude Code runs the whole chain.

## The System

| Component | Purpose |
|-----------|---------|
| Claude Code | The engine — runs workflows, not just answers questions |
| Obsidian | Long-term memory — plain-text knowledge base organized by topic |
| Cursor | Visual workspace — sidebar with vault, terminal panel with Claude Code |
| Playwright | Browser automation — navigate pages, click, fill forms |
| Firecrawl | Web scraping — pull clean markdown from any page or search |
| Web Clipper | One-click save any article to raw/ inbox |

## Folder Structure
- `raw/` — inbox, dump articles with one click
- `wiki/` — librarian domain, structured notes organized by topic
- `output/` — finished reports and analyses

## The CLAUDE.md Rulebook
Most important file. Tells Claude Code it's a librarian. Defines compile workflow: raw → identify topic → write wiki article → update `_index.md` → update `_master-index.md`. Forces consistency across all sessions.

## Four-Verb Workflow
1. **Clip** — browser extension saves to raw/
2. **Compile** — weekly batch process of raw/ into wiki/
3. **Query** — ask the library, get cross-referenced answers
4. **Audit** — monthly health check of the knowledge base

## Real Example
Screening for capital deployment across 5 names, only had 2. Prompt: "Go to finviz.com, pull insider trading for last 2 weeks. Analyze buy signals. Top 10 watchlist with reasoning." Claude Code + Firecrawl: 3 minutes. Manual: 90+ minutes.

## Key Takeaways

1. **"Code" in Claude Code is misleading** — it's a workflow engine, not a coding tool
2. **Chatbot → Operator shift** — stop asking for help with one task, hand off the whole chain
3. **Memory compounds** — Obsidian + CLAUDE.md = research never leaks again
4. **`--dangerously-skip-permissions` is safe with guardrails** — CLAUDE.md file boundaries are enough
5. **Playwright for interactive scraping** — screeners, IR pages, regulator portals
6. **Firecrawl for bulk scraping** — insider data, annual reports, news searches
7. **One hour to set up, forever to benefit** — the system keeps getting smarter
