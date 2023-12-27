import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from frontend.pages.login_form import LoginForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginForm()
    login_window.show()
    app.exec()
