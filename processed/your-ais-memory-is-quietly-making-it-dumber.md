---
tags:
- agents
- agent-memory
- claude-md
- skills
- agent-harness
- context-management
- claude-code
- agents-md
source: https://x.com/mvanhorn/status/2070966613994795489
date: 2026-06-28
type: bookmark
author: mvanhorn
summary: Matt Van Horn cut 218 auto-loaded memory files to six after the harness silently
  truncated a 46KB index; argues push memory and bloated CLAUDE.md degrade adherence,
  and skill-specific lessons belong in versioned skills as PRs—not private memory
  journals.
raw: '[[raw/mvanhorn_2070966613994795489]]'
description: Matt Van Horn cut 218 auto-loaded memory files to six after the harness
  silently truncated a 46KB index; argues push memory and bloated CLAUDE.md degrade
  adherence, and skill-specific lessons belong in versioned skills as PRs—not private
  memory journals.
---

# Your AI's Memory Is Quietly Making It Dumber

Matt Van Horn (June 2026 X Article) — companion to his loop-engineering thread; operational guide for **always-on** agent context.

## Key takeaways

1. **Push vs pull memory** — Session-injected memory and `CLAUDE.md` are *push* layers; cramming them hurts the context window mechanically. *Pull* stores (retrieval APIs, MCP memory servers) answer queries on demand and are not opposites to deleting bloat—they need pruning too.

2. **218 → 6 files** — A 46KB memory index was partially dropped each session before the agent ever saw it. Survivors: cross-skill safety scar tissue, global formatting/secrecy rules, canonical paths—not per-skill fixes.

3. **Skills > memory journaling** — ~39% of audited entries were lessons for one skill; correct home is a **PR into that skill** so behavior changes for all users and git versions the fix. "Anything more than twice → skill"; scaffold by pointing at an existing skill's structure.

4. **CLAUDE.md / AGENTS.md hygiene** — Global file under 200 lines (his: 19). Strip tech stack and generic rules the model reads from the repo. Project convention: single line `@AGENTS.md` or symlink so Claude Code, Codex, Cursor share one source.

5. **Disable auto-memory after migration** — Auto-memory read/write is one switch; move kept facts to `CLAUDE.md`, then turn off auto-memory to stop silent regrowth (`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`).

## Why it matters

Counter-narrative to "give the agent a bigger brain every session." Aligns with harness design: **expensive real estate is what loads every turn**—whether Hermes MEMORY.md, Claude auto-memory, or monolithic project rules. Pairs with skills-as-compounding-units from the same author's loop writing.

## Related

- [[wtf-is-a-loop]]
- [[gbrain-markdown-git-brain-mem0]]
- [[agent-memory-landscape-2026]]
- [[how-to-give-your-agent-memory]]
- [[build-claude-skill-never-paste-prompt-0xlagosaur]]
- [[hermes-seven-skills-cobi-bean]]
- [[9-step-loop-claude-code-senior-engineer]]