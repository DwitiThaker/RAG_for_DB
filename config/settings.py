import os
from dotenv import load_dotenv

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

MONGODB_URI = require_env("MONGODB_URI")
DB_NAME = require_env("DB_NAME")
QDRANT_URL = require_env("QDRANT_URL")
QDRANT_API_KEY = require_env("QDRANT_API_KEY")
GOOGLE_API_KEY = require_env("GOOGLE_API_KEY")
