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
    feedback_entry = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent,
        "prompt": prompt.strip(),
        "output": output.strip(),
        "feedback": feedback
    }

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(feedback_entry) + "\n")

    print(f"📝 Logged feedback for {agent}: {feedback}")
