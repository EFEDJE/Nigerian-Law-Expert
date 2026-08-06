from app.rag.models import Section
from app.rag.models import Chunk
from app.rag.splitter import LegalTextSplitter


class Chunker:
    def __init__(self):
        self.text_splitter = LegalTextSplitter()

    def create_chunks(
            self,
            sections: list[Section],
    ) -> list[Chunk]:
        chunks = []
        chunk_id = 0

        for section in sections:
            split_text = self.text_splitter.split(section.text)

            for piece in split_text:
                chunk = Chunk(
                    chunk_id=chunk_id,
                    document="Constitution of the Federal Republic of Nigeria",
                    chapter=section.chapter,
                    part=section.part,
                    article=section.article,
                    section_title=section.section_title,
                    page=section.page,
                    text=piece
                )

                chunks.append(chunk)
                chunk_id += 1

        return chunks