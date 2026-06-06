---
title: "Iceberg: The Prompts That Unleash Opus 4.8"
tags: ["prompt-engineering", "claude", "agents", "productivity"]
source: https://x.com/0xchasetm/status/2061363479525663170
date: 2026-06-01
published: 2026-06-01
authors: ["@0xChaseTM"]
type: bookmark
raw: "[[raw/x_0xchasetm_iceberg-opus-48-prompts]]"
---

# Iceberg: The Prompts That Unleash Opus 4.8

## Key Takeaways

- Five-layer prompt engineering framework for Claude Opus 4.8, from surface to seabed:
  1. **Effort Control** — use the new Low→Max thinking slider; Max for decisions that matter, leave Adaptive Thinking on
  2. **Negative Space** — tell Claude what to CUT ("skip the obvious," "no hedging," "cut the disclaimers") to eliminate the 40% padding most answers contain
  3. **The Wrong Question** — force Claude to challenge your premise BEFORE answering ("what assumption am I making that could be wrong?")
  4. **The Second Pass** — 4.8 is 4x better at catching its own errors but only audits when told ("review this like a senior engineer reviewing a junior's PR")
  5. **The Persona** — cast Claude as a specific expert ("forensic accountant hunting fraud" vs "helpful assistant") — pulls from completely different, deeper parts of the same model
- 4.8 is the first version honest enough to hold expert standards for real — older models were just confident cosplay
- Core insight: the model is identical for everyone. The only variable is you.

## Prompt Cheatsheet

| Layer | Trigger Line |
|-------|-------------|
| Negative Space | "Skip the obvious — assume I already know the basics." |
| Negative Space | "No hedging. Take a position." |
| Wrong Question | "Before you answer — what assumption am I making that could be wrong?" |
| Wrong Question | "Steelman the case that I'm asking the wrong question entirely." |
| Second Pass | "Now audit your own answer. Where is it most likely wrong?" |
| Second Pass | "Review this like a senior engineer reviewing a junior's PR. Be ruthless." |
| Persona | "You're a CFO reviewing this with your own capital on the line." |
| Persona | "Respond as someone who's done this 500 times and lost money twice." |

## Why This Matters

- Directly applicable to your daily Claude/LLM usage — these prompts aren't model-specific, most work across frontier models
- The Persona layer connects to your investing workflow — "forensic accountant," "short-seller building the bear case," "real estate investor who's been burned" are all roles you'd use
- The Second Pass is the single highest-leverage habit — applies to code reviews, analysis, planning
- The "negative space" concept is underappreciated in prompt engineering — telling the model what NOT to say is often more important than what TO say

## Summary

@0xChaseTM presents a five-layer prompt engineering framework for Claude Opus 4.8: Effort Control (thinking depth), Negative Space (what to cut), The Wrong Question (challenge premises), The Second Pass (self-audit), and The Persona (expert role-casting). The core argument: 4.8's real power is locked behind how you prompt it — the model ships identical for everyone, and the difference between "modest upgrade" and "how is this the same model" is entirely in the prompts.

## Source

[X Article by @0xChaseTM](https://x.com/0xchasetm/status/2061363479525663170)
