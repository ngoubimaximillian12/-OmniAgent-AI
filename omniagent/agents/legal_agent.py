import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from omniagent.agents.base_agent import BaseAgent
from omniagent.llm.llm_provider import LLMProvider
from omniagent.memory.memory_utils import log_and_embed, retrieve_similar_prompts

class LegalAgent(BaseAgent):
    """
    LegalAgent summarizes and interprets legal documents.
    """

    def __init__(self):
        super().__init__(
            name="LegalAgent",
            description="Summarizes and interprets legal documents.",
            input_type="text",
            tools=["pdf_parser"],
            memory_scope="user"
        )
        self.llm = LLMProvider.get_llm()

    def run(self, task, context=None, memory=None):
        """
        Processes legal tasks using the LLM with optional memory context.
        """
        memory_context = memory or retrieve_similar_prompts(task)

        prompt = f"You are a legal assistant.\nTask: {task}\nMemory: {memory_context or 'None'}"

        result = self.llm.run(prompt)

        log_and_embed(agent=self.name, prompt=task, output=result)

        return result
