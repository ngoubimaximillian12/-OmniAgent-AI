import faiss
import numpy as np

# Use 384 for all-MiniLM embeddings, adjust if needed
VECTOR_DIM = 384

# FAISS in-memory index
INDEX = faiss.IndexFlatL2(VECTOR_DIM)

# Store original prompt strings linked to vectors
MEMORY_STORE = []


def add_memory(prompt: str, vector: np.ndarray):
    """
    Adds a prompt vector to the FAISS index and links it to the original prompt.

    Args:
        prompt (str): The input string
        vector (np.ndarray): Its embedding vector (float32)
    """
    global INDEX, MEMORY_STORE
    vector = np.array([vector], dtype='float32')
    INDEX.add(vector)
    MEMORY_STORE.append(prompt)


def search_memory(query_vector: np.ndarray, top_k: int = 3):
    """
    Searches the FAISS index for similar prompts.

    Args:
        query_vector (np.ndarray): Embedding of the current query
        top_k (int): Number of results to return

    Returns:
        list[str]: The top matching prompt strings
    """
    global INDEX, MEMORY_STORE
    query_vector = np.array([query_vector], dtype='float32')
    if INDEX.ntotal == 0:
        return []

    distances, indices = INDEX.search(query_vector, top_k)
    return [MEMORY_STORE[i] for i in indices[0] if i < len(MEMORY_STORE)]
