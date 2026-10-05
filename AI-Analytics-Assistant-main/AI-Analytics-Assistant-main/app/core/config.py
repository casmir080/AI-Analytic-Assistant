from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from /app directory
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")


settings = Settings()