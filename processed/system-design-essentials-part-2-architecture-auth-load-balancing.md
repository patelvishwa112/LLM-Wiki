---
title: "System Design Essentials Part 2: Architecture Styles, Auth and Load Balancing"
type: bookmark
description: "Anurag's System Design Essentials items 21-40 — event-driven architecture, serverless, CDN, queues vs pub/sub, background jobs, cron, proxies, auth/authz, JWT, OAuth, and five load-balancing algorithms."
tags: [architecture, distributed-systems, scaling, networking, systems, fundamentals]
source: https://x.com/anurag_gharat/status/2104493200870433145
date: 2026-09-28
author: Anurag
summary: "Anurag's System Design Essentials items 21-40 — event-driven architecture, serverless, CDN, queues vs pub/sub, background jobs, cron, proxies, auth/authz, JWT, OAuth, and five load-balancing algorithms."
raw: "[[raw/anurag_gharat_2104493200870433145]]"
---

# System Design Essentials Part 2: Architecture Styles, Auth and Load Balancing

**Source:** Anurag, 2026-09-28. Second of three long-form X articles in the System Design Essentials series, numbered items 21–40, continuing directly from the 20 building blocks of part 1.

The premise is stated up front: knowing the components is not the same as knowing how to put them together. Where part 1 enumerated primitives, this installment is about compositional choice — which architectural style fits, where to spend optimization effort, and what each decision costs later. It runs 20 numbered blocks that cluster naturally into three groups: asynchronous composition (event-driven architecture, serverless, CDN, message queues, pub/sub, background jobs, cron), request-path placement (reverse vs forward proxy), and identity plus traffic distribution (authentication, authorization, JWT, OAuth, browser storage, load balancing and its five algorithms).

The async group is taught by failure mode rather than definition. Event-driven architecture is motivated by the synchronous dependency: if a callee is slow or down, the whole flow dies, so instead a service emits an event (ORDER_PLACED, USER_CREATED) and stops waiting, with producer, consumer and event broker as the three blocks. Serverless is corrected at the name level — servers still exist, you just stop provisioning and patching them — with cold start, statelessness, per-request auto-scaling and pay-per-use as the properties, and a narrow fit: event-driven tasks, unpredictable traffic, fast development. Message queues get the same treatment, contrasted against a direct producer→consumer call that requires the consumer to be up and fast at all times; the queue absorbs the outage, and the invoice-generation example shows the order service answering the client immediately while a worker pulls "SendInvoice" at its own pace. Pub/sub is then differentiated from a queue in one line: a queue delivers each message to one consumer, pub/sub fans it out to every subscriber on a topic.

The middle blocks are about work that should not block a request — background jobs (job/task, job queue on Redis, RabbitMQ, SQS or BullMQ, worker process, with async, scheduled, recurring and delayed patterns) and cron, with the five-field syntax table (`0 0 * * *` nightly, `0 */6 * * *` every six hours). The two proxy blocks are deliberately paired so the asymmetry sticks: a forward proxy sits in front of the client and hides the client from the server (privacy, content filtering, geo-bypass), a reverse proxy sits in front of the server and hides the server from the client (load balancing, SSL termination, caching, request routing, compression).

The final group covers identity and traffic. Authentication is "who are you" and authorization is "what are you allowed to do", illustrated with an employee who is authenticated but not permitted to delete another employee. JWT gets its three-part anatomy (header with the signing algorithm, payload claims like userId/role/exp, signature proving the token was not tampered with) and its payoff: signature verification instead of a database lookup. OAuth is framed as the credential-sharing problem it removes — your app never sees the Google password, only a scoped access token obtained after the redirect-and-approve flow. Cookies, local storage and session storage are distinguished by lifetime and by whether the browser attaches them automatically. Load balancing closes the piece: add servers, then solve routing with round robin, least response time, least connections, weighted round robin (weights for uneven hardware) and IP hash for sticky sessions.

## Why it matters

For AI systems, most of these are the difference between a demo and a service. Agent runs are long and non-blocking by nature, so the queue/pub-sub split and the background-job pattern are the literal architecture of a tool-calling loop that must return a response before the model finishes thinking. The auth blocks matter because an agent acting on a user's behalf needs a scoped token, not the user's credential — that is the OAuth argument, and it is also the argument for short-lived, narrowly scoped credentials in MCP servers. Load-balancing algorithms are the same decision an inference gateway makes when routing across replicas or providers, and the reverse-proxy position is where rate limiting, caching and TLS termination actually live.

## Key points

- Synchronous calls create tight coupling: one slow or dead callee takes down the whole flow; EDA decouples by having the caller emit an event and return.
- Serverless trades cold-start latency for zero provisioning — functions are event-triggered, auto-scaling, stateless, billed per use.
- CDNs cache static assets (CSS, JS, HTML, images) on edge servers near the user; cache hit returns immediately, miss fetches from origin and populates the edge. Wrong tool for live, highly dynamic data like a bank balance.
- Queue vs pub/sub is the one-to-one vs one-to-many distinction: a message queue delivers each message to a single consumer, pub/sub fans out to every subscriber of a topic.
- A queue buys decoupling, buffering of traffic spikes, and durability — messages persist until successfully processed, so a crashed consumer loses nothing.
- Background jobs move non-critical work (confirmation email, invoice PDF, SMS, analytics sync) out of the Create Order API path so the response is not gated on it.
- Cron uses five fields; `0 0 * * *` is daily midnight, `0 */6 * * *` is every six hours, and no user request triggers the job.
- Forward proxy hides the client from the server; reverse proxy hides the server from the client and is where load balancing, SSL termination, caching and compression sit.
- JWT = header + payload (claims) + signature over both with a secret, verified without a database lookup; the signature is what proves it was not altered.
- OAuth's flow: redirect to the provider, authenticate there, approve a scope, receive an authorization code, exchange it for an access token — the app never sees the password.
- Cookies are sent automatically on every HTTP request; local storage persists across browser restarts; session storage dies with the tab.
- Five balancing algorithms: round robin (sequential cycling), least response time, least connections, weighted round robin (Server A weight 3 gets 3 of every 4 requests), IP hash (same client → same server, useful for sticky sessions).
- The post labels item 37 "Least Response Time" but describes it as routing to the server with the fewest active connections — the two are separate algorithms and item 38 then covers least connections on top of response times.

## Related

- [[system-design-essentials-20-building-blocks]]
- [[system-design-essentials-caching-rate-limiting]]
- [[browser-internals-chromium-architecture]]
- [[how-to-clear-technical-interview-2026-shubh]]
- [[making-ai-agent-production-ready-sarthakrastogi]]
