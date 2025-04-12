import sqlite3
import os
import random

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    # Удалим старые таблицы
    cursor.executescript('''
    DROP TABLE IF EXISTS grades;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS teachers;
    DROP TABLE IF EXISTS admins;
    ''')

    # Создание таблиц
    cursor.executescript('''
    CREATE TABLE admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    );

    CREATE TABLE grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );
    ''')

    # Данные: админ
    cursor.execute("INSERT INTO admins (name, login, password) VALUES (?, ?, ?)", ("Administrator", "admin", "admin123"))

    # Преподаватели
    teachers = [("Alice Smith", "alice", "alice123"), ("Bob Johnson", "bob", "bob123")]
    cursor.executemany("INSERT INTO teachers (name, login, password) VALUES (?, ?, ?)", teachers)

    cursor.execute("SELECT id FROM teachers WHERE login = 'alice'")
    alice_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM teachers WHERE login = 'bob'")
    bob_id = cursor.fetchone()[0]

    # Курсы
    courses = [
        ("Python", alice_id),
        ("C++", alice_id),
        ("Java", bob_id),
        ("JavaScript", bob_id)
    ]
    cursor.executemany("INSERT INTO courses (name, teacher_id) VALUES (?, ?)", courses)

    cursor.execute("SELECT id, name FROM courses")
    course_map = {name: cid for cid, name in cursor.fetchall()}

    # Студенты
    first_names = [f"Student {i+1}" for i in range(50)]
    students = [(name, f"student{i+1}", "pass123") for i, name in enumerate(first_names)]
    cursor.executemany("INSERT INTO students (name, login, password) VALUES (?, ?, ?)", students)

    cursor.execute("SELECT id FROM students")
    student_ids = [row[0] for row in cursor.fetchall()]

    # Распределение студентов по курсам
    assignments = {
        course_map["Python"]: student_ids[:15],
        course_map["C++"]: student_ids[15:25],
        course_map["Java"]: student_ids[25:40],
        course_map["JavaScript"]: student_ids[40:]
    }

    # Оценки
    possible_grades = ["A", "B", "C", "D", "F"]
    grades_data = []
    for course_id, s_list in assignments.items():
        for sid in s_list:
            grade = random.choice(possible_grades)
            grades_data.append((sid, course_id, grade))

    cursor.executemany("INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)", grades_data)

    conn.commit()
    conn.close()
