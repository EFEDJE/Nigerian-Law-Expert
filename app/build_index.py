from app.rag.loader import DocumentLoader
from app.rag.parser import LegalParser
from app.rag.chunker import Chunker
from app.rag.embeddings import EmbeddingModel
from app.rag.vectordb import VectorDatabase

DOCUMENT_PATH = "data/nigeria_constitution.pdf"

print("Loading document...")

loader = DocumentLoader()
pages = loader.load_pdf(DOCUMENT_PATH)

print("Parsing sections...")

parser = LegalParser(start_page=23)
sections = parser.parse(pages)

print(f"Sections: {len(sections)}")

print("Creating chunks...")

chunker = Chunker()
chunks = chunker.create_chunks(sections)

print(f"Chunks: {len(chunks)}")

print("Generating embeddings...")

embedding_model = EmbeddingModel()

embeddings = embedding_model.encode_many(
    [chunk.text for chunk in chunks]
)

print("Building vector database...")

vector_db = VectorDatabase()

vector_db.build(
    embeddings=embeddings,
    chunks=chunks
)

print("Saving index...")

vector_db.save(
    "storage/vector.index",
    "storage/chunks.pkl"
)

print("Done!")