import json
from datetime import datetime
import os

LESSON_LOG_PATH = "lessons_learned.json"

def log_lesson(agent: str, prompt: str, output: str, feedback: str, note: str = None):
    """
    Logs detailed lessons learned, including feedback and optional notes.

    Args:
        agent (str): The agent's name
        prompt (str): The original task prompt
        output (str): The agent's output
        feedback (str): User feedback ("Yes"/"No" or thumbs)
        note (str): Optional additional insight or explanation
    """
    lesson = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent,
        "prompt": prompt.strip(),
        "output": output.strip(),
        "feedback": feedback,
        "note": note or ""
    }

    with open(LESSON_LOG_PATH, "a") as f:
        f.write(json.dumps(lesson) + "\n")

    print(f"📘 Lesson logged for {agent} — feedback: {feedback}")
