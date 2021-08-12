import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets


class Welcome(QWidget):
    def __init__(self):
        super(Welcome, self).__init__()
        self.title = "Welcome !"
        uic.loadUi("page/welcome.ui", self)
