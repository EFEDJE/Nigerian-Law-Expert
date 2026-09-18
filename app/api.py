from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.rag.embeddings import EmbeddingModel
from app.rag.vectordb import VectorDatabase
from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.rag.generator import Generator
from app.rag.advisor import NigerianLawAdvisor
from app.schemas import QuestionRequest


app = FastAPI(title='Nigerian Law Expert API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", 'https://nigerian-law-expert.onrender.com'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

vector_db = VectorDatabase()
vector_db.load(
    "storage/vector.index",
    "storage/chunks.pkl"
)
retriever = Retriever(embedding_model=EmbeddingModel(), vector_db=vector_db)
advisor = NigerianLawAdvisor(retriever=retriever, prompt_builder=PromptBuilder(), generator=Generator())


@app.post("/ask")
def ask(request: QuestionRequest):
    answer = advisor.ask(request.question)
    return {
        "answer": answer
    }