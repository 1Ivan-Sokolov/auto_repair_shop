# Form implementation generated from reading ui file 'frontend/car_user.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 611)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.searchLine = QtWidgets.QLineEdit(parent=self.groupBox)
        self.searchLine.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.searchLine.setPlaceholderText("")
        self.searchLine.setObjectName("searchLine")
        self.horizontalLayout_2.addWidget(self.searchLine)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout.addWidget(self.searchButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tw_user_list = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tw_user_list.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_user_list.setAlternatingRowColors(True)
        self.tw_user_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tw_user_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_user_list.setColumnCount(1)
        self.tw_user_list.setObjectName("tw_user_list")
        self.tw_user_list.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(0, item)
        self.tw_user_list.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.tw_user_list)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список пользователей"))
        self.searchLine.setText(_translate("MainWindow", "Поиск"))
        self.searchButton.setText(_translate("MainWindow", "Найти"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Характеристика"))
        item = self.tw_user_list.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "номер заявки"))
        item = self.tw_user_list.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата добавления"))
        item = self.tw_user_list.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Автомобиль"))
        item = self.tw_user_list.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип неисправности"))
        item = self.tw_user_list.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание проблемы"))
        item = self.tw_user_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Характеристики"))
