import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets


class View1(QDialog):
    def __init__(self):
        super(View1, self).__init__()
        uic.loadUi("view/view_1.ui", self)


class View2(QDialog):
    def __init__(self):
        super(View2, self).__init__()
        uic.loadUi("view/view_2.ui", self)


# 윈도우 클래스 선언
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_design.ui", self)
        # self.btn_naver.clicked.connect(lambda: self.goto(self.btn_naver))
        self.connect_events()

    def connect_events(self):
        for widget in self.sidebar.findChildren(QPushButton):
            print(
                widget.objectName()
            )  # 위젯의 오브젝트 이름까지 접근했음 이제 해당 파일의 View만 어떻게 연결시켜서 불러오면됨

    def go_to(self, btn_obj):
        print(str(btn_obj.__name__))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    # myWindow.section_body.addWidget(View1())

    widget = QStackedWidget()
    view1 = View2()
    widget.addWidget(view1)
    myWindow.section_layout.addWidget(widget)

    myWindow.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print("Error Type:", be.__class__.__name__)
        print(be)
        print("Exiting...!!!")
