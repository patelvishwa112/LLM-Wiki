---
tags:
  - pstack
  - planning
  - context-engineering
  - agent-harness
  - prototyping
  - architecture
  - verification
  - skills
  - agent-ops
  - code-quality
source: https://x.com/poteto/status/2097732320606507506
date: 2026-09-09
author: lauren (@poteto)
type: bookmark
description: "pstack Pt. 2 — supervise a smarter agent by priming context (/teach, /how, /why, /recall) and planning through prototypes and /architect arenas instead of abstract plans; code is the plan."
summary: "Plan in code, not prose: prime the agent's context, use /recall and /teach to rebuild mental models, prototype competing designs with /poteto-mode, run /architect arenas with cross-model judging, and only then write a tactical plan tied to proof."
raw: "[[raw/poteto_2097732320606507506]]"
status: current
as_of: 2026-09-09
---

# The Complete Guide to pstack Pt. 2 — Supervising Someone Smarter Than You

Continuation of [[the-complete-guide-to-pstack-part-1-verification]] (Pt. 1 source: [[raw/poteto_2094457600259842065]]). Once verification works, the next question is *what to build and how to specify it*.

## The two failure modes

1. The agent can't understand your intent — because it is under- or poorly specified.
2. The agent lacks the context to do the work correctly.

Both reduce to one job: **prime the context window with high-quality context**. The agent may write working code without it, but quality drops.

## Rebuilding the mental model

- `/teach` — makes the agent restate a change in terms you can check, including the tradeoffs it rejected. It delegates to `/how` and `/why`.
- `/how` — traces runtime mechanics; on large subsystems it fans out parallel explorer agents on fast models.
- `/why` — reconstructs intent from historical evidence: git history and PR review comments, Linear, Notion design docs, Slack, Datadog monitors, Sentry, code lineage, warehouse events. Code says what; `/why` recovers *why it was written that way*.
- `/recall` — pulls your own recent transcripts so a fresh agent recovers context instead of starting over.

She notes these help the agent too: frontier models still assert confidently without reading the code, and being forced to teach builds the model's own mental model.

## "I don't believe in planning" — plan through code

Harnesses with plan modes "over-specify implementation details and under-specify everything else." Abstract plans give the *illusion* of progress. Her substitutes:

- **Readme-driven development** for shared code/packages: write the tutorial first, then work backwards to API and architecture. She built `/technical-writing` (Diátaxis: tutorial / how-to / reference / explanation, plus `/unslop`) because the first agent-written READMEs mixed all four modes into slop.
- **Prototyping playbook**: throwaway sketches in the app or a scratch dir; 2–3 variants behind a switcher; drive them with the verification skill; screenshot each and measure timing/layout. "Prototyping is planning, but with code." Playbooks are conditionally loaded reference files inside `/poteto-mode` (23 of them as of v0.15.0), not separate skills.
- **`/architect`** for larger changes, in five phases: ground (run `/how` and `/why` over affected systems) → sketch (independent candidate runners, often across model families, each producing call-site usage, core types, signatures, rationale) → cross-judge (a different model scores candidates against a strict rubric) → implement against the sketch → **scrap when wrong**. Empirical proof the architecture is wrong: the same workaround appearing at unrelated call sites, or types needing `any`/forced casts.

Her explicit anti-pattern: adversarially reviewing abstract plans. Agents hallucinate theoretical risks and edge cases that never happen. Answer open questions with prototypes and verification instead.

## When you actually want a plan

Use the multi-phase planning playbook *after* the design is settled: `/poteto-mode turn this design into a plan`. Every task is structured around proof — tests alone don't count, the code must have been run. An automated script validates the plan's structure, then it executes item by item as small, self-contained, reviewable PRs. For week-long projects she may commit plans temporarily and delete them after.

## Prompt patterns worth copying

- Ambiguous bug: `investigate why background workers periodically fail with timeout errors. give me a breakdown of what we know, what data you used, and your best hypotheses.`
- New boundary: `we need to add rate limiting for external webhooks. /architect this first, and answer any open questions with prototypes. let me review before proceeding.`
- Migration: `create a plan to migrate our entire UI library to StyleX. break the migration into small, verifiable PRs. each PR must have its visual regression tests and live verification steps. i want the final result to be 100% identical compared to the original - bugs included`
- Slack triage: `repro this with /control-app. if it repros on main, fix it and show me a video as proof`

## Verdict

Sharpest available counter to plan-mode theatre: **specification should be executable**. Her strongest claim — plans written in prose get validated by vibes, prototypes get validated by measurement — is right, and the `/architect` scrapping rule (any/forced casts or repeated workarounds = wrong architecture) is a concrete falsification test. Caveats: it assumes the Pt. 1 verification CLI exists, is tightly coupled to Grok Bot/Cursor cloud agents, and the volume numbers are self-reported.

## Related

- [[the-complete-guide-to-pstack-part-1-verification]]
- [[designing-loops-with-fable-5]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[harness-engineering-2026-discipline]]
- [[agent-workflows-silent-degradation-verification-vladic]]
