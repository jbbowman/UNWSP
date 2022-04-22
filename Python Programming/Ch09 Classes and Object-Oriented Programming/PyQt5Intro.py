from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1000, 200, 500, 500)
        self.setWindowTitle('Window Title')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Label')
        self.label.move(50, 50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('Button')
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('Button pressed')
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    application = QApplication(sys.argv)

    window1 = MyWindow()

    window1.show()
    sys.exit(application.exec_())

window()
