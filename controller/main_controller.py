from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from controller.login_controller import LoginController

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/main_window.ui", self)

        self.btn_student.clicked.connect(self.open_student_login)
        self.btn_teacher.clicked.connect(self.open_teacher_login)
        self.btn_admin.clicked.connect(self.open_admin_login)

    def open_student_login(self):
        self.login_window = LoginController(role="student")
        self.login_window.show()
        self.hide()

    def open_teacher_login(self):
        self.login_window = LoginController(role="teacher")
        self.login_window.show()
        self.hide()

    def open_admin_login(self):
        self.login_window = LoginController(role="admin")
        self.login_window.show()
        self.hide()
