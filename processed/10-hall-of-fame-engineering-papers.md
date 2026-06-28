---
tags:
- papers
- distributed-systems
- systems
- engineering
source: https://x.com/thesupereng/status/2065361684747719164
date: 2026-06-12
type: bookmark
author: thesupereng
summary: A curated reading path through 10 foundational systems papers that shaped
  Hadoop, Cassandra, Kafka, Kubernetes, OpenTelemetry, and modern distributed infrastructure,
  with one-line ideas and visible industry legacy for each.
raw: '[[raw/thesupereng_2065361684747719164]]'
description: A curated reading path through 10 foundational systems papers that shaped
  Hadoop, Cassandra, Kafka, Kubernetes, OpenTelemetry, and modern distributed infrastructure,
  with one-line ideas and visible industry legacy for each.
---

# 10 Hall of Fame Engineering Papers

A single post compressing the key ideas from 10 papers that turned real-world failures (disks fail, networks partition, clocks lie) into reusable designs still powering production systems today.

## The List (Reading Path)

1. **The Google File System (2003)** — Design storage around failure and large sequential workloads. Legacy: HDFS, distributed object/file storage.
2. **MapReduce (2004)** — Hide distributed execution behind a tiny programming model. Legacy: Hadoop, batch data platforms, data-parallel APIs.
3. **Bigtable (2006)** — A sparse, sorted, distributed map can scale structured data. Legacy: HBase, Cassandra, Accumulo, wide-column databases.
4. **Dynamo (2007)** — Trade some consistency for always-on writes and availability. Legacy: Dynamo-style stores, Riak, Cassandra, tunable quorums.
5. **Spanner (2012)** — Global transactions are possible with consensus and bounded clock uncertainty. Legacy: Cloud Spanner, distributed SQL, CockroachDB/YugabyteDB ideas.
6. **Kafka (2011)** — Treat messaging as a durable, partitioned, replayable log. Legacy: Event streaming, CDC, event-driven architectures.
7. **Raft (2014)** — Make consensus understandable enough to implement and operate. Legacy: etcd, Consul, CockroachDB, TiKV, Kafka KRaft.
8. **Dapper (2010)** — Trace one request across an entire distributed call graph. Legacy: Zipkin, Jaeger, OpenTelemetry tracing.
9. **Borg (2015)** — Run diverse workloads on one shared cluster through declarative control loops. Legacy: Kubernetes and cloud-native orchestration.
10. **The Tail at Scale (2013)** — At scale, rare slow operations become normal user experience. Legacy: Hedged requests, percentile SLOs, latency-aware systems.

## Key Themes Across Papers
- **Failure is normal**: GFS, Dynamo, and Tail at Scale treat hardware/network issues as routine rather than exceptional.
- **Simplicity at the API, complexity in the runtime**: MapReduce, Raft, and Borg demonstrate the power of moving hard problems into shared infrastructure.
- **Observability and uncertainty**: Dapper and Spanner show that understanding what is happening (tracing) and modeling what cannot be known precisely (clock bounds) are first-class concerns at scale.

## Why This Matters
These papers are not just historical; their patterns appear in nearly every production distributed system today. The post frames them as a practical reading path rather than a theoretical leaderboard.