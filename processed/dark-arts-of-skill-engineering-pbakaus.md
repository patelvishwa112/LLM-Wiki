---
type: bookmark
description: "Paul Bakaus (Impeccable) — nine dark arts for skill engineering: skills as harness extensions that force model defaults via sub-agents, routing, memory, stdout scripts, hooks, live browser, multi-harness compile, and weakest-model gates."
tags: ["skills", "agent-harness", "harness-engineering", "claude-code", "codex", "hooks", "multi-agent", "progressive-disclosure", "design", "frontend", "impeccable", "cross-harness"]
source: https://x.com/pbakaus/status/2077114326985687525
date: 2026-07-14
author: pbakaus
summary: "Paul Bakaus (Impeccable) — nine dark arts for skill engineering: skills as harness extensions that force model defaults via sub-agents, routing, memory, stdout scripts, hooks, live browser, multi-harness compile, and weakest-model gates."
raw: "[[raw/pbakaus_2077114326985687525]]"
---

# The Dark Arts of Skill Engineering

Long-form from **Paul Bakaus** (@pbakaus) on turning vibed personal skills into battle-hardened **harness extensions**, drawn from open-source **Impeccable** (design toolkit for coding agents; hundreds of thousands of users).

## Core reframe

- Creating a skill is trivial; creating an **effective, portable** skill is hard (consistency across harnesses, models, projects, users, OSes, weak models).
- A skill is not a saved prompt — it is a **plugin that extends the harness** where the model has gaps.
- Great skills make models do things they **do not want** to do (ask questions first, avoid slop fonts/hover scales, stop AI beige, etc.). Prose summons the median; machinery forces outcomes.

## Nine dark arts

1. **Make them argue** — Blind adversarial sub-agents for review/audit/ranking (e.g. design director LLM vs deterministic detector; synthesize, never concatenate). Codex may need explicit permission to spawn.
2. **Force divergence** — Bans move to next-safe latent region (Inter ban → next default font). Prefer: discard top-3 safe picks; generate many + blind distinctness filter; seed from external scripts (`palette.mjs --from`).
3. **Route like a frontier model** — SKILL.md as MoE-style router; load one expert file per command (Impeccable: 23 commands, one expert in context each time). Avoid mile-long conflicting SKILL.md.
4. **Give them memory** — Files/snapshots across sessions (critique writes scored snapshot; polish reads as backlog; path-based slug so teammates share memory). Mentions Compound Engineering, @mattpocockuk teach skill.
5. **Scripts that talk back** — Run script; **stdout is the next instruction** (JIT env-aware guidance). Cache trade-off: breaks prompt caching.
6. **Hooks that fight back** — PostToolUse etc. always-on guardrails (deterministic slop scan → system reminder → agent fixes). Calibrate carefully (tokens, false positives); runtime-generated UI is a blind spot.
7. **Live-wire the browser** — Dev page as second input (`/impeccable live`: inject picker, blocking poll, edit loop). Multimodal polish without MCP/React-only Agentation constraints; harness wake differences matter (Claude vs Codex).
8. **Compile to every harness** — Treat skill as source (`SKILL.src.md`) with build for AskUserQuestion vs Codex tools, `/` vs `$`, per-model ban patches. Popular `npx skills` insufficient → custom installer (`npx impeccable`).
9. **Design for the weakest model** — Unskippable gates; step-by-step for Haiku/Sonnet/Luna class; if a gate can be skipped, it will be. Frontier models hide weak prose.

## Why it matters

Highest-signal public checklist for production skill design beyond prompt wordsmithing. Maps cleanly to Hermes/Claude Code skill authoring: progressive disclosure, hooks, sub-agents, verification layers, and cross-runtime packaging. Complements SkillsBench/measured skill quality work with operational patterns.

## Links

- Install: `npx impeccable skills install` / [impeccable.style](https://impeccable.style)
- Talk + starter: [github.com/pbakaus/impeccable-talks](https://github.com/pbakaus/impeccable-talks)

## Related

- [[writing-good-skills-measured-rulebook-aparna]]
- [[how-to-create-right-skill-ai-agent]]
- [[anthropic-claude-code-skills-lessons]]
- [[build-claude-skill-never-paste-prompt-0xlagosaur]]
- [[learn-harness-engineering]]
- [[harness-engineering-2026-discipline]]
- [[how-to-never-get-writers-block-chatgpt-voice-codex-jxnl]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[the-great-flattening-tokenmaxx-vorflux-myprasanna]]
- [[addy-osmani-agent-skills-open-source]]
