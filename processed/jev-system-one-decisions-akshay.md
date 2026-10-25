---
title: "Jev Clearly Explained: System One Decisions Instead of Chat"
type: bookmark
description: "TypeSafe's Jev as a semantic decision engine: typed Choice/Score/Noul outputs, calibrated probabilities, 70-500ms and $0.042/M input tokens."
tags: [agents, structured-outputs, routing, cost-optimization, inference, calibration]
source: https://x.com/akshay_pachaar/status/2101037514945597645
date: 2026-09-18
author: Akshay 🚀
summary: "TypeSafe's Jev as a semantic decision engine: typed Choice/Score/Noul outputs, calibrated probabilities, 70-500ms and $0.042/M input tokens."
raw: "[[raw/akshay_pachaar_2101037514945597645]]"
---

# Jev Clearly Explained: System One Decisions Instead of Chat

**Source:** Akshay 🚀, 2026-09-18. A long explainer on Jev, the "System One" decision model released by TypeSafe AI on September 15, 2026, including an unusually candid section on where the marketing overreaches.

Jev's premise is that most software judgments — is this ticket urgent, which model should handle this request, is this shell command dangerous, does this passage answer the question — have a known, small answer space. Sending them to a generative model means paying for sequential token generation, then parsing and validating the output: workable, but structurally wasteful for a five-way choice. Jev instead takes state (text or JSON) plus a list of declared questions and returns typed answers with probabilities. Three primitives cover the space: Choice picks from a list you define, Score places input on an ordered scale, Noul is the boolean (probability between 0 and 1). Questions in one request are evaluated in parallel, so the code can ask every independent question about the same state once instead of chaining calls.

The design keeps branching in ordinary code — the "smart switch statement" framing is accurate, not dismissive. The model supplies fuzzy judgment; the program owns control flow and thresholds. Probabilities are the point: a billing-vs-technical result that barely favors billing should not auto-route, so high confidence acts, medium confidence escalates to a stronger model or asks for confirmation, low confidence goes to a human. TypeSafe trains for this with RLCD (Reinforcement Learning for Calibrated Decisions), targeting confidence that matches accuracy across many predictions. Reported performance is 70–500 ms end-to-end and $0.042 per million input tokens with output free, with headline claims of roughly 200× faster and 400× cheaper positioned by the author as a ceiling from vendor-run workflow evals rather than a promise.

The honest limits are the most useful part. "Jev cannot hallucinate" only means it cannot emit an option outside the schema or malformed prose — it can confidently pick the wrong valid option, which can still refund the wrong customer or approve a destructive command. It cannot write, summarize, or explain; it is unreliable for arithmetic, counting, date comparison, and exact string work; it struggles when the decision hides several reasoning steps; it cannot extract unknown values, so candidates must be found first; and irrelevant context degrades accuracy. Weights are closed, input is text-only, and independent calibration data is scarce. If deterministic code already solves the problem, the if-statement wins.

## Why it matters

This is the clearest articulation so far of a split that agent builders keep rediscovering: generative models for plan, prose, and code; a small calibrated classifier for the high-frequency judgments wrapped around them — model routing, tool-risk gating, verification, retrieval reranking. The economics change what is worth doing at all: a judgment too expensive to run on every row can move into the normal data pipeline, and a per-tool-call gate becomes affordable. The probability interface is the operational detail that matters, since confidence tiers turn a classifier into a policy with reviewable thresholds.

## Key points

- Released September 15, 2026 by TypeSafe AI; purpose-built for bounded decisions, not generation.
- Three output primitives: Choice (option + distribution), Score (ordered scale), Noul (boolean probability).
- All questions in a request are evaluated in parallel; code owns branching, model supplies judgment.
- Reported 70–500 ms latency and $0.042 per million input tokens, output free; ~200× faster / 400× cheaper claims are vendor-eval ceilings.
- Trained with RLCD so that a 90% confidence answer is right about 90% of the time; thresholds belong in versioned code.
- Hallucination claim is narrow: schema cannot be violated, but a schema-valid wrong answer is still possible.
- Best-fit uses: support triage, model routing, tool-risk gating (read-only / reversible / destructive), retrieval reranking, prompt-injection screening, high-volume labeling.
- Wrong-fit: open-ended answers, arithmetic, counting, date comparison, multi-step hidden reasoning, unknown-value extraction.
- Rollout pattern: one bounded decision → rubric written first → shadow mode → accuracy-vs-confidence plot → automate the safest branch → version the questions like code.

## Related

- [[rlm-structured-outputs]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[twenty-core-agent-concepts-sairahul1]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
