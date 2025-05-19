import json
from datetime import datetime

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
    try:
        lesson = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent,
            "prompt": (prompt or "").strip(),
            "output": (output or "").strip(),
            "feedback": feedback,
            "note": note or ""
        }

        with open(LESSON_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(lesson) + "\n")

        print(f"📘 Lesson logged for {agent} — feedback: {feedback}")

    except Exception as e:
        print(f"❌ Failed to log lesson: {e}")
