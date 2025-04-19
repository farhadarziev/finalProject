import sqlite3

def get_student_info(username, password):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.id, s.name, c.name, t.name
        FROM students s
        JOIN courses c ON s.course_id = c.id
        JOIN teachers t ON c.teacher_id = t.id
        WHERE s.login = ? AND s.password = ?

    """, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def get_student_grades(student_id):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT exam1, project1, exam2, project2, exam3, project3
        FROM grades
        WHERE student_id = ?

    """, (student_id,))
    grades = cursor.fetchone()
    conn.close()
    return grades

