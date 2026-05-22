---
title: Constitutional AI
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [alignment, constitutional-ai, rlhf]
sources: [raw/papers/arxiv-2212.08073.md, raw/papers/arxiv-2310.13798.md, raw/papers/constitution.md, raw/articles/anthropic-news-claude-new-constitution.md]
confidence: high
---

# Constitutional AI

Constitutional AI (CAI) is Anthropic's approach to training models to be helpful
and harmless using a written set of principles — a "constitution" — rather than
relying purely on human feedback labels. The model critiques and revises its own
outputs against the constitution, generating preference data without per-example
human labeling for harmfulness.

## What the sources say

- [[arxiv-2212.08073]] — Original CAI paper: harmlessness from AI feedback,
  combining self-critique with RL from AI feedback (RLAIF)
- [[arxiv-2310.13798]] — Specific versus general principles: how principle
  specificity affects steering and generalization
- [[constitution]] — The text of Claude's constitution
- [[anthropic-news-claude-new-constitution]] — Public update to Claude's
  constitution; explains the values changes and rationale

## Connections

CAI is the foundation that [[claude-values-and-character]] is built on, and
the practical substrate for [[ai-alignment]] at Anthropic. The classifier
variant of these ideas appears in [[jailbreaks-and-defenses]] via the
[[anthropic-research-constitutional-classifiers]] research line.

## Related

- [[ai-alignment]]
- [[rlhf]]
- [[claude-values-and-character]]
- [[jailbreaks-and-defenses]]
- [[claude-models]]
