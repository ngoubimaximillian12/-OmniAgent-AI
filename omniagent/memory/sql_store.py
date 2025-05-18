import sqlite3
from config import SQLITE_DB_PATH
from datetime import datetime
import os

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
