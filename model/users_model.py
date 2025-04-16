import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from controller.admin_controller import AdminController
from controller.teacher_controller import TeacherController
from controller.student_controller import StudentController
from model.users_model import check_credentials

class LoginController(QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.role = role
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'view2', 'loginview.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Login")

        self.loginbtn.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.usernamelg.text()
        password = self.passwwr.text()

        user = check_credentials(username, password, self.role)

        if user:
            if self.role == "admin":
                self.open_admin()
            elif self.role == "teacher":
                self.open_teacher(user["linked_id"])
            elif self.role == "student":
                self.open_student(user["linked_id"])
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def open_admin(self):
        self.admin_win = AdminController()
        self.admin_win.show()
        self.close()

    def open_teacher(self, teacher_id):
        self.teacher_win = TeacherController(teacher_id)
        self.teacher_win.show()
        self.close()

    def open_student(self, student_id):
        self.student_win = StudentController(student_id)
        self.student_win.show()
        self.close()
        

