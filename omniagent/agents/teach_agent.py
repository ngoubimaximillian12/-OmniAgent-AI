from agents.base_agent import BaseAgent
from llm.llm_provider import LLMProvider
from memory.memory_utils import log_and_embed

class TeachAgent(BaseAgent):
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
        prompt = f"Explain this concept clearly for a beginner: {task}"
        result = self.llm.run(prompt)
        log_and_embed(self.name, task, result)
        return result
