---
title: "Using Claude Code: Spending Your Effort"
type: bookmark
description: "Anthropic's Thariq on what Claude Code effort levels actually buy: more verification and edge-case testing, with Terminal Bench 3 jumps from low to xhigh."
tags: [claude-code, anthropic, evals, benchmarks, verification, cost-optimization, reasoning]
source: https://x.com/trq212/status/2103576349499855160
date: 2026-09-25
author: Thariq
summary: "Anthropic's Thariq on what Claude Code effort levels actually buy: more verification and edge-case testing, with Terminal Bench 3 jumps from low to xhigh."
raw: "[[raw/trq212_2103576349499855160]]"
---

# Using Claude Code: Spending Your Effort

**Source:** Thariq, 2026-09-25. A long X article from an Anthropic engineer on how to pick Claude Code effort levels, backed by his own eval runs on Terminal Bench 3.0.

Thariq's framing is that effort is an approximation of how much compute the model should spend, communicated the way you would brief a human: asked for something in an hour you deliver the best version that meets the ask and expect iteration; asked for twelve hours you go and do it properly. What changes with effort is not politeness or verbosity but how much independent judgement the model applies and how much verification and edge-case testing it performs on its own. His claim about the newest models — Fable 5.1 and Opus 5.5 — is that each effort step now shows both a benchmark uptick and a token uptick, without breaking the prompt cache in Claude Code.

The empirical core is Terminal Bench 3.0, a community-sourced benchmark spanning security, hardware, ML, science, software, operations and media, with genuinely hostile tasks (an 8-bit console in Verilog on an FPGA, Takens' embedding theorem in Lean 4, merging 16 MoE checkpoint shards to reproduce reference logits, an end-to-end EU trade-statistics filing). On `html-js-filter`, an HTML sanitizer that must strip every JavaScript-smuggling vector, Fable 5.1 goes from 1/5 at low effort to 5/5 at xhigh; a low attempt is a two-minute one-pass filter tested against a single hand-written page, while an xhigh attempt takes about 33 minutes and adversarially reviews its own draft, reads the installed parser's source for bugs, runs a standard XSS suite, and writes a random-document fuzzer. Similar low→high sweeps: `mvcc-lsm-compaction` 0/5 → 4/5 at xhigh, `cli-2ph-simple` 0/5 → 5/5 at high, `gsea-proteomics` 0/5 → 4/5 at high.

The failure taxonomy is the most useful part: more effort reduces failures caused by missing edge cases, and does not fix failures where the model chose the wrong approach. Effort also matters less as specification improves — on a heavily specified build task, models at different effort levels produced fairly similar designs — so effort and specification are substitutes. The workflow he landed on for feature work: have Claude interview you to fill the gaps in your spec, implement on low effort, review and iterate on low, then verify and test on high.

## Why it matters

Effort is the main cost dial in Claude Code and most teams set it once by vibe. This gives a rule with a mechanism behind it: spend high effort where verification is the bottleneck (security, code review, hardware, brownfield bug fixes) and low/medium where you want speed and to stay in the loop. The failure-mode finding is the operationally important one — throwing max effort at a wrong-approach problem burns tokens without moving the score, so the diagnostic question is whether a failure is missing edge cases or a bad plan.

## Key points

- Lineage of effort: each level changes how much independent judgement and self-verification the model does, plus token spend — and reportedly no longer breaks the Claude Code prompt cache.
- `html-js-filter`: Fable 5.1 goes 1/5 at low → 5/5 at xhigh; low attempts take ~2 min in one pass, xhigh ~33 min with adversarial self-review, parser source reading, XSS suite and a fuzzer.
- `mvcc-lsm-compaction` 0/5 → 4/5 at xhigh (~1 min vs ~11 min per attempt); `cli-2ph-simple` 0/5 → 5/5 at high; `gsea-proteomics` 0/5 → 4/5 at high.
- Effort fixes missing-edge-case failures but not wrong-approach failures.
- Effort and specification are substitutes: a detailed spec collapses the spread between effort levels.
- Underspecified builds scale visibly with effort (a log and a graph at low, a heat chart at max); design mockups went from 1 minute at low to 28 minutes at max.
- Recommended loop: spec interview → implement low → review/iterate low → verify and test high.
- Rule of thumb — low for brainstorming/sketching, medium for feature implementation, high for verification-heavy or brownfield work, max for fully autonomous multi-step builds and security review.

## Related

- [[controlling-reasoning-effort-in-llms]]
- [[harbor-by-terminal-bench-multi-language-agent-evaluation-fr]]
- [[claude-code-self-correcting-setup]]
- [[opus-48-token-economy-guide]]
- [[9-step-loop-claude-code-senior-engineer]]
