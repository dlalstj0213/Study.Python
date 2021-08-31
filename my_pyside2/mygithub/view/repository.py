import sys
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets

from ui.ui_repository import *
from view.repo_item import RepoItem
#########################################
# MAIN WINDOW CLASS
#########################################


class Repository(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for x in range(0, 3):
            # colums
            for y in range(0, 3):
                self.createNewWidgets(x, y)

    def createNewWidgets(self, row_num, col_num):
        view = RepoItem()
        self.ui.gridLayout.addWidget(
            view, row_num, col_num, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Repository()
    window.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print(be)
##########################################
# END ==>
##########################################
