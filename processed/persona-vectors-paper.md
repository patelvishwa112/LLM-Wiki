---
tags:
- persona-vectors
- mechanistic-interpretability
- steering
- activation-engineering
- alignment
- sycophancy
- finetuning
- arxiv
source: https://arxiv.org/abs/2507.21509
raw: '[[raw/persona-vectors-arxiv-2507.21509]]'
date: 2026-05-28
type: paper
authors:
- Runjin Chen
- Andy Arditi
- Henry Sleight
- Owain Evans
- Jack Lindsey
description: Persona Vectors — Monitoring and Controlling Character Traits in LLMs
---

# Persona Vectors — Monitoring and Controlling Character Traits in LLMs

Chen, Arditi, Sleight, Evans, Lindsey | arXiv 2507.21509 | Jul 2025

## Key Takeaways

- **Persona vectors are activation-space directions** for character traits: evil, sycophancy, hallucination
- **Deployment monitoring** — detect personality fluctuations in real-time
- **Training shift prediction** — finetuning personality changes correlate with vector shifts
- **Two intervention modes:** post-hoc correction + preventative steering during training
- **Data flagging** — identify individual training samples that induce undesirable shifts
- **Fully automated** — extract vectors for any trait from just a natural-language description

## Connection to Ghost Experiment

Our ghost experiment found persona peaks at L14 (31%) then fades — but we used supervised persona prompts (helpful/unhelpful). This paper provides a method for automated extraction of clean persona vectors without labeled contrast pairs. Key question: does the automated method produce cleaner vectors than our supervised approach?

## Source

https://arxiv.org/abs/2507.21509
