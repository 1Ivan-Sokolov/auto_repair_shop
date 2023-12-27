from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from frontend.car_user import Ui_MainWindow


class CarList(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
