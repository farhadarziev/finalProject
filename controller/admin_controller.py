from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from controller.course_view_controller import CourseController  

class AdminController(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("view2/admview.ui", self)

        self.pybtn.clicked.connect(lambda: self.open_course("Python"))
        self.cbtn.clicked.connect(lambda: self.open_course("C++"))
        self.jbtn.clicked.connect(lambda: self.open_course("Java"))
        self.jsbtn.clicked.connect(lambda: self.open_course("JavaScript"))

    def open_course(self, course_name):
        self.hide()
        self.course_view = CourseController(course_name)
        self.course_view.show()

