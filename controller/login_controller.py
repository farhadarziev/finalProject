from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from controller.admin_controller import AdminController
from controller.teacher_controller import TeacherController
from controller.student_controller import StudentController
from model.user_model import check_user_credentials

class LoginController(QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.role = role
        uic.loadUi("view2/loginview.ui", self)
        self.setWindowTitle(f"{role.capitalize()} Login")

        self.loginbtn.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.usernamelg.text()
        password = self.passwwr.text()

        user = check_user_credentials(username, password)
        print(f"[DEBUG] login result: {user}")  # можно удалить позже

        if user:
            role = user["role"]
            if role == "admin":
                self.hide()
                self.admin = AdminController()
                self.admin.show()
            elif role == "teacher":
                self.hide()
                self.teacher = TeacherController(username, password)
                self.teacher.show()
            elif role == "student":
                self.hide()
                self.student = StudentController(username, password)
                self.student.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")




