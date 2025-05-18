from sentence_transformers import SentenceTransformer

# Load a compact and fast model for embedding
# You can change this to BGE or others later
MODEL_NAME = "all-MiniLM-L6-v2"

try:
    embedder = SentenceTransformer(MODEL_NAME)
except Exception as e:
    print(f"⚠️ Failed to load embedding model: {e}")
    embedder = None


def embed(text: str):
    """
    Embeds a single piece of text into a vector.

    Args:
        text (str): The input text or prompt

    Returns:
        list[float]: The embedding vector
    """
    if not embedder:
        raise RuntimeError("Embedding model is not available.")
    return embedder.encode([text])[0]
