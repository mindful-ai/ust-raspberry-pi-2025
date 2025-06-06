import sqlite3

DB_FILE = "sensor_data.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with open("schema.sql", "r") as f:
        schema = f.read()
    conn = get_db_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()
