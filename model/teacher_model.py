import sqlite3

def get_teacher_courses(teacher_id):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM courses WHERE teacher_id = ?", (teacher_id,))
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1]} for row in rows]

def get_students_by_course(course_id):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT students.id, students.name, grades.grade
        FROM students
        LEFT JOIN grades ON students.id = grades.student_id AND grades.course_id = ?
    ''', (course_id,))
    result = cursor.fetchall()
    conn.close()
    return result

def update_student_grade(student_id, course_id, grade):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    # Если оценка уже есть, обновим
    cursor.execute('''
        SELECT id FROM grades WHERE student_id = ? AND course_id = ?
    ''', (student_id, course_id))
    row = cursor.fetchone()

    if row:
        cursor.execute('''
            UPDATE grades SET grade = ? WHERE student_id = ? AND course_id = ?
        ''', (grade, student_id, course_id))
    else:
        cursor.execute('''
            INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)
        ''', (student_id, course_id, grade))

    conn.commit()
    conn.close()
