---
tags:
- claude-code
- dynamic-workflows
- obsidian
- second-brain
- skills
- subagents
- claude
source: https://x.com/artemxtech/status/2062582596190498864
date: 2026-06-04
type: bookmark
author: Artem Zhutov (@ArtemXTech)
raw: '[[raw/artemxtech_2062582596190498864]]'
description: Claude Dynamic Workflows for Your Second Brain
---

# Claude Dynamic Workflows for Your Second Brain

## Key Takeaways

- **Dynamic Workflows solve three core agent problems at once.** Agent laziness (deterministic program execution ensures all items addressed), self-preferential bias (isolated sub-agent context windows), and goal drift (no multi-turn context thread contamination). This is the biggest Claude Code update since skills and subagents.
- **Three concrete second-brain patterns demonstrated.** (1) Mine 50 sessions for recurring corrections → 86 mined, verified against actual sessions → package into skills. (2) Mine 31 daily notes → Haiku per note, Opus synthesize → recurring tension points with dated evidence. (3) Mine NotebookLM notebook → extract transcripts → analyze → paste-ready implementation prompts.
- **Workflows live inside skills.** Keep workflows as JavaScript files self-contained within skills. Don't blend them — one entity (the skill) with the workflow inside. "I don't want to contaminate my skills with the workflow."
- **More patterns available:** Classify and act, fan out and synthesize, tournament (attempts + judge), loop until done (scheduled daily digest), deep verification (claim extractor → per-claim source checker → verified report).

## Summary

Artem Zhutov demonstrates Claude Dynamic Workflows applied to knowledge management rather than coding. The core insight: Dynamic Workflows turn Claude Code into a deterministic, reliable system for processing unstructured personal knowledge at scale. Three real examples show mining sessions for recurring corrections, mining daily notes for repeating patterns, and mining NotebookLM notebooks for implementable ideas — each producing structured HTML reports with verified evidence. The workflows-embedded-in-skills pattern is the recommended integration approach.

## Related

- [[every-agentic-engineering-hack-june-2026]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[learn-harness-engineering]]
