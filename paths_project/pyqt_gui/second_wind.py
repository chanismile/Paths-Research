# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_wind.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_secondWindow(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filter_by_hours = QtWidgets.QRadioButton(self.centralwidget)
        self.filter_by_hours.setGeometry(QtCore.QRect(20, 60, 91, 17))
        self.filter_by_hours.setObjectName("filter_by_hours")
        self.filter_by_hours_in_specific_date = QtWidgets.QRadioButton(self.centralwidget)
        self.filter_by_hours_in_specific_date.setGeometry(QtCore.QRect(20, 100, 161, 17))
        self.filter_by_hours_in_specific_date.setObjectName("filter_by_hours_in_specific_date")
        self.filter_by_area = QtWidgets.QRadioButton(self.centralwidget)
        self.filter_by_area.setGeometry(QtCore.QRect(20, 140, 82, 17))
        self.filter_by_area.setObjectName("filter_by_area")
        self.filter_by_specific_area = QtWidgets.QRadioButton(self.centralwidget)
        self.filter_by_specific_area.setGeometry(QtCore.QRect(20, 180, 121, 17))
        self.filter_by_specific_area.setObjectName("filter_by_specific_area")
        self.filter = QtWidgets.QPushButton(self.centralwidget)
        self.filter.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.filter.setObjectName("filter")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.date_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.date_calendar.setGeometry(QtCore.QRect(190, 60, 321, 191))
        self.date_calendar.setGridVisible(True)
        self.date_calendar.setObjectName("date_calendar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filter_by_hours.setText(_translate("MainWindow", "filter by hours"))
        self.filter_by_hours_in_specific_date.setText(_translate("MainWindow", "filter by hours in specific date"))
        self.filter_by_area.setText(_translate("MainWindow", "filter by area"))
        self.filter_by_specific_area.setText(_translate("MainWindow", "filter by specific area"))
        self.filter.setText(_translate("MainWindow", "filter"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Select the filters you want</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

