import requests
from omniagent.agent_registry import AGENTS
from omniagent.utils.deepseek_api import call_deepseek_api  # Import the above helper

API_URL = "http://localhost:8000/run-agent"

def run_agent_safely(agent_name: str, task: str, user: str = "default") -> str:
    """
    Tries to run the agent on backend API; if backend fails,
    falls back to calling the DeepSeek API directly.
    """
    try:
        response = requests.post(API_URL, json={
            "agent_name": agent_name,
            "task": task,
            "user": user
        }, timeout=5)
        if response.status_code == 200:
            return response.json().get("result") or "No result from backend."
        else:
            print(f"⚠️ Backend returned status {response.status_code}, falling back to DeepSeek API.")
            raise Exception("Backend failure")
    except Exception as e:
        print(f"⚠️ Backend call failed ({e}), falling back to DeepSeek API.")

        # Call DeepSeek API directly on fallback
        deepseek_result = call_deepseek_api(task)
        return deepseek_result
