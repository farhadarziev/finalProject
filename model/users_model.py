import sqlite3

def login_user(role, login, password):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    table = "students" if role == "student" else "teachers" if role == "teacher" else "admins"

    try:
        cursor.execute(f"SELECT id, name FROM {table} WHERE login = ? AND password = ?", (login, password))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "name": row[1]}
    except Exception as e:
        print("Ошибка логина:", e)
    return None
