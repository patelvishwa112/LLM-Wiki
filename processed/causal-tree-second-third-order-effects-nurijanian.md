---
title: "/causal-tree: see ahead with 2nd/3rd order effects of decisions"
tags: [pm, decision-making, product-discovery, skills, claude-code, ai-pm-os, causal-reasoning, risk, second-order-effects, productivity]
source: https://x.com/nurijanian/status/2082065077021335632
date: 2026-07-28
published: 2026-07-28
authors: ["@nurijanian"]
type: bookmark
description: "Root-cause alone is incomplete — causal-tree maps backward whys plus five-order forward effects, evidence gaps, and assumptions for team review."
summary: "Root-cause alone is incomplete — causal-tree maps backward whys plus five-order forward effects, evidence gaps, and assumptions for team review."
author: nurijanian
raw: "[[raw/nurijanian_2082065077021335632]]"
---

# /causal-tree: see ahead with 2nd/3rd order effects of decisions

@nurijanian (George / prodmgmt.world): root-cause analysis explains **why** a problem may exist but not the **consequences** of the fix. Teams can “solve” a likely cause and create a new limit elsewhere. Before committing, map the **full causal chain** — past causes, future effects, and the assumptions linking them — so other PMs can stress-test the logic.

## Method

### 1. Work backward from the open question
- Put the product question at the top.
- Chain “why” **≥5 levels**; stop when the next why doesn’t deepen the cause.
- **Branch** when multiple causes fit (one neat chain favors a single story).
- Treat endpoints as root-cause **candidates**.
- Attach **evidence** on every link; mark missing sources, challenged claims, unknown ties.

### 2. Trace the proposed action forward
- Place the action beside the chain.
- First-order effect → next → through **five orders**.
- Add **helpful and harmful** branches (relief here may create a limit there or weaken the expected win).
- Forward pass is for **inspection**, not a forecast.

### Map shape

```
Open question
→ backward why-chain
→ root-cause candidates
→ evidence and gaps on uncertain links
Proposed action
→ 1st … 5th-order consequences
→ positive and negative branches
```

Backward = why the problem may exist. Forward = what the action may cause. Final review tests assumptions that join them.

### 3. Test every link
- Write the **belief** behind each link.
- Add a **second plausible cause**.
- Note **facts that would change your mind**.
- Check reverse causality, common factors, false precision; don’t treat a likely sequence as proof.

### 4. Show where you are guessing
- Mark AI-generated branches as guesses.
- Keep unsupported links and alternatives visible.
- Use the map to pick **which links to test**.

AI can extend chains and list beliefs; the PM supplies product context and **owns every claim**.

## Why It Matters

Pairs with Why/What/How issue trees: Why-tree finds causes; **causal-tree** adds second-order risk before How-style action. Turns private PM confidence into a reviewable assumption surface — same spirit as decision memos and structure-problem.

## Skeptical read

Pitch: `causal-tree` skill in **AI PM OS** (243 skills, Claude Code/Cowork/Cursor, $499/yr ≤10 PMs). Framework stands without the product. Depth-5 chains can become cargo-cult if evidence marks stay empty.

## Source

[/causal-tree — @nurijanian](https://x.com/nurijanian/status/2082065077021335632)

## Related

- [[mckinsey-issue-tree-why-what-how-nurijanian]]
- [[structure-problem-top-down-bottom-up-decision-memo]]
- [[opportunity-ai-pm-os-workflow]]
- [[problem-first-skill-invert-bad-ideas]]
- [[ambient-pm-agents-evidence-first-prd]]
- [[bezos-writing-framework-six-page-memos-dickiebush]]
