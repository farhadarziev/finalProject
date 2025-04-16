def get_student_info(student_id):
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    cursor.execute("SELECT full_name, course FROM students WHERE id = ?", (student_id,))
    student_row = cursor.fetchone()

    cursor.execute("SELECT project1, project2, project3, exam1, exam2, exam3 FROM grades WHERE student_id = ?", (student_id,))
    grade_row = cursor.fetchone()

    conn.close()

    return student_row[0], student_row[1], grade_row


