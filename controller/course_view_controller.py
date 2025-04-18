from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
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
        self.course_name = course_name.lower()

        print("[DEBUG] ВСЕ ЭЛЕМЕНТЫ В ОКНЕ:")
        for attr in dir(self):
            if not attr.startswith("__"):
                print(" >", attr)

        if self.course_name == "py":
            if hasattr(self, "backbtnpy"):
                self.backbtnpy.clicked.connect(self.go_back)
            if hasattr(self, "addbtn"):
                print("[DEBUG] addbtn подключается")
                self.addbtn.clicked.connect(self.add_row)
            if hasattr(self, "delbtn"):
                print("[DEBUG] delbtn подключается")
                self.delbtn.clicked.connect(self.delete_row)

        elif self.course_name == "java":
            if hasattr(self, "backjbtnpy"):
                self.backjbtnpy.clicked.connect(self.go_back)
            if hasattr(self, "addjbtn"):
                print("[DEBUG] addjbtn подключается")
                self.addjbtn.clicked.connect(self.add_row)
            if hasattr(self, "deljbtn"):
                print("[DEBUG] deljbtn подключается")
                self.deljbtn.clicked.connect(self.delete_row)

    def go_back(self):
        self.close()
        from controller.admin_controller import AdminController
        self.window = AdminController()
        self.window.show()

    def get_table(self):
        if self.course_name == "py" and hasattr(self, "pythtable"):
            return self.pythtable
        elif self.course_name == "java" and hasattr(self, "javatable"):
            return self.javatable
        print("[DEBUG] Таблица не найдена")
        return None

    def add_row(self):
        print("[DEBUG] Кнопка Add нажата")
        table = self.get_table()
        if table:
            if table.columnCount() < 7:
                table.setColumnCount(7)
                table.setHorizontalHeaderLabels(["Name", "Exam1", "Proj1", "Exam2", "Proj2", "Exam3", "Proj3"])
            row_count = table.rowCount()
            table.insertRow(row_count)
            table.setItem(row_count, 0, QTableWidgetItem("New Student"))
            for i in range(1, 7):
                table.setItem(row_count, i, QTableWidgetItem("0"))

    def delete_row(self):
        print("[DEBUG] Кнопка Delete нажата")
        table = self.get_table()
        if table:
            selected = table.currentRow()
            if selected >= 0:
                table.removeRow(selected)
            else:
                QMessageBox.warning(self, "Warning", "Please select a row to delete.")
