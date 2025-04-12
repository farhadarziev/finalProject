from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from model.user_model import get_student_courses_and_grades

class StudentController(QWidget):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        uic.loadUi("view/student_view.ui", self)

        print("xcdcd")
        self.load_data()

    def load_data(self):
        courses, grades = get_student_courses_and_grades(self.student_id)
        print("Загрузка курсов и оценок...")

        self.table_courses.setRowCount(len(courses))
        for i, course in enumerate(courses):
            self.table_courses.setItem(i, 0, QTableWidgetItem(course))

        self.table_grades.setRowCount(len(grades))
        for i, (course, grade) in enumerate(grades):
            self.table_grades.setItem(i, 0, QTableWidgetItem(course))
            self.table_grades.setItem(i, 1, QTableWidgetItem(grade))
