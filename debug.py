from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".env")

print("Exists:", env_path.exists())
print("Absolute path:", env_path.resolve())

loaded = load_dotenv(dotenv_path=env_path)

print("Loaded:", loaded)
print("Key:", os.getenv("GOOGLE_API_KEY"))