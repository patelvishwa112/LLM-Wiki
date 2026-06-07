---
tags:
  - anthropic
  - claude-code
  - agents
  - orchestration
  - code-review
  - planning
  - evals
  - startups
source: https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
date: 2026-05-27
author: Anthropic (CodeRabbit case study)
type: bookmark
summary: "CodeRabbit built an agent orchestration layer on Claude that inserts a structured planning phase before code generation. The system coordinates Claude Opus (strategic direction), Sonnet (sequencing into steps), and Haiku (narrow tool use) to produce a collaborative PRD reviewed by stakeholders before implementation. Key insight: planning quality determines output quality, and late validation in AI workflows is very expensive. Evaluated via hand-tuned LLM judges + downstream code quality metrics."
related:
  - "[[harness-engineering-2026-discipline]]"
  - "[[anthropic-claude-code-skills-lessons]]"
---

# CodeRabbit: Agent Orchestration on Claude

**Source:** Anthropic. CodeRabbit (2M PRs/week, 15K+ customers). VP of AI: David Loker.

## Problem

AI coding tools collapse the time between idea and prototype. But the most frequent failure mode is code that compiles and passes tests yet **doesn't solve the problem it was built to solve.** Developers assume agents share their implicit context. Vague prompts force agents to fill gaps with plausible — but often wrong — assumptions.

Example: Loker built a memory system. The agent generated working code. When asked for usage instructions, it told him to "pass in a user token." There was no login page. He'd specified that users were needed but never said they needed to sign in. Hours of work landed in a product missing a front door.

## Solution: Planning Before Code

An orchestration layer that runs **before** any code generation:

1. **Coordinate multiple Claude models** to analyze requirements and surface assumptions
2. **Produce a structured execution plan** defining what to build and constraints
3. **Output a collaborative PRD** — reviewed by stakeholders before implementation starts
4. **Claude Code picks up the plan** and generates a fine-grained implementation plan

> "Not meant to replace Claude Code's Plan Mode. It's a higher-level orchestration that happens before Claude Code, to point it in a narrow, right direction where everything that needs to be explicit is made explicit."

## Model Routing

| Model | Role | Rationale |
|-------|------|-----------|
| **Opus** | Orchestration loop, high-level strategy, problem understanding | Complex reasoning, direction-setting |
| **Sonnet** | Sequencing strategy into structured planning steps | Balanced speed/capability |
| **Haiku** | Context distillation, narrow tool use | Matches Sonnet on specific tasks at lower cost |

> "If Haiku does as well as Sonnet on a given task, we use Haiku. If the eval harness tells us plan quality improves when we give Opus more room, we give it more room. We don't guess."

## Evaluation Infrastructure

- Library of LLM judges scoring plan quality across specific dimensions
- Hand-tuned examples + manual inspection as starting point
- Downstream metrics: does generated code work, contain extra scope, how many tokens
- A/B: same task with and without planning to isolate planning's value
- Iterated on plan granularity: too granular = stale with codebase shifts; too high-level = room for assumption-filling

## Best Practices

1. **Define the outcome and how to measure it.** Be explicit about the Maximum Possible Product.
2. **Surface implicit assumptions.** Ask Claude: what's missing? What's still implicit?
3. **Identify forgotten edge cases.** Ask Claude to find cases you haven't considered.
4. **Create a record of work.** Chronicle planning artifacts — a quality gate and onboarding tool.

## Key Insight

> The cheaper code generation gets, the more expensive it becomes to move in the wrong direction. Late validation in AI workflows is very expensive. The plan itself becomes a quality gate — if it's good upfront, the downstream effect is pronounced.
