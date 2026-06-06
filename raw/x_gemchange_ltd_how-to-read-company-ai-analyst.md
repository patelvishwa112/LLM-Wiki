---
source_url: https://x.com/gemchange_ltd/status/2060757358297469365
title: "How to Read Any Company With AI Like an Analyst"
author: "@gemchange_ltd (gemchanger)"
published: 2026-05-30
ingested: 2026-06-01
sha256: 2ec0fc2098ba6d9a7d10a561ea605a6827b86bba55de8e5786e3b8b73503d83a
platform: X (Article)
tags: ["finance", "agents", "mcp", "coding-tools", "investing", "crypto"]
stats: "275K views, 609 bookmarks, 219 likes, 20 reposts"
---

# How to Read Any Company With AI Like an Analyst

By @gemchange_ltd | May 30, 2026 | 275K views, 609 bookmarks

## Content

Spring 1998, six MBA students at Cornell ran one equation on Enron's financials and got -1.89 back. The cutoff for "this company is probably cooking the books" is -2.22. Enron was past it. And again, these were students, not some forensic accounting shop.

They stuck the report up on the school website. The whole street still had Enron rated buy around then, and most of them kept it there until a few weeks before it went to zero.

> It was a public filing anyone could've pulled and one formula that takes maybe 20 minutes by hand. That's the whole thing I'm about to walk you through, except you'll run it in seconds and you can point it at any company or token on earth.

Not financial advice, do your own research. Forensic scores are probability flags not proof. I build tooling for professional prediction market traders @coldvisionXYZ.

## L0: Data House

Every public company in the US files with the SEC, and the SEC just hands it all over through an API called EDGAR. You hit a URL and get back every number a company ever reported, already structured.

2 things make EDGAR a weapon:
- Full text search. It indexes the actual text of every filing ever submitted, so you can search a phrase like "material weakness" across the entire market and pull back every company that just quietly admitted its accounting controls are broken.
- Structured financials. Every line item, every quarter, machine readable, going back years.

**edgartools** is the one you want. Pip install, no key, and it parses 10-Ks, 8-Ks, insider Form 4s, 13F fund holdings, all of it into clean Python objects. It ships an MCP server too, so you can point Claude right at it and go "compare Apple and Microsoft revenue growth over 3 years" and it actually goes and grabs the real filings instead of making up numbers.

**sec-edgar-downloader** is the one everybody finds first. It just downloads the raw filing and dumps you into a pile of HTML to parse yourself. That was the move a few years ago, now it's just pain. Use edgartools.

**BamSEC** if you only want to read filings without EDGAR's interface from 1998. Clean reader, side by side compare, free for most of what you need.

## L1 - Catch Liars

You've got the numbers. Before you read a single sentence of management talking about their "transformational year," you run a few formulas on the raw figures. Academics built these off decades of actual fraud cases.

**Beneish M-Score** is the Enron one. Eight inputs mashed into a single number. Heaviest input is total accruals over total assets — the fastest way to fake earnings is to book income that never showed up as cash. Next flag is sales growth that's just too clean to be honest. Above -2.22 you go investigate. Enron printed -1.89.

**Altman Z-Score** is your bankruptcy read. Mixes profitability, leverage and how hard the assets are working into one distress score. Under 1.81 is the danger zone.

**Sloan accruals ratio** is earnings quality. Earnings made of cash are real, earnings made of accruals reverse. Drift past about 25% either way and the earnings are basically an accounting mirage about to unwind.

**Piotroski F-Score**, 9 yes/no points on whether a company is actually getting financially stronger. 6 or up is healthy.

The thing that turns this from homework into a workflow is running all 4 at once across your whole watchlist and only reading the names that flag.

And please don't reimplement these off some random blog, half the M-Score code on GitHub is subtly wrong.

**FinanceToolkit** repo has 150+ ratios - Beneish, Altman, Piotroski, Sloan, all of them - with the formulas written out in the open so you can audit a number when you don't trust it. Pair it with an FMP key for data and you're set. https://github.com/JerBouma/FinanceToolkit

Beneish runs on last year's data so the manipulation might already be unwinding by the time you see it. It misses some real frauds and false-flags some clean ones. A bad score means open the filing. It's never on its own a reason to short.

## L2: AI Read the Words for You

You screened, something flagged, now you open the 10-K, which is 100+ pages of legalese.

**Wrong way:** pasting the whole filing into a chat box and going "is this a good company." It drowns and tells you whatever you want to hear.

**Good way:** Ask it to diff this year's against last year's. Pull the Risk Factors section out of this year's 10-K and last year's, hand both to the model: "Tell me only what's new this year or what got cut, quote the new language, ignore the boilerplate that's in both."

A company that quietly slips in a paragraph about customer concentration just told you a big client is wobbling. One that deletes a line about a key supplier just told you a relationship ended. None of that ever hits the press release.

Same diff works on the MD&A and the footnotes. Enron's entire fraud lived in footnotes about off-balance-sheet entities. The story was a lie, the footnotes weren't.

**edgar-crawler** repo exists basically just to rip those item sections — Risk Factors and MD&A — into clean JSON.

**Paid tools:**
- **Hudson Labs** (was Bedrock AI): Under-the-radar pick. Cross-year red flag extraction, going-concern language, material weaknesses. ~$100/mo. Best value per dollar.
- **AlphaSense**: Institutional default, ~15-20k/seat. Owns Tegus — library of thousands of paid interviews with former execs and customers.
- **Daloopa**: Model-ready financials with every number hyperlinked back to its exact spot in the filing. Enterprise pricing.
- **Fintool**: AI-first, US equities, citations on everything, standing alerts. Decent middle ground.

## L3: Crypto

Same idea. In stocks the fraud hides in accruals and footnotes. In crypto it hides in supply schedules and holder concentration, both sitting on a public chain you can read for free.

**DefiLlama** is your EDGAR equivalent. Free API, no key, covers every protocol's TVL, fees, revenue and unlock schedule.

A protocol has 3 numbers that map straight onto a normal company:
- Fees = gross revenue
- Revenue = the slice the protocol actually keeps (net)
- Earnings = revenue minus tokens printed to bribe users

**Token Terminal** standardizes these across every major chain. ~$350/mo but free tier + DefiLlama gets you most of the way.

**Unlock schedules:** Tokens don't all exist at launch, team and VC allocations vest over years. Any single unlock over 5% of circulating supply is a red flag. Arbitrum's first big cliff unlocked an amount of ARB roughly equal to the entire circulating supply at the time.

3 shapes: Cliff (violent dump on one day), Linear vest (slow drip), Emissions (activity-based). A cliff into a VC wallet is the one that ends portfolios.

**Holder concentration:** If a handful of wallets hold most of supply and they're labeled team or early VC fund — you're the exit liquidity.

**Tools:**
- **Arkham**: Free for individuals. De-anon engine is the real deal — publicly traced billions in stolen bitcoin back to a hack.
- **Nansen**: Smart money tracking. Cut Pro to ~$49/mo. Labels are the product.
- **Dune**: 100K+ community SQL dashboards. Free tier is plenty.
- **Messari**: Strong qualitative research. Enterprise-leaning pricing.
- **Tokenomist** (was Token Unlocks): Dedicated unlock calendar.

## L4: One System

- **virattt/ai-hedge-fund**: AI agents modeled on famous investor philosophies that argue over a stock. The investor-persona thing is a gimmick, don't trade it live. But as a free lesson in how to orchestrate analysis agents — data-fetcher → screener → reasoner — it's the best teacher on GitHub. https://github.com/virattt/ai-hedge-fund
- **OpenBB**: Open source Bloomberg terminal. Connect data vendors once, MCP server so an agent can drive it. Powerful but heavy setup. https://github.com/OpenBB-finance/OpenBB
- **FinGPT / FinRobot**: Open financial LLMs you can fine-tune. Academically impressive but for most people a frontier model with the prompts above does the job. https://github.com/ai4finance-foundation/finrobot

## In order

Tool layer first → Screen layer (forensic scores on everything entering your universe) → Read layer (year over year diff on survivors) → Synthesis (model writes the memo with citations, you read the memo instead of 200 pages).

On models: Claude or GPT both work. If touching sensitive data, run open model locally through Ollama. The model was never the moat. The moat is wiring it to clean, verified, source-linked data and pointing disciplined math at it.

## L5: Build L1

Full Python script: `forensic_screener.py` — hands it a ticker, pulls real filings from EDGAR, computes Beneish, Altman, Piotroski and accruals ratio, and optionally runs year-over-year Risk Factors diff with Claude.

The script is included in the article (~200 lines). Key components:
- Uses `edgartools` to pull SEC filings
- Computes all 4 forensic scores from raw financial data
- Optional `--diff` flag runs Claude to compare Risk Factors year-over-year
- Configurable thresholds for all scores
- Handles multiple tickers in one run

Requirements: `pip install edgartools anthropic`, set `SEC_IDENTITY` and `ANTHROPIC_API_KEY` env vars.
