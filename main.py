from PyQt5.QtWidgets import QApplication
import sys
from controller.main_controller import MainController
from model.database import init_db

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    main_window = MainController()
    main_window.show()
    sys.exit(app.exec_())
