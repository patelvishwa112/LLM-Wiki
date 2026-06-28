---
tags:
- agents
- rlm
- structured-outputs
- subagents
- recursive-language-models
- agent-harness
- json-schema
source: https://x.com/neural_avb/status/2063907440509571354
date: 2026-06-08
type: bookmark
author: neural_avb
title: RLM Agents live healthier when they talk via Structured Outputs
summary: How structured outputs (JSON schema) dramatically improve subagent communication
  in Recursive Language Models — free-text fan-out fails with 62 subagents, boolean
  schema routing succeeds at same cost.
raw: '[[raw/neural_avb_2063907440509571354]]'
related:
- '[[wtf-is-a-loop]]'
- '[[4-agent-trading-desk]]'
description: How structured outputs (JSON schema) dramatically improve subagent communication
  in Recursive Language Models — free-text fan-out fails with 62 subagents, boolean
  schema routing succeeds at same cost.
---

# RLM Structured Outputs

## Key Takeaways

1. **Free-text subagent responses cause failure at scale.** 62 subagents all returning prose variations of "no mention found" overwhelm the aggregator. The root agent resorts to hallucinating answers.

2. **Structured outputs act as an external attention mask.** Boolean schema (`{"type": "boolean"}`) lets the main agent skip irrelevant chunks entirely — only reads the ones that returned True. This is external sparsification of the input.

3. **Same cost, dramatically better results.** Both approaches cost ~$0.04 with Minimax M3. The structured output approach just doesn't fail.

4. **Schema validation is the linchpin.** fast-rlm validates on every FINAL call with retry-not-restart semantics. The REPL state is preserved; only the output value needs fixing.

5. **This generalizes beyond booleans.** Any JSON schema works — nested objects, lists, Pydantic models. The model knows the contract at REPL startup and must satisfy it.

## The Core Insight

Low-powered reasoning models lose the plot when reading too many tokens at once. Structured outputs externalize the filtering — the subagent does binary classification, the main agent only reads relevant chunks. It's a form of compute-efficient attention sparsification.

## Connection to Agent Harnesses

This is the same pattern as loop verification (see [[wtf-is-a-loop]]): structured feedback gates make multi-agent systems trustworthy. Free-form text between agents is a failure mode. Contracts (schemas, validation) are the fix.
