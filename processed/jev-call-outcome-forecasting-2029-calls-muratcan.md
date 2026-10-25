---
title: "2,029 Real Calls, Zero-Shot Turn-Level Forecasting with Jev"
type: bookmark
description: "Muratcan Koylan's production experiment: structural-only call traces fed to Jev for 38,012 turn-level booking forecasts at 118 ms median, AUC 0.78 and 94% ranking by call end, $3 total."
tags: [evals, observability, production, trace-data, inference, models]
source: https://x.com/muratcan/status/2104959648482701686
date: 2026-09-29
author: Muratcan Koylan
summary: "Muratcan Koylan's production experiment: structural-only call traces fed to Jev for 38,012 turn-level booking forecasts at 118 ms median, AUC 0.78 and 94% ranking by call end, $3 total."
raw: "[[raw/muratcan_2104959648482701686]]"
---

# 2,029 Real Calls, Zero-Shot Turn-Level Forecasting with Jev

**Source:** Muratcan Koylan (@muratcan), 2026-09-29. A video-plus-text post reporting a zero-shot experiment running Jev over his team's AI receptionist call logs.

The setup deliberately removes language. Two thousand twenty-nine real phone calls from an AI receptionist were reduced to structure only — meaning turns, tool calls, workflow stages, timing — with no transcripts or audio, so the model never saw a word of speech. Jev then made 38,012 turn-level forecasts about what would happen next in each call, from the state of the call so far, and every completed call was graded against what actually happened in the EHR (booked or not booked).

Operationally it looks like a live scoring layer rather than a batch analysis: 118 ms median latency per forecast, and a retrospective pass that asked five typed questions of each call and returned 10,145 answers in 26 seconds with 256 requests in flight. The whole evaluation cost $3. No fine-tuning, no examples from their data — the discrimination is zero-shot.

Quality rose with call progress, which is the expected shape for a state-based predictor: by roughly the halfway point AUC was 0.78, and near the end of a call Jev ranked calls correctly 94% of the time. Koylan's own caveat is that Jev over-weighted visible errors that the receptionist agent usually recovers from, so some of the apparent risk is noise the workflow already handles.

## Why it matters

This is a template for evaluating an agent without reading its transcripts: serialize the trace as state, ask a cheap classifier-model for the outcome you care about at each step, and join to ground truth in the system of record. At $3 per 2,029 calls and ~100 ms per decision, this is cheap enough to run continuously in production as an early-warning signal — booking probability dropping mid-call, or a workflow stage stalling — rather than as a quarterly eval.

## Key points

- 2,029 real AI-receptionist calls, structure only (turns, tool calls, workflow stage, timing); no transcripts or audio.
- 38,012 turn-level forecasts at 118 ms median latency.
- 5 typed questions per call → 10,145 answers in 26 seconds, 256 requests in flight.
- Zero-shot: no fine-tuning, no in-domain examples; scored against EHR outcomes.
- AUC 0.78 by the halfway point of a call; 94% correct ranking near the end.
- Total cost for the experiment: $3.
- Failure mode: over-focus on visible errors that the agent typically recovers from, i.e. false alarms from recoverable states.

## Related

- [[continual-learning-replit-agent-vibench]]
- [[improving-agents-data-mining-traces]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[trace-turn-level-reward-credit-assignment-agents]]
- [[continuous-trace-intelligence-braintrust-topics]]
