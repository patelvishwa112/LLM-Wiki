---
tags: ["second-brain", "obsidian", "agents", "hermes", "knowledge-graph", "karpathy", "cronjob", "creator-economy"]
source: https://x.com/leopardracer/status/2073340097051689327
date: 2026-07-04
type: bookmark
author: leopardracer
description: "Living Obsidian wiki built Karpathy-style; four Hermes cron agents (Post, Build, Stoic, Note) ingest Claude.ai/Code history, write back to wiki pages, and deliver journal insights every six hours."
summary: "Living Obsidian wiki built Karpathy-style; four Hermes cron agents (Post, Build, Stoic, Note) ingest Claude.ai/Code history, write back to wiki pages, and deliver journal insights every six hours."
raw: "[[raw/leopardracer_2073340097051689327]]"
---

# Living wiki second brain (leopardracer)

Workflow beyond static **CLAUDE.md** memory: an **Obsidian vault** as a **living wiki** (Karpathy-style, one page per topic). Agents **write to the wiki before** replying, so each run compounds structure—new topics spawn pages automatically.

**Data sources:** exported Claude.ai zip, local Claude Code sessions under `~/.claude/projects/`, plus the author’s articles, journals, and X note stats. Pipelines distill chats into clean notes and a **psychology profile** page; private threads can be excluded by prompt.

**Four angle agents (cron ~6h):**

| Agent | Role |
|-------|------|
| Post | Revenue-linked content ideas + web proof |
| Build | Unshipped builds from Code sessions → next ship |
| Stoic | Journal + psychology profile → daily coaching |
| Note | Substack note patterns → next draft |

**Automation:** Hermes + `SOUL.md` / `SKILL.md` (Google Drive folder linked in post) sets vault path and cron; alternative is a scheduled local Claude routine.

## Why it matters

- Concrete pattern for **index-first, write-back** agent memory (aligned with OKF / LLM-wiki ideas) instead of stuffing context each chat.
- Shows **cron + multi-persona** decomposition over one generic assistant.
- Overlaps vault topics: Obsidian compounding, Hermes scheduling, GBrain-style git wikis.

## Skeptical read

- Heavy **creator-economy** framing; income and subscriber anecdotes are not independently verified here.
- Setup depends on **large personal exports** and manual approval of wiki links—ops cost is real.
- Treat Drive templates as starting points; filter private data generously.

## Related

- [[second-brain-obsidian-night-shift-300-agent-swarm]]
- [[open-knowledge-format-okf-google]]
- [[agent-memory-four-layer-stack-matthew-gunnin]]
- [[knowledge-system-compounding-obsidian-vellum]]
- [[gbrain-markdown-git-brain-mem0]]