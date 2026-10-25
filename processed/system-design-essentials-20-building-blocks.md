---
title: "System Design Essentials — 20 Building Blocks"
type: bookmark
description: "Anurag's long-form primer: 20 core system design blocks from client-server and scaling through ACID/BASE, CAP, sharding, HTTP, microservices, API styles and polling vs webhooks."
tags: [architecture, scaling, databases, distributed-systems, fundamentals, backend]
source: https://x.com/anurag_gharat/status/2102227321256337439
date: 2026-09-22
author: Anurag
summary: "Anurag's long-form primer: 20 core system design blocks from client-server and scaling through ACID/BASE, CAP, sharding, HTTP, microservices, API styles and polling vs webhooks."
raw: "[[raw/anurag_gharat_2102227321256337439]]"
---

# System Design Essentials — 20 Building Blocks

**Source:** Anurag, 2026-09-22. A ~19.5K-character article-length post, first in a series, working through the primitives of system design one block at a time with a diagram, the problem each solves, and its trade-off.

The article is organised as a checklist rather than a narrative, and its structure is the point: each of the 20 blocks is presented as an independent building block that can be composed. It starts at the foundation — client-server (2-tier when the client talks straight to the database, 3-tier once an application server is inserted), and the two scaling directions: vertical (more RAM, compute, storage on one box, cheap early, hard ceiling) versus horizontal (more machines, the fan-out pattern).

The middle section is database doctrine. Storage options are enumerated; ACID (atomicity, consistency, isolation, durability) is contrasted with BASE (basically available, soft state, eventually consistent), with the money-transfer example used to make rollback concrete. CAP is then framed correctly: partitions happen, so the real choice is CP versus AP, and ACID leans CP while BASE leans AP. From there the article walks the operational layer — primary/replica replication with synchronous versus asynchronous write paths, vertical versus horizontal partitioning, and sharding as horizontal partitioning with a shard key (range, hash or geo) — noting the honest trade-off that replication cannot fix write load because every replica holds the full dataset, and that cross-shard queries and atomic cross-shard transactions get hard.

The final third is the interface layer. HTTP is described as stateless over TCP with the standard method and status-code table; monolithic versus modular-monolithic versus microservices is laid out with matching advantage/disadvantage lists; the API gateway is positioned as the single entry point doing auth, routing, logging, load balancing, rate limiting, caching and protocol translation (HTTP → gRPC). REST's six constraints, SOAP's rigid XML Envelope, and GraphQL's fix for REST's over-fetching and under-fetching follow, with a side-by-side profile-page example (two REST calls versus one shaped query). WebSockets get the HTTP 101 upgrade explanation, gRPC gets ProtoBuf plus HTTP/2 as the reason it is fast, and the piece closes on the push/pull distinction: polling repeatedly asks (payment-status example), webhooks invert the direction so the server POSTs to a registered URL when the event fires.

## Why it matters

For people building AI systems, most production failures are not model failures but composition failures — an agent service that cannot shard its state, a tool-calling layer with no rate limiting, a status UI built on polling where a webhook belonged. This is a compact vocabulary sheet for those decisions, and the ACID/BASE and CAP framing is the same trade space that agent memory and eval stores now sit in. It is also a reminder that the interview-relevant primitives have not moved much even as the workloads on top of them did.

## Key points

- 20 blocks covered in one post: client-server, vertical vs horizontal scaling, databases, ACID vs BASE, CAP, relational vs non-relational, replication, partitioning, sharding, HTTP, monolith, microservices, API gateway, REST, SOAP, GraphQL, WebSocket, gRPC, polling, webhooks.
- ACID is defined as Atomicity, Consistency, Isolation, Durability — the post's own expansion ("Fault Tolerance") is loose, durability is the standard fourth property.
- BASE prioritises availability and eventual consistency; ACID leans CP under CAP, BASE leans AP.
- Replication scales reads, not writes: one primary takes writes, N replicas serve reads, so the primary remains the write ceiling.
- Synchronous replication waits for replica acknowledgement before responding; asynchronous responds first and syncs in the background.
- Sharding is horizontal partitioning keyed by range, hash or geo; cross-shard queries and atomic cross-shard transactions are the cost.
- REST is six constraints (uniform interface, stateless, client-server, cacheable, layered system, code-on-demand); GraphQL collapses many endpoints into one `POST /graphql` and lets the client shape the response.
- WebSocket upgrades an HTTP request to a persistent two-way channel on status 101; gRPC wins on speed via ProtoBuf binary serialisation over HTTP/2.
- Polling wastes requests and can overload the server; webhooks are the push inversion — the client registers a URL and the server calls it on the event.

## Related

- [[how-to-clear-technical-interview-2026-shubh]]
- [[browser-internals-chromium-architecture]]
- [[thinking-database-infinite-context-polygres-daleverett]]
- [[making-ai-agent-production-ready-sarthakrastogi]]
- [[multi-gpu-inference-tp-pp-sp-ep-mainzonx]]
