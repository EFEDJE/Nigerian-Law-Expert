import faiss
import pickle
import numpy as np

from app.rag.models import Chunk

class VectorDatabase:
    def __init__(self):
        self.index = None
        self.chunks = []

    def build(
            self,
            embeddings: np.ndarray,
            chunks: list[Chunk]
    ):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(
            embeddings.astype('float32')
        )
        self.chunks = chunks

    def search(
            self,
            query_embedding: np.ndarray,
            k: int=5
    ) -> list[tuple[float, Chunk]]:
        scores, indices = self.index.search(query_embedding.astype('float32'), k)
        results = []
        for score, index in zip(scores[0], indices[0]):
            results.append((float(score), self.chunks[index]))
        return results
    
    def save(self, index_path: str, chunks_path: str):
        faiss.write_index(self.index, index_path)
        with open(chunks_path, 'wb') as f:
            pickle.dump(self.chunks, f)

    def load(self, index_path: str, chunks_path: str):
        self.index = faiss.read_index(index_path)

        with open(chunks_path, 'rb') as f:
            self.chunks = pickle.load(f)
