import sqlite3


def get_student_courses_and_grades(student_id):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT courses.name
        FROM grades
        JOIN courses ON grades.course_id = courses.id
        WHERE grades.student_id = ?
    ''', (student_id,))
    courses = [row[0] for row in cursor.fetchall()]

    cursor.execute('''
        SELECT courses.name, grades.grade
        FROM grades
        JOIN courses ON grades.course_id = courses.id
        WHERE grades.student_id = ?
    ''', (student_id,))
    grades = [(row[0], row[1]) for row in cursor.fetchall()]
    conn.close()
    return courses, grades
