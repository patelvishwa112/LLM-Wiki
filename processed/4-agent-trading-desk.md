---
tags: ["trading", "agents", "agent-orchestration", "horizon", "risk-management", "backtesting"]
source: https://x.com/zodchiii/status/2063919809281110474
date: 2026-06-08
type: bookmark
author: zodchiii
summary: "4-agent trading desk architecture: Hunter scans for setups, Analyst validates with backtests and risk metrics via Horizon, Executor places orders, Monitor watches positions with kill switches and alerts. Build order: Analyst+Executor first, then Monitor, then Hunter. Total cost under $100/month."
raw: "[[raw/zodchiii_2063919809281110474]]"
---

# How to build a 4-agent trading desk that finds and trades opportunities while you sleep

darkzodchi's blueprint for an autonomous trading system.

## The Four Agents
1. **Hunter** — Scans news, sentiment, technicals, macro events; outputs 5-15 setups/day.
2. **Analyst** — Backtests (5+ years), Sharpe, drawdown, correlation, risk/reward via Horizon.
3. **Executor** — Places trades (Alpaca, Binance, etc.) with position sizing.
4. **Monitor** — Real-time P&L alerts, break-even stops, daily loss limits, anomaly detection.

## Key Principle
Separation of concerns + verification at every handoff. The expensive part is not the model — it's making sure the loop doesn't blow up your account at 3 a.m.

Relevant to agent orchestration, risk management, and production agent systems.