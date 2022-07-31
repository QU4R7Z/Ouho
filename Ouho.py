import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# //////////////////////////////////////////////////////////////////////////////
def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


# //////////////////////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Ouho")
        appIcon = QIcon(load_file("Icon/OUHO.png"))
        self.setWindowIcon(appIcon)
        self.setGeometry(0, 0, 400, 600)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
