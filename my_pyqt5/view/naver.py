import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets


class Naver(QDialog):
    def __init__(self):
        super(Naver, self).__init__()
        self.title = "이건 Naver 채용 공고 화면임"
        uic.loadUi("ui/view_1.ui", self)
