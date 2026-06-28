---
tags:
- dspy
- gepa
- prompt-optimization
- prompt-engineering
- evals
- llm-judges
- pretraining
- microsoft-ai
- mai-thinking
source: https://x.com/harold_matmul/status/2069836410052325711
date: 2026-06-24
type: bookmark
author: harold_matmul
summary: Microsoft AI's Harold Benoit on dspy.GEPA as compute-driven prompt search
  with Genetic-Pareto optimization, strong reflection LLMs, and graders that return
  scores plus text feedback.
raw: '[[raw/harold_matmul_2069836410052325711]]'
description: Microsoft AI's Harold Benoit on dspy.GEPA as compute-driven prompt search
  with Genetic-Pareto optimization, strong reflection LLMs, and graders that return
  scores plus text feedback.
---

# Are You Still Tuning Your LLMs by Hand? (An Ode to GEPA)

Harold Benoit (@harold_matmul, Microsoft AI) argues **dspy.GEPA** is underused: it turns prompt tuning from hours of manual failure analysis into an optimization loop that spends **compute instead of researcher time**, while forcing solid **eval + grader** hygiene.

## Key takeaways

- **Thesis:** Keep GPUs productive by automating prompt search; GEPA was used in **MAI-Thinking-1** pretraining data curation (web-page quality judges).
- **Old vs new workflow:** Same upfront data understanding and eval building; replace hand-written prompt iteration with a **dspy.GEPA loop** rerunnable across base models in minutes.
- **Mechanism:** Reflection LLM (e.g. Opus, GPT-5.5) summarizes mistakes; **Genetic-Pareto** optimizer picks candidates; task **grader** supplies score **and** textual feedback for richer signal than scalar-only search.
- **Eval overload:** "Eval" means train/val data **plus** the grader (human labels, rubric LLMs, reward models).
- **Use cases:** STEM/code page quality filters, human+GEPA label bootstrapping for embedding classifiers, distilling vague human priors into explicit prompts from ~100 labels.
- **vs finetune / embeddings:** Favors **quality** and **time-to-first-solution** — external strong models, quality–cost Pareto frontiers, on-the-fly prompt switches, matched inference numerics, reasoning for hard grading; distill later if scale demands it.

## Why it matters

Connects DSPy-style **programmatic prompt optimization** to production-scale **data curation** and positions prompt tuning as first-class engineering (evals required, fast iteration) before committing to finetunes or cheap classifiers.

## Related

- [[automate-writing-llm-prompts-dspy]] — DSPy generate/evaluate/optimize loop for prompts
- [[langchain-fireworks-trace-judge-100x-cheaper]] — Trace-derived judges for agent/LLM tasks
- [[agent-harness-should-repair-itself]] — Evals and regression testing in production harnesses
- [[how-to-give-your-agent-memory]] — Trace → analyze → update context loop (complementary lifecycle)