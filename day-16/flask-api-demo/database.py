import sqlite3

DB_NAME = "items.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with open("schema.sql") as f:
        schema = f.read()
    conn = get_db_connection()
    conn.executescript(schema)
    conn.close()
