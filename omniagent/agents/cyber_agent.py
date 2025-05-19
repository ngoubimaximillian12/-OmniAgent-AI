import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from omniagent.agents.base_agent import BaseAgent
from omniagent.llm.llm_provider import LLMProvider
from omniagent.memory.memory_utils import log_and_embed, retrieve_similar_prompts

class CyberAgent(BaseAgent):
    """
    CyberAgent detects vulnerabilities, CVEs, and security issues.
    """

    def __init__(self):
        super().__init__(
            name="CyberAgent",
            description="Detects vulnerabilities, CVEs, and security issues.",
            input_type="text",
            tools=["log_parser", "vuln_scanner"],
            memory_scope="task"
        )
        self.llm = LLMProvider.get_llm()

    def run(self, task, context=None, memory=None):
        """
        Executes cybersecurity analysis task using the LLM.
        Uses memory context if available.
        """
        memory_context = memory or retrieve_similar_prompts(task)

        prompt = f"You are a cybersecurity analyst.\nTask: {task}\nMemory: {memory_context or 'None'}"

        result = self.llm.run(prompt)

        log_and_embed(agent=self.name, prompt=task, output=result)

        return result
