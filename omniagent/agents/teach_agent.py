import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from omniagent.agents.base_agent import BaseAgent
from omniagent.llm.llm_provider import LLMProvider
from omniagent.memory.memory_utils import log_and_embed

class TeachAgent(BaseAgent):
    """
    TeachAgent explains technical or academic concepts in a clear manner.
    """

    def __init__(self):
        super().__init__(
            name="TeachAgent",
            description="Explains technical or academic concepts.",
            input_type="text",
            tools=[],
            memory_scope="global"
        )
        self.llm = LLMProvider.get_llm()

    def run(self, task, context=None, memory=None):
        """
        Generates a clear explanation for the given concept/task.
        """
        prompt = f"Explain this concept clearly for a beginner: {task}"

        result = self.llm.run(prompt)

        log_and_embed(agent=self.name, prompt=task, output=result)

        return result
