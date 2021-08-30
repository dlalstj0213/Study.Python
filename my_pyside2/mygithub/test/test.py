import sys
from PySide2.QtWebEngineWidgets import QWebEngineView
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets

#############################################
# IMPORT GUI FILE
from ui_test import *
#############################################


#########################################
# MAIN WINDOW CLASS
#########################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        brower_widght = QtGuiWidgets.QVBoxLayout()
        brower_widght.addWidget(self.browser)
        self.setCentralWidget(self.browser)


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
