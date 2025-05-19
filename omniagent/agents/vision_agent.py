import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from omniagent.agents.base_agent import BaseAgent
from omniagent.llm.llm_provider import LLMProvider
from omniagent.memory.memory_utils import log_and_embed, retrieve_similar_prompts

class VisionAgent(BaseAgent):
    """
    VisionAgent extracts text and context from images or PDFs,
    and leverages memory for enhanced understanding.
    """

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
        """
        Processes image or PDF content and generates understanding.

        Args:
            task (str): Text content extracted from file or description.
            context (dict, optional): Additional info.
            memory (list, optional): Relevant memory entries.

        Returns:
            str: LLM response with extracted insights.
        """
        memory_context = memory if memory is not None else retrieve_similar_prompts(task)
        prompt = f"You are an image understanding agent.\nTask: {task}\nMemory: {memory_context or 'None'}"

        result = self.llm.run(prompt)

        log_and_embed(agent=self.name, prompt=task, output=result)

        return result
