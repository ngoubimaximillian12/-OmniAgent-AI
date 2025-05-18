from agents.base_agent import BaseAgent
from memory.memory_utils import retrieve_similar_prompts

class MemoryAgent(BaseAgent):
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
        results = retrieve_similar_prompts(task)
        return "\n---\n".join(results or ["No relevant memory found."])
