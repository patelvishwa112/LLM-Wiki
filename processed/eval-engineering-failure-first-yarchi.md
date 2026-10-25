---
title: Eval engineering, explained from failures up
type: bookmark
description: "Yarchi's five-step recipe for eval engineering: mine 100 real failures into 3-4 types, put code checks before model judges, keep each judge binary, and validate it against your own labels."
tags: [evals, llm-judges, rubrics, agents, verification]
source: https://x.com/undefinedKi/status/2099590541650378856
date: 2026-09-14
author: Yarchi
summary: "Yarchi's five-step recipe for eval engineering: mine 100 real failures into 3-4 types, put code checks before model judges, keep each judge binary, and validate it against your own labels."
raw: "[[raw/undefinedKi_2099590541650378856]]"
---

# Eval engineering, explained from failures up

**Source:** Yarchi, 2026-09-14. A short explanatory thread on building an eval suite, quote-tweeting Viv Trivedy's release of an Eval Engineering Skill.

Yarchi's framing is the useful part: the model does the work, but a human still decides what counts as right, and every such decision is a place the agent cannot run without you. Eval engineering is writing "right" down so a machine can check it instead — the thing that tells you whether a prompt edit or a model swap broke something.

The build order is failure-first rather than rubric-first. Pull a hundred real failed runs, read them by hand, describe each failure in your own words, then cluster the descriptions; three or four types will cover most of it, and they are rarely the ones you predicted. This is Yarchi's explanation for why generic judges fail, illustrated with Hamel Husain's example of a "helpfulness" judge that passed an answer wiring a bathroom to the wrong room — the rubric measured tone and missed reference.

Checks come in two layers, cheapest first. Code handles anything deterministic — does it parse, does it compile, is the field present, does the number have a source — because code is free and returns the same verdict every time. A model judge is reserved for what code cannot cover, and each judge decides exactly one thing, answered yes or no rather than on a one-to-five scale. Before trusting a judge, feed it examples you labelled yourself; if it disagrees with you, fix the rubric rather than the agent. Two or three code checks plus one or two model checks is described as a complete suite.

## Why it matters

This is the smallest viable on-ramp to evals for teams that keep shipping prompt and model changes with no regression signal, and it inverts the common failure mode of inventing metrics before reading failures. The binary-judge rule is the operational payoff: one decision per judge and yes/no outputs make disagreement with your own labels actionable, which is what turns a judge into a regression gate rather than a scoreboard.

## Key points

- Eval engineering = writing down what "right" means so a machine can check it, removing the human from the loop's critical path.
- Start from ~100 real failed runs read by hand; cluster into 3-4 failure types.
- Expected failure types are usually not the actual ones, which is why generic judges miss.
- Hamel Husain's example: a "helpfulness" judge passed an answer that connected a bathroom to the wrong place.
- Layer 1 is code: parses, compiles, field present, number has a source.
- Layer 2 is a model judge, only for what code cannot check; one decision per judge, binary not 1-5.
- Validate the judge on self-labelled examples; disagreement means fixing the rubric, not the agent.
- Suite size: 2-3 code checks plus 1-2 model checks.

## Related

- [[eval-engineering-merge-gate-hanakoxbt]]
- [[agent-evals-practical-guide]]
- [[how-to-build-eval-set-you-can-maintain-lotte]]
- [[do-automated-evals-work-parlance-labs]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
