class LLMProvider:
    _llm_instance = None

    @staticmethod
    def get_llm():
        if LLMProvider._llm_instance is None:
            LLMProvider._llm_instance = OmniAgent()
        return LLMProvider._llm_instance

# Minimal dummy OmniAgent for testing
class OmniAgent:
    def run(self, prompt: str) -> str:
        # This should connect to your actual LLM backend
        return f"Simulated response for prompt: {prompt}"
