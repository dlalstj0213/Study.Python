import sys
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets

from ui.ui_repository import *
from view.repo_item import RepoItem
from service.git_service import GitService
#########################################
# MAIN WINDOW CLASS
#########################################


class Repository(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mygit = GitService(
            "dlalstj0213")
        repos = self.mygit.find_all_repo()
        i = (len(repos) // 3) + 1
        cnt = 0
        for x in range(0, i):
            # colums
            for y in range(0, 3):
                if cnt == len(repos):
                    break
                self.createNewWidgets(repos[cnt], x, y)
                cnt += 1

    def createNewWidgets(self, repo, row_num, col_num):
        view = RepoItem(repo)
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
