import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from mss import mss
from time import sleep

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 50
        self.title = "Screenshot"

        self.counter = QLabel(self)
        self.counter.setText('Say x in 5 seconds')
        self.counter.move(80, 15)
        self.counter.setStyleSheet('QLabel {font-size: 14px; color: silver}')
        self.counter.resize(130, 20)

        picBt = QPushButton(' ', self)
        picBt.move(20, 15)
        picBt.resize(40, 20)
        picBt.setStyleSheet('QPushButton {background-color: red; border-radius: 5}')
        picBt.clicked.connect(self.picture)	

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setStyleSheet('QMainWindow {background-color: #444445}')
        self.show()      

    def picture(self):
        self.counter.setText(f"Done!")
        sleep(5)
        with mss() as sct:
            sct.shot() 

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())