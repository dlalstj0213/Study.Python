# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacempvMeg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 875)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu_container.sizePolicy().hasHeightForWidth())
        self.slide_menu_container.setSizePolicy(sizePolicy)
        self.slide_menu_container.setMinimumSize(QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QSize(200, 16777215))
        self.slide_menu_container.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slide_menu.sizePolicy().hasHeightForWidth())
        self.slide_menu.setSizePolicy(sizePolicy1)
        self.slide_menu.setMinimumSize(QSize(198, 600))
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.app_frame = QFrame(self.slide_menu)
        self.app_frame.setObjectName(u"app_frame")
        self.app_frame.setFrameShape(QFrame.StyledPanel)
        self.app_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.app_frame)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.lbl_app_name = QLabel(self.app_frame)
        self.lbl_app_name.setObjectName(u"lbl_app_name")
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_app_name.setFont(font)
        self.lbl_app_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_app_name.setMouseTracking(False)

        self.horizontalLayout_8.addWidget(self.lbl_app_name, 0, Qt.AlignLeft|Qt.AlignTop)

        self.lbl_app_icon = QLabel(self.app_frame)
        self.lbl_app_icon.setObjectName(u"lbl_app_icon")
        self.lbl_app_icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_app_icon.setPixmap(QPixmap(u":/icons/icons/github.svg"))

        self.horizontalLayout_8.addWidget(self.lbl_app_icon, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.app_frame, 0, Qt.AlignTop)

        self.slide_menu_items = QFrame(self.slide_menu)
        self.slide_menu_items.setObjectName(u"slide_menu_items")
        self.slide_menu_items.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slide_menu_items.sizePolicy().hasHeightForWidth())
        self.slide_menu_items.setSizePolicy(sizePolicy2)
        self.slide_menu_items.setMinimumSize(QSize(0, 0))
        self.slide_menu_items.setMaximumSize(QSize(16777215, 16777215))
        self.slide_menu_items.setMouseTracking(False)
        self.slide_menu_items.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.slide_menu_items)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.slide_menu_items)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy2)
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color: rgb(9, 5, 13);\n"
"	text-align: left;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	font-weight: bold;\n"
"	font-family: Nirmala UI;\n"
"	font-size: 15px;\n"
"	margin-left: 10px;\n"
"	border-radius: 5px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	background-color: rgb(9, 5, 13);\n"
"	text-align: left;\n"
"}\n"
"\n"
"QToolBox::tab::selected{\n"
"	background-color: rgb(24, 24, 36);\n"
"    border-right: 5px solid rgb(65, 65, 97);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"	font-family: Nirmala UI;\n"
"	font-size: 13px;\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	font-family: Nirmala UI;\n"
"}")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1.setEnabled(True)
        self.menu_1.setGeometry(QRect(0, 0, 198, 747))
        self.menu_1.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.menu_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 0, 0, 0)
        self.frame_10 = QFrame(self.menu_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.github_browser_button = QPushButton(self.frame_10)
        self.github_browser_button.setObjectName(u"github_browser_button")
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setBold(True)
        font1.setWeight(75)
        self.github_browser_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.github_browser_button.setIcon(icon)
        self.github_browser_button.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.github_browser_button)

        self.repository_button = QPushButton(self.frame_10)
        self.repository_button.setObjectName(u"repository_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.repository_button.setIcon(icon1)

        self.verticalLayout_8.addWidget(self.repository_button)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.verticalLayout_8.addWidget(self.pushButton_12)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)

        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.On)
        self.toolBox.addItem(self.menu_1, icon3, u"GIT")
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setGeometry(QRect(0, 0, 200, 747))
        self.menu_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout_9 = QVBoxLayout(self.menu_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 0, 0, 0)
        self.frame_11 = QFrame(self.menu_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)

        self.verticalLayout_10.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon4)

        self.verticalLayout_10.addWidget(self.pushButton_14)


        self.verticalLayout_9.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.menu_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignTop)

        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.menu_2, icon5, u"SETTINGS")

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_5.addWidget(self.slide_menu_items)


        self.verticalLayout_2.addWidget(self.slide_menu)

        self.exit_frame = QFrame(self.slide_menu_container)
        self.exit_frame.setObjectName(u"exit_frame")
        self.exit_frame.setMaximumSize(QSize(16777215, 16777215))
        self.exit_frame.setFrameShape(QFrame.StyledPanel)
        self.exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.exit_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 3, 0, 0)
        self.exit_button = QPushButton(self.exit_frame)
        self.exit_button.setObjectName(u"exit_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon6)
        self.exit_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.exit_button, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.exit_frame)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"*{\n"
"	background-color: rgb(9, 5, 13);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(65, 65, 97);\n"
"	/*background-color: rgb(24, 24, 36);*/\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.frame_4 = QFrame(self.header_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame_12)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon7)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout_7.addWidget(self.frame_12)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 6, 0, 0)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(150, 0))
        self.lineEdit.setStyleSheet(u"border-bottom: 3px solid rgb(230, 5, 64);")

        self.horizontalLayout_6.addWidget(self.lineEdit, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_6, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 6, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.horizontalLayout_7.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon11)
        self.minimize_window_button.setIconSize(QSize(20, 21))

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon12)
        self.restore_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon13)
        self.close_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)

        self.frame.raise_()
        self.frame_4.raise_()

        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy2.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy2)
        self.main_body_contents.setStyleSheet(u"")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon14)

        self.verticalLayout_3.addWidget(self.pushButton_7, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_app_name.setText(QCoreApplication.translate("MainWindow", u"MY GITGUB", None))
        self.lbl_app_icon.setText("")
        self.github_browser_button.setText(QCoreApplication.translate("MainWindow", u"GitHub Browser", None))
        self.repository_button.setText(QCoreApplication.translate("MainWindow", u"Repository", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"SUB_MENU", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.menu_1), QCoreApplication.translate("MainWindow", u"GIT", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"SUB_MENU", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"SUB_MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Some text you would like to fill here", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.menu_2), QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.open_close_side_bar_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Modern UI v 1.1.1", None))
        self.pushButton_7.setText("")
    # retranslateUi

