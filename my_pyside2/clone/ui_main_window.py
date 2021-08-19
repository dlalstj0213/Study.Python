# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowXvdmkP.ui'
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
        MainWindow.resize(1300, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 40))
        self.main_header.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(83, 0, 124);\n"
"}\n"
"")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titlebar_container = QFrame(self.main_header)
        self.titlebar_container.setObjectName(u"titlebar_container")
        self.titlebar_container.setStyleSheet(u"")
        self.titlebar_container.setFrameShape(QFrame.NoFrame)
        self.titlebar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.titlebar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.titlebar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(80, 0))
        self.left_menu_toggle.setMaximumSize(QSize(80, 16777215))
        self.left_menu_toggle.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	/*border-radius: 5px;*/\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(120, 0, 180);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(65, 0, 98);\n"
"}")
        self.left_menu_toggle.setFrameShape(QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle_btn = QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setObjectName(u"left_menu_toggle_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu_toggle_btn.sizePolicy().hasHeightForWidth())
        self.left_menu_toggle_btn.setSizePolicy(sizePolicy)
        self.left_menu_toggle_btn.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.titlebar = QFrame(self.titlebar_container)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setFrameShape(QFrame.NoFrame)
        self.titlebar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.titlebar)


        self.horizontalLayout_2.addWidget(self.titlebar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(120, 16777215))
        self.top_right_btns.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	/*border-radius: 5px;*/\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(120, 0, 180);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(65, 0, 98);\n"
"}")
        self.top_right_btns.setFrameShape(QFrame.NoFrame)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 2, 0)
        self.restore_btn = QPushButton(self.top_right_btns)
        self.restore_btn.setObjectName(u"restore_btn")
        sizePolicy.setHeightForWidth(self.restore_btn.sizePolicy().hasHeightForWidth())
        self.restore_btn.setSizePolicy(sizePolicy)
        self.restore_btn.setMinimumSize(QSize(37, 30))
        self.restore_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restore_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_btn.setIcon(icon1)
        self.restore_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restore_btn)

        self.minimize_btn = QPushButton(self.top_right_btns)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon2)
        self.minimize_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.top_right_btns)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
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
        self.main_body.setStyleSheet(u"background-color: rgb(65, 0, 98);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_body)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(160, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(83, 0, 124);\n"
"}\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(83, 0, 124);\n"
"	color: rgb(230, 230, 230);\n"
"	\n"
"	text-align: left;\n"
"	background-repeat: none;\n"
"	padding-left: 40px;\n"
"	background-position: center left;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(120, 0, 180);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(65, 0, 98);\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.left_menu_top_btns = QFrame(self.left_side_menu)
        self.left_menu_top_btns.setObjectName(u"left_menu_top_btns")
        self.left_menu_top_btns.setFrameShape(QFrame.NoFrame)
        self.left_menu_top_btns.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_btns)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.left_menu_top_btns)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(100, 0))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.pushButton_3)

        self.pushButton_4 = QPushButton(self.left_menu_top_btns)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(100, 0))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-image: url(:/icons/icons/cil-user.png);\n"
"")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton_4)


        self.verticalLayout_3.addWidget(self.left_menu_top_btns)

        self.pushButton_2 = QPushButton(self.left_side_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icons/icons/cil-settings.png);")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.left_side_menu, 0, 0, 1, 1)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.center_main_items)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.gridLayout.addWidget(self.center_main_items, 0, 1, 1, 1)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMaximumSize(QSize(100, 16777215))
        self.right_side_menu.setStyleSheet(u"")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_side_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.right_side_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_3)


        self.gridLayout.addWidget(self.right_side_menu, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 20))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(83, 0, 124);\n"
"}\n"
"")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_toggle_btn.setText("")
        self.restore_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SETTING", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MAIN BODY ITEMS HERE okay", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RIGHT MENU", None))
    # retranslateUi

