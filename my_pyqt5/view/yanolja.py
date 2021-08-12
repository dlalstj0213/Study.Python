import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets


class Yanolja(QDialog):
    def __init__(self):
        super(Yanolja, self).__init__()
        self.title = "야놀자 뷰우우~"
        uic.loadUi("ui/view_2.ui", self)
