import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

from ui_main_window import Ui_MainWindow


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TaskSystem()
    ex.show()
    sys.exit(app.exec())

