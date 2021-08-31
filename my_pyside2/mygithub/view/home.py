import sys
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets

from ui.ui_home import *
#########################################
# MAIN WINDOW CLASS
#########################################


class Home(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print(be)
##########################################
# END ==>
##########################################
