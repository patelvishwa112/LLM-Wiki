---
tags: ["gtm", "sales", "loop-engineering", "agents", "codex", "evals", "self-improvement", "karpathy", "agent-harness", "human-in-the-loop", "outbound", "productivity"]
source: https://x.com/nifinet/status/2078851409068654639
date: 2026-07-19
type: bookmark
description: "Nicolas Finet applies Karpathy cheap-metric agent loops to outbound: versioned scoring/plays, outcome memory, eval gate, human-merge PRs."
author: nifinet
summary: "Nicolas Finet applies Karpathy cheap-metric agent loops to outbound: versioned scoring/plays, outcome memory, eval gate, human-merge PRs."
raw: "[[raw/nifinet_2078851409068654639]]"
---

# GTM as versioned code — outbound Karpathy loop

**Nicolas Finet (@nifinet)** — long-form blueprint for turning outbound/GTM into self-improving, file-backed code, with Codex as the weekly improver and a product CTA for yourmax.ai.

## Thesis

Karpathy: any metric you can evaluate cheaply can go to an agent swarm. **Reply rate** is cheap enough. Build **two loops**:

1. **Inner (execution):** sense market → score account → write from signal → check message → log outcome → learn from reply.
2. **Outer (meta):** Codex reads last week’s outcomes, edits scoring/play files, runs eval, opens PR with evidence + score. **Sending and merging stay human.**

Framing: **GTM as versioned code that improves from the market.**

## Repo shape (offline-first)

| Path | Role |
|------|------|
| `AGENTS.md` | Law — narrow scope before anything else |
| `config/scoring.yaml` | Visible judgment (signals/weights) |
| `prompts/` + `config/plays.yaml` | Message plays |
| `memory/outcomes.jsonl` | Touch outcomes + **reason** field |
| `evals/score.py` + fixtures | Gate improver cannot talk past |

Prove improvement on local files before CRM/delivery wiring.

## Eight-step build (compressed)

1. **Law first** — job is: read outcomes, one file change, prove help, wait. Operational short `AGENTS.md`, not a compliance TOC.
2. **Judgment in config** — ~5 signals; argue with lines, not buried Python. Avoid junk-drawer overfitting.
3. **Outcomes as memory** — write when outcome lands; rich reasons beat `no_reply`. Validate log before improver.
4. **Eval gate** — fixtures include ugly misses; one number + inspectable fails. Example: baseline failed intentional “should draft” case → useful.
5. **One scoring change** — reject story-driven weight bumps that don’t fix known misses; prefer one boring line + outcome-backed reason.
6. **Prompt lane separate** — don’t mix scoring + copy in one PR; small banned_lines / structure fixes; taste-needed copy stays review-marked.
7. **PR control layer** — human merge; never auto-merge “because friction.”
8. **Weekly cadence** — not after every reply (overfit); first tune-ups manual until proposals are boring.

## What good looks like vs breaks

Good: weekly small PR, evidence + eval, stranger can read outcomes.jsonl after a week. Breaks: Friday memory backfill, multi-concept diffs, fixtures of only wins, unreviewed PR pile, auto-merge, delivery before improvement-loop proof.

## Skeptical read

Ends with **yourmax.ai** managed product pitch and “DM for full repo.” Pattern value stands without the product: file-visible policy, outcome memory, hard eval, human gate — same lit-factory / back-pressure instincts as software-factory writing. Treat clone-and-run claims and managed “same system” as marketing until repo is public.

## Why it matters

Concrete transfer of Autoresearch/Karpathy swarm thinking from training metrics to **GTM playbooks**, with disciplined outer-loop design (one concept, eval gate, no send/merge automation). Pair with vault notes on self-improving systems and software factories (dark vs lit).

## Related

- [[karpathys-autoresearch-is-changing-how-campaigns-g]]
- [[anthropic-gtm-claude-code-workflows]]
- [[software-factories-light-and-dark-addy-osmani]]
- [[self-improving-ai-native-company-deel-bug-loop-westgarth]]
- [[fable-5-self-improving-system-14-steps]]
- [[continual-learning-replit-agent-vibench]]
- [[improving-agents-data-mining-traces]]
- [[how-to-create-loops-claude-code-sairahul1]]
- [[addy-osmani-agent-autonomy-ladder-six-levels]]
- [[human-in-the-loop-agent-loops]]
