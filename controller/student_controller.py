from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from model.student_model import get_student_info, get_student_grades

class StudentController(QMainWindow):
    def __init__(self, username, password):
        super().__init__()
        uic.loadUi("view2/student_view.ui", self)

        student_info = get_student_info(username, password)
        if not student_info:
            print("Ошибка: студент не найден")
            self.close()
            return

        self.student_id, self.student_name, self.course_name, self.teacher_name = student_info

        self.studentcourse1.setText(f"Course: {self.course_name}")
        self.studentteacher1.setText(f"Teacher: {self.teacher_name}")
        self.studentname1.setText(f"Student: {self.student_name}")
        self.studentexit1.clicked.connect(self.close)

        self.load_grades()

    def load_grades(self):
        grades = get_student_grades(self.student_id)
        if not grades:
            return

        labels = ["1. Exam", "2. Project", "3. Exam", "4. Project", "5. Exam", "6. Project"]
        self.studenttable1.setRowCount(6)
        self.studenttable1.setColumnCount(1)
        self.studenttable1.setHorizontalHeaderLabels(["Grade"])

        for i, grade in enumerate(grades):
            self.studenttable1.setItem(i, 0, QTableWidgetItem(str(grade)))
            self.studenttable1.setVerticalHeaderItem(i, QTableWidgetItem(labels[i]))






