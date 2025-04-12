from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from model.admin_model import get_students_by_course, get_teacher_by_course

class CourseViewController(QMainWindow):
    def __init__(self, course_name):
        super().__init__()
        uic.loadUi("view/course_view.ui", self)
        self.setWindowTitle(f"{course_name} - Students & Teacher")

        # ✅ Подключаем кнопку "Back"
        self.btn_back.clicked.connect(self.go_back)

        # Загрузка данных
        students = get_students_by_course(course_name)
        teacher = get_teacher_by_course(course_name)

        self.label_teacher.setText(f"Teacher: {teacher}")

        self.table_students.setRowCount(len(students))
        self.table_students.setColumnCount(2)
        self.table_students.setHorizontalHeaderLabels(["Student", "Grade"])

        for i, (student_name, grade) in enumerate(students):
            self.table_students.setItem(i, 0, QTableWidgetItem(student_name))
            self.table_students.setItem(i, 1, QTableWidgetItem(str(grade)))

    def go_back(self):
        from controller.admin_controller import AdminController
        self.admin_menu = AdminController()
        self.admin_menu.show()
        self.close()
