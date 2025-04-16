import sys
from PyQt5.QtWidgets import QApplication
from controller.main_controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainController()
    main_window.show()
    sys.exit(app.exec_())
