<!-- sha256: 234b165b186445989ff52c0ea89690ba336d56933a2f692b70fa1a6a159f24b0 -->

Amit Shekhar — June 5, 2026 — Outcome School
https://outcomeschool.com/blog/how-does-a-vector-database-work

How does a Vector Database work?

What is a Vector Database?
A Vector Database is a special kind of database that stores data as numbers and helps us find items that are similar in meaning, not just items that match exactly. Vector Database = Vector (list of numbers) + Database (organized storage). It stores lists of numbers and quickly finds the lists most similar to a given list.

A quick recap of embeddings
An embedding is a list of numbers that represents the meaning of something — a word, sentence, image, or song. A special AI model turns data into numbers such that similar meaning = similar numbers. Example: "king" → [0.91, 0.12, 0.55], "queen" → [0.89, 0.15, 0.58], "banana" → [0.10, 0.95, 0.03]. King and queen are close; banana is far. Each embedding is a vector — that's what we store inside a vector database.

Why normal databases fall short
Normal databases (MySQL, PostgreSQL) excel at exact matching. Search "apple" → finds every row with exactly "apple". But search "fruit that keeps the doctor away" → no exact match found. Normal DBs match words, not meaning. PostgreSQL with pgvector can add vector search, but it uses the same vector search ideas — the real question isn't normal vs vector, it's whether the database can search by meaning.

What a Vector Database stores (three things per item):
1. The vector — list of numbers (embedding) representing meaning
2. The original data — actual text/image/product to show back to user
3. Metadata — extra info (category, date, author, price) for filtering

Metadata filtering: pre-filtering (filter then search) is usually better than post-filtering (search then drop).

How do we measure similarity? Three metrics:

1. Cosine similarity — measures angle between vectors (direction only, not length). Range: -1 to 1. Close to 1 = very similar, 0 = unrelated, -1 = opposite. Most popular for text/semantic search. Formula: (A·B)/(|A|×|B|). Two sentences with same meaning point same direction even if one is longer.

2. Dot product — multiply matching numbers, add results. Larger = more similar. Affected by vector length, so works best with normalized vectors. Formula: A·B = Σ(a_i × b_i).

3. Euclidean distance — straight-line distance between two points. SMALLER = more similar. Formula: √Σ(a_i - b_i)². Best for image and spatial data where position matters.

The nearest neighbour problem: Given one query vector, find the closest stored vectors from millions. Brute force (compare against every vector) is too slow at scale — 100M vectors × 1000 dimensions = 100B calculations per search.

Approximate Nearest Neighbour (ANN) and indexing: Trade tiny accuracy for huge speed. Instead of checking every vector, cleverly skip most and only check likely close ones. Recall measures accuracy — if ANN returns 9 of the true top 10, recall = 90%.

An index is a smart structure organizing vectors in advance so searches jump straight to promising areas (like finding a friend: go to right city → right street → check a few houses, instead of knocking on every door).

HNSW explained (Hierarchical Navigable Small World):
Built in layers. Top layer: few points, big jumps (city map). Middle: more points, medium steps (town map). Bottom: all points, fine steps (street map). Search starts at top → big jumps toward query → drops down → smaller steps → reaches closest neighbours. Most widely used index in modern vector DBs.

IVF explained (Inverted File Index):
Group similar vectors into clusters in advance (with center points). Search: compare query ONLY with cluster centers → pick few closest clusters → search only inside those. 100M vectors / 100 clusters = 1M per cluster. Search 3 closest = check 3M instead of 100M. Trade-off: might miss true closest if it's in a skipped cluster.

PQ explained (Product Quantization):
Shrinks each vector to save memory (doesn't pick which vectors to check). 128-number vector × 4 bytes = 512 bytes. For 1B vectors = 512 GB. PQ: split vector into pieces → for each piece, find closest sample in codebook → store just the sample number (1 byte). 128-number vector becomes 8 codes × 1 byte = 8 bytes (64x savings). Often combined with IVF (IVF-PQ) for billion-scale search.

Code example using FAISS:
import faiss, numpy as np
dimension = 4
index = faiss.IndexFlatL2(dimension)
vectors = np.array([[0.91,0.12,0.55,0.10],[0.10,0.95,0.03,0.40],[0.88,0.15,0.58,0.12]], dtype="float32")
index.add(vectors)
query = np.array([[0.90,0.13,0.56,0.11]], dtype="float32")
distances, ids = index.search(query, 2)
# Returns [[0 2]] and [[0.0004 0.0013]] — apple and doctor articles are closest

Real-world applications: Semantic search, RAG for LLMs (vectors stored → query finds relevant docs → LLM writes answer from them), Recommendations, Image search, Duplicate/fraud detection.