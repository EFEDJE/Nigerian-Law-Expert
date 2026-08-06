import numpy as np
from app.rag.embeddings import EmbeddingModel
from app.rag.vectordb import VectorDatabase
from app.rag.models import Chunk


class Retriever:
    def __init__(self, embedding_model: EmbeddingModel, vector_db: VectorDatabase):
        self.embedding_model = embedding_model
        self.vector_db = vector_db

    def retrieve(self, query: str, k: int = 5) -> list[Chunk]:
        query_embedding = self.embedding_model.encode(query)
        query_embedding = np.array([query_embedding], dtype=np.float32)
        return self.vector_db.search(query_embedding=query_embedding, k=k)