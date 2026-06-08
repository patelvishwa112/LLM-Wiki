---
tags: ["agents", "trading", "multi-agent", "orchestration", "automation", "finance"]
source: https://x.com/zodchiii/status/2063919809281110474
date: 2026-06-08
type: bookmark
author: zodchiii
title: "How to build a 4-agent trading desk that finds and trades opportunities while you sleep"
summary: "A practical guide to building a 4-agent trading system: Hunter (scans), Analyst (validates), Executor (places trades), Monitor (babysits). Under $100/month total cost."
raw: "[[raw/zodchiii_2063919809281110474]]"
related: ["[[wtf-is-a-loop]]", "[[rlm-structured-outputs]]"]
---

# 4-Agent Trading Desk

## Key Takeaways

1. **Separation of concerns is the architecture.** Four agents, one job each: Hunter scans, Analyst validates, Executor places, Monitor babysits. Skip any one and the system breaks in a specific, predictable way.

2. **Common failure modes map to missing agents.** Hunter-only = emotional manual trading. No Analyst = blind execution. No Monitor = catastrophic overnight loss.

3. **The Analyst is where 90% of homemade setups die.** Building a proper backtest engine with 5+ years of data, Sharpe ratios, drawdown analysis, and correlation checks takes 2-3 months of coding solo. Horizon productizes this layer.

4. **Build order matters.** Analyst + Executor first (paper trade), Monitor second (safety net), Hunter last (by then you know what passes filters).

5. **Under $100/month total.** Claude API ($30-60), cloud server ($5-15), broker accounts (free). Hedge fund equivalent: $50K/month.

## Architecture Pattern

This is the same multi-agent pipeline pattern appearing across domains:
- **Trading:** Hunter → Analyst → Executor → Monitor
- **Code review:** Lint → Test → Review → Merge (roborev pattern)
- **RLM subagents:** Scan → Filter → Aggregate → Validate
- **Loop orchestration:** Dispatch → Execute → Verify → Retry/Complete

The handoff between agents is what makes the system work. Each agent has exactly one job. Contracts between them are critical (see [[rlm-structured-outputs]] for structured output validation).

## Cost Consciousness

The cost stack mirrors the loop discourse (see [[wtf-is-a-loop]]): the expensive resource is no longer the model call but the orchestration. Capping iterations, detecting no-progress, and budget ceilings are universal guardrails.
