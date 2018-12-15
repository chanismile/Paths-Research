# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from second_wind import *
import controller

class Ui_MainWindow(object):
    def openSecondWindow(self):
        self.window = QtWidgets.QMainWindow()

        self.ui = Ui_secondWindow()
        self.ui.setup(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_lable = QtWidgets.QLabel(self.centralwidget)
        self.welcome_lable.setGeometry(QtCore.QRect(60, 100, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(22)
        self.welcome_lable.setFont(font)
        self.welcome_lable.setObjectName("welcome_lable")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 120, 271, 111))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(343, 156, 271, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 160, 93, 28))
        # self.pushButton.clicked.connect(self.openSecondWindow)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        global CSV_NAME
        CSV_NAME = ''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_lable.setText(_translate("MainWindow", "Welcome! "))
        self.label.setText(_translate("MainWindow", "Enter a csv file name:"))
        self.pushButton.setText(_translate("MainWindow", "ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

