from app.rag.embeddings import EmbeddingModel
from app.rag.vectordb import VectorDatabase
from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.rag.generator import Generator
from app.rag.advisor import NigerianLawAdvisor


embedding_model = EmbeddingModel()

vector_db = VectorDatabase()

vector_db.load(
    "storage/vector.index",
    "storage/chunks.pkl"
)

retriever = Retriever(
    embedding_model=embedding_model,
    vector_db=vector_db
)

advisor = NigerianLawAdvisor(
    retriever=retriever,
    prompt_builder=PromptBuilder(),
    generator=Generator()
)
