# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowGCXPEE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import os

# Conver qrc resource file to python resource file
os.system("pyrcc5 python_app.qrc -o python_app_rc.py")
# pyrcc5 -o resources.py resources.qrc

import python_app_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1164, 915)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"background-color: rgb(83, 0, 124);")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titlebar_container = QFrame(self.main_header)
        self.titlebar_container.setObjectName(u"titlebar_container")
        self.titlebar_container.setStyleSheet(u"")
        self.titlebar_container.setFrameShape(QFrame.StyledPanel)
        self.titlebar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.titlebar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.titlebar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(100, 0))
        self.left_menu_toggle.setMaximumSize(QSize(100, 16777215))
        self.left_menu_toggle.setStyleSheet(
            u"QPushButton {\n"
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "	background-color: rgb(120, 0, 180);\n"
            "}"
        )
        self.left_menu_toggle.setFrameShape(QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.left_menu_toggle)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.titlebar = QFrame(self.titlebar_container)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.titlebar)

        self.horizontalLayout_2.addWidget(self.titlebar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setStyleSheet(
            u"QPushButton {\n"
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "	background-color: rgb(120, 0, 180);\n"
            "}"
        )
        self.top_right_btns.setFrameShape(QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.top_right_btns)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(
            u":/icons/icons/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.restore_btn = QPushButton(self.top_right_btns)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restore_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_btn.setIcon(icon2)
        self.restore_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restore_btn)

        self.close_btn = QPushButton(self.top_right_btns)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_btn)

        self.horizontalLayout_2.addWidget(self.top_right_btns)

        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(83, 0, 124);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(100, 16777215))
        self.left_side_menu.setStyleSheet(u"")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.left_side_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 290, 91, 121))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)

        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.center_main_items)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 160, 521, 281))
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMaximumSize(QSize(100, 16777215))
        self.right_side_menu.setStyleSheet(u"")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.right_side_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 290, 81, 121))
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.right_side_menu)

        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"background-color: rgb(83, 0, 124);")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.pushButton.setText("")
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"LEFT MENU", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"MAIN BODY ITEMS HERE okay", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"RIGHT MENU", None)
        )

    # retranslateUi
