from agents.base_agent import BaseAgent
from llm.llm_provider import LLMProvider
from memory.memory_utils import log_and_embed, retrieve_similar_prompts

class VisionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="VisionAgent",
            description="Extracts text and context from images or PDFs.",
            input_type="file",
            tools=["pdf_parser", "ocr_tool"],
            memory_scope="task"
        )
        self.llm = LLMProvider.get_llm()

    def run(self, task, context=None, memory=None):
        memory_context = retrieve_similar_prompts(task)
        prompt = f"You are an image understanding agent.\nTask: {task}\nMemory: {memory_context or 'None'}"
        result = self.llm.run(prompt)
        log_and_embed(self.name, task, result)
        return result
