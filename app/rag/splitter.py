from langchain_text_splitters import RecursiveCharacterTextSplitter

class LegalTextSplitter:
    def __init__(
            self,
            chunk_size: int = 1000,
            chunk_overlap: int = 150
        ):
        self.chunk_size = chunk_size
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", "; ", ", ", " ", ""]
        )

    def split(self, text: str) -> list[str]:
        if len(text) <= self.chunk_size:
            return [text]
        return self.splitter.split_text(text)