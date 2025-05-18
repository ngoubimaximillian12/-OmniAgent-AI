import requests
from llm.llm_provider import LLMProvider
from agent_registry import AGENTS

API_URL = "http://localhost:8000/run-agent"

def run_agent_safely(agent_name, task, user="default"):
    try:
        # Try backend first
        response = requests.post(API_URL, json={
            "agent_name": agent_name,
            "task": task,
            "user": user
        }, timeout=5)
        if response.status_code == 200:
            return response.json().get("result")
        else:
            raise Exception("Backend failed")
    except Exception:
        # Fallback: use local model directly
        agent = AGENTS.get(agent_name)
        if agent:
            return agent.run(task)
        return f"❌ Agent '{agent_name}' not available."
