---
tags:
- claude-code
- agents
- skills
- feedback-loops
- verification
- code-review
- claude
source: https://x.com/delba_oliveira/status/2062203743387459836
date: 2026-06-03
type: bookmark
author: Delba Oliveira (Anthropic)
raw: '[[raw/delbaoliveira_2062203743387459836]]'
description: 'Feedback Loops: Help Claude Code Complete Ambitious Tasks With Less
  Babysitting'
---

# Feedback Loops: Help Claude Code Complete Ambitious Tasks With Less Babysitting

## Key Takeaways

- **Self-verification is the autonomy multiplier.** Claude already self-verifies against deterministic signals (type errors, lint, failing tests, runtime errors). The gap is the manual checks you run after it responds and before merge. Encode those and Claude's first response gets dramatically closer to final.
- **Two-layer verification architecture.** Layer 1: verification inside the agentic loop (skills that encode your manual checks). Layer 2: a second agent reviews before merge — clean context, no bias from the original coding session.
- **Encode domain processes as skills.** Write down your team's best-practices process. Use `/skill-creator` to have Claude interview you. For qualitative checks (not pass/fail), set rubrics with Claude. Example: frontend verify skill with Chrome DevTools MCP for browser testing and Core Web Vitals audit.
- **Bundle skills into workflows.** The Claude Code team's internal skill bundles `/simplify` (clean diff) → `/verify` (end-to-end check) → design check → open PR → watch CI. A single skill that orchestrates the full development lifecycle.
- **Fresh-agent review catches biases.** A new agent doesn't carry the same context or assumptions as the coding agent. This isolation makes reviews more honest. Options: `/review` (quick), `/code-review` plugin (parallel subagents), or managed Claude Code Review on every PR.

## Summary

Delba Oliveira (Anthropic, Claude Code team) describes a practical framework for making Claude Code more autonomous through structured feedback loops. The core idea: the more manual verification steps you encode as skills, the less babysitting Claude needs.

The framework has two layers. Inside the agentic loop, encode your domain's verification process as a skill — frontend teams would use browser tools for visual checks and Core Web Vitals audits, backend teams would use test suites and linting, etc. Before merge, use a second agent for unbiased code review — it doesn't carry the original coding session's context or assumptions.

The end state is bundled skill workflows that replicate your entire dev lifecycle: simplify the diff, verify end-to-end, check design, open PR, watch CI, fix failures. Claude runs the whole loop while you work on other things.
