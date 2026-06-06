---
title: AI Alignment
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [alignment, safety, rlhf, constitutional-ai]
sources: [raw/anthropic/articles/*, raw/anthropic/papers/*]
confidence: high
---

# AI Alignment

The problem of ensuring AI systems behave in ways consistent with human
values, intentions, and preferences. Anthropic has been a pioneering force
in alignment research since its founding.

## Core Approaches

### Constitutional AI (CAI)
Training models using a set of principles (a "constitution") rather than
solely human feedback. See [[constitutional-ai]] for a full synthesis.
Key papers:
- [[arxiv-2212.08073]] — Constitutional AI: Harmlessness from AI Feedback
- [[arxiv-2310.13798]] — Specific vs General Principles for Constitutional AI

### RLHF (Reinforcement Learning from Human Feedback)
Training language models to be helpful and harmless using human preference data.
See [[rlhf]] for a full synthesis.
- [[arxiv-2204.05862]] — Training a Helpful and Harmless Assistant

### Scalable Oversight
Ensuring alignment scales to superhuman systems. See [[scalable-oversight]]
for a full synthesis.
- [[arxiv-2211.03540]] — Measuring Progress on Scalable Oversight
- [[arxiv-2312.09390]] — Weak-to-Strong Generalization

## Recent Developments (2025-2026)

- **Teaching Claude Why:** See [[agentic-misalignment]]
- **Alignment Faking:** See [[alignment-faking]]
- **Reward Hacking:** See [[reward-hacking-and-tampering]]
- **Sleeper Agents / Deceptive Alignment:** See [[deceptive-alignment]]
- **Persona Monitoring:** See [[persona-vectors]]

## Key People

- [[dario-amodei]] (CEO, co-founder)
- [[anthropic]] — organization page with full leadership roster

## Open Questions

- Can current alignment techniques scale to superhuman systems?
- How to detect and prevent deceptive alignment? See [[deceptive-alignment]], [[anthropic-research-auditing-hidden-objectives]]
- What is the right "constitution" for AI systems? See [[claude-values-and-character]]

## Related sub-pages

- [[constitutional-ai]]
- [[rlhf]]
- [[scalable-oversight]]
- [[alignment-faking]]
- [[deceptive-alignment]]
- [[agentic-misalignment]]
- [[reward-hacking-and-tampering]]
- [[sycophancy]]
- [[claude-values-and-character]]
- [[responsible-scaling-policy]]
