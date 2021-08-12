import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets


class ErrorPage(QWidget):
    def __init__(self):
        super(ErrorPage, self).__init__()
        self.title = "Page Not Found!"
        uic.loadUi("page/error_page.ui", self)
