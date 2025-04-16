from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from model.admin_model import get_students_by_course, get_teacher_by_course

class CourseController(QWidget):
    def __init__(self, course_name):
        super().__init__()
        ui_file = f"view2/ad{course_name.lower()}.ui"
        uic.loadUi(ui_file, self)
        self.setWindowTitle(f"{course_name} - Students")

        students = get_students_by_course(course_name)
        teacher = get_teacher_by_course(course_name)

        self.teacher_label.setText(f"Teacher: {teacher}")  # убедись, что имя метки — teacher_label

        self.table_students.setRowCount(len(students))
        for i, student in enumerate(students):
            self.table_students.setItem(i, 0, QTableWidgetItem(student["name"]))



