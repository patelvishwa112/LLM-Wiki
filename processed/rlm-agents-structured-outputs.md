---
tags: ["rlm", "structured-outputs", "subagents", "recursive-language-models", "agent-harness", "json-schema"]
source: https://x.com/neural_avb/status/2063907440509571354
date: 2026-06-08
type: bookmark
author: neural_avb
summary: "RLM subagents produce far cleaner, hallucination-resistant results when forced to return structured outputs (JSON Schema) instead of free-text. Case study on The Coxon Fund shows free-text fan-out leads to aggregation failure; boolean schema routing succeeds with the same token budget. Validation happens at FINAL() in the REPL."
raw: "[[raw/neural_avb_2063907440509571354]]"
---

# RLM Agents live healthier when they talk via Structured Outputs

AVB demonstrates a practical fix for a common RLM failure mode.

## The Problem
Free-text subagent responses in Recursive Language Models create aggregation hell: 62 noisy, contradictory prose summaries overwhelm the root agent, leading to hallucinated final answers.

## The Fix
Use JSON Schema structured outputs for subagent communication:
- Subagents return a validated boolean (or other schema) instead of prose.
- The root agent only reads the True chunks.
- Validation at FINAL() enforces the contract inside the REPL.
- Retry on schema failure instead of restarting.

## Result
Same token budget (~$0.04), dramatically lower hallucination risk, cleaner attention masking via external sparsification.

Directly relevant to Hermes RLM harness design, subagent communication, and structured output patterns.