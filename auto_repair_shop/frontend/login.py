# Form implementation generated from reading ui file 'frontend/car.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 376)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(240, 240, 181, 21))
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(240, 280, 181, 21))
        self.cancelButton.setObjectName("cancelButton")
        self.usernameInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(170, 60, 301, 31))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(170, 130, 301, 31))
        self.passwordInput.setObjectName("passwordInput")
        self.text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text.setGeometry(QtCore.QRect(120, 10, 381, 31))
        self.text.setObjectName("text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Войти"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.usernameInput.setPlaceholderText(_translate("MainWindow", "Login"))
        self.passwordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добро пожаловать в автомастерскую</p></body></html>"))