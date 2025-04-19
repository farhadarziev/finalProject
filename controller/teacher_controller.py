from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from model.teacher_model import get_students_by_course, get_teacher_info, get_teacher_course_name
from model.teacher_model import update_student_grades
from PyQt5.QtCore import pyqtSignal

class TeacherController(QMainWindow):
    grade_updated_signal = pyqtSignal()  

    def __init__(self, teacher_id):
        super().__init__()
        try:
            uic.loadUi("view2/teacher_view.ui", self)

            teacher_info = get_teacher_info(teacher_id)
            if not teacher_info:
                QMessageBox.critical(self, "Error", "The instructor was not found in the database.")
                self.close()
                return

            self.teacher_id, self.teacher_name = teacher_info
            self.label_teacher.setText(f"Teacher: {self.teacher_name}")

            self.course_name = get_teacher_course_name(self.teacher_id)
            self.label_course.setText(f"Course: {self.course_name}")

            self.load_students()
            self.grade_updated_signal.connect(self.load_students) 
            self.btn_exit.clicked.connect(self.close)

        except Exception as e:
            print("[ERROR in TeacherController __init__]:", e)
            QMessageBox.critical(self, "Error", f"Error when loading the instructor interface:\n{e}")
            self.close()

    def load_students(self):
        try:
            students = get_students_by_course(self.course_name)
            self.table_students.setRowCount(len(students))
            self.table_students.setColumnCount(7)
            self.table_students.setHorizontalHeaderLabels([
                "Name", "Exam 1", "Project 1", "Exam 2", "Project 2", "Exam 3", "Project 3"
            ])
            self.table_students.verticalHeader().setVisible(False)

            for row, student in enumerate(students):
                student_id, name, *grades = student
                self.table_students.setItem(row, 0, QTableWidgetItem(name))
                for col, grade in enumerate(grades):
                    self.table_students.setItem(row, col + 1, QTableWidgetItem(str(grade)))

        except Exception as e:
            print("[ERROR in load_students]:", e)
            QMessageBox.critical(self, "Error", f"Failed to load students:\n{e}")
            self.close()

    def save_grades(self):
        """Saving grade changes to the database"""
        student_id = get_student_id_by_name(self.table_students.item(self.table_students.currentRow(), 0).text())
        grades = {
            "exam1": self.table_students.item(self.table_students.currentRow(), 1).text(),
            "project1": self.table_students.item(self.table_students.currentRow(), 2).text(),
            "exam2": self.table_students.item(self.table_students.currentRow(), 3).text(),
            "project2": self.table_students.item(self.table_students.currentRow(), 4).text(),
            "exam3": self.table_students.item(self.table_students.currentRow(), 5).text(),
            "project3": self.table_students.item(self.table_students.currentRow(), 6).text(),
        }
        update_student_grades(student_id, grades)

        
        self.grade_updated_signal.emit()

def get_table_data(table):
    try:
        data = {}
        for row in range(table.rowCount()):
            student_name = table.item(row, 0).text()
            student_id = get_student_id_by_name(student_name)
            if student_id:
                grades = {
                    "exam1": int(table.item(row, 1).text()),
                    "project1": int(table.item(row, 2).text()),
                    "exam2": int(table.item(row, 3).text()),
                    "project2": int(table.item(row, 4).text()),
                    "exam3": int(table.item(row, 5).text()),
                    "project3": int(table.item(row, 6).text()),
                }
                update_student_grades(student_id, grades)
    except Exception as e:
        print("[ERROR in get_table_data]:", e)

def get_student_id_by_name(name):
    try:
        import sqlite3
        import os
        db_path = os.path.join(os.path.dirname(__file__), "..", "database", "sis.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM students WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    except Exception as e:
        print("[ERROR in get_student_id_by_name]:", e)
        return None