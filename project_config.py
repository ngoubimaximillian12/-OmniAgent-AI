import os
from dotenv import load_dotenv
from dotenv import load_dotenv
load_dotenv()  # This loads environment variables from your .env file
SQLITE_DB_PATH = ... # Your actual DB path or config here


# Load environment variables from .env or system environment
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
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")

# === UI or Runtime Flags (optional) ===
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
