---
tags:
  - evals
  - agents
  - langchain
  - harbor
  - skills
  - rlvr
  - harness-engineering
source: https://x.com/vtrivedy10/status/2092266609838604368
date: 2026-08-25
type: bookmark
author: vtrivedy10
description: "LangChain Labs — two-step pipeline for agent evals: world spec plus task specs in markdown, then Spec2Task into Harbor; human review stays on specs, not code."
summary: "LangChain Labs — two-step pipeline for agent evals: world spec plus task specs in markdown, then Spec2Task into Harbor; human review stays on specs, not code."
raw: "[[raw/vtrivedy10_2092266609838604368]]"
published: 2026-08-25
---

# How we Build Agent Environments & Tasks

Viv Trivedy (@Vtrivedy10), LangChain Labs, with @hwchase17, @nickhollon10, @ArjunNargolwala. Aug 25 2026. Packaged as an `eval-engineering` skill.

## Glossary (their terms)

Task = input + environment + test script/rubric. Dataset = collection of tasks. Harbor = task/eval framework. Traces = agent trajectories. **Task spec** = markdown describing one task. **World spec** = shared project knowledge used to write specs or turn specs into tasks.

## Why a spec

Building one representative task is expensive. Split “what should this task be?” (human-heavy) from “build the Harbor task” (agent-automatable). Specs are the review surface — markdown, not raw env code. Version like code.

Pipeline: Spec generation → Spec2Task.

## World spec

Not task-specific. Lives across the dataset: schemas, mock APIs (Salesforce/Notion), trace parsers, rubric conventions (programmatic vs LLM-as-judge), synthetic-data scripts, common user questions mined from traces.

Best way to get it: pair with a coding agent on the **first 1–3 tasks**, then have it write what it learned as a world-spec skill. The eval-engineering skill does both.

Agent work while bootstrapping: scan repo (prompts/tools/skills), cluster traces, decide live vs mock APIs, catalog schemas, plan synthetic data.

Examples: GTM (mock Salesforce, missing-data lookup), prompt-opt, code review from merged PRs, trace-mining (needles in a huge corpus).

## Spec2Task learnings

- Refine by running real agents and reading trajectories (catch leaky placeholders, over-specific instructions).
- Calibrate difficulty with model tiers (e.g. gpt-5.6-Luna vs Sol). If a strong model reward-hacks, the task is broken.
- Agents pick bad data generators — give them rules: LLM+rubric for free text, sqlite+schema scripts for tables.

## End-to-end

1. eval-engineering + traces + repo → first task + world-spec skill
2. Human reviews the world spec
3. New thread: world spec + eval-engineering → second task (validates the skill)
4. Repeat until confident
5. Scale: mine last-N-days traces → many **specs** for human review
6. Spec2Task those in parallel

Humans still needed: (a) does the spec match the real domain, (b) agents default to easy tasks — calibrate via trajectories.

## Why it matters

Operationalizes Foody (“evals are the PRD”) and Ethayarajh (RLVR environments). Continuous: production data and models change; envs must too. Also answers cheap-model / simpler-prompt / bash-only harness questions.

## Skeptical read

LangChain selling Harbor + a skill. World spec can encode the team’s biases. “Agents create easy tasks” is the load-bearing failure mode — if calibration is skipped, you hill-climb a toy.

## Related

- [[era-of-evals-brendan-foody]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[aiesi-post-training-world-adaptation]]
- [[ai-native-sdlc-playbook]]
- [[harbor-rl-coding-environments]]
- [[writing-good-skills-measured-rulebook-aparna]]
