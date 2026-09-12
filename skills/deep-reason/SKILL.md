---
name: deep-reason
description: >-
  Invoke for any vault question that wants judgement, consequences, trade-offs, causation, or a
  recommendation — "why", "how should", "what happens if", "is it worth", "compare", "implications",
  "strategy", "should I". Runs depth-triaged multi-order reasoning that pairs the vault's own
  knowledge with the web, reasons in 1st/2nd/3rd orders, surfaces contradictions, and answers with a
  visible reasoning chain, labelled sources ([vault]/[web]/[inference]), and calibrated confidence.
  Do NOT invoke for simple lookups (what/who/when/define/link) — those take the fast-path.
type: meta
tags: [meta, reasoning, skill, second-brain]
status: current
as_of: 2026-09-12
---

# deep-reason

Named-mode entry point for deep reasoning over the vault. The full spec lives in
`docs/reasoning-protocol.md` — this skill is the trigger + the checklist; it does not restate the doc.

## When this fires vs. not (DEPTH TRIAGE)
- **This skill (DEEP):** why / how should / what happens if / trade-off / risk / compare / should I /
  implications / strategy; or ≥2 vault domains implicated; or a decision/recommendation is requested;
  or a wrong answer costs more than the extra tokens.
- **NOT this skill (FAST):** a fact, definition, link, number, list, or "what does my vault say about X"
  answerable from ≤2 notes. Answer via the fast-path (T1 retrieve → compact contract → stop). See
  `docs/reasoning-protocol.md` §0.

## The loop (execute in order — full detail in docs/reasoning-protocol.md §1)
1. **Decompose** into 2–5 ordered sub-questions; split factual (retrievable) from judgement (reasoned).
2. **Retrieve own knowledge** — call the retrieval protocol in `docs/retrieval-protocol.md` via `ROUTER.md`
   (grep `INDEX.tsv` → score → open ≤3 notes → ≤1 hop). Carry each note's `date`, `status` (T3), conflicts.
3. **Reason in orders** — 1st (direct facts/answer), 2nd (implications, who/what next), 3rd (systemic,
   feedback loops, long-horizon, non-obvious). Each order must add what the prior didn't.
4. **Gap-fill with web** — name the missing/stale fact FIRST (don't reflex-search); `WebSearch`/`WebFetch`
   (never curl); capture URL + recency; verify; on vault↔web conflict prefer recent + flag T3 supersession.
5. **Synthesize** — produce the insight no single note holds; calibrate facts- and reasoning-confidence
   separately.

## Output contract (docs/reasoning-protocol.md §2)
Emit: ANSWER · REASONING CHAIN (sub-questions + 1st/2nd/3rd orders) · CONTRADICTIONS/TENSIONS ·
CONFIDENCE (High/Med/Low, facts + reasoning) · RECENCY (vault freshness + web-checked date + superseded?) ·
SOURCES — every line labelled **[vault] / [web] / [inference]**.

## Write-back (docs/reasoning-protocol.md §3)
If the run produced a durable cross-domain insight, filled a real gap, resolved a contradiction, or found a
superseded note: write a new `processed/slug.md` (`status: current`, `as_of` today), respect T3 supersession
(`docs/supersession.md`) instead of editing in place, rebuild `INDEX.tsv`. Write back the conclusion + its
provenance, not the whole transcript. Skip write-back for one-off lookups or Low-confidence inference.
