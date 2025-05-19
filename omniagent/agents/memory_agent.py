import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from omniagent.agents.base_agent import BaseAgent
from omniagent.memory.memory_utils import retrieve_similar_prompts

class MemoryAgent(BaseAgent):
    """
    MemoryAgent retrieves similar past prompts and outputs to assist user queries.
    """

    def __init__(self):
        super().__init__(
            name="MemoryAgent",
            description="Finds similar past prompts and outputs.",
            input_type="text",
            tools=[],
            learnable=False,
            memory_scope="user"
        )

    def run(self, task, context=None, memory=None):
        """
        Retrieves and returns similar memory entries related to the input task.
        """
        results = retrieve_similar_prompts(task)
        return "\n---\n".join(results or ["No relevant memory found."])
