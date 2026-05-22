---
title: AI Alignment
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [alignment, safety, rlhf, constitutional-ai]
sources: [raw/articles/*, raw/papers/*]
confidence: high
---

# AI Alignment

The problem of ensuring AI systems behave in ways consistent with human
values, intentions, and preferences. Anthropic has been a pioneering force
in alignment research since its founding.

## Core Approaches

### Constitutional AI (CAI)
Training models using a set of principles (a "constitution") rather than
solely human feedback. Key papers:
- [[arxiv-2212.08073]] — Constitutional AI: Harmlessness from AI Feedback
- [[arxiv-2310.13798]] — Specific vs General Principles for Constitutional AI

### RLHF (Reinforcement Learning from Human Feedback)
Training language models to be helpful and harmless using human preference data:
- [[arxiv-2204.05862]] — Training a Helpful and Harmless Assistant

### Scalable Oversight
Ensuring alignment scales to superhuman systems:
- [[arxiv-2211.03540]] — Measuring Progress on Scalable Oversight
- [[arxiv-2312.09390]] — Weak-to-Strong Generalization

## Recent Developments (2025-2026)

- **Teaching Claude Why:** Reducing agentic misalignment by teaching models
  the reasons behind instructions
- **Alignment Faking:** Studying when models appear aligned but aren't
- **Automated Alignment Researchers:** Using LLMs for scalable oversight

## Key People

- Dario Amodei (CEO, co-founder)
- Daniela Amodei (President, co-founder)
- Various alignment team researchers

## Open Questions

- Can current alignment techniques scale to superhuman systems?
- How to detect and prevent deceptive alignment?
- What is the right "constitution" for AI systems?
