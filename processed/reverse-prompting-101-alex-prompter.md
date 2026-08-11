---
tags: ["prompt-engineering", "productivity", "writing", "agents", "context-engineering", "skills", "communication"]
source: https://x.com/alex_prompter/status/2086807496942068197
date: 2026-08-10
type: bookmark
description: "Reverse prompting / Flipped Interaction — state a goal, let the model interview you one question at a time, then produce; flip control on fuzzy work."
author: alex_prompter
summary: "Reverse prompting / Flipped Interaction — state a goal, let the model interview you one question at a time, then produce; flip control on fuzzy work."
raw: "[[raw/alex_prompter_2086807496942068197]]"
---

# Reverse Prompting 101

@alex_prompter field guide to **reverse prompting** (model interviews you before delivering work). Same idea as Vanderbilt **Flipped Interaction Pattern** (Jules White et al., 2023 “16 prompt patterns”) and Alex Finn’s Jul 2026 popularization.

Disambiguate: **not** “reverse prompt engineering” (inferring a prompt from finished output).

## Pattern

1. Give a **goal**  
2. Model asks questions until it has enough (prefer **one at a time**)  
3. Only then produce the deliverable  
4. **Stopping condition** so the interview ends  

Why it works: you hold unique context; the model often knows which details change quality. Normal monologue prompts force you to guess what to include.

## Practical recipes

**One-liner append**

> Before you answer, ask me the questions you need to do this well. One at a time.

**System / standing rule**

> For any task that is ambiguous, large, or new, interview me before producing anything. Ask one question at a time. Stop when you have what you need.

**Two-prompt goal audit (from thread lineage)**

1. Based on everything I just told you, what else do you need to know to help me reach these goals faster?  
2. What tasks could you take off my plate right now to move me toward them?

## When to use

- **Flip:** fuzzy, high-stakes, novel, multi-constraint work (strategy, briefs, lesson design, personal goals)  
- **Normal prompt:** short unambiguous tasks (“rewrite this sentence”)  

Failure modes: endless/lazy questions; using interviews on trivial tasks. Steer when questions miss.

Working test: a good interview should make you **pause at least once** on a question you wouldn’t have volunteered.

## Why it matters

Cheap interaction upgrade for agents and chat: compounds self-knowledge (answers quality) rather than prompt-library polishing that depreciates with each model release. Pairs with skills/progressive disclosure and human-in-the-loop judgment notes.

## Skeptical read

Creator newsletter CTA at end. Technique is old (2023 patterns); value is the operational framing and failure modes, not novelty.

## Related

- [[loop-engineering-quietly-ate-prompt-engineering]]
- [[how-to-design-a-loop-that-prompts-your-agent]]
- [[iceberg-opus-48-prompts]]
- [[david-ogilvy-writing-coach-claude-skill]]
- [[bezos-writing-framework-six-page-memos-dickiebush]]
- [[how-to-never-get-writers-block-chatgpt-voice-codex-jxnl]]
- [[writing-agent-skills-posthog-ian-vanagas]]
- [[context-engineering-field-guide-phosphenq]]
