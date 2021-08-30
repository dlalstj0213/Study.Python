import sys
import os
from PySide2 import QtCore, QtGui

#############################################
# IMPORT GUI FILE
from ui_interface import *
#############################################


#########################################
# MAIN WINDOW CLASS
#########################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # FOR LOOP
        # 10 rows
        for x in range(0, 10):
            # colums
            for y in range(0, 4):
                self.createNewWidgets(x, y)

        # Apply new stylesheet to new last frame
        self.ui.frame9_3.setStyleSheet("background-color: red;")
        # Apply new stylesheet to new first frame
        self.ui.frame0_0.setStyleSheet("background-color: black;")

    def createNewWidgets(self, row_num, col_num):
        # CREATE NEW UNIQUE NAMES FOR THE WIDGETS
        new_name = "frame" + str(row_num) + "_" + str(col_num)

        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        # USE setObjectName() to give your object a new name
        self.frame.setObjectName(new_name)
        self.frame.setMinimumSize(QSize(100, 100))
        self.frame.setMaximumSize(QSize(100, 100))
        self.frame.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        # CREATE new attribute to Ui_Mainwindow
        # Syntax : setattr(obj, var, val)
        # Parameters :
        # obj : Object whose which attribute is to be assigned
        # var : Object attribute which has to be assigned
        # val : value with which variable is to be assigned
        setattr(self.ui, new_name, self.frame)

        #
        # void QGridLayout::addLayout(QLayout *layout, int row, int column, int rowSpan, int columnSpan, Qt::Alignment alignment = Qt::Alignment())
        #
        self.ui.gridLayout.addWidget(
            self.frame, row_num, col_num, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

##########################################
# END ==>
##########################################
