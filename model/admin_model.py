import sqlite3

def get_all_students():
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, login FROM students")
    result = cursor.fetchall()
    conn.close()
    return result

def get_all_teachers():
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, login FROM teachers")
    result = cursor.fetchall()
    conn.close()
    return result

def delete_user(table, user_id):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
