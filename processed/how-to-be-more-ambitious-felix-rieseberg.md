---
title: "How to be more ambitious: a tutorial for humans with models"
type: bookmark
description: "Felix Rieseberg turns 'be more ambitious with AI' into four levers — altitude, depth, range (speed is commoditized) — plus the self-efficacy research behind them."
tags: [agents, prompt-engineering, productivity, anthropic, agent-harness, ambition]
source: https://x.com/felixrieseberg/status/2110023283169247623
date: 2026-10-13
author: Felix Rieseberg
summary: "Felix Rieseberg turns 'be more ambitious with AI' into four levers — altitude, depth, range (speed is commoditized) — plus the self-efficacy research behind them."
raw: "[[raw/felixrieseberg_2110023283169247623]]"
---

# How to be more ambitious: a tutorial for humans with models

**Source:** Felix Rieseberg (@felixrieseberg), Anthropic engineering lead on Claude, 2026-10-13. A blog tutorial (posted to X) on how to operate models at a level above "write me this function".

Rieseberg starts from the observation that model capability is lumpy — Tao's "astounding in some directions, inadequate in others" — so a few users fly while most still use Claude as a smarter autocomplete. "We should be more ambitious" is a rallying cry that gives no instructions, so he decomposes ambition into four types and deliberately skips the first: **speed** (same work, less time) is already the commoditized baseline. That leaves altitude, depth and range.

**Altitude** is moving from the task to the outcome — asking for an app that stays crash-free instead of a list of crash fixes, or asking for a better early-warning mechanism than the quarterly deck rather than better slides. It is the axis that produces durable workflows: work that no longer needs a human to hand out the next task, at the price of rebuilding the surrounding plumbing (crash-report ingestion, version-to-commit mapping, machines for every OS) so the model can close its own loop. **Depth** means borrowing the instruments of a field's best practitioners rather than their vocabulary — databases and statistical models instead of markdown tables, deliberately unreasonable targets, adversarial re-tests of assumptions against raw data, and an outside judge because models are unreliable graders of their own output. **Range** imports other disciplines, best unlocked by converting nouns into verbs ("a deck" becomes "get busy people to believe a story about cause and effect and decide under uncertainty in 30 minutes") and then assembling the crew that verb implies, red team included.

The last third is the argument for why this needs a tutorial at all: the binding constraint is self-efficacy, not model capability. He strings together the goal-setting literature (Locke and Latham's 35 years of work: specific hard goals beat "do your best"), Collison's "Fast" list, Dantzig mistaking two unsolved statistics problems for homework in 1939, Bannister's four-minute mile and the 46 days before anyone matched it, and Linux shipping as "just a hobby". Hard things get done once someone believes they are possible, and models shorten the lag between belief and attempt.

## Why it matters

The four axes are a usable specification of what "agentic" work should look like: altitude decides whether you built a workflow or a chat, depth decides whether the output would survive a domain expert's review, range decides whether the answer is worth reading. Depth's insistence on an outside judge and raw data is the same conclusion the verification literature reaches from the failure side — self-assessment does not count as evidence.

For anyone building or buying AI tooling, the operational requirements he names (shell access, software install, MCP data connectors, per-OS machines) are the actual product surface; the ambition ceiling is set by the harness, not the prompt.

## Key points

- Four ambition types: Speed (skipped as commoditized), Altitude (task → outcome), Depth (expert instruments, raw data, outside judge), Range (multiple fields).
- Altitude is the axis that removes the human from the loop, but it requires workflow work first: crash reports, a version↔commit map, and Windows/macOS/Linux machines so the model can reproduce and verify.
- Depth tactics: ask for 200ms when you need 5s; give raw data and demand the assumption be reproduced or falsified; ask for a customer simulation that predicts on unseen logs; never let the model grade itself.
- Reusable depth prompt: have the model state what a top professional would do that you didn't ask for, the rawest starting material, the specific tools, and what external signal would prove the result right — then rewrite your prompt.
- Range: replace nouns with verbs (from *The Art of Innovation*), then "assemble the crew" — plus a red team of short seller and forensic accountant. Do what the expert does, don't roleplay the expert.
- Scale limits acknowledged: "'Claude, go make money' doesn't seem to work for most businesses by itself in 2026."
- Evidence cited: Locke & Latham's 35 years of goal-setting research; Bannister 1954 (sole sub-4:00 holder for 46 days); Sawe's sub-2:00 marathon with the runner-up also under two hours; Dantzig, 1939.

## Related

- [[not-ambitious-enough-with-claude]]
- [[addy-osmani-agent-autonomy-ladder-six-levels]]
- [[agents-behave-like-employees-six-shifts]]
- [[problem-first-skill-invert-bad-ideas]]
