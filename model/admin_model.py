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

def get_students_by_course(course_name):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, g.grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        JOIN courses c ON g.course_id = c.id
        WHERE c.name = ?
    """, (course_name,))
    result = cursor.fetchall()
    conn.close()
    return result


def get_teacher_by_course(course_name):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.name
        FROM teachers t
        JOIN courses c ON t.id = c.teacher_id
        WHERE c.name = ?
    """, (course_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Not Assigned"
