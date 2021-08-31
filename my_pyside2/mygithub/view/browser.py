import sys
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView

from ui.ui_browser import *
#########################################
# MAIN WINDOW CLASS
#########################################


class Browser(QMainWindow):
    def __init__(self, url="https://www.github.com/dlalstj0213"):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        self.setCentralWidget(self.browser)


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser("https://www.github.com/dlalstj0213")
    window.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print(be)
##########################################
# END ==>
##########################################
