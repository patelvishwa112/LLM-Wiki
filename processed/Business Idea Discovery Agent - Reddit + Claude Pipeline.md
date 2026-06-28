---
tags:
- ai-agents
- business-ideas
- reddit-scraping
- claude
- opportunity-discovery
- market-research
- automation
- praw
- nlp
source: https://x.com/damir_akaza/article/2059621796052193667
raw: '[[raw/damir_akaza_2059621796052193667]]'
type: bookmark
created: 2026-05-30
related:
- '[[Bookmarks Index]]'
description: Business Idea Discovery Agent — Reddit Scraping + Claude Pipeline
---

# Business Idea Discovery Agent — Reddit Scraping + Claude Pipeline

**Author:** damir akaza (@Damir_Akaza)
**Date:** May 27, 2026
**Engagement:** 26.5K views · 178 bookmarks · 124 likes

## Core Idea

An AI agent that scrapes Reddit (and other forums) to extract real people's needs, wishes, and frustrations — then clusters them and scores each cluster as a potential business opportunity. $3-8 per run. Full Python code included.

The central insight: "Business ideas already exist. They're just not in your head. They're on Reddit, on forums, in the comments under your competitors' videos."

## Architecture — 4-Stage Pipeline

| Stage | Tool | What It Does | Cost |
|-------|------|--------------|------|
| 1. Collection | PRAW (Reddit API) | Pulls top 50 posts/month + top 5 comments from each subreddit | Free |
| 2. Extraction | Claude Sonnet 4.6 | Extracts structured needs (type, intensity, payment signal) from each post | $1-3 |
| 3. Clustering | Claude Opus 4.7 | Groups 200-500 needs into clusters of the same underlying need | $2-5 |
| 4. Scoring | Claude Opus 4.7 | Evaluates top 10 clusters as businesses with skeptical prompt | (included above) |

The clustering stage is where the magic happens — different people describe the same need in different words, and without grouping, you'd never see the pattern.

## Use Cases by Subreddit

- **SaaS ideas** → r/Entrepreneur, r/SmallBusiness, r/freelance, r/Solopreneur
- **Content topics** → r/parenting, r/personalfinance, r/relationships
- **E-commerce products** → r/gardening, r/woodworking, r/dogs, r/cycling
- **Customer research** → competitor user communities
- **Trend detection** → 20 niche subreddits, tracking frequency changes month-over-month

## Key Technical Details

- Each stage is a separate Claude call with its own structured prompt
- Extraction prompt is highly structured — ignores political rants, vague complaints, obvious-existing-solution cases
- Scoring prompt is deliberately skeptical: "Most needs are NOT a business"
- Output: JSON with 10 opportunities sorted by score, each with reasoning, source links, product direction, red flags
- Extensible: can swap fetch_posts() for Hacker News, X API, Discourse, Stack Exchange, YouTube comments

## Honest Limitations

1. **Market sizing is weak** — Claude doesn't know TAM
2. **Competition awareness is incomplete** — post-cutoff startups are invisible
3. **"Would pay" signals are weak** — people saying ≠ people paying
4. **Agent doesn't make decisions** — it gives a shortlist; you still need to verify (read sources, talk to 5 people, Google competitors, landing page test)
