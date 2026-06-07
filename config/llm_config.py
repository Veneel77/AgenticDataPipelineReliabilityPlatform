import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL = "gemini/gemini-2.5-flash"

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)