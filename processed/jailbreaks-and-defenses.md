---
title: Jailbreaks and Defenses
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [safety, jailbreaks, classifiers]
sources: [raw/anthropic/articles/anthropic-research-constitutional-classifiers.md, raw/anthropic/papers/arxiv-2501.18837.md, raw/anthropic/papers/arxiv-2404.11018.md, raw/anthropic/papers/arxiv-2308.14132.md, raw/anthropic/papers/arxiv-2306.05499.md]
confidence: high
---

# Jailbreaks and Defenses

Jailbreaks are inputs that bypass a model's safety training. Defenses range
from training-time interventions (constitutional methods) to inference-time
guards (input/output classifiers, perplexity-based detectors).

## What the sources say

### Attacks
- [[arxiv-2404.11018]] — "Many-Shot In-Context Learning": shows that long
  contexts can elicit behaviors that single-turn safety training suppresses
- [[arxiv-2306.05499]] — Prompt injection attacks on LLM-integrated apps
- [[arxiv-2308.14132]] — Detecting LM attacks with perplexity

### Defenses
- [[anthropic-research-constitutional-classifiers]] — Anthropic's deployed
  classifier system trained from a constitution
- [[arxiv-2501.18837]] — The Constitutional Classifiers paper
- [[anthropic-news-model-safety-bug-bounty]] — Program for finding new
  jailbreaks at scale

## Related

- [[constitutional-ai]]
- [[red-teaming]]
- [[ai-cybersecurity]]
- [[detecting-misuse]]
- [[claude-models]]
