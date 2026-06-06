---
tags: [dspy, prompt-engineering, prompt-optimization, llm, automation, evaluation, meta-prompting, llm-as-judge, production, reliability]
source: https://towardsdatascience.com/automate-writing-your-llm-prompts/
type: article
author: W Brett Kennedy
date: 2026-06-05
---

# Automate Writing Your LLM Prompts with DSPy

**TL;DR:** DSPy automates the full prompt lifecycle — generation, evaluation, and optimization — replacing manual prompt engineering with an ML-style train/test loop.

## The Problem with Manual Prompt Engineering

Traditional prompt engineering has a fundamental flaw: it's both **time-consuming and unreliable**:

- Testing candidate prompts is tedious — you realistically test far fewer inputs than needed
- LLMs are stochastic — same prompt returns different responses, some better than others
- For 20 documents × 3 tests each = 60 tests — nobody actually does this
- Long-form outputs (summaries, critiques) are near-impossible to evaluate consistently
- Experienced developers can spend **hours or days on a single prompt** and still not be certain it's the strongest

## The ML Contrast

With traditional ML, we automate evaluation: run test set → get predictions → execute scoring function (MSE, F1, AUROC) → single number indicating quality. Prompt engineering ignores decades of software development best practices.

## What DSPy Does

Three major capabilities:

| # | Capability | Description |
|---|-----------|-------------|
| 1 | **Generate** | Provide a high-level task signature like `"document → assessment_of_plausibility"` — DSPy auto-generates the prompt |
| 2 | **Evaluate** | Provide test data + a Python scoring function — DSPy runs all test cases and returns an overall score |
| 3 | **Optimize** | Meta-prompting loop: one LLM generates candidate prompts, another evaluates them, DSPy learns from failures |

## Optimization Loop

```
best_prompt = ""
loop:
  generate new candidate prompt (via meta-prompting)
  evaluate candidate prompt
  if best so far → best_prompt = current
```

- **Early stopping:** weak prompts quit early (don't waste tokens on full test set)
- **Learns as it goes:** sees not just which test cases fail, but **why** — uses this to suggest increasingly better candidates

## Evaluation Function Pattern

For classification/regression tasks:

```python
def evaluate_answer(test_instance, model_prediction):
    return abs(test_instance.ground_truth - model_prediction)
```

For long-form outputs: use **LLM-as-a-judge** — removes human bias and enables automation.

## Minimal Working Example

```python
import dspy

lm = dspy.LM("openai/gpt-4o-mini", api_key=OPENAI_API_KEY)
dspy.settings.configure(lm=lm)

predictor = dspy.Predict("question, context → answer, confidence")
prediction = predictor(question="What is the capital of France?", context="")
print(prediction.answer, prediction.confidence)
# Output: Paris, High
```

## When to Use

- **Use DSPy** whenever you'd otherwise do manual prompt engineering
- **Skip DSPy** only when the task is trivially simple or you don't need a strong prompt
- Typical runtime: 20-30 minutes (or more) to find a strong prompt
- Monitor LLM costs, but higher-quality prompts are cheaper long-term
- Easy to constrain: specify a small number of candidate prompts and take the strongest

## Bottom Line

DSPy consistently outperforms manual prompt engineering in experiments. For any non-trivial LLM application, DSPy functions as an automated prompt engineering assistant — set up the code and let it do the work. Also worth reading: *Building LLM Applications with DSPy* (Manning, Kennedy & Smorodinsky).