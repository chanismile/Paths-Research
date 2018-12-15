from PyQt5 import QtWidgets, uic
import main
a =''
def func():
    global a
    a = str(dlg.csv_namw_edit_text.text())

app = QtWidgets.QApplication([])
dlg = uic.loadUi("main.ui")


dlg.pushButton.clicked.connect(func)
dlg.show()
app.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

