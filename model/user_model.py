import sqlite3
import os

def check_user_credentials(username, password):
    # Строим абсолютный путь к базе
    base_dir = os.path.dirname(os.path.abspath(__file__))  # model/
    db_path = os.path.join(base_dir, '..', 'database', 'sis.db')

    print("[DEBUG] using db path:", db_path)  # можешь оставить для проверки

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT role, linked_id FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return {"role": result[0], "linked_id": result[1]} if result else None


