import sqlite3
import os

def get_db():
    base = os.path.dirname(os.path.abspath(__file__))
    return sqlite3.connect(os.path.join(base, '..', 'database', 'sis.db'))

def get_teacher_info(teacher_id):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name FROM teachers WHERE id=?", (teacher_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_teacher_course_name(teacher_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM courses WHERE teacher_id=?", (teacher_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_students_by_course(course_name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, g.exam1, g.project1, g.exam2, g.project2, g.exam3, g.project3
        FROM students s
        JOIN courses c ON s.course_id = c.id
        JOIN grades g ON s.id = g.student_id
        WHERE c.name = ?
    """, (course_name,))
    result = cursor.fetchall()
    conn.close()
    return result



