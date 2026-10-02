# Embedding Model Evaluation (Phase 0)

## Context
We need to select an embedding model for Liora's Retrieval-Augmented Generation (RAG) feature. We evaluated `all-MiniLM-L6-v2` and `BAAI/bge-small-en-v1.5` using a small representative dataset.

## Evaluated Models

### 1. `all-MiniLM-L6-v2`
- **Embedding Dimension**: 384
- **Size**: ~80 MB (very fast to load)
- **Latency**: Sub-millisecond per short document
- **Retrieval relevance**: Good baseline performance. It successfully maps exact matches and basic semantic similarities.

### 2. `BAAI/bge-small-en-v1.5`
- **Embedding Dimension**: 384
- **Size**: ~130 MB
- **Latency**: Marginally slower than MiniLM but still highly performant for local execution.
- **Retrieval relevance**: Excellent. Exhibits stronger semantic understanding out-of-the-box, particularly for domain-specific queries and nuanced intent, which is critical for an educational assistant like Liora.

## Decision
We recommend **`BAAI/bge-small-en-v1.5`** as the default embedding model for Liora. It shares the same dimensionality (384) as `all-MiniLM`, making migration easy if needed, but provides superior retrieval accuracy with minimal latency overhead.

*Note: The system is designed to keep the embedding provider swappable (e.g., via a standard `EmbeddingProvider` interface) so we are not permanently locked into this model.*
