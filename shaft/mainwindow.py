from PySide6.QtWidgets import QMainWindow
from ui.shaft_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
