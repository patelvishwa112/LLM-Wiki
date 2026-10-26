---
tags:
  - code-review
  - claude-code
  - anthropic
  - evals
  - verification
  - ci-cd
  - feature-flags
  - agent-harness
  - code-quality
  - agent-ops
source: https://x.com/addyosmani/status/2114604912520921136
date: 2026-10-26
author: Addy Osmani (@addyosmani)
type: bookmark
description: "How the Claude Code team reviews code when Claude writes ~90%: six blocking layers plus rollback — pre-PR proof, multi-agent AI review, security gate, CI, risk-scaled human approval, merge queue — with incidents as the eval set."
summary: "Code review at agent volume: replace 'did someone read it?' with 'what could go wrong and which check catches it' — automate most reading, gate on blast radius, keep humans for taste, dangerous code, architecture and accountability."
raw: "[[raw/addyosmani_2114604912520921136]]"
status: current
as_of: 2026-10-26
---

# How the Claude Code Team Does Code Review

Addy Osmani's account of the Claude Code team's review process, where Claude writes roughly **90% of the code**. The numbers are the argument:

- Merged PRs more than **doubled** June → September, while the share of PRs that had to be reverted **fell by more than 40%**.
- Their monorepo went from ~2,500 changes/day in May to **30,000/day** in September.
- Since the Code Review research preview, the share of internal PRs receiving substantive review comments went from **16% → 54%**.

## The reframe

They replaced "did someone read the code?" with: **"what could go wrong with this change, and what check — automated or human — is the right one to catch it?"** Review stops being a gate after the fact and becomes a spellcheck you run while writing. Most changes are already reviewed and corrected by Claude once before a human looks.

They also treat **human time as a dual-sided cost**: review time *plus* the time spent fixing bugs that bad code introduces. Cutting the first while raising the second is not a win.

## The six layers (+ rollback)

1. **Pre-PR verification** — ask for a runnable result (tests, build, screenshot diff vs design), then a subagent reviews the diff with fresh context. Plus internal skills: bug hunting, diff reduction, e2e validation, UI-vs-design check. Boris Cherny's estimate: a verification process improves Claude's output quality 2–3×.
2. **AI review on every PR** — the diff is read against the whole codebase and the stated intent; for bug fixes it hunts the root cause. Findings are vetted by **multiple parallel agents plus a vote** to kill false positives; style/diagnostic nits are filtered (A/B tested). Findings are labeled Important / Nit / Pre-existing, and every thread must be fixed or resolved with a reason — often an agent fixes it overnight.
3. **Security review that can block** — an open finding blocks merge; auto-closes when a later commit fixes it.
4. **Automated checks that block** — lint, type checks, tests on all platforms, build; PR template asks how it was tested and how to revert (the author owns those answers, not Claude).
5. **Human approval scaled by risk** — a **classifier assigns risk by the change, not the author**; some paths always need a second approval (owner-marked sensitive files, CI workflows). Trusted repo owners get relaxed paths. **Agent approvals never count as human approval**, the operator of an agent-authored PR is always a required reviewer, and approval is only valid for one commit.
6. **Merge queue, feature flags, staged rollout** — checks run on main with the change applied; new features go to employees first, then latest channel, then stable.
7. **Fast feedback and rollback** — weekly on-call; every incident review asks *which layer should have caught this*.

## Making the reviewer better

Their **incident set is the eval set**: collect PRs that caused incidents, their fix-forwards and reverts, have engineers verify location and correctness, and score the review system against that collection **daily**. Noise is measured by what humans do with each comment (fixed, rejected, intentional, didn't matter). Any change to prompts, tools or model requires rescoring. Not yet built: circuit breakers that tighten approvals automatically.

## What humans are still for

Whether to build it at all (vision, taste, goals); auditing dangerous code (billing, auto-updater, CI workflows); architecture review, which sets conventions; verifying proofs — "if you can't describe what the checks would miss, don't ask for a 👍"; and taking responsibility. "You land it, you own it" holds because changes are small, everything is revertible, and blast radius sets the review bar.

On shared understanding — the second purpose of review — they have no formal mechanism. When someone needs to learn a slice of the codebase they ask Claude for a fresh explainer (sometimes a visual artifact) rather than reading trivial diffs. Open channels substitute for diff-reading as ambient awareness.

## Implementation checklist (their short version)

Before the PR: checklist in a short `CLAUDE.md`; formatters/linters via hooks; `/code-review` + `/security-review`; a `REVIEW.md` tracking recurring issues. On every PR: enforce CI; PR template with Testing / Risk / How to revert; one repo first with an AI reviewer, iterate `REVIEW.md` a few weeks; automated security review; all threads resolved. Approval: risk levels set by change; lenient paths only for trusted authors; dismiss approvals on new commits; humans required for auth, billing, CI, release, installers. Merging: merge queue, feature flags, internal-first staged rollout, one-step revert. Post-merge: log incidents/reverts as evals, track human effort.

## Verdict

The best-evidenced description of review at agent volume I have — it is the operational version of [[eval-engineering-merge-gate-hanakoxbt]] and the missing "after the code is written" half of [[why-harness-engineering-is-so-hard-winterarc]]. Two things to steal regardless of team size: **(1) convert every revert and incident into a permanent eval case, (2) gate on blast radius, never on lines read.** Caveats: Anthropic-scale tooling (classifiers, multi-agent voting, merge queue) is not free, and the 90% figure is about their own product, so the revert-rate drop is the number that actually carries the argument.

## Related

- [[eval-engineering-merge-gate-hanakoxbt]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[ai-velocity-pod-senior-engineer-agents-mardehaym]]
- [[software-factories-light-and-dark-addy-osmani]]
- [[addy-osmani-agent-skills-open-source]]
- [[agent-workflows-silent-degradation-verification-vladic]]
