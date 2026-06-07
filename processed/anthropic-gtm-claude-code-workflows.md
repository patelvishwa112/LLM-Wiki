---
tags:
  - anthropic
  - claude-code
  - claude-cowork
  - gtm
  - sales
  - skills
  - productivity
  - enterprise
  - mcp
source: https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
date: 2026-06-05
author: Anthropic
type: bookmark
summary: "How Jared Sires, a non-technical AE at Anthropic, used Claude Code to build CLAFTS (email drafting in his voice), daily brief/recap skills, and a 20+ skill Sales plugin for Claude Cowork. The plugin — used by 80% of the sales org — integrates Salesforce, Intercom, Gong, Gmail, Google Drive, BigQuery via MCP. Key skills: /customer-context (360° account view in 90s) and /pipeline-management (at-risk deals, forecasting)."
related:
  - "[[claude-cowork-product-guide]]"
  - "[[claude-cowork-best-practices]]"
  - "[[anthropic-claude-code-skills-lessons]]"
---

# GTM Engineering with Claude Code: Jared Sires' Workflows

**Source:** Anthropic. Jared Sires — no coding experience before Claude Code, now GTM architect building tools for Anthropic's entire sales org.

## Tools Built

| Tool | Function | Impact |
|------|----------|--------|
| **CLAFTS** (Claude Drafts) | Gmail-integrated email drafts in Jared's voice; pulls context from Google Drive, doc search, product docs | 10-15 hrs/week saved; answers tied to latest product docs, not memory |
| **CLAFTS Tones** | Pattern-matching for writing style across audience types (customers, peers, family) | Matching tone per relationship |
| **Daily Brief** | Morning skill: reads calendar, runs web search on contacts, produces talking points (Google Calendar + CRM via MCP) | Prep before first call |
| **Daily Recap** | End-of-day skill: pulls from Google Docs, meeting notes → follow-up emails | Same pattern as CLAFTS |

## Sales Plugin for Claude Cowork

- **Adoption:** ~80% of Anthropic sales org within months; remaining 20% are new hires
- **Integrations:** Salesforce, Intercom, Gong, Google Calendar, Gmail, Google Drive, BigQuery via MCP
- **Scheduled execution:** reps queue skills to run automatically

### Anchor Skills

| Skill | Function |
|-------|----------|
| `/customer-context` | 360° account view across all sources in ~90 seconds |
| `/pipeline-management` | At-risk deals, forecasting guidance, progression recommendations |

## Development Approach

- 4,300 lines of code, almost all written by Claude Code
- "Hundreds of iterations" on the system prompt to match writing voice
- Web search keeps drafts current with Anthropic's rapidly-changing product docs
- Ships skills as Claude Cowork plugins with MCP connectors — installable in minutes

## Key Insight

> With Claude Code, the technical barrier dissolves. A non-coder can design and build tools that scale across a team. "I have space to work more creatively and strategically, and there's no turning back."
