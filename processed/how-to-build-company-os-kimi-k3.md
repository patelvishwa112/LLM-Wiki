---
tags:
- agents
- agent-harness
- harness-engineering
- multi-agent
- kimi
- kimi-k3
- company-os
- human-in-the-loop
- verification
- orchestration
- agent-ops
- enterprise
- state-management
source: https://x.com/av1dlive/status/2079607748396994789
date: 2026-07-28
type: bookmark
author: Avid (@Av1dlive)
raw: "[[raw/av1dlive_2079607748396994789]]"
description: "Nine-element Company OS guide (vocab, world, store, heartbeat, memory, cockpit, gate, CLI, fenced runtime) built with Kimi K3"
summary: "Avid's builder guide treats multi-agent ops as a company OS — six always-on questions and nine required elements, each with a generalized coding-agent prompt and a check — not a nicer chat UI."
---

# How to Build a Company OS using Kimi K3 (Builder's Guide)

## Key takeaways

- **A company OS is not a chat skin.** It is continuous answers to six operator questions: who owns what, which goals matter, what is blocked, how fast money is burning, what is waiting on your yes, and what happened while you were gone. Fewer than six is a demo.
- **Nine required elements (in order):** vocabulary (7 nouns) → seeded world → single source of truth (store + pure reducer) → heartbeat → domain memory (hydrate-before-write) → operator cockpit → approval gate → deterministic command line → fenced real agent runtime.
- **Three governing principles:** (1) a company is state (one typed tree; screens are windows); (2) power flows through gates (spend/hire/ship/fire queue for explicit yes; failed checks → "Override and approve"); (3) what is not written down did not happen (append-only log).
- **Method over repo:** reference is meridian-company-os (React 19 + TS + Vite, MIT). Do not copy files — take principle + prompt + check; regenerate with your agent. Loop: write prompt → `kimi -p` → run check; fix the prompt, never hand-patch the file.
- **Kimi K3 as worker tier:** open-weight MoE used for eight of nine builds; reducer escalated to a frontier model. Skills: Superpowers (planning/review), Context7 (version-accurate docs). Cheap agentic coding + open weights is the pick for all-day agent runtime, not peak closed benchmarks alone.
- **Runtime fence is the feature:** concurrency one (HTTP 409), 8k input cap, 180s kill timer, isolated workdir, zero credential leakage, bind 127.0.0.1, degrade to sim if CLI missing.
- **Rollout weeks:** observe sim → gate + commands → connect real runtime and attack the fences → one real agent/task/budget with zero unexpected spend.

## Summary

Long-form X Article (~4.5k words) from @Av1dlive on building an operating structure around cheap coding agents. Thesis: agents that spend, ship, and hire are a company; chat-window tooling is the wrong control surface. Each of nine builds ships a stack-agnostic prompt, what the reference produced (types, seed, ~1.4k-line reducer, 2.6s tick, Approvals inbox, regex CLI, local Kimi bridge), and a concrete check (typecheck, dual-boot seed, three cockpit questions in under ten seconds, fence attacks, etc.).

**Seven domain nouns:** Actor, Goal, Task, Approval/Decision, Ledger, Log/Event, Company — closed status unions; money/tokens as numbers. **Gate law lives in the reducer**, not only UI. **Deterministic commands first**, model only as fallback. Closing challenge: name the seven nouns of *your* company and which two you almost merged.

Reference: https://github.com/codejunkie99/meridian-company-os (`prompts/` per element). Same author as the earlier swarm guide.

## Skeptical read

- Reference UI is a React dashboard over simulated spend; Week 4 "real money" is aspirational relative to most solo agent setups.
- Benchmark/cost claims for K3 vs Fable/Sol age quickly — treat as July 2026 snapshot.
- Repo/CTA is the delivery vehicle; the durable value is the nine-element checklist and checks, not Meridian branding.

## Related

- [[how-to-build-ai-agent-swarms]]
- [[sierra-pinecone-singular-company-agent]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[own-your-intelligence-harrison-chase]]
- [[learn-harness-engineering]]
- [[the-great-flattening-tokenmaxx-vorflux-myprasanna]]
- [[software-factory-linear-claude-cloud-routines]]
- [[software-factories-light-and-dark-addy-osmani]]
