from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from model.teacher_model import get_teacher_info, get_teacher_course_name, get_students_by_course

class TeacherController(QMainWindow):
    def __init__(self, teacher_id):
        super().__init__()
        uic.loadUi("view2/teacher_view.ui", self)

        teacher_info = get_teacher_info(teacher_id)
        if not teacher_info:
            print("Ошибка: преподаватель не найден")
            self.close()
            return

        self.teacher_id, self.teacher_name = teacher_info
        self.label_teacher.setText(f"Teacher: {self.teacher_name}")

        self.course_name = get_teacher_course_name(self.teacher_id)
        self.label_course.setText(f"Course: {self.course_name}")

        self.load_students()
        self.btn_exit.clicked.connect(self.close)

    def load_students(self):
        students = get_students_by_course(self.course_name)
        self.table_students.setRowCount(len(students))
        self.table_students.setColumnCount(6)
        self.table_students.setHorizontalHeaderLabels([
            "Exam 1", "Project 1", "Exam 2", "Project 2", "Exam 3", "Project 3"
        ])

        for row, (name, *grades) in enumerate(students):
            self.table_students.setVerticalHeaderItem(row, QTableWidgetItem(name))
            for col, grade in enumerate(grades):
                self.table_students.setItem(row, col, QTableWidgetItem(str(grade)))

