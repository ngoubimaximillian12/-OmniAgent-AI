from agents.base_agent import BaseAgent
from llm.llm_provider import LLMProvider
from memory.memory_utils import log_and_embed, retrieve_similar_prompts
from llm.prompt_manager import build_prompt
from llm.response_parser import clean_response

class CodeAgent(BaseAgent):
    """
    CodeAgent handles generation, debugging, explanation of code.
    It uses the OmniAgent LLM and interacts with memory modules.
    """

    def __init__(self):
        super().__init__(
            name="CodeAgent",
            description="Writes, fixes, or explains code using best practices.",
            input_type="code",
            tools=["syntax_checker", "code_executor"],
            memory_scope="task",
            learnable=True
        )
        self.llm = LLMProvider.get_llm()

    def run(self, task, context=None, memory=None):
        """
        Executes the code-related task using the LLM.
        Adds memory context and stores result for future use.
        """
        # Retrieve relevant memory based on task text
        relevant_memory = retrieve_similar_prompts(task)

        # Build structured prompt
        prompt = build_prompt(
            agent_name=self.name,
            task=task,
            context=context,
            memory=relevant_memory
        )

        # Run generation using the shared OmniAgent model
        raw_output = self.llm.run(prompt)

        # Clean up and trim output
        final_output = clean_response(raw_output)

        # Save result into memory and vector index
        log_and_embed(agent=self.name, prompt=task, output=final_output)

        return final_output
