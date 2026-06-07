---
title: "Hermes Agent Model Stack — The Best Models For Each Job"
tags: ["hermes", "hermes-agent", "models", "model-selection", "llm-providers", "openai-codex", "claude-sonnet", "gemini", "deepseek", "qwen", "grok", "openrouter", "nous-research", "agent-ops", "cost-optimization", "coding-tools", "productivity"]
source: https://x.com/zaimiri/status/2063694809592635430
date: 2026-06-07
published: 2026-06-07
authors: ["zaimiri (@zaimiri)"]
type: bookmark
raw: "[[raw/zaimiri_2063694809592635430]]"
related: ["[[hermes-goal-mode-guide]]", "[[hermes-as-lifeos]]"]
summary: "Zaimiri's guide to picking models for Hermes Agent — not based on benchmarks, but on cost psychology, tool reliability, and task routing. Covers 8 model paths with pros/cons, use cases, and setup commands."
---

# Hermes Agent Model Stack — The Best Models For Each Job

Zaimiri's guide to choosing models for Hermes Agent. The core thesis: the "best model" for an agent is not the smartest on a benchmark. It is the model you can afford to run for hours without flinching, with enough reasoning quality that you still trust it near your filesystem.

## Agent Psychology vs Chatbot Psychology

A chatbot needs one clean answer. An agent needs to survive long loops, call tools cleanly, read messy context, recover from bad assumptions, and avoid wasting money. The model that wins is not the one with the highest benchmark score — it is the one whose cost doesn't poison the psychology of using agents freely.

## The 8 Model Paths

### 1. OpenAI Codex OAuth — Best Default

- **Role:** Daily driver
- **Why:** Subscription billing removes the per-token taximeter. You stop hesitating before subagents, multi-pass work, and deep inspection.
- **Setup:** `hermes model` → choose OpenAI Codex, or `hermes auth add codex-oauth`
- **Caveat:** Entitlement depends on your OpenAI/Codex plan.

### 2. Claude Sonnet 4.6 — Best Quality Pick

- **Role:** High-trust review model
- **Why:** Excels at the boring parts of agent work — reading instructions, respecting plans, noticing edge cases, not getting too clever near files.
- **Setup:** `hermes chat --provider anthropic --model claude-sonnet-4-6`
- **Caveat:** Cost. Use it when quality/judgment matters, not for every tiny task.

### 3. Gemini 2.5 Pro + Flash — Best Long-Context Pair

- **Role:** Document reader / cheap auxiliary
- **Why:** Gemini Pro is strong on long-context reading, broad document analysis, repo understanding. Flash handles summaries, routing, fast low-risk passes.
- **Setup:** `hermes chat --provider gemini --model gemini-2.5-pro`
- **Caveat:** Not always preferred for delicate multi-step tool-heavy coding loops.

### 4. DeepSeek V3.2 — Best Budget Workhorse

- **Role:** High-volume worker
- **Why:** Cheap enough for routine coding, subagents, batch tasks, first drafts, inspection passes. Makes Hermes affordable to use constantly.
- **Setup:** `hermes chat --provider deepseek --model deepseek-chat`
- **Caveat:** Verify important edits. Send final diffs through Claude/Codex.

### 5. xAI Grok OAuth — Subscription Path for X Ecosystem

- **Role:** Optional subscription model
- **Why:** If already paying for Grok/SuperGrok, no new billing account needed. xAI Responses API with caching for multi-turn sessions.
- **Setup:** `hermes auth add xai-oauth` or `hermes chat --provider xai --model grok-4.3`
- **Caveat:** Test on your exact tasks before making it your only model.

### 6. Qwen3 Coder — Best Coding-Budget Alternative

- **Role:** Cheap coding model
- **Why:** Coding-focused without expensive providers. Multiple paths: Qwen OAuth, Alibaba DashScope, Alibaba Coding Plan — do not mix these up.
- **Setup:** `hermes chat --provider alibaba --model qwen3-coder-plus` or `--provider alibaba-coding-plan`
- **Caveat:** Verify before big edits. Good for "lots of attempts, strong model reviews the patch."

### 7. OpenRouter — One Key, Many Models

- **Role:** Flexible testing/routing layer
- **Why:** Try many models without setting up each provider separately. Compare Claude/Gemini/DeepSeek/Qwen/Grok on the same prompt.
- **Setup:** `hermes chat --provider openrouter --model anthropic/claude-sonnet-4.6`
- **Caveat:** Adds an aggregator between you and the upstream model.

### 8. Nous Portal — Best All-in-One Beginner Path

- **Role:** Simplest setup
- **Why:** One OAuth login covers frontier models + Tool Gateway (search, browser, images, TTS). Official Nous Research subscription gateway.
- **Setup:** `hermes setup --portal` or `hermes model` → choose Nous Portal
- **Caveat:** Portal convenience doesn't guarantee every model behind it is best for every job.

## Recommended Stack

For a normal power user, don't pick one model:

| Job | Model |
|-----|-------|
| Main daily driver | OpenAI Codex OAuth |
| High-trust review | Claude Sonnet 4.6 |
| Long-context reading | Gemini 2.5 Pro |
| Cheap worker | DeepSeek V3.2 or Qwen3 Coder |
| Flexible testing | OpenRouter |
| Beginner/all-in-one | Nous Portal |
| Optional subscription | xAI Grok OAuth |

Hermes is an operating layer, not a single chat window: Telegram → Skills → Memory → Cron → Subagents → Profiles → MCP/Tools, with models routed by job, not ego.

The edge is getting Hermes cheap enough, reliable enough, and contextual enough that you actually use it every day.
