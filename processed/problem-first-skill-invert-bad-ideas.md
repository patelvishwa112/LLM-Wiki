---
tags: [skills, agents, claude-code, claude-cowork, pm, problem-first, triage, templates]
source: https://x.com/nurijanian/status/2063186118409929161
date: 2026-06-06
type: bookmark
author: nurijanian
summary: A Claude/Cowork skill that decompresses proposed solutions back into underlying problems. Treats solutions as "compressed confessions" of sensed-but-unarticulated problems. 8-section output includes assumption challenges with risk+validation tests and 3 alternative framings. Also works in reverse for triaging your own ideas — 90% die at "evidence status: none."
related: [[feedback-loops-claude-code-less-babysitting]], [[Dynamic Workflows in Claude Code]], [[colleague-skill-dot-skill]]
---

# /problem-first — A Skill to Invert Bad Ideas

By George from prodmgmt.world (@nurijanian)

## Core Insight

**Solution as compressed confession.** When a team hands you a solution ("build a notification system"), treat it not as an execution request but as evidence of a real problem they sensed but couldn't articulate. Decompress it backward.

The same skill runs in reverse: feed your own half-baked idea in, and it extracts the problem you think you're solving. Most ideas die at "Evidence Status: none."

## The 8-Section Output

1. **Solution-jumping diagnosis** — what signal triggered the proposal?
2. **Underlying problem** — decompressed from the solution artifact
3. **Assumption challenges** — each with risk-if-wrong and a validation test (the section humans skip)
4. **Problem statement** — crisp, testable
5. **Three alternative framings** — surface the jump the team made; each leads to a different build
6. Draft message to the team
7. Evidence status
8. Validation plan

## Key Example

Team says: "build a notification system."

Three alternative framings that surface:
- **A:** Users don't know when context changed → state-change indicators, activity feeds
- **B:** Users don't trust the system → status visibility, audit trails, confidence signals
- **C:** Users want to delegate watching → subscriptions, agent-driven alerts

None of those are "a notification system." The team's brief folded all three into one feature spec.

## Why AI > Human for This

Under time pressure, humans skip sections 3 (assumption challenges), 5 (alternative framings), and 6 (draft message). AI runs all 8 every time. 90 seconds vs an hour.

## Reverse Use: Idea Triage

The bottleneck is triage capacity, not idea generation. Ran across 50 backlog ideas → 90% died at evidence status → 3-5 survived → 1 pitched with evidence pack assembled.

This pattern generalizes beyond PM: any time a stakeholder proposes a specific technical change, decompress before executing.
