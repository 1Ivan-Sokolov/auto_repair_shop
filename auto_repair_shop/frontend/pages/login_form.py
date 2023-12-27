import requests
from frontend.login import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from frontend.pages.car_list import CarList as CarListWidown


class LoginForm(QMainWindow, Ui_MainWindow):
    window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        json_data = {
            'first_name':self.usernameInput.text(),
            'password':self.passwordInput.text()
        }
        response = requests.post('http://127.0.0.1:8000/client/login', json=json_data)
        if response.status_code == 200:
            self.list_window = CarListWidown()
            self.list_window.show()
            self.close()
        else:
            self.close()
