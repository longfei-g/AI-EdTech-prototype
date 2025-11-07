# database.py
import sqlite3

DB_PATH = "progress.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (user_id TEXT, mission TEXT, category TEXT, sdg TEXT,
                  challenges INT, ideas INT, originality FLOAT,
                  reflection TEXT, summary TEXT, reports TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_progress(data: dict):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO progress (user_id, mission, category, sdg, challenges, ideas, originality, reflection, summary, reports)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (data['user_id'], data['mission'], data['category'], data['sdg'],
               data['challenges'], data['ideas'], data['originality'],
               data['reflection'], data['summary'], data['reports']))
    conn.commit()
    conn.close()

def get_progress(user_id: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM progress WHERE user_id=?", (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows