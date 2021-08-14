from components.career_item import CareerItem
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets

items = [
    {
        "title": "chaeyong1",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong2",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong3",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong4",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong5",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong6",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong7",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "chaeyong8",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "채용9",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
    {
        "title": "채용10",
        "date": "2021/08/12 ~ 2021/08/12",
        "tag": "태그, 태그, 태그",
        "link": "링크",
    },
]


class Naver(QWidget):
    def __init__(self):
        super(Naver, self).__init__()
        self.init()
        self.load_item()
        self.load_item_view()

    def init(self):
        self.title = "이건 Naver 채용 공고 화면임"
        uic.loadUi("page/naver.ui", self)
        pass

    # 크롤링 모듈로부터 데이터 받아오는 함수
    def load_item(self):
        self.items = items

    # 컴포넌트 생성 및 값 설정
    def load_item_view(self):
        for idx, item in enumerate(self.items):
            widget = CareerItem(item, idx)
            self.content_layout.addWidget(widget)
