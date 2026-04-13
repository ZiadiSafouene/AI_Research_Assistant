from ai_research_assistant.src.retrieval.embedder import embed_texts

def query_vector_store(store, query: str, k=5):
    query_embedding = embed_texts([query])[0]
    return store.search(query_embedding, k)