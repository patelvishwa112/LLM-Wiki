---
tags: ["skills", "prompt-engineering", "agents", "gpt-6", "coding-agents"]
source: https://x.com/pvncher/status/2095991462416490862
date: 2026-09-04
type: bookmark
description: "eric provencher (@pvncher): Astra needs shorter skill descriptions, progressive disclosure, less itinerary-prompts; AGENTS.md overconstraint now hurts; define completion and persistence."
author: pvncher
summary: "eric provencher (@pvncher): Astra needs shorter skill descriptions, progressive disclosure, less itinerary-prompts; AGENTS.md overconstraint now hurts; define completion and persistence."
raw: "[[raw/pvncher_2095991462416490862]]"
---

# Rethinking Skills and Prompts for GPT-6 Astra

eric provencher (@pvncher). Last-year scaffolding is now bloat.

## Skills

Too many skills → Codex shortens descriptions → worse routing. Descriptions with "pick me" energy load the wrong file.

Updates to `$skill-creator`: (1) shortest description that still says *when* to use it (DB-anything vs migrations-only). (2) Progressive disclosure: root as router to supporting docs/scripts. (3) Stop writing elaborate itineraries — overspecific guidance now hinders. Repo skills are used by other models; Sol/Luna help can overconstrain Astra.

## AGENTS.md

Applies on every repo task. Requiring a full repo map before a typo fix burns context. Astra finds files without being pushed to read everything. "Always run tests" can cause unnecessary testing. Astra is thorough but **tentative** — AGENTS.md can grant permission for a known-safe local test loop without per-step approval.

## Decision boundaries and persistence

Old "always ask first" language, written for reckless prior models, makes Astra stop where you'd want it to continue. Sol-style long runs vs Astra returning after first implementation. **Define completion in the request** (running, inspecting, fixing). If you want exploration past first pass, say the stop condition.

Closer: audit existing skills/AGENTS.md against this, then attempt something you wouldn't have before.

## Related

- [[gpt6-astra-looped-transformers-rasbt]]
- [[astra-computer-use-a11y-kylejeong]]
- [[software-factory-uber-scale]]
