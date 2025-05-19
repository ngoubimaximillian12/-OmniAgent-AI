from .sql_store import save_to_sql
from .embedder import embed
from .vector_store import add_memory, search_memory

def log_and_embed(agent: str, prompt: str, output: str):
    """
    Stores prompt and output in SQL + embeds the prompt to vector memory.

    Args:
        agent (str): Agent name (e.g. CodeAgent)
        prompt (str): User task input
        output (str): Agent's response
    """
    save_to_sql(agent, prompt, output)
    vector = embed(prompt)
    add_memory(prompt, vector)

def retrieve_similar_prompts(query: str, top_k: int = 3):
    """
    Retrieves semantically similar prompts using the vector store.

    Args:
        query (str): Current prompt/task
        top_k (int): Number of results to return

    Returns:
        list[str]: Similar prompts from vector memory
    """
    query_vector = embed(query)
    return search_memory(query_vector, top_k=top_k)
