import sqlite3
import os
import random

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/sis.db")
    cursor = conn.cursor()

    cursor.executescript('''
    DROP TABLE IF EXISTS grades;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS teachers;
    DROP TABLE IF EXISTS admins;
    ''')


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
        password TEXT NOT NULL,
        course TEXT NOT NULL
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
        project1 INTEGER,
        project2 INTEGER,
        project3 INTEGER,
        exam1 INTEGER,
        exam2 INTEGER,
        exam3 INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    ''')

    
    cursor.execute("INSERT INTO admins (name, login, password) VALUES (?, ?, ?)", ("Administrator", "admin", "admin123"))

 
    teachers = [("Alice Smith", "alice", "alice123"), ("Bob Johnson", "bob", "bob123")]
    cursor.executemany("INSERT INTO teachers (name, login, password) VALUES (?, ?, ?)", teachers)


    cursor.execute("SELECT id FROM teachers WHERE login = 'alice'")
    alice_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM teachers WHERE login = 'bob'")
    bob_id = cursor.fetchone()[0]


    courses = [
        ("Python", alice_id),
        ("Java", bob_id)
    ]
    cursor.executemany("INSERT INTO courses (name, teacher_id) VALUES (?, ?)", courses)


    students = [
        ("Beth Grimes", "beth", "beth123", "Python"),
        ("Christopher Watkins", "chris", "chris123", "Python"),
        ("Charles Stark", "charles", "charles123", "Python"),
        ("Gerald Lee", "gerald", "gerald123", "Java"),
        ("Louise Lawrence", "louise", "louise123", "Java"),
        ("Gary Bates-Baker", "gary", "gary123", "Java")
    ]
    cursor.executemany("INSERT INTO students (name, login, password, course) VALUES (?, ?, ?, ?)", students)

    cursor.execute("SELECT id, course FROM students")
    student_data = cursor.fetchall()

    for student_id, course in student_data:
        grades = [random.randint(60, 100) for _ in range(6)]
        cursor.execute('''
            INSERT INTO grades (student_id, project1, project2, project3, exam1, exam2, exam3)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (student_id, *grades))

    conn.commit()
    conn.close()
