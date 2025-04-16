from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from model.student_model import get_student_info  # Функция должна вернуть имя, курс, оценки

class StudentController(QMainWindow):
    def __init__(self, student_id):
        super().__init__()
        uic.loadUi("view2/student_view.ui", self)  # путь до твоего .ui файла

        student_data = get_student_info(student_id)  # например, словарь: {'name': 'Lori Little', 'course': 'Python', 'grades': [...]}

        # Обновим интерфейс
        self.label_course.setText(f"Course: {student_data['course']}")
        self.label_name.setText(f"Student: {student_data['name']}")

        # Таблица оценок
        grades = student_data['grades']  # например, [85, 90, 78, 92, 88, 75]
        for i, grade in enumerate(grades):
            self.table_grades.setItem(i, 0, QTableWidgetItem(f"Grade {i+1}"))
            self.table_grades.setItem(i, 1, QTableWidgetItem(str(grade)))

