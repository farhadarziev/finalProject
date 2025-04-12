from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from model.admin_model import get_all_students, get_all_teachers, delete_user

class AdminController(QWidget):
    def __init__(self, admin_id=None):
        super().__init__()
        uic.loadUi("view/admin_view.ui", self)

        self.load_students()
        self.load_teachers()

        self.btn_delete_student.clicked.connect(self.delete_selected_student)
        self.btn_delete_teacher.clicked.connect(self.delete_selected_teacher)

    def show(self):
        super().show()

    def load_students(self):
        students = get_all_students()
        self.table_students.setRowCount(len(students))
        for i, (id, name, login) in enumerate(students):
            self.table_students.setItem(i, 0, QTableWidgetItem(str(id)))
            self.table_students.setItem(i, 1, QTableWidgetItem(name))
            self.table_students.setItem(i, 2, QTableWidgetItem(login))

    def load_teachers(self):
        teachers = get_all_teachers()
        self.table_teachers.setRowCount(len(teachers))
        for i, (id, name, login) in enumerate(teachers):
            self.table_teachers.setItem(i, 0, QTableWidgetItem(str(id)))
            self.table_teachers.setItem(i, 1, QTableWidgetItem(name))
            self.table_teachers.setItem(i, 2, QTableWidgetItem(login))

    def delete_selected_student(self):
        row = self.table_students.currentRow()
        student_id = int(self.table_students.item(row, 0).text())
        delete_user("students", student_id)
        self.load_students()

    def delete_selected_teacher(self):
        row = self.table_teachers.currentRow()
        teacher_id = int(self.table_teachers.item(row, 0).text())
        delete_user("teachers", teacher_id)
        self.load_teachers()
