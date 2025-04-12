from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
from controller.student_controller import StudentController
from controller.teacher_controller import TeacherController
from controller.admin_controller import AdminController
from model.users_model import login_user

class LoginController(  QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.role = role
        uic.loadUi("view/login_window.ui", self)
        self.btn_login.clicked.connect(self.handle_login)

        self.view = None

    def handle_login(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        print("login passed")

        user = login_user(self.role, login, password)
        if user:
            if self.role == "student":
                self.view = StudentController(user["id"])
            elif self.role == "teacher":
                self.view = TeacherController(user["id"])
            elif self.role == "admin":
                self.view = AdminController(user["id"])
            self.view.show()
            self.hide()
        else:
            print("neverno")
            self.label_error.setText("Неверный логин или пароль")

