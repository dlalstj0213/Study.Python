import sys
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets

from ui_main import *
from test import MainWindow as TestMain
#########################################
# MAIN WINDOW CLASS
#########################################


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        view = TestMain()
        self.ui.stackedWidget.addWidget(view)
        self.ui.stackedWidget.setCurrentWidget(view)


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        window.browser.close()
##########################################
# END ==>
##########################################
