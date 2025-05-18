from agents.base_agent import BaseAgent
from llm.llm_provider import LLMProvider
from memory.memory_utils import log_and_embed, retrieve_similar_prompts

class DataAgent(BaseAgent):
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
        memory_context = retrieve_similar_prompts(task)
        prompt = f"You are a data analyst.\nTask: {task}\nMemory: {memory_context or 'None'}"
        result = self.llm.run(prompt)
        log_and_embed(self.name, task, result)
        return result
