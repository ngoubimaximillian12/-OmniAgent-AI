import json
from datetime import datetime
import os

LOG_PATH = "feedback_log.json"

def log_feedback(agent: str, prompt: str, output: str, feedback: str):
    """
    Logs feedback from the user about an agent's output.

    Args:
        agent (str): Name of the agent (e.g. CodeAgent)
        prompt (str): The original user input
        output (str): The output produced by the agent
        feedback (str): "Yes" / "No" / Thumbs Up / Down
    """
    try:
        feedback_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent,
            "prompt": (prompt or "").strip(),
            "output": (output or "").strip(),
            "feedback": feedback
        }

        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(feedback_entry) + "\n")

        print(f"📝 Logged feedback for {agent}: {feedback}")

    except Exception as e:
        print(f"❌ Failed to log feedback: {e}")
