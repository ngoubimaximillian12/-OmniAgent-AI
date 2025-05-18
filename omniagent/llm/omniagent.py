from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from config import MODEL_PATH

class OmniAgent:
    """
    Core LLM wrapper that loads the DeepSeek model and exposes a `.run()` method
    for all agents to use in a unified way.
    """

    def __init__(self):
        print(f"🔧 Loading DeepSeek model from: {MODEL_PATH}")
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True)
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def run(self, prompt: str, temperature: float = 0.7, max_tokens: int = 512) -> str:
        """
        Runs the model and returns the generated text.
        """
        output = self.generator(prompt, max_length=max_tokens, do_sample=True, temperature=temperature)
        return output[0]["generated_text"].replace(prompt, "").strip()
