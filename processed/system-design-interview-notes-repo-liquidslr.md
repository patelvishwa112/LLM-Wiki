---
title: "System Design Interview Notes — 28-Chapter Open Repo"
type: bookmark
description: "Pointer to liquidslr/system-design-notes, 27k-star Markdown notes for all 28 chapters of Alex Xu's System Design Interview Vol 1 and 2, each with primary-source reading lists."
tags: [distributed-systems, architecture, systems, interview, resources]
source: https://x.com/jianw851/status/2107508223549092294
date: 2026-10-06
author: Jian Wang
summary: "Pointer to liquidslr/system-design-notes, 27k-star Markdown notes for all 28 chapters of Alex Xu's System Design Interview Vol 1 and 2, each with primary-source reading lists."
raw: "[[raw/jianw851_2107508223549092294]]"
---
# System Design Interview Notes — 28-Chapter Open Repo

**Source:** Jian Wang, 2026-10-06. A one-line recommendation of the `liquidslr/system-design-notes` GitHub repo as complete system-design-interview prep material.

Jian Wang's post is a bare pointer — the entire content is "All you need for System Design Interviews" plus the repo link — so its value is in what the repo contains. It is a Markdown transcription of Alex Xu's *System Design Interview: An Insider's Guide*, Volumes 1 and 2, organised as 28 numbered chapter folders: scaling from zero to millions of users, back-of-the-envelope estimation, the interview framework, rate limiter, consistent hashing, key-value store, unique ID generator, URL shortener, web crawler, notification system, news feed, chat, search autocomplete, YouTube, Google Drive, proximity service, nearby friends, Google Maps, distributed message queue, metrics/monitoring/alerting, ad click aggregation, hotel reservation, distributed email, S3-like object storage, gaming leaderboard, payment system, digital wallet, and stock exchange.

Each chapter is a full design walkthrough in the book's format — requirements, estimation, high-level design, deep dives — rather than a summary. More useful for depth, each folder also carries a further-reading list of primary sources: the Dynamo (SOSP 2007) and BigTable (OSDI 2006) papers, Cassandra architecture docs, Google's Maglev load-balancer paper, Tom White's consistent hashing write-up and Stanford CS168 notes, Uber's `uber-go/ratelimit` implementation, and Martin Fowler's CircuitBreaker bliki entry.

Provenance matters for how much to trust it: ~26.9k stars, ~5.0k forks, 35 commits, three contributors. Chapters 1–16 date from early 2025, chapters 17–28 were added April–June 2026, latest commit 2026-08-12, and the README explicitly calls the notes a work in progress. A rendered version is also published at pagefy.io.

## Why it matters

This is a free, git-tracked substitute for a paid interview-prep course, and the per-chapter reading lists are the part that actually transfers — the same papers (Dynamo, BigTable, Maglev, Kafka-style queues) underpin the storage and serving layers people build for AI products. For anyone designing inference infrastructure, retrieval backends, or agent tooling that has to survive production load, the canonical-design chapters are a faster grounding than reading vendor docs cold.

## Key points

- 28 chapter folders covering the full Vol 1 + Vol 2 syllabus of Alex Xu's *System Design Interview*.
- ~26.9k GitHub stars, ~5.0k forks, 35 commits, 3 contributors; latest commit 2026-08-12.
- Chapters 1–16 landed Jan 2025; chapters 17–28 added Apr–Jun 2026; README flags it as work in progress.
- Each chapter pairs a design walkthrough with primary sources (Dynamo, BigTable, Cassandra, Maglev, CS168 consistent hashing, Uber ratelimit, Fowler on circuit breakers).
- Rendered HTML version at pagefy.io; source author is Gaurav Kumar (liquidslr).

## Related

- [[10-hall-of-fame-engineering-papers]]
- [[how-to-clear-technical-interview-2026-shubh]]
- [[browser-internals-chromium-architecture]]
- [[what-is-kv-cache-llms]]
- [[inference-optimizations-sub-second-llm-checklist]]
