import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]


class Form(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = uic.loadUi("view/status.ui")
        self.ui.setupUi(self)


# 윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 불러오기
        self.ui = uic.loadUi("main.ui", self)
        # 시그널(signal) - 슬롯 연결
        self.btn_1.clicked.connect(self.print_one)
        print(self.main)
        self.main_layout.addWidget(Form(self))
        print("Button:", self.btn_1)

    def print_one(self):
        print("Clicked!!!")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
