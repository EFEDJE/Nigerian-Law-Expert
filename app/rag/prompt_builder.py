from app.rag.models import Chunk


class PromptBuilder:
    def __init__(self):
        self.system_prompt = """
You are an expert Nigerian constitutional lawyer.

Your task is to answer ONLY using the supplied legal context.

If the answer cannot be found in the context,
say:

"I could not find the answer in the supplied legal documents."

Do not invent laws.

Do not guess.

Always cite the Article number when possible.
""".strip()

    def build(self, question:str, chunks:list[Chunk]) -> str:
        context = ""
        for chunk in chunks:
            context += (
                f"Article {chunk.article}\n"
                f"{chunk.section_title}\n\n"
                f"{chunk.text}\n\n"
                "----------------------------------\n\n"
            )
        prompt = (
            f"{self.system_prompt}\n\n"
            f"Context:\n\n"
            f"{context}\n"
            f"Question:\n"
            f"{question}\n\n"
            f"Answer:"
        )
        return prompt