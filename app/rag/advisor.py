from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.rag.generator import Generator


class NigerianLawAdvisor:

    def __init__(
        self,
        retriever: Retriever,
        prompt_builder: PromptBuilder,
        generator: Generator
    ):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.generator = generator

    def ask(
        self,
        question: str,
        k: int = 5
    ) -> str:

        results = self.retriever.retrieve(
            question,
            k=k
        )

        chunks = [
            chunk
            for _, chunk in results
        ]

        prompt = self.prompt_builder.build(
            question=question,
            chunks=chunks
        )

        return self.generator.generate(prompt)