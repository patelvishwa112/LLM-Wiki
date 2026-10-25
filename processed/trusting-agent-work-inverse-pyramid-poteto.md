---
title: "Trusting agent work: the inverse pyramid of enforcement"
type: bookmark
description: "Morgan's quote-tweet of Lauren's checklist: trust agents by pushing effort up an inverse pyramid — codebase invariants first, static analysis next, prose third, human review last."
tags: [agents, verification, code-review, agent-harness, harness-engineering, static-analysis, human-in-the-loop]
source: https://x.com/morganlinton/status/2111169018082054497
date: 2026-10-16
author: Morgan
summary: "Morgan's quote-tweet of Lauren's checklist: trust agents by pushing effort up an inverse pyramid — codebase invariants first, static analysis next, prose third, human review last."
raw: "[[raw/morganlinton_2111169018082054497]]"
---

# Trusting agent work: the inverse pyramid of enforcement

**Source:** Morgan (@morganlinton), 2026-10-16. A short quote-tweet reporting that his Grok bot ingested Lauren's (@poteto) agent-trust post, learned from it, and then flagged a past situation where the advice would have helped.

The substance is Lauren's four-layer answer to "how do you trust your agents' work more?", ordered as an inverse pyramid — most effort at the top, least at the bottom, because the top layers are deterministic and permanent while the bottom ones are judgment and attention. Layer 1 is codebase improvement: architecture, stronger types and invariants, clear boundaries. Her reasoning is mechanical rather than stylistic — agents copy what exists and take the shortest path, so make the easy thing the right thing; a problem eliminated categorically in code never has to be considered again. Layer 2 is static analysis: lint rules, tests, CI, and verification such as TLA+, described as very token-efficient ways to catch issues ahead of time. Layer 3 is prose — comments, rules, AGENTS.md, skills — everything that cannot be enforced and therefore depends on agent judgment; use it minimally but do use `/create-verification-skill`.

Layer 4 is human review, which she calls the hardest to scale and openly concedes is already impractical: at the rate agents land code it is "pretty much impossible to thoroughly review every PR". The effort saved there should be redirected to the highest-leverage point — designing an environment where agents do the right thing by default. She then turns the checklist into a bootstrap prompt for a new project: mine Slack and past code-review comments where she gave architecture feedback, `/recall` past transcripts to learn how she steers agents, run `/poteto-mode` with `/correct` and `/architect` over past commits to find recurring agent pitfalls and propose a rearchitecture plan, answer open questions by prototyping rather than asking her, back the plan with real data, and confirm the rewritten prompt with `/sharpen` and `/in-your-own-words` first.

Morgan's contribution is the demonstration and the mechanism: pasting a post into a bot and telling it to learn is enough for a persistent agent to internalise the rule set, and his reported payoff was retrospective self-criticism — the bot identifying a past moment where the guidance would have changed its behaviour.

## Why it matters

This is the cheapest available ordering for anyone trying to raise agent autonomy: spend the budget on code-level determinism before spending it on prompts, and treat human review as the thing you are trying to buy back rather than the safety net you rely on. It also reframes AGENTS.md and skills as the layer you want *least* of — a good signal when reviewing harnesses that are nothing but prose.

The self-review anecdote points at a second mechanism worth noting: distributing a rule set through the agent's own memory, so compliance is reinforced by the same system producing the work, and the agent can audit its past behaviour against a new standard.

## Key points

- Inverse pyramid, top to bottom: codebase invariants → static analysis → prose → human review; effort should be concentrated at the top because those layers are deterministic.
- "Agents love to copy what exists and take the shortest path, so make the easy thing the right thing" — the design principle behind layer 1.
- Static analysis named concretely: lint rules, tests, CI, TLA+ verification; described as token-efficient pre-emptive checking.
- Prose (comments, AGENTS.md, skills) is for what cannot be enforced; use minimally, plus `/create-verification-skill`.
- Human review is acknowledged as unscalable at current landing rates; redirect that effort into environment design.
- Bootstrap prompt: mine Slack/PR feedback, `/recall` transcripts, `/poteto-mode` with `/correct` + `/architect` over past commits, prototype instead of asking, confirm the prompt via `/sharpen` and `/in-your-own-words`.
- Reception: 6,888 likes / 514 reposts on Lauren's post; Morgan reports his Grok bot learned it and self-flagged a past miss.

## Related

- [[agent-workflows-silent-degradation-verification-vladic]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[software-factories-no-slop-dzhng]]
- [[why-harness-engineering-is-so-hard-winterarc]]
