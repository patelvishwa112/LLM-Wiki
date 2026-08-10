---
tags: ["claude", "opus", "fable-5", "anthropic", "cost-optimization", "token-economy", "agents", "coding-tools", "models", "ai-strategy", "effort-dial", "prompt-caching", "safety"]
source: https://x.com/notegoyard/status/2086768712804126959
date: 2026-07-24
type: bookmark
description: "YARD on Opus 5 — same price as Opus 4.8 with an effort dial; Anthropic pitches intelligence per dollar, not peak smarts (Fable 5 still higher)."
author: notEgoyard
summary: "YARD on Opus 5 — same price as Opus 4.8 with an effort dial; Anthropic pitches intelligence per dollar, not peak smarts (Fable 5 still higher)."
raw: "[[raw/notegoyard_2086768712804126959]]"
---

# Opus 5 explained (effort dial / intentional “downgrade”)

@notEgoyard breakdown of Anthropic’s **Opus 5** launch framing (ship date cited as July 24): not the smartest model in the stack (that’s **Fable 5**), priced like **Opus 4.8**, optimized for **intelligence per dollar**.

## What shipped (as stated)

- **Opus 5** — flagship-tier, live same day across Anthropic surfaces
- Pricing: **$5 / $25 per M tokens** (in/out) — same as Opus 4.8, better output
- New default on Claude Max; strong option on Pro
- Comes “close” to Fable 5 on most tasks at roughly **half the burn**
- Fourth model in under two months after Mythos 5, Fable 5, Sonnet 5 — cadence is part of the story

## Effort dial (core product shift)

Same model, variable compute:

| Mode | Role |
|------|------|
| Low | Most of the intelligence, fraction of tokens |
| Medium / High | Closer to Fable-tier reasoning when needed |
| Fast | ~2.5× speed at ~2× price when latency > depth |

Intelligence becomes a **variable cost**, not a hard model switch. Launch charts emphasize **performance at a given cost**, not peak-only.

## Why “downgrade” is the wrong frame

- Most spend is middle-band work: coding loops, docs, agent calls × hundreds/day
- **Fable 5** — hard frontier / multi-day unsupervised slice
- **Opus 5** — default daily work + dial up when one task earns it
- Responds to Fable-era complaints: token burn on ordinary tasks (+ export-control / safety controversy context in June)

## Safety / deployment notes (from post)

- Internal behavioral audit **2.3** — lowest misconduct among current Claude models cited
- Stronger Constitution adherence than Opus 4.8, Sonnet 5, even Fable 5
- Trails Mythos 5 on bio research and **offensive** cyber on purpose
- OSS-Fuzz style testing: finds vulns ~like Mythos, weaker at turning them into working exploits

## Side releases

- **Mid-conversation tool changes** without invalidating prompt cache
- **Automatic fallbacks** — safety-flagged requests can route to another model instead of hard block

## Operator pattern

- Agent loops / batch pipelines: **Opus 5 low effort for ~95%**, Fable for hard ~5%
- Bonus UGC-agency stack: low effort intake/scripts, medium/high strategy, video layer (Higgsfield/Kling/etc.) orchestrated by Opus, per-client `CLAUDE.md`

## Why it matters

Makes the model race explicitly about **smarts per dollar per task per day** — same theme as token-economy / harness-cost notes. Practical routing guide for multi-model Claude stacks.

## Skeptical read

Creator/UGC agency ending is productized advice; verify live pricing, effort-mode APIs, and safety numbers against Anthropic docs. “Half the cost of Fable” depends on mix and effort settings.

## Related

- [[opus-48-token-economy-guide]]
- [[iceberg-opus-48-prompts]]
- [[fable-5-self-improving-system-14-steps]]
- [[how-to-actually-use-claude-fable-5]]
- [[designing-loops-with-fable-5]]
- [[fable-manager-sol-worker-nateherk]]
- [[fable-5-mythos-prompting-masterclass]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[aftermarket-harnesses-ttunguz]]
- [[deep-agents-prompt-caching]]
