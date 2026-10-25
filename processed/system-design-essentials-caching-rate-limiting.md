---
title: "System Design Essentials Part 3: Caching, Rate Limiting, Distributed Systems"
type: bookmark
description: "Anurag's final System Design Essentials installment (items 41-60) — caching strategies, idempotency keys, dedup, consistent hashing, rate-limiter algorithms, DNS, SSE, and circuit breakers."
tags: [distributed-systems, architecture, systems, caching, rate-limiting, networking]
source: https://x.com/anurag_gharat/status/2106960326436794427
date: 2026-10-05
author: Anurag
summary: "Anurag's final System Design Essentials installment (items 41-60) — caching strategies, idempotency keys, dedup, consistent hashing, rate-limiter algorithms, DNS, SSE, and circuit breakers."
raw: "[[raw/anurag_gharat_2106960326436794427]]"
---
# System Design Essentials Part 3: Caching, Rate Limiting, Distributed Systems

**Source:** Anurag, 2026-10-05. Third and final part of a System Design Essentials series (numbered items 41–60), published as a long-form X article on the optimization layer of scalable systems.

This installment covers the machinery you add once the basic request path exists. It opens with caching: the hit/miss/invalidation vocabulary, then the five placement strategies side by side — cache-aside (app asks cache, on miss loads from DB and populates), read-through (cache sits in front of the DB and loads itself), write-through (write to cache and DB in the same path), write-around (write to DB only, cache fills on later misses), and write-back (write to cache, flush to DB periodically, trading durability for write throughput). The presentation is comparative rather than prescriptive: each strategy is defined by where the write lands and who owns the fill.

The middle section is about correctness under retries. Idempotency is defined as repeat-safety (GET/PUT/DELETE are naturally idempotent, POST usually is not), motivated by the classic double-charge case where a payment times out, the client retries, and the server has already committed the first request. Idempotency keys — a client-generated unique value the server records so a repeat key returns the stored result — are offered as the mechanism that makes POST retryable. Deduplication is positioned as the mirror image: dedup happens at the sender or infrastructure layer and drops repeats before processing (message-ID check on at-least-once queues), while idempotency lives in the receiver's logic; production systems run both, dedup to catch most repeats and idempotency as the safety net.

The distributed-systems section names the four hard constraints (consistency, availability, fault tolerance, latency) and explains consistent hashing through the modulo-rehash failure: with five servers `hash(key) % 5`, dropping one makes it `% 4` and nearly every key remaps. Placing servers and keys on a ring and walking clockwise confines remapping to the removed node's arc, and the same construction covers shard movement. From there the post covers vector databases (embeddings for semantic search, recommendation, RAG, image/audio search), rate limiting (limit dimensions — per user, API key, IP, org, endpoint — and the 429 response), and four limiters: fixed window, sliding window (per-request timestamps, more memory, no boundary bursts), token bucket (fixed refill rate, absorbs bursts), and leaky bucket (labelled "Leaky Window" in the post; constant drain rate, rejects bursts). It closes with DNS resolution order and record types, Server-Sent Events over `text/event-stream` on a long-lived HTTP connection, and the circuit breaker's closed → open → half-open state machine.

## Why it matters

These are exactly the primitives an AI API needs and most agent stacks get wrong: prompt/response caching placement, idempotency keys on tool calls that spend money or mutate state, dedup on at-least-once event streams, per-key rate limits on token-expensive endpoints, and circuit breakers so one dead model provider does not cascade into your orchestrator. The framing is conventional web-systems knowledge, but the retry-safety and rate-limit sections transfer directly to LLM serving, where a single retried request can cost real tokens and a single unthrottled client can starve everyone else.

## Key points

- Five cache strategies distinguished by write path: cache-aside, read-through, write-through, write-around, write-back (write-back defers DB writes, trading durability for throughput).
- Fixed window is simplest but permits boundary bursts (a client can send 2× the limit across a window edge); sliding window fixes that at the cost of storing per-request timestamps.
- Token bucket allows bursts up to bucket depth while enforcing an average rate; leaky bucket instead enforces a constant drain rate and rejects bursts.
- Idempotency lives in receiver logic and returns the stored result for a repeated idempotency key; dedup lives in the sender/infra layer and drops duplicate message IDs. At-least-once queues need both.
- `hash(key) % N` remaps almost every key when N changes; consistent hashing confines remapping to the arc of the removed node.
- Circuit breaker states: closed (count failures) → open (block all calls) → half-open (probe with a few requests) → closed on success.
- DNS lookup order: browser cache → OS cache → ISP resolver → root → TLD → authoritative, with A/AAAA/CNAME/MX record types.
- SSE is plain HTTP with `text/event-stream` held open — server push without WebSocket bidirectionality.

## Related

- [[what-is-kv-cache-llms]]
- [[deep-agents-prompt-caching]]
- [[cerebras-knowledge-base-hybrid-search-mcp]]
- [[browser-internals-chromium-architecture]]
- [[how-to-clear-technical-interview-2026-shubh]]
