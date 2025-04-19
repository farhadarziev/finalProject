import os
import sqlite3

def get_db_connection():
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(base_dir, "..", "database", "sis.db")
    return sqlite3.connect(db_path)

def update_student_grades(student_id, grades_dict):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE grades
        SET exam1 = ?, project1 = ?, exam2 = ?, project2 = ?, exam3 = ?, project3 = ?
        WHERE student_id = ?
        ''',
        (
            grades_dict.get("exam1", 0),
            grades_dict.get("project1", 0),
            grades_dict.get("exam2", 0),
            grades_dict.get("project2", 0),
            grades_dict.get("exam3", 0),
            grades_dict.get("project3", 0),
            student_id
        )
    )

    conn.commit()
    conn.close()

def get_students_by_course(course_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            SELECT s.id, s.name, g.exam1, g.project1, g.exam2, g.project2, g.exam3, g.project3
            FROM students s
            JOIN grades g ON s.id = g.student_id
            JOIN courses c ON s.course_id = c.id
            WHERE LOWER(c.name) = LOWER(?)
        """
        cursor.execute(query, (course_name,))
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        print("[ERROR in get_students_by_course]:", e)
        return []

def get_teacher_info(teacher_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM teachers WHERE id = ?", (teacher_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        print("[ERROR in get_teacher_info]:", e)
        return None

def get_teacher_course_name(teacher_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM courses WHERE teacher_id = ?", (teacher_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    except Exception as e:
        print("[ERROR in get_teacher_course_name]:", e)
        return None
