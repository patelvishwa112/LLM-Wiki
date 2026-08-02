---
tags: ["loop-engineering", "graph-engineering", "harness-engineering", "agents", "agent-harness", "verification", "context-management", "subagents", "production"]
source: https://x.com/ArchiveExplorer/status/2080621294979023358
date: 2026-08-01
type: bookmark
description: "Bottom-up LOOP→GRAPH→HARNESS tutorial with offline demo repo; empty child contexts and rule-based verify-first loops."
author: ArchiveExplorer
summary: "Bottom-up LOOP→GRAPH→HARNESS tutorial with offline demo repo; empty child contexts and rule-based verify-first loops."
raw: "[[raw/ArchiveExplorer_2080621294979023358]]"
---

# LOOP → GRAPH → HARNESS: whole pipeline in one sitting

## Key Takeaways

- Problem: agents re-read whole sheets/codebases each turn — **context pollution**, not insufficient window size.
- Nested stack (bottom-up):
  1. **LOOP** — gather → act → **verify** (rule-based lint/compile preferred); write verifier first; budgeted retries.
  2. **GRAPH** — fan-out loops on slices; design **return shape first**; end with **adversarial checker** with no loyalty to producers.
  3. **HARNESS** — tools + **empty child context** on spawn (never fork parent) + sandbox; prefer few general tools (e.g. grep).
- Demo intentionally fails on edge (`0s` duration parse) so loop retries with robust parser — “jagged edge” teaching case.
- Claimed main-agent context can stay tiny (demo cites ~218 bytes) when children absorb heavy material and return one clean result.
- Offline repo: https://github.com/Archive228/loop-graph-harness (`./run.sh`, no keys).
- Positions itself against hype “courses” by citing real talk timecodes.

## Why it matters

Executable twin of marfin’s architecture essay: code-first isolation rules (no context fork, verifier-first, adversarial merge gate) that make harness/loop/graph operational rather than buzzwords.

## Related

- [[master-agent-architecture-harness-loop-graph-marfin]]
- [[wtf-is-a-loop]]
- [[learn-harness-engineering]]
- [[loop-engineering-clearly-explained]]
- [[graph-engineering-three-commitments-cyrilxbt]]
- [[graph-engineering-substance-over-meme-akshay]]
