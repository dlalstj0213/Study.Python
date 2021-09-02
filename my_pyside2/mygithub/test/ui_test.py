# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'testTnMPKG.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from custom_qstacked_widgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 90, 431, 311))
        font = QFont()
        font.setFamily(u"\uad74\ub9bc")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 90, 431, 311))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 90, 431, 311))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nxt = QPushButton(self.frame)
        self.nxt.setObjectName(u"nxt")

        self.horizontalLayout.addWidget(self.nxt)

        self.page1 = QPushButton(self.frame)
        self.page1.setObjectName(u"page1")

        self.horizontalLayout.addWidget(self.page1)

        self.page2 = QPushButton(self.frame)
        self.page2.setObjectName(u"page2")

        self.horizontalLayout.addWidget(self.page2)

        self.prev = QPushButton(self.frame)
        self.prev.setObjectName(u"prev")

        self.horizontalLayout.addWidget(self.prev)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Page 1", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Page 2", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Page 3", None))
        self.nxt.setText(QCoreApplication.translate(
            "MainWindow", u"next", None))
        self.page1.setText(QCoreApplication.translate(
            "MainWindow", u"Page1", None))
        self.page2.setText(QCoreApplication.translate(
            "MainWindow", u"Page2", None))
        self.prev.setText(QCoreApplication.translate(
            "MainWindow", u"previous", None))
    # retranslateUi
