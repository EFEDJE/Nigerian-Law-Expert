import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class Generator:
    def __init__(self, model: str = "models/gemini-3.1-flash-lite"):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(model=self.model, contents=prompt)
        return response.text