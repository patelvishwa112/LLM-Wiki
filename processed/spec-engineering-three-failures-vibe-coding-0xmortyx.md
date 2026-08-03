---
tags: ["spec-engineering", "agents", "agent-harness", "claude-code", "verification", "planning", "context-management", "coding-tools", "loop-engineering"]
source: https://x.com/0xmortyx/status/2084221348616765863
date: 2026-08-03
type: bookmark
description: "Spec engineering answers three vibe-coding failures — intent drift, context decay, unverifiable output — by making the spec the primary artifact."
author: 0xmortyx
summary: "Spec engineering answers three vibe-coding failures — intent drift, context decay, unverifiable output — by making the spec the primary artifact."
raw: "[[raw/0xmortyx_2084221348616765863]]"
---

# Spec Engineering: three failures of vibe coding (@0xmortyx)

## Key takeaways

Vibe coding (loose intent, agent fills gaps) works for toys and dies on real codebases/teams/timelines. Spec engineering makes the **specification the primary artifact**; code is generated and checked against it.

### 1. Intent drift

- “Add login” forces dozens of silent micro-decisions (auth provider, lockout, session length…).
- **Fix:** write acceptance criteria **before** code so guessing happens once on paper (in/out of scope, testable behaviors).

### 2. Context decay

- Effective context fills; older architectural decisions get evicted/summarized; contradictions look like “two reasonable implementations.”
- **Fix:** durable structured spec re-read every session (e.g. `auth.spec.md`: JWT not server sessions) instead of chat-only memory.

### 3. Unverifiable output

- Without written “done,” review is opinion war.
- **Fix:** acceptance criteria specific enough to pass/fail as fact; living specs stay checked against the real system (static markdown still drifts).

Tools converging on this: Spec Kit, Kiro, OpenSpec, BMAD, Cursor rules, Augment Cosmos, etc.

## Closing

Vibe coding isn’t “bad” for throwaway prototypes. Spec engineering is the fix once codebase, team, or timeline get real.

## Related

- [[9-step-loop-claude-code-senior-engineer]]
- [[loop-engineering-technical-roadmap-h100envy]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[structure-problem-top-down-bottom-up-decision-memo]]

## Source

https://x.com/0xmortyx/status/2084221348616765863
