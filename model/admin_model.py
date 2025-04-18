import sqlite3

def get_students_by_course(course):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name FROM students s 
        JOIN courses c ON s.course_id = c.id 
        WHERE c.name = ?
    """, (course,))
    students = [{"name": row[0]} for row in cursor.fetchall()]
    conn.close()
    return students

def get_teacher_by_course(course):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.name FROM teachers t 
        JOIN courses c ON t.id = c.teacher_id 
        WHERE c.name = ?
    """, (course,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Not Assigned"



