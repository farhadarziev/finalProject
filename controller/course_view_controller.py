from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import os

class CourseViewController(QMainWindow):
    def __init__(self, course_name):
        super().__init__()
        
        ui_files = {
            "py": "pythview.ui",
            "java": "javaview.ui",      
        }

        ui_file = ui_files.get(course_name.lower(), "pythview.ui")
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'view2', ui_file)
        uic.loadUi(ui_path, self)

        self.setWindowTitle(f"Course: {course_name.capitalize()}")

        # Подключение back-кнопки с любым именем
        for btn_name in ["backbtn", "backbtnpy", "backjbtnpy"]:
            if hasattr(self, btn_name):
                getattr(self, btn_name).clicked.connect(self.go_back)
                break  # нашли кнопку — подключили, хватит

    def go_back(self):
        self.close()
        from controller.admin_controller import AdminController
        self.window = AdminController()
        self.window.show()

