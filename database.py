import sqlite3

def connect_db():
    return sqlite3.connect("jobs.db")

def create_table():
    with connect_db() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            salary TEXT,
            status TEXT
        )
        """)