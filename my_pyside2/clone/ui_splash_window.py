# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading_windowgJgdSp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import python_app_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(742, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_bg_frame = QFrame(self.centralwidget)
        self.main_bg_frame.setObjectName(u"main_bg_frame")
        self.main_bg_frame.setGeometry(QRect(10, 89, 600, 400))
        self.main_bg_frame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(55, 115, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom: 5px solid rgb(255, 209, 65);\n"
"border-right: 5px solid rgb(54, 110, 156);\n"
"border-top: 5px solid rgb(54, 110, 156);\n"
"border-left: 5px solid rgb(255, 209, 65);")
        self.main_bg_frame.setFrameShape(QFrame.StyledPanel)
        self.main_bg_frame.setFrameShadow(QFrame.Raised)
        self.logo_frame = QFrame(self.main_bg_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(0, 0, 181, 151))
        self.logo_frame.setStyleSheet(u"image: url(:/images/image/python_logo.png);\n"
"background-color: none;\n"
"border: none")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.middle_line_first = QFrame(self.main_bg_frame)
        self.middle_line_first.setObjectName(u"middle_line_first")
        self.middle_line_first.setGeometry(QRect(70, 20, 600, 600))
        self.middle_line_first.setStyleSheet(u"background-color: none;\n"
"border: 10px solid rgb(51, 106, 150);\n"
"border-radius: 300px;")
        self.middle_line_first.setFrameShape(QFrame.StyledPanel)
        self.middle_line_first.setFrameShadow(QFrame.Raised)
        self.welcome_label = QLabel(self.main_bg_frame)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(180, 130, 351, 71))
        font = QFont()
        font.setFamily(u"Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet(u"border: none;\n"
"background-color: none;")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.more_info_frame = QFrame(self.main_bg_frame)
        self.more_info_frame.setObjectName(u"more_info_frame")
        self.more_info_frame.setGeometry(QRect(120, 200, 481, 201))
        self.more_info_frame.setStyleSheet(u"background-color: rgb(51, 106, 150);\n"
"border-bottom: 5px solid rgb(255, 209, 65);\n"
"border-top: 5px solid rgb(54, 110, 156);\n"
"border-right: 5px solid rgb(255, 209, 65);\n"
"border-left: 5px solid rgb(255, 209, 65);\n"
"border-radius: 20px;")
        self.more_info_frame.setFrameShape(QFrame.StyledPanel)
        self.more_info_frame.setFrameShadow(QFrame.Raised)
        self.loading_status = QLabel(self.more_info_frame)
        self.loading_status.setObjectName(u"loading_status")
        self.loading_status.setGeometry(QRect(10, 10, 461, 51))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.loading_status.setFont(font1)
        self.loading_status.setStyleSheet(u"border:none;\n"
"color:rgb(255, 255, 255);")
        self.loading_status.setAlignment(Qt.AlignCenter)
        self.loading_progress_status = QLabel(self.more_info_frame)
        self.loading_progress_status.setObjectName(u"loading_progress_status")
        self.loading_progress_status.setGeometry(QRect(320, 70, 141, 41))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.loading_progress_status.setFont(font2)
        self.loading_progress_status.setStyleSheet(u"border:none;\n"
"color:rgb(255, 255, 255);")
        self.loading_progress_status.setAlignment(Qt.AlignCenter)
        self.loading_progress_status.setWordWrap(True)
        self.credit_label = QLabel(self.more_info_frame)
        self.credit_label.setObjectName(u"credit_label")
        self.credit_label.setGeometry(QRect(20, 150, 221, 41))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setBold(True)
        font3.setWeight(75)
        self.credit_label.setFont(font3)
        self.credit_label.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")
        self.my_progressBar = QProgressBar(self.more_info_frame)
        self.my_progressBar.setObjectName(u"my_progressBar")
        self.my_progressBar.setGeometry(QRect(20, 80, 301, 21))
        self.my_progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color:rgb(51, 106, 150);\n"
"	border-style:none;\n"
"	text-align:center;\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(79, 162, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 10px;\n"
"}")
        self.my_progressBar.setValue(24)
        self.python_frame = QFrame(self.centralwidget)
        self.python_frame.setObjectName(u"python_frame")
        self.python_frame.setGeometry(QRect(480, 10, 250, 250))
        self.python_frame.setStyleSheet(u"image: url(:/images/image/python.png);")
        self.python_frame.setFrameShape(QFrame.StyledPanel)
        self.python_frame.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"WELCOME", None))
        self.loading_status.setText(QCoreApplication.translate("MainWindow", u"Initializing Desk App", None))
        self.loading_progress_status.setText(QCoreApplication.translate("MainWindow", u"Please wait...", None))
        self.credit_label.setText(QCoreApplication.translate("MainWindow", u"Designed by Minseo Rhie", None))
    # retranslateUi

