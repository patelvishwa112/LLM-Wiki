---
tags:
  - hermes
  - agent-harness
  - obsidian
  - vault
  - folder-structure
  - productivity
  - context-engineering
  - second-brain
source: https://x.com/wandermist/status/2071930382581195105
date: 2026-06-30
type: bookmark
author: wandermist
description: "Vault INDEX.md + concern-based numbered folders cut Hermes file-navigation time (~2 min → ~10–26s on author’s tasks) without changing models."
raw: "[[raw/wandermist_2071930382581195105]]"
summary: "Vault INDEX.md + concern-based numbered folders cut Hermes file-navigation time (~2 min → ~10–26s on author’s tasks) without changing models."
---

# Hermes speedup via vault INDEX scaffolding

Case study: **folder layout**, not model swap, dominated latency for file-heavy Hermes workflows.

## Insight

Humans file by **content type**; agents need **task/concern locality** and explicit **entry points**. Without a map, capable models burn turns on search and wrong-file opens (including archives).

## Pattern

| Layer | Purpose |
|-------|---------|
| `INDEX.md` (major folder root) | Subfolder purposes, canonical files, where to start |
| Numbered concern folders | Predictable traversal order |
| `Archived/` (or `06.Archived`) | Keep active tree small |

Author reports large reductions in files opened and wall time on five recurring tasks (directional benchmark, not formal eval).

## Anti-patterns

- INDEX per subfolder
- Deep taxonomies
- Premature full-vault reorg
- Stale sync copies mistaken for agent confusion

## Diagnostic

If common tasks exceed ~30s or hit multiple wrong files, add one INDEX at the worst folder root and retest before expanding.

## Why it matters

Aligns with OKF/wiki **index-first** navigation and Hermes **file/search** tool behavior—cheap harness work that multiplies any model.

## Related

- [[open-knowledge-format-okf-google]]
- [[hermes-seven-skills-cobi-bean]]
- [[hermes-goal-mode-guide]]
- [[claude-dynamic-workflows-second-brain]]
- [[harness-is-the-product-context-aware-agents]]