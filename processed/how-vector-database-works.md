---
tags: [vector-database, embeddings, similarity-search, ann, hnsw, ivf, pq, faiss, cosine-similarity, rag, semantic-search, indexing]
source: https://outcomeschool.com/blog/how-does-a-vector-database-work
raw: "[[raw/outcomeschool_vector-database]]"
type: article
author: Amit Shekhar (Outcome School)
date: 2026-06-05
---

# How Does a Vector Database Work?

**Core idea:** A vector database finds items similar in meaning, not exact matches. It stores embeddings (lists of numbers), and uses similarity metrics + indexing to search millions of vectors in milliseconds.

## What It Stores (per item)

| Component | Purpose |
|-----------|---------|
| **Vector** | The embedding — meaning as numbers |
| **Data** | Original text/image to show users |
| **Metadata** | Filters (category, date, author) |

## Three Similarity Metrics

| Metric | Measures | Similar = | Best For |
|--------|----------|-----------|----------|
| Cosine similarity | Angle (direction only) | Value close to 1 | Text, semantic search |
| Dot product | Direction + size | Larger value | Normalized vectors |
| Euclidean distance | Straight-line gap | Smaller value | Image, spatial data |

## The Nearest Neighbour Problem

Given a query vector, find the closest stored vectors. Brute force (compare against all) = 100B calculations for 100M vectors × 1000 dims. Not viable at scale.

## ANN: Approximate Nearest Neighbour

Trade tiny accuracy for huge speed. **Recall** = % of true top results found (90% recall in ms > 100% in seconds).

An **index** pre-organizes vectors so searches jump to promising areas.

## Three Index Types

### HNSW (Hierarchical Navigable Small World)
Layered graph: top layer = few points, big jumps → middle = more points, medium steps → bottom = all points, fine steps. Most widely used. "Find a friend: go to right city → right street → few houses."

### IVF (Inverted File Index)
Pre-group vectors into clusters. Search: compare query to cluster centers → pick closest few → search only inside those. 100M vectors / 100 clusters × 3 clusters = check 3M instead of 100M.

### PQ (Product Quantization)
Memory compression, not search routing. Split vector into pieces → replace each with closest codebook entry → store code numbers (1 byte each). 512 bytes → 8 bytes (64x savings). Combined with IVF = **IVF-PQ**, the standard for billion-scale.

## Code (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatL2(4)
index.add(vectors)  # stored embeddings
distances, ids = index.search(query, k=2)
```

For production scale, swap IndexFlatL2 for HNSW/IVF — same API.

## Applications

1. **Semantic search** — search by meaning, not exact words
2. **RAG for LLMs** — find relevant docs → feed to LLM → answer from private data
3. **Recommendations** — products/people with similar embedding vectors
4. **Image search** — upload photo, find visually similar
5. **Duplicate/fraud detection** — similar items = similar vectors