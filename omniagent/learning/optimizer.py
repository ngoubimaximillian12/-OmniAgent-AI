import json
from collections import Counter
import os

FEEDBACK_LOG_PATH = "feedback_log.json"
LESSON_LOG_PATH = "lessons_learned.json"

def summarize_feedback():
    """
    Analyzes feedback logs and returns summary statistics.
    """
    if not os.path.exists(FEEDBACK_LOG_PATH):
        return "No feedback log found."

    with open(FEEDBACK_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total = len(lines)
    if total == 0:
        return "No feedback entries yet."

    feedback_data = [json.loads(line) for line in lines]
    feedback_counter = Counter(entry.get("feedback", "").lower() for entry in feedback_data)
    agent_counter = Counter(entry.get("agent", "") for entry in feedback_data)

    summary = {
        "total_feedback": total,
        "by_feedback": dict(feedback_counter),
        "by_agent": dict(agent_counter),
    }
    return summary

def list_problematic_tasks(agent_filter=None, limit=5):
    """
    Retrieves tasks with negative feedback, optionally filtered by agent.
    """
    if not os.path.exists(LESSON_LOG_PATH):
        return []

    with open(LESSON_LOG_PATH, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f]

    negative_feedbacks = {"no", "👎", "bad"}

    filtered = [
        e for e in entries
        if e.get("feedback", "").lower() in negative_feedbacks and
        (agent_filter is None or e.get("agent") == agent_filter)
    ]

    # Return most recent limited entries
    return filtered[-limit:]
