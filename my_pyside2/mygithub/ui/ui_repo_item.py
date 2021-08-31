# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repo_itemOomCUs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(722, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.item_content = QFrame(self.centralwidget)
        self.item_content.setObjectName(u"item_content")
        self.item_content.setMinimumSize(QSize(500, 300))
        self.item_content.setMaximumSize(QSize(500, 300))
        self.item_content.setStyleSheet(u"QFrame#item_content{\n"
"	border: 5px solid rgb(130, 130, 194);\n"
"	border-radius: 50px;\n"
"}")
        self.item_content.setFrameShape(QFrame.StyledPanel)
        self.item_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.item_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(self.item_content)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.repo_name_frame = QFrame(self.frame)
        self.repo_name_frame.setObjectName(u"repo_name_frame")
        self.repo_name_frame.setFrameShape(QFrame.StyledPanel)
        self.repo_name_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.repo_name_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_repo_icon = QLabel(self.repo_name_frame)
        self.lbl_repo_icon.setObjectName(u"lbl_repo_icon")
        self.lbl_repo_icon.setPixmap(QPixmap(u":/icons/icons/inbox.svg"))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_repo_icon)

        self.lbl_repo_name = QLabel(self.repo_name_frame)
        self.lbl_repo_name.setObjectName(u"lbl_repo_name")
        font = QFont()
        font.setFamily(u"Nirmala UI Semilight")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_repo_name.setFont(font)
        self.lbl_repo_name.setTextFormat(Qt.AutoText)
        self.lbl_repo_name.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lbl_repo_name)


        self.verticalLayout_2.addWidget(self.repo_name_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.repo_info_frame = QFrame(self.frame)
        self.repo_info_frame.setObjectName(u"repo_info_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.repo_info_frame.sizePolicy().hasHeightForWidth())
        self.repo_info_frame.setSizePolicy(sizePolicy1)
        self.repo_info_frame.setFrameShape(QFrame.StyledPanel)
        self.repo_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.repo_info_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.repo_info_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.repo_info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.repo_info_frame)


        self.verticalLayout_3.addWidget(self.frame)

        self.repo_control_frame = QFrame(self.item_content)
        self.repo_control_frame.setObjectName(u"repo_control_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.repo_control_frame.sizePolicy().hasHeightForWidth())
        self.repo_control_frame.setSizePolicy(sizePolicy2)
        self.repo_control_frame.setMinimumSize(QSize(0, 0))
        self.repo_control_frame.setMaximumSize(QSize(16777215, 16777215))
        self.repo_control_frame.setFrameShape(QFrame.StyledPanel)
        self.repo_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.repo_control_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.repo_control_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.repo_control_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.repo_control_frame, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.item_content, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_repo_icon.setText("")
        self.lbl_repo_name.setText(QCoreApplication.translate("MainWindow", u"Repository Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"# Repository Description : input your repository description here", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"# Language : input your language here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BUTTON_1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"BUTTON_2", None))
    # retranslateUi

