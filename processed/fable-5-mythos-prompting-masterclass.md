---
tags: ["anthropic", "fable-5", "mythos", "prompting", "claude", "agent-management", "loops"]
source: https://x.com/aiedge_/status/2065064961999847849
date: 2026-06-11
type: bookmark
author: aiedge_
summary: "Plain-English guide to prompting Anthropic's Fable 5 (Mythos): long-running autonomous tasks, first-pass accuracy, clarifying questions, 50+ subagent management, superior vision, and coding/security audits. Optimal prompt structure includes Context + Request + Output format + Constraints. Effort levels (high/xhigh/ultracode) are the main control knob. Includes memory system and /loop patterns."
raw: "[[raw/aiedge__2065064961999847849]]"
---

# Fable 5 (Mythos) Prompting Masterclass by Anthropic

AI Edge's translation of Anthropic's official playbook for the new Fable 5 model (also called Mythos).

## What Makes Fable 5 Different
- Designed for sustained, multi-day, goal-directed autonomous work (pairs with /goal or /loop).
- Gets things right the first time — far less iteration needed.
- Proactively asks clarifying questions before starting complex runs.
- Built to manage 50+ parallel subagents.
- Significantly better at interpreting dense images, screenshots, and visual data.
- Especially strong at codebase review, debugging, and security audits.

## How to Prompt Fable 5
- **Effort levels** are the primary control: high is default; xhigh for hardest problems; ultracode for full autonomous orchestration.
- Always give the "why" behind the task (larger context + who it's for + what the output enables).
- Keep instructions short — over-engineering can degrade quality.
- Explicitly tell it when to pause and check in (destructive actions, scope changes).
- Provide a memory system (simple markdown file) with one-lesson-per-file + one-line summaries.

## Optimal Prompt Structure
1. Context (files, data, larger task)
2. Request (one clear sentence)
3. Output format (exactly how to deliver)
4. Constraints (what not to assume)

## /loops
/loop <interval> + goal is a powerful pattern for autonomous monitoring and work.

## Caveats
- Runs longer than expected at high effort.
- Can go beyond what you asked (use check-ins).
- Old skills/prompts from prior models may perform worse.
- May decline "safe" requests (cybersecurity, life sciences).
- Higher token cost.

Directly relevant to Hermes prompting, skill design, and goal-execution patterns with the newest Claude models.