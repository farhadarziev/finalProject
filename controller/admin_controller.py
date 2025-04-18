from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from controller.course_view_controller import CourseViewController  # импортируем правильный контроллер

class AdminController(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view2/admview.ui", self)
        self.setWindowTitle("Admin Panel")

        self.pybtn.clicked.connect(self.open_python_course)
        self.jbtn.clicked.connect(self.open_java_course)

    def open_python_course(self):
        self.hide()  
        self.python_window = CourseViewController("py")  # передаем параметр "py" для Python
        self.python_window.show()

    def open_java_course(self):
        self.hide()  
        self.java_window = CourseViewController("java")  # передаем параметр "java" для Java
        self.java_window.show()



