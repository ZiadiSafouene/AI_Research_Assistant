from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

class QdrantStore:
    def __init__(self, collection_name: str, dim: int):
        self.client = QdrantClient(":memory:")  
        self.collection_name = collection_name

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
        )

    def add(self, embeddings, texts, metadata):
        points = []

        for i, (emb, text, meta) in enumerate(zip(embeddings, texts, metadata)):
            points.append(
                PointStruct(
                    id=i,
                    vector=emb.tolist(),
                    payload={
                        "text": text,
                        "metadata": meta
                    }
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query_embedding, k=5):
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding.tolist(),
            limit=k
        )

        output = []
        for r in results.points:
            output.append({
                "text": r.payload["text"],
                "metadata": r.payload["metadata"],
                "score": r.score
            })

        return output