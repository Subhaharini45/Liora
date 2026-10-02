import time
from sentence_transformers import SentenceTransformer

# Embedding evaluation spike (Phase 0H)
# Models to evaluate
models = [
    "all-MiniLM-L6-v2",
    "BAAI/bge-small-en-v1.5"
]

# Sample Liora evaluation dataset
documents = [
    "Endee Vector DB is a high-performance vector database founded in 2025.",
    "Liora is an AI-powered adaptive learning assistant.",
    "Streamlit provides a fast way to build data applications in Python.",
    "RAG stands for Retrieval-Augmented Generation, used to ground LLM responses.",
    "PostgreSQL is a powerful, open-source object-relational database system.",
    "Vector embeddings capture the semantic meaning of text in a high-dimensional space."
]

queries = [
    "What is Endee?",
    "How does Liora work?",
    "What does RAG mean?"
]

def evaluate_model(model_name: str):
    print(f"\n--- Evaluating {model_name} ---")
    start_time = time.time()
    try:
        model = SentenceTransformer(model_name)
        load_time = time.time() - start_time
        print(f"Model load time: {load_time:.2f}s")
        
        start_time = time.time()
        doc_embeddings = model.encode(documents)
        embed_time = time.time() - start_time
        
        dim = len(doc_embeddings[0])
        print(f"Embedding dimension: {dim}")
        print(f"Time to embed {len(documents)} docs: {embed_time:.4f}s")
        
        query_embeddings = model.encode(queries)
        
        # Simple similarity check
        from sentence_transformers import util
        import torch
        
        print("\nRetrieval Test:")
        for i, query in enumerate(queries):
            cosine_scores = util.cos_sim(query_embeddings[i], doc_embeddings)[0]
            top_result = torch.argmax(cosine_scores).item()
            print(f"Q: '{query}' -> Top Match: '{documents[top_result]}' (Score: {cosine_scores[top_result]:.4f})")
            
    except Exception as e:
        print(f"Failed to evaluate {model_name}: {str(e)}")

if __name__ == "__main__":
    for m in models:
        evaluate_model(m)
