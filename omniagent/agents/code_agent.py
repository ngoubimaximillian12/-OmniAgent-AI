from omniagent.agents.base_agent import BaseAgent
from omniagent.llm.llm_provider import LLMProvider
from omniagent.memory.memory_utils import log_and_embed, retrieve_similar_prompts
from omniagent.llm.prompt_manager import build_prompt
from omniagent.llm.response_parser import clean_response

class CodeAgent(BaseAgent):
    """
    CodeAgent handles generation, debugging, explanation of code.
    Uses the OmniAgent DeepSeek LLM directly for all queries.
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
        Always use DeepSeek LLM to handle the task fully.

        - Retrieve relevant memory (if not provided)
        - Build detailed prompt with memory and context
        - Run the DeepSeek LLM directly
        - Clean, log, and return the output
        """
        # Get similar past memory if not supplied
        relevant_memory = memory if memory else retrieve_similar_prompts(task)

        # Build the prompt with agent name, task, context, and memory
        prompt = build_prompt(
            agent_name=self.name,
            task=task,
            context=context,
            memory=relevant_memory
        )

        # Directly run the prompt on the DeepSeek LLM (no fallback)
        raw_output = self.llm.run(prompt)

        # Clean response to remove prompt echoes etc.
        final_output = clean_response(raw_output)

        # Log the input/output pair for future retrieval
        log_and_embed(agent=self.name, prompt=task, output=final_output)

        return final_output
