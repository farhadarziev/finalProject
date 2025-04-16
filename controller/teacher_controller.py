from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from model.teacher_model import get_teacher_courses, get_students_by_course, update_student_grade
from model.teacher_model import get_teacher_info, get_teacher_courses, get_students_by_course, update_student_grade


class TeacherController(QMainWindow):
    def __init__(self, username, password):
        super().__init__()
        uic.loadUi("view2/bobview.ui", self)

        # Получаем данные преподавателя
        teacher_info = get_teacher_info(username, password)
        if not teacher_info:
            print("Ошибка: преподаватель не найден")
            self.close()
            return

        self.teacher_id, self.teacher_name = teacher_info
        self.setWindowTitle(f"{self.teacher_name} | Teacher Panel")

        self.load_courses()
        self.combo_courses.currentIndexChanged.connect(self.load_students)
        self.btn_update_grade.clicked.connect(self.update_grade)

    def show(self):
        super().show()

    def load_courses(self):
        self.courses = get_teacher_courses(self.teacher_id)
        self.combo_courses.clear()
        for course in self.courses:
            self.combo_courses.addItem(course['name'], course['id'])

    def load_students(self):
        course_id = self.combo_courses.currentData()
        students = get_students_by_course(course_id)
        self.table_students.setRowCount(len(students))
        for i, (student_id, name, grade) in enumerate(students):
            self.table_students.setItem(i, 0, QTableWidgetItem(name))
            self.table_students.setItem(i, 1, QTableWidgetItem(grade if grade else ""))
            self.table_students.setVerticalHeaderItem(i, QTableWidgetItem(str(student_id)))

    def update_grade(self):
        row = self.table_students.currentRow()
        student_name = self.table_students.item(row, 0).text()
        new_grade = self.table_students.item(row, 1).text()
        student_id = int(self.table_students.verticalHeaderItem(row).text())
        course_id = self.combo_courses.currentData()

        update_student_grade(student_id, course_id, new_grade)
