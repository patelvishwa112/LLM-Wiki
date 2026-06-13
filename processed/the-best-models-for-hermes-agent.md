---
tags: ["hermes", "models", "providers", "codex", "claude", "gemini", "deepseek", "openrouter", "nous-portal"]
source: https://x.com/zaimiri/status/2063694809592635430
date: 2026-06-07
type: bookmark
author: zaimiri
summary: "Practical model stack for Hermes Agent: Codex OAuth as the default daily driver (removes per-token anxiety for long loops), Claude Sonnet 4.6 for high-trust review, Gemini 2.5 Pro for long-context reading, DeepSeek V3.2 or Qwen3 Coder for cheap volume work, OpenRouter for flexibility, and Nous Portal for one-login simplicity. Stresses that the 'best' model is the one you can afford to run for hours without hesitation."
raw: "[[raw/zaimiri_2063694809592635430]]"
---

# The Best Models For Hermes Agent

zaimiri's recommended model stack for Hermes, optimized for long-running agent loops rather than single-answer chatbots.

## Core Principle
The best model for Hermes is not the smartest on benchmarks — it is the one you can afford to run for hours without psychological friction, with enough reasoning quality that you trust it near your filesystem.

## Recommended Stack

1. **OpenAI Codex OAuth** — Best default daily driver
   - Removes the "taximeter" anxiety of per-token billing.
   - Ideal for long loops, subagents, repo edits, terminal tasks.
   - Setup: `hermes model` or `hermes auth add codex-oauth`

2. **Claude Sonnet 4.6** — Best quality for serious tool work
   - Excellent at reading instructions, respecting plans, noticing edge cases.
   - Use for complicated refactors, debugging, planning-heavy tasks, family-office work.
   - Use as review model after cheaper first pass.

3. **Gemini 2.5 Pro + Flash** — Best long-context and utility pair
   - Strong at reading repos, summarizing logs, comparing documents.
   - Flash for cheap auxiliary tasks.

4. **DeepSeek V3.2** — Best budget workhorse
   - Enables high-volume, casual Hermes usage.
   - Good for first drafts, subagents, batch tasks, routine coding.

5. **Qwen3 Coder** — Best coding-budget alternative
   - Strong for code-heavy work and repo tasks.

6. **OpenRouter** — Best for model testing and flexibility
   - One key for many models; great for comparing options.

7. **Nous Portal** — Best beginner-friendly all-in-one
   - OAuth login covers multiple models + Tool Gateway features.

8. **xAI Grok** — Best if already in the xAI ecosystem
   - OAuth or API key support.

## Takeaway
Build a small routed stack rather than picking one model. The edge comes from making Hermes cheap enough, reliable enough, and contextual enough that you actually use it every day.

Directly relevant to Hermes configuration and daily usage patterns.