---
title: RLHF (Reinforcement Learning from Human Feedback)
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [alignment, rlhf]
sources: [raw/papers/arxiv-2204.05862.md, raw/papers/arxiv-2009.01325.md, raw/papers/arxiv-2112.00114.md, raw/papers/arxiv-2210.10760.md]
confidence: high
---

# RLHF

Reinforcement Learning from Human Feedback trains language models against a
reward model fit to human preference comparisons. It is the workhorse technique
for steering large models toward helpfulness and harmlessness, and the baseline
that [[constitutional-ai]] augments with AI-generated feedback.

## What the sources say

- [[arxiv-2204.05862]] — "Training a Helpful and Harmless Assistant with RLHF":
  Anthropic's foundational HH paper
- [[arxiv-2009.01325]] — "Learning to summarize from human feedback": the
  early pre-Anthropic work that established the recipe
- [[arxiv-2112.00114]] — "A General Language Assistant as a Laboratory for
  Alignment": Anthropic's testbed for assistant alignment
- [[arxiv-2210.10760]] — "Reward Modeling for Mitigating Overoptimization in
  RLHF": studies the Goodhart-style failure mode where the policy exploits the
  reward model

## Limitations

RLHF rewards what humans approve of, not what is true or safe in the limit —
which motivates research on [[sycophancy]], [[reward-hacking-and-tampering]],
and [[scalable-oversight]].

## Related

- [[ai-alignment]]
- [[constitutional-ai]]
- [[scalable-oversight]]
- [[reward-hacking-and-tampering]]
- [[sycophancy]]
