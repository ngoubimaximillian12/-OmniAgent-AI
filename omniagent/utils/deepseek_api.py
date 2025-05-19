import requests
import os

DEESEEK_API_URL = "https://api.deepseek.com/chat/completions"  # Correct chat completions endpoint
DEESEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-97a3b77ff1f6491db73deb0d6614225b")  # Load from env or fallback

def call_deepseek_api(task: str, model: str = "deepseek-chat") -> str:
    """
    Calls the DeepSeek chat completions API with the given task prompt.
    Returns the generated response text or error message.
    """
    headers = {
        "Authorization": f"Bearer {DEESEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task}
        ],
        "stream": False
    }

    try:
        response = requests.post(DEESEEK_API_URL, json=payload, headers=headers, timeout=60)  # 60 seconds timeout
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ DeepSeek API call failed: {str(e)}"
