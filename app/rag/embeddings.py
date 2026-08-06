from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

    def encode(self, text:str):
        return self.model.encode(text, normalize_embeddings=True)
    
    def encode_many(self, texts: list[str]):
        return self.model.encode(
            texts,
            normalize_embeddings=True
            )