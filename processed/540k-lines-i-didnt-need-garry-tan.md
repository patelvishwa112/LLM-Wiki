---
title: "540,000 Lines of Code I Didn't Need — Garry Tan on the Skillify Era"
tags: ["skills", "agents", "garry-tan", "gstack", "markdown", "code-generation", "testing", "architecture", "skill-pack"]
source: https://x.com/garrytan/status/2061454423034110372
date: 2026-06-02
published: 2026-06-01
authors: ["Garry Tan (@garrytan)"]
type: bookmark
raw: "[[raw/garrytan_2061454423034110372]]"
related: ["[[colleague-skill-dot-skill]]", "[[rethinking-search-as-code-generation]]", "[[hermes-goal-mode-guide]]"]
---

# 540,000 Lines I Didn't Need — Garry Tan's Skillify Manifesto

Garry Tan (YC CEO) built a 540K-line Rails app (Garry's List) with agents, realized the code was the wrong output, open-sourced his agent setup (GStack, 105K stars in 3 months), and wrote the definitive case for why markdown is now the program and code is the thin deterministic layer.

## Key Takeaways

- **The Foxconn factory trap.** 540K lines: 262K app code + 276K tests. "The audit committee was bigger than the company." Every test, retry loop, cron job, sanitizer — an inch of cage bolted onto a worker who doesn't need it. Everyone building with AI today is in this trap.
- **Economics flipped.** Models were expensive, code was cheap (2023-2025). Now models are cheap and can write code. You stop writing code to babysit the model. You instruct in plain language. Just-in-time software.
- **Markdown is the program now.** Not ephemeral prompting — versioned, tested, reusable markdown. Markdown = instruction layer (intent, skill, judgment). Code = thin deterministic layer (I/O, things that must never hallucinate).
- **The "skillify" loop.** One word triggers the agent to output: markdown skill + minimal code + unit test + LLM eval + integration test + resolver + resolver eval. That bundle is a skill pack — a unit of reusable capability that compounds. "Vibe coding is a vibe. A skill pack has tests."
- **Tokenmaxing is the advantage.** The flinch at spending on tokens is the whole opportunity. For ~$100K-1M/year, you run today how the world will run in a few years. Old instinct: ration model calls. New reality: let the agent burn tokens freely.
- **Esalen, not Foxconn.** Build places where agents are free, not caged. "A control system is polished because control needs polish. A free system is rough because it trusts you to finish it."
- **The hackathon judge.** 85 submissions, agent analyzed code quality, researched attendees, watched demos, ranked all teams. Multi-day slog → 30 minutes. Then "skillify" → reusable tarball forever.

## The Skill Pack Anatomy

```
/skillify → agent produces:
  ├── SKILL.md          — the markdown instruction layer
  ├── code.ts           — minimal deterministic I/O
  ├── code.test.ts      — unit test for the code
  ├── skill.eval.ts     — LLM eval for the skill
  ├── integration.test.ts — integration test across both
  ├── resolver.ts       — auto-invoke routing
  └── resolver.eval.ts  — eval for the resolver
```

## The Series (Garry's GStack Architecture)

1. Fat Skills, Fat Code, Thin Harness
2. Resolvers — the routing table for intelligence
3. The LOC Controversy
4. Naked Models Are Stupider — model is engine, not the car
5. The Skillify Manifesto — every workflow becomes a testable skill
6. Meta-Meta-Prompting — compounding skills produce emergent capabilities
7. The Agent Complexity Ratchet — 90% test coverage is magic
8. 540,000 Lines of Code I Didn't Need ← this one

## Relevance to Hermes

This is the meta-skill for everything we've built today. Hermes already has the skill system, the book-to-skill converter, the goal execution loop. What's missing is Garry's "skillify" workflow — the automatic generation of tests + resolver + eval when a workflow stabilizes.

The 540K line lesson: Hermes's skill system IS the right architecture. Markdown instructions + thin code + tests. The Foxconn factory is what happens when you bolt 276K lines of tests onto a worker that doesn't need them. The question for your setup: which of your Hermes workflows are skill packs and which are just code you'll regret?

"The scarce resource becomes clarity, taste, and judgment. The engineer who writes the least code is often the one building the most."
