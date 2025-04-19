from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
import os
import sqlite3

class CourseViewController(QMainWindow):
    def __init__(self, course_name):
        super().__init__()

        ui_files = {
            "py": "pythview.ui",
            "java": "javaview.ui",
        }

        ui_file = ui_files.get(course_name.lower(), "pythview.ui")
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'view2', ui_file)
        uic.loadUi(ui_path, self)
        self.setWindowTitle(f"Course: {course_name.capitalize()}")
        self.course_name = course_name.lower()

        
        COURSE_NAME_MAP = {
            "py": "Python",
            "java": "Java"
        }

        course_db_name = COURSE_NAME_MAP.get(self.course_name, "Python")


        table = self.get_table()
        if table:
            students = get_students_by_course(course_db_name)
            table.setRowCount(len(students))
            table.setColumnCount(7)
            table.setHorizontalHeaderLabels(["Name", "Exam1", "Proj1", "Exam2", "Proj2", "Exam3", "Proj3"])
            for i, row in enumerate(students):
                table.setItem(i, 0, QTableWidgetItem(row[0]))
                for j in range(1, 7):
                    table.setItem(i, j, QTableWidgetItem(str(row[j])))
        else:
            print("[ERROR] Таблица не найдена")
            

        
        if self.course_name == "py":
            if hasattr(self, "backbtnpy"):
                self.backbtnpy.clicked.connect(self.go_back)
            if hasattr(self, "addbtn"):
                self.addbtn.clicked.connect(self.add_row)
            if hasattr(self, "delbtn"):
                self.delbtn.clicked.connect(self.delete_row)

        elif self.course_name == "java":
            if hasattr(self, "backjbtnpy"):
                self.backjbtnpy.clicked.connect(self.go_back)
            if hasattr(self, "addjbtn"):
                self.addjbtn.clicked.connect(self.add_row)
            if hasattr(self, "deljbtn"):
                self.deljbtn.clicked.connect(self.delete_row)

    def get_table(self):
        if self.course_name == "py" and hasattr(self, "pythtable"):
            return self.pythtable
        elif self.course_name == "java" and hasattr(self, "javatable"):
            return self.javatable
        return None

    def go_back(self):
        self.close()
        from controller.admin_controller import AdminController
        self.window = AdminController()
        self.window.show()

    def add_row(self):
        table = self.get_table()
        if table:
            if table.columnCount() < 7:
                table.setColumnCount(7)
                table.setHorizontalHeaderLabels(["Name", "Exam1", "Proj1", "Exam2", "Proj2", "Exam3", "Proj3"])
            row_count = table.rowCount()
            table.insertRow(row_count)
            table.setItem(row_count, 0, QTableWidgetItem("New Student"))
            for i in range(1, 7):
                table.setItem(row_count, i, QTableWidgetItem("0"))

    def delete_row(self):
        table = self.get_table()
        if table:
            selected = table.currentRow()
            if selected >= 0:
                table.removeRow(selected)
            else:
                QMessageBox.warning(self, "Warning", "Please select a row to delete.")

def get_students_by_course(course_name):
    try:
        db_path = os.path.join(os.path.dirname(__file__), "..", "database", "sis.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT s.name, g.exam1, g.project1, g.exam2, g.project2, g.exam3, g.project3
            FROM students s
            JOIN grades g ON s.id = g.student_id
            JOIN courses c ON g.course_id = c.id
            WHERE LOWER(c.name) = LOWER(?)
        """, (course_name,))
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return []
