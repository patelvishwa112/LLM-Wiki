---
tags:
  - software-factory
  - agents
  - verification
  - interpretability
  - skills
  - agent-harness
  - harness-engineering
  - loop-engineering
source: https://x.com/dzhng/status/2090252351533973768
date: 2026-08-19
type: bookmark
author: dzhng
description: "dzhng — slop is a verification bottleneck; treat unread first-party code as interpretability: seams, sensors, and a least-confident decision ledger from a separate auditor."
summary: "dzhng — slop is a verification bottleneck; treat unread first-party code as interpretability: seams, sensors, and a least-confident decision ledger from a separate auditor."
raw: "[[raw/dzhng_2090252351533973768]]"
published: 2026-08-19
---

# Building software factories (with no slop)

David (@dzhng), Aug 19 2026. Skills repo: https://github.com/dzhng/skills

## Claim

SOTA models can write code. Slop is what happens when generation is unbounded and verification is a human reading the artifact. Skim → LGTM → quality drifts. Embracing slop or slowing generation both lose. The remaining move: stop making human reading the bottleneck.

Worse: the artifact may stop being human-readable (Claude-speak, AI-native languages, machine code). AI reviewers pinned to that artifact get less useful as it goes opaque.

Engineering output is a solved problem, not code. The deliverable is the system of specify / delegate / verify / trust.

## You already ship unread code

Dependencies, transitive deps, org accountability without VPs reading diffs. Unreadability is now reaching first-party code.

## Interpretability, not review

Slice into domain-specific pieces with clear I/O. Attach sensors. Interrogate with real user journeys. Never require reading the implementation. The interface is the review surface.

Readable layer must move **up**, not vanish:

- Invariants (checkable must-always-be-true)
- Traces at seams
- Attack surface
- **Decisions** where the spec was silent

## Decision ledger

After a run, a skill dumps every silent choice, least-confident first. Two-day run → tens of thousands of unread lines, ~30 decisions that matter. Human reads the 30, pushes back on ~4.

That is what good senior review always was (wrong abstraction, not nits).

Auditor = independent sub-agent. Never the implementer. Audit cannot change code or it optimizes for a clean report.

## Fog of war

Hard part is finding independently verifiable slices, not "break into tasks." Scout known / unknown / blindspot before planning. Re-slice when a territory hides more map. He reports a 1d16h unattended run reviewed via ledger, not diff.

Loop: map fog → codify spec → build in loop (re-slice when stale) → review ledger.

## Why it matters

Complement to Addy Osmani light/dark factories and comprehension-debt: here the inspected outputs are **intent + behavior**, code is the compiler target. Pairs with skills-as-procedural-memory (Liu) and trajectory judges.

## Skeptical read

WIP personal skills, one builder (@duetchat). Ledger quality is the hidden dependency — if the auditor misses the load-bearing guess, you get confident slop. "Never read implementation" is overstated even by the author (he walks it back: still read some code; still learn engineering).

## Related

- [[software-factories-light-and-dark-addy-osmani]]
- [[software-factory-linear-claude-cloud-routines]]
- [[skills-what-are-they-good-for-samzliu]]
- [[writing-good-skills-measured-rulebook-aparna]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[show-me-visual-reps-coding-agents-dexhorthy]]
