import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets
from view.welcome import Welcome
from view.error_page import ErrorPage

# 메인윈도우 클래스 선언
class MainWindow(QMainWindow):
    txt_status = None

    def __init__(self):
        super().__init__()
        uic.loadUi("ui_design.ui", self)
        self.current_menu = None
        self.prev_menu = None
        self.widget_content = QStackedWidget()
        self.init_main()

    def init_main(self):
        self.section_layout.addWidget(self.widget_content)
        self.connect_events()
        welcome = Welcome()
        self.go_to(target=welcome)
        self.section_title.setText("# " + welcome.title)
        MainWindow.txt_status = self.txt_status

    # 메뉴 이벤트 연결
    def connect_events(self):
        self.btn_news.clicked.connect(lambda: self.go_to(self.btn_news))
        self.btn_naver.clicked.connect(lambda: self.go_to(self.btn_naver))
        self.btn_kakao.clicked.connect(lambda: self.go_to(self.btn_kakao))
        self.btn_line.clicked.connect(lambda: self.go_to(self.btn_line))
        self.btn_coupang.clicked.connect(lambda: self.go_to(self.btn_coupang))
        self.btn_baemin.clicked.connect(lambda: self.go_to(self.btn_baemin))
        self.btn_daangn.clicked.connect(lambda: self.go_to(self.btn_daangn))
        self.btn_toss.clicked.connect(lambda: self.go_to(self.btn_toss))
        self.btn_zigbang.clicked.connect(lambda: self.go_to(self.btn_zigbang))
        self.btn_yanolja.clicked.connect(lambda: self.go_to(self.btn_yanolja))

        # self.sidebar.findChild(QPushButton, "btn_naver").clicked.connect(
        #     lambda: self.go_to("btn_naver")
        # )

        # 실패, 반복문만 사용하면 이벤트 결과가 덮여씌여짐...ㅡㅡ
        # 문자열 배열로 하드코딩해서 해도 결과는 같음...
        # for button in self.sidebar.findChildren(QPushButton):
        #     button.clicked.connect(lambda: self.go_to(button))

    def go_to(self, btn_obj="", target=None):
        view = None
        if target == None:
            view = self.load_view(btn_obj.objectName())
        else:
            view = target

        if view == None:
            error_page = ErrorPage()
            self.section_title.setText("# " + error_page.title)
            self.go_to(target=error_page)
            if self.prev_menu != None:
                self.prev_menu.setStyleSheet("")
            return
        # QStackWidget의 인덱스를 계속해서 추가하는 방법도 있지만
        # 그냥 현재 위젯을 삭제하고 다시 새로운 위젯을 추가하여 인덱스를 0으로 고정시키는 방법을 구상함
        if self.widget_content.currentWidget() != None:
            self.widget_content.removeWidget(self.widget_content.currentWidget())
        self.widget_content.addWidget(view)
        # self.widget_content.setCurrentIndex(self.widget_content.currentIndex() + 1) # 인덱스 추가
        self.widget_content.setCurrentIndex(0)

        if self.widget_content.currentWidget() != None and target == None:
            self.section_title.setText("# " + view.title)
            if self.prev_menu != None:
                self.prev_menu.setStyleSheet("")
            self.prev_menu = btn_obj
            btn_obj.setStyleSheet(
                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"
            )
            MainWindow.append_status_msg("페이지 로드 성공")

    # 모듈 동적 임포트 후 뷰 클래스 로드
    # ex) btn_something -> find -> view.Something()
    def load_view(self, object_name):
        mod = None
        try:
            module_name = str(object_name).split("_")[1]
            class_name = module_name[0].upper() + module_name[1:]
            mod = __import__("view." + str(module_name), fromlist=[str(module_name)])
        except BaseException as be:
            print(be)
            MainWindow.append_status_msg(str(be), be.__class__.__name__)
        else:
            return getattr(mod, class_name)()
        return None

    @classmethod
    def append_status_msg(cls, msg, error_type=None):

        simple_html = '<font color="white">'
        error_html = '<font color="DeepPink">'
        warn_html = '<font color="yellow">'
        success_html = '<font color="Lime">'
        info_html = '<font color="Aqua">'
        end_html = "</font><br>"

        default = str(datetime.datetime.now()) + " >>> "
        status_msg = ""

        # print(cls.txt_status.toPlainText())  # 값 거져오기
        # cls.txt_status.setText(msg) # 값 대입
        error_type = (
            None if error_type == None or error_type.strip() == "" else error_type
        )
        if error_type == None:
            status_msg += info_html + default + simple_html + msg
        else:
            status_msg += error_html + default + error_type + "::: " + warn_html + msg

        cls.txt_status.append(status_msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print("Error Type:", be.__class__.__name__)
        print(be)
        print("Exiting...!!!")
