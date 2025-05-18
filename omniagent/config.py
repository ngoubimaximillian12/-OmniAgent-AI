import os
from dotenv import load_dotenv

# Load from .env or system environment
load_dotenv()

# === LLM Configuration ===
MODEL_PATH = os.getenv("MODEL_PATH", "deepseek-ai/deepseek-coder-6.7b-instruct")

# === Local Database ===
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "omniagent.db")

# === Optional Vector Store (e.g. Qdrant) ===
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")

# === API Keys (optional for tools) ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "")

# === UI or Runtime Flags (optional) ===
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
