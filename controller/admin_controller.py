from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from controller.course_view_controller import CourseViewController

class AdminController(QMainWindow):
    def __init__(self, admin_id=None):
        super().__init__()
        uic.loadUi("view/admin_courses.ui", self)
        self.setWindowTitle("Admin - Course Overview")

        self.btn_python.clicked.connect(lambda: self.open_course("Python"))
        self.btn_cpp.clicked.connect(lambda: self.open_course("C++"))
        self.btn_java.clicked.connect(lambda: self.open_course("Java"))
        self.btn_js.clicked.connect(lambda: self.open_course("JavaScript"))

    def open_course(self, course_name):
        self.course_view = CourseViewController(course_name)
        self.course_view.show()
        self.hide()

