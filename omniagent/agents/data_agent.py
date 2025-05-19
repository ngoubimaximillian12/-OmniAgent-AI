import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from omniagent.agents.base_agent import BaseAgent
from omniagent.llm.llm_provider import LLMProvider
from omniagent.memory.memory_utils import log_and_embed, retrieve_similar_prompts

class DataAgent(BaseAgent):
    """
    DataAgent handles data queries, SQL commands, and chart summaries.
    """

    def __init__(self):
        super().__init__(
            name="DataAgent",
            description="Handles data queries, SQL, and chart summaries.",
            input_type="text",
            tools=["csv_loader", "sql_parser"],
            memory_scope="task"
        )
        self.llm = LLMProvider.get_llm()

    def run(self, task, context=None, memory=None):
        """
        Executes the data analysis task using the LLM.
        Uses provided memory context or fetches similar prompts.
        """
        memory_context = memory or retrieve_similar_prompts(task)

        prompt = f"You are a data analyst.\nTask: {task}\nMemory: {memory_context or 'None'}"

        result = self.llm.run(prompt)

        log_and_embed(agent=self.name, prompt=task, output=result)

        return result
