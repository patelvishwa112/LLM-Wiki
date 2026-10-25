---
title: "Building a Harness with Jev"
type: bookmark
description: "Sydney Runkle shows how to wire TypeSafe's Jev System One classifier into a LangChain harness for model routing and tool-risk gating without a chat call per decision."
tags: [agents, agent-harness, routing, cost-optimization, inference, structured-outputs, langchain]
source: https://x.com/sydneyrunkle/status/2100754364545761643
date: 2026-09-18
author: Sydney Runkle
summary: "Sydney Runkle shows how to wire TypeSafe's Jev System One classifier into a LangChain harness for model routing and tool-risk gating without a chat call per decision."
raw: "[[raw/sydneyrunkle_2100754364545761643]]"
---

# Building a Harness with Jev

**Source:** Sydney Runkle (LangChain), 2026-09-18. An X long-form article on using TypeSafe AI's Jev classifier model inside a LangChain agent loop.

The pitch starts from a cost observation: the agent loop is "LLM decides → tool executes → model evaluates → repeat", so every branch costs a full model call. Tool calling and structured outputs made agents integrable with ordinary software, but they did not make the loop cheap. Jev attacks the loop's decision points instead of its generation.

Jev is not a chat LLM — it emits no text. It is a "System One" model: you pass a `state` (text, structured data, or LangChain messages) plus `questions`, and get back typed answers with probabilities. Three question types are supported: **Choice** (probability per option plus overall confidence), **Score** (a continuous score over ordered levels plus the distribution), and **Noul** (probability that a yes/no statement is true). Because questions are evaluated in parallel, adding more questions barely changes latency and only costs the tokens for the extra questions.

The LangChain integration ships as `langchain-typesafe` with a `TypeSafeClassifier` whose `.invoke()` returns classification results. The article's two concrete arms are `ModelRouterMiddleware`, which asks Jev to pick the cheapest sufficient model from criteria you define (and keeps the probabilities in agent state), and `AutoModeMiddleware(tools=["bash"])`, which classifies tool calls for risky decisions and blocks them before execution — a reproduction of the closed-source safety classifier that coding harnesses like Claude Code, Codex, and Cursor already ship.

## Why it matters

The harness layer is where cost and latency are decided, and Jev makes a distinct architectural claim: not every step in the loop needs a generative model. If a calibrated classifier can make the routing, gating, and triage calls that currently burn a frontier-model turn, the economics of long agent runs change materially — and tool-risk gating, previously a proprietary feature of a few coding harnesses, becomes something any team can add in a middleware hook.

## Key points

- Vendor-reported on classification tasks: up to **200x faster** inference and **400x lower cost** than comparable LLMs (TypeSafe's own launch figures of 20–200x faster, 40–400x cheaper).
- Three question types — Choice, Score, Noul — each returning calibrated probabilities plus a confidence value; multiple questions per state are evaluated in parallel.
- Docs example: a frustrated Stripe-connection support ticket returns `noul: 0.999` for `is_urgent`.
- `ModelRouterMiddleware` picks a model per run from the latest user message ("least costly model that can complete the task"), with probabilities preserved in agent state.
- `AutoModeMiddleware(tools=["bash"])` blocks risky tool calls before execution — the closed harness classifier pattern, now open.
- Integration surface: `pip install langchain-typesafe`, `TYPESAFE_API_KEY`, state as text / structured data / messages, so it drops into nodes or middleware.
- Named early users: Kyle Jeong (Browserbase) for sub-cent browser agents, Jarrod Watts for a live trading agent, Ryan Vogel for email triage at scale.

## Related

- [[jev-system-one-decisions-akshay]]
- [[jev-as-judge-probability-uncertainty-signal]]
- [[text-classification-bag-of-words-to-jev-rasbt]]
- [[how-to-build-custom-agent-harness-langchain]]
