# controller/main_controller.py

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from controller.login_controller import LoginController

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view2/mainview.ui", self)  # Убедись, что путь и имя файла совпадают

        # Привязка кнопок
        self.stdbtn.clicked.connect(self.open_student_login)
        self.teabtn.clicked.connect(self.open_teacher_login)
        self.admbtn.clicked.connect(self.open_admin_login)

    def open_student_login(self):
        print("Student button clicked")
        self.login_controller = LoginController(role="student")
        self.login_controller.show()
        self.close()

    def open_teacher_login(self):
        print("Teacher button clicked")
        self.login_controller = LoginController(role="teacher")
        self.login_controller.show()
        self.close()

    def open_admin_login(self):
        print("Admin button clicked")
        self.login_controller = LoginController(role="admin")
        self.login_controller.show()
        self.close()



