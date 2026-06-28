---
title: How to Read Any Company With AI Like an Analyst
tags:
- finance
- agents
- mcp
- coding-tools
- investing
- crypto
- analysis
source: https://x.com/gemchange_ltd/status/2060757358297469365
date: 2026-06-01
published: 2026-05-30
authors:
- '@gemchange_ltd'
type: bookmark
raw: '[[raw/x_gemchange_ltd_how-to-read-company-ai-analyst]]'
description: How to Read Any Company With AI Like an Analyst
---

# How to Read Any Company With AI Like an Analyst

## Key Takeaways

- Full pipeline for AI-powered company analysis: EDGAR data → forensic screening (Beneish M, Altman Z, Sloan accruals, Piotroski F) → year-over-year risk factor diff with Claude → synthesis memo
- **edgartools** is the killer Python library — parses all SEC filings into clean objects, ships an MCP server so Claude can query real filings instead of hallucinating numbers
- Year-over-year Risk Factors diff is the single highest-signal AI read on a company — new/deleted language reveals what lawyers are scared of, which never hits press releases
- Crypto equivalent: DefiLlama (free API) for on-chain financials, unlock schedules + holder concentration as the crypto forensic screen, Arkham for free wallet de-anonymization
- Complete working Python script included (~200 lines): `forensic_screener.py` — ticker in, all 4 forensic scores out, optional Claude-powered risk factor diff
- The model isn't the moat — wiring it to clean, verified, source-linked data with disciplined math is the moat
- Open source stack recommendations: FinanceToolkit (150+ ratios), ai-hedge-fund (agent orchestration reference), OpenBB (Bloomberg terminal), edgar-crawler (section extraction)

## Tools & Repos Mentioned

| Tool | Purpose | Cost |
|------|---------|------|
| edgartools | SEC filing parser + MCP server | Free |
| FinanceToolkit | 150+ financial ratios (Beneish, Altman, etc.) | Free |
| DefiLlama | Crypto protocol financials | Free API |
| Arkham | Wallet de-anonymization | Free for individuals |
| Dune | Community SQL dashboards | Free tier |
| Hudson Labs | Automated red flag extraction | ~$100/mo |
| Fintool | AI-first equity analysis | Mid-tier |
| Nansen | Smart money tracking | ~$49/mo |
| Token Terminal | Standardized crypto financials | ~$350/mo |
| AlphaSense | Institutional research + Tegus interviews | $15-20K/seat |

## Why This Matters

- Directly applicable to your investing workflow — the forensic screening + risk factor diff pipeline can be wired into Hermes as an MCP server or cron job
- edgartools MCP server is a concrete pattern for how to give Claude access to verified financial data
- The "diff this year vs last year" AI prompt pattern is brilliant and reusable beyond finance
- Aligns with your macro/investing focus and technical skills — you could build the L5 screener as a Hermes tool
- The ai-hedge-fund repo is worth studying as a reference for multi-agent orchestration (data-fetcher → screener → reasoner)

## Summary

@gemchange_ltd presents a full-stack guide to reading companies with AI, structured in layers: L0 (SEC EDGAR data via edgartools), L1 (forensic math — Beneish M-Score, Altman Z, Sloan accruals, Piotroski F), L2 (AI-powered year-over-year risk factor diffing), L3 (crypto equivalent with DefiLlama, unlock schedules, holder concentration), L4 (orchestration systems like ai-hedge-fund, OpenBB), and L5 (complete working Python script). The core insight: the model isn't the moat — clean verified data + disciplined math is. The article went viral (275K views, 609 bookmarks) for good reason.

## Source

[X Article by @gemchange_ltd](https://x.com/gemchange_ltd/status/2060757358297469365)
