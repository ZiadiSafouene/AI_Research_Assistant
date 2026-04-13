import os
from ai_research_assistant.src.ingestion.pipeline import process_paper
from ai_research_assistant.src.ingestion.chunker import chunk_text
from ai_research_assistant.src.retrieval.embedder import embed_texts
from ai_research_assistant.src.retrieval.qdrant.vector_store import QdrantStore

def build_qdrant_store(papers_dir: str):
    all_chunks = []
    metadata = []

    for file in os.listdir(papers_dir):
        if file.endswith(".pdf"):
            path = os.path.join(papers_dir, file)

            text = process_paper(path)
            chunks = chunk_text(text)

            all_chunks.extend(chunks)
            metadata.extend([{"source": file}] * len(chunks))

    embeddings = embed_texts(all_chunks)

    store = QdrantStore(
        collection_name="papers",
        dim=len(embeddings[0])
    )

    store.add(embeddings, all_chunks, metadata)

    return store