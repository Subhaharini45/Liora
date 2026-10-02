# Architecture Decision Record (ADR-002): Embedding Model

## Context
Liora needs to convert text into vector embeddings for semantic search in Endee.

## Decision
We will use `BAAI/bge-small-en-v1.5` run locally via `sentence-transformers`.

## Alternatives Considered
- `all-MiniLM-L6-v2`: Faster but slightly lower retrieval accuracy on nuanced queries.
- Cloud Embeddings (e.g., OpenAI `text-embedding-3-small`): Introduces latency and recurring costs.

## Evidence
- Our local embedding evaluation (`experiments/embedding_eval.py`) confirmed that `BAAI/bge-small-en-v1.5` yields superior semantic matching for our educational queries while remaining lightweight (384 dimensions).

## Consequences
- The application will need to bundle or download the model weights (~130MB) on first run.

## Status
Approved (Phase 0)
