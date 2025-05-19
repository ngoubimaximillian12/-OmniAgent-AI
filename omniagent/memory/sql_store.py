import sys
import os
import sqlite3
from datetime import datetime

# Add the root project directory to sys.path so project_config can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from project_config import SQLITE_DB_PATH


def init_db():
    """
    Initializes the SQLite database with a memory table if it doesn't exist.
    """
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent TEXT NOT NULL,
            prompt TEXT NOT NULL,
            output TEXT NOT NULL,
            user TEXT DEFAULT 'default',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ SQLite memory DB initialized")


def save_to_sql(agent: str, prompt: str, output: str, user: str = "default"):
    """
    Saves a prompt + result pair to the memory table.

    Args:
        agent (str): Agent name
        prompt (str): The original task or question
        output (str): The response returned
        user (str): Optional user ID
    """
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO memory (agent, prompt, output, user)
        VALUES (?, ?, ?, ?)
    ''', (agent, prompt, output, user))

    conn.commit()
    conn.close()
