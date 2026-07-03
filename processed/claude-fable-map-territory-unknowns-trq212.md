---
tags:
  - claude
  - fable
  - claude-code
  - agents
  - prompt-engineering
  - planning
  - artifacts
  - context-engineering
  - coding-tools
source: https://x.com/trq212/status/2073100352921215386
date: 2026-07-03
type: bookmark
author: trq212
description: "Thariq (Anthropic) on Fable 5—map (prompts/skills) vs territory (codebase); bottleneck is clarifying unknowns via blind-spot passes, prototypes, interviews, plans, implementation notes."
summary: "Thariq (Anthropic) on Fable 5—map (prompts/skills) vs territory (codebase); bottleneck is clarifying unknowns via blind-spot passes, prototypes, interviews, plans, implementation notes."
raw: "[[raw/trq212_2073100352921215386]]"
---

# Claude Fable — map, territory, and unknowns

**@trq212 (Thariq)** on **Claude Fable 5**: long-horizon quality is limited by how well you **surface unknowns** between your instructions (map) and where work actually happens (territory).

## Framework

| Bucket | Meaning |
|--------|---------|
| Known knowns | Explicit in prompt |
| Known unknowns | You know you don't know |
| Unknown knowns | Tacit "I'll know it when I see it" |
| Unknown unknowns | Blind spots |

## Instruction tradeoff

Over-spec → no pivot; under-spec → wrong industry defaults. Unknowns cause both failure modes.

## Playbook (cheap before expensive)

**Before:** blind-spot pass, HTML brainstorms/prototypes, structured **interviews**, **code references** (not screenshots), implementation plans highlighting reversible decisions.

**During:** `implementation-notes.md` for plan deviations.

**After:** pitch packages for reviewers; **quiz** before merge.

## Fable launch anecdote

Non-expert video edit via Claude Code—probe Whisper/ffmpeg, Remotion prototype, teach color grading before grading.

## Why it matters

Official articulation of **agentic coding as unknown management**—complements vault notes on feedback loops, harness context, and PRD/review workflows.

## Related

- [[feedback-loops-claude-code-less-babysitting]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[multi-perspective-prd-review-claude-code]]
- [[learn-harness-engineering]]
- [[claude-code-changed-what-agents-look-like]]
- [[problem-first-skill-invert-bad-ideas]]