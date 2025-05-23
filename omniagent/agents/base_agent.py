from abc import ABC, abstractmethod
from learning.feedback_loop import log_feedback

class BaseAgent(ABC):
    """
    Abstract base class that defines the structure for all OmniAgent agents.
    Each agent must implement the run() method.
    """

    def __init__(self, name, description, input_type, tools=None, memory_scope="task", learnable=True):
        """
        Initializes the base properties of an agent.

        Args:
            name (str): The internal name of the agent.
            description (str): Short description of the agent's function.
            input_type (str): Input type expected ("text", "code", "file", etc.).
            tools (list): List of tools this agent can use.
            memory_scope (str): Memory namespace - "user", "global", or "task".
            learnable (bool): Whether the agent can receive and apply feedback.
        """
        self.name = name
        self.description = description
        self.input_type = input_type
        self.tools = tools or []
        self.memory_scope = memory_scope
        self.learnable = learnable

    @abstractmethod
    def run(self, task: str, context: dict = None, memory: list = None) -> str:
        """
        Main execution method of the agent. Must be implemented by all child agents.

        Args:
            task (str): The user input or task to perform.
            context (dict, optional): Additional task context.
            memory (list, optional): Retrieved related memory items.

        Returns:
            str: The generated response or result.
        """
        pass

    def learn(self, feedback: str, prompt: str, output: str):
        """
        Optional learning method triggered after task execution with user feedback.

        Args:
            feedback (str): Feedback string ("Yes" or "No").
            prompt (str): Original user input.
            output (str): Result generated by the agent.
        """
        if self.learnable:
            log_feedback(self.name, prompt, output, feedback)
