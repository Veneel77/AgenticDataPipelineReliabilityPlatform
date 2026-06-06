import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiService:

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_response(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text