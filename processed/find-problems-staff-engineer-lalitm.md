---
tags:
  - career
  - productivity
  - problem-first
  - product-discovery
  - staff-engineer
  - clear-thinking
source: https://lalitm.com/post/find-problems-staff-engineer/
date: 2026-07-25
type: article
author: lalitm
description: "Lalit Maganti — staff engineers find work by absorbing ambient problems, waiting for repeats, collapsing requests into a common shape, then pressure-testing before building."
summary: "Lalit Maganti — staff engineers find work by absorbing ambient problems, waiting for repeats, collapsing requests into a common shape, then pressure-testing before building."
raw: "[[raw/lalitm_find-problems-staff-engineer]]"
published: 2026-07-25
---

# How I Find Problems to Solve as a Staff Engineer

Lalit Maganti (2026-07-25). Infrastructure / developer tools at a large company with bottom-up roadmap influence. Written for a senior trying to make staff. Caveat: less room in top-down orgs.

## Claim

Don't block calendar time to "think strategically" at a blank page. Act like a sponge: absorb day-to-day noise, let it sit, wait for connections. The career-defining projects were problems leaders did not yet know existed.

## Absorb problems, not requests

People narrate friction in meetings, chat, email. Pull the thread: "If X existed, would that solve it?" Users ask for a solution; keep digging to the job-to-be-done. Sit with the team, walk workflows, try their bugs yourself. Seek people who see more of the org (critical-system owners, cross-team, downstream) and ask what they keep seeing.

## Let problems accumulate

Building the first vocal request is how you ship unused features. Wait. Independently repeated problems rise in priority. Different-looking complaints may share a shape. One-off excitement fades. Mechanism (mental note vs written log) is personal; the point is holding unresolved problems long enough for evidence.

## Find the common shape

Perfetto example: years of one-off UI asks (pin these tracks, open zoomed here, custom aggregation, bookmarklet workarounds) collapsed into "personalize without imposing on everyone" → extensible UI, not N features.

A common shape is a **hypothesis**. Elegance is not evidence. He almost unified two Perfetto problems with a transparent cache; the RFC/prototype forced a split. Both halves shipped.

Best untangling: long walks, not forced desk thinking.

## Pressure-test before building

- Low-risk + useful → just ship, tell the manager
- Unsure it works or how hard → throwaway prototype
- Big and convinced → full effort: RFCs, 1:1s, talks, coalition

Also trying to convince yourself. Stop if nobody sees the value or you hit a wall. Park if timing is wrong.

You do not have to be the implementer. Shaping the problem is the staff output.

Perfetto: plugins were not enough (internal teams could not open-source). Macros as lightweight extensions + extension servers. Dozens of internal teams; other companies use extension servers too.

## The loop

Solve a useful problem → people bring you earlier → wider view → more patterns. Early: you must ship to prove judgment. Later: org trusts your assessment; you influence the roadmap without owning every project. Conversations are inputs to building, not a replacement for technical work.

## Why it matters

Same decompress-the-request move as /problem-first. Complements Goedecke "keep thinking" (slow synthesis) and Cole (questions over blank-page themes). Staff-level ideation is evidence accumulation, not brainstorming.

## Skeptical read

Autonomy-heavy infra/devtools shop. Waiting can look like inaction in a top-down org. "Mental note" does not scale; the written log is the safer default.

## Related

- [[problem-first-skill-invert-bad-ideas]]
- [[how-to-keep-thinking-sean-goedecke]]
- [[productize-problems-you-already-solved-eptwts]]
- [[agent-native-career-advice-philhchen]]
- [[antithesis-principle-shreyas-doshi]]
