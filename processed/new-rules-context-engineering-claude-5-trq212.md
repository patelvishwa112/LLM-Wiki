---
tags: ["context-engineering", "claude-code", "claude", "fable", "opus", "skills", "prompt-engineering", "progressive-disclosure", "agent-harness", "anthropic", "agents", "coding-tools"]
source: https://x.com/trq212/status/2080710971228918066
blog_url: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
date: 2026-07-24
type: bookmark
description: "Anthropic removed 80%+ of Claude Code system prompt for Opus/Fable 5; shift from rigid rules to judgment, progressive disclosure, and rich references."
author: trq212
summary: "Anthropic removed 80%+ of Claude Code system prompt for Opus/Fable 5; shift from rigid rules to judgment, progressive disclosure, and rich references."
raw: "[[raw/trq212_2080710971228918066]]"
---

# The new rules of context engineering for Claude 5 models

Thariq Shihipar (@trq212, Anthropic MTS) on how **context engineering** (system prompt + Skills + CLAUDE.md + memory + tools — not just the user message) changes for Claude 5-class models (Opus 5, Fable 5).

## Headline result

Anthropic **removed over 80% of Claude Code’s system prompt** for advanced models with **no measurable loss** on coding evals. Many older “best practices” are now myths because the model has better judgment and more context channels (memory, artifacts, skills, deferred tools).

## Then → Now

| Old practice | New practice |
|---|---|
| Hard **rules** (“never write comments”) | Let Claude use **judgment** / match surrounding code style |
| Lots of **examples** for tools | Design expressive **interfaces** (enums, params); examples can shrink exploration |
| Dump everything **up front** | **Progressive disclosure** — skills, deferred ToolSearch tools, file trees |
| **Repeat** instructions in system + tool desc | Single source: **tool descriptions** |
| Manual **CLAUDE.md memory** (# hotkey) | **Auto-memory** of relevant work |
| Simple markdown **specs/plans** | **Rich references** — HTML artifacts, test suites, port-from code, **rubrics** + verifier agents |

Example rewrite: from “default to no comments / never multi-paragraph docstrings” → “Write code that reads like the surrounding code: match its comment density, naming, and idiom.”

## Apply to your stack

- **System prompt** — product role/behavior; main lever if you build your own harness (Claude Code users rarely touch this).
- **CLAUDE.md** — light repo purpose + **gotchas**, not filesystem-obvious facts; point to verification skills instead of stuffing process.
- **Skills** — lightweight, opinionated, team-specific; split long skills; avoid over-constraint except high-stakes areas.
- **References** — prefer code/HTML mockups over prose screenshots; rubrics enable dynamic verifier workflows.
- **Simplify** — `/doctor` (`claude doctor`) rightsizes skills and CLAUDE.md; pairs with Fable field guide for advanced prompting.

## Why it matters

- Explicit Anthropic guidance that **over-hobbling** (conflicting CLAUDE.md + skills + system rules) burns reasoning budget.
- Aligns vault themes: progressive disclosure skills, harness as product, Fable planning/artifacts, verification loops.
- Actionable ops: slim CLAUDE.md, move process into skills, design tool schemas, use artifacts/tests as specs.

## Related

- [[claude-fable-map-territory-unknowns-trq212]]
- [[how-to-actually-use-claude-fable-5]]
- [[context-engineering-field-guide-phosphenq]]
- [[anthropic-claude-code-skills-lessons]]
- [[writing-good-skills-measured-rulebook-aparna]]
- [[harness-is-the-product-context-aware-agents]]
- [[claude-code-changed-what-agents-look-like]]
- [[Dynamic Workflows in Claude Code]]
