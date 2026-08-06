import pymupdf
from app.rag.models import Page


class DocumentLoader:
    def load_pdf(self, filepath: str) -> list[Page]:
        document = pymupdf.open(filepath)
        pages = []

        for page_number, page in enumerate(document):
            text = page.get_text()

            lines = [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ]

            pages.append(
                Page(
                    page = page_number + 1,
                    lines=lines
                )
            )
                
        document.close()
        return pages
    

    def load_txt(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()