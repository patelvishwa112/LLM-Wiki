---
tags: ["agents", "meta-agents", "agent-harness", "shepherd", "reversible-execution", "kv-cache", "supervision", "stanford"]
source: https://x.com/_avichawla/status/2073746091795960237
date: 2026-07-05
type: bookmark
author: _avichawla
description: "Shepherd records agent runs as copy-on-write execution traces so meta-agents can fork, replay, and revert live sandbox+KV state—CooperBench 28.8%→54.7% with a supervisor; repo shepherd-agents/shepherd."
summary: "Shepherd records agent runs as copy-on-write execution traces so meta-agents can fork, replay, and revert live sandbox+KV state—CooperBench 28.8%→54.7% with a supervisor; repo shepherd-agents/shepherd."
raw: "[[raw/_avichawla_2073746091795960237]]"
---

# Shepherd — reversible agent execution traces

Avi Chawla’s writeup of **Shepherd** (Stanford; alpha, `shepherd-ai` on PyPI): treat long agent runs like **versioned execution**, not just chat logs.

## Problem

Long coding/research runs accumulate **live state** (filesystem, processes, packages, KV cache). A late mistake forces either expensive fix-forward or restart-from-scratch—with **non-deterministic** re-roll of early steps. Git restores files, not process memory or warm cache.

## Mechanism

- **Typed event trace** — each agent–environment step is a commit bundling **process + filesystem** (COW).
- **Fork/replay** from any commit restores real state; project claims **~5×** faster than `docker commit` and **>95%** KV reuse on unchanged prefixes.
- **Meta-agent supervisor** can revert before bad effects land; irreversible externals (email, charges) must be blocked upstream.

## Evidence called out

**CooperBench** pair-coding: supervisor lifted pass rate **28.8% → 54.7%**.

## Repo (user-linked)

https://github.com/shepherd-agents/shepherd — tasks as reviewable proposals (`select`/`discard`), docs at docs.shepherd-agents.ai, paper arXiv:2605.10913. Deeper README capture: [[raw/github_shepherd-agents_shepherd]].

## Why it matters

Infrastructure for **reliable multi-step agents** where harness engineering meets systems: complements self-repairing harness / regression-lock ideas (post references Akshay’s harness-drift thread).

## Related

- [[rl-agents-system-prompt-reward-function]]
- [[kv-caching-llms-clearly-explained-avichawla]]
- [[secure-automated-learning-loops-modal-claude-code]]
- [[agent-harness-engineering-agentforge]]
- [[designing-loops-with-fable-5]]