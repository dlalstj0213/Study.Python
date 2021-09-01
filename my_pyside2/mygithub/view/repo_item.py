from service.git_service import GitRepository
import sys
from typing import Dict
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtGuiWidgets

from ui.ui_repo_item import *
#########################################
# MAIN WINDOW CLASS
#########################################


class RepoItem(QMainWindow):
    def __init__(self, repo: GitRepository):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setContents(repo)

    def setContents(self, repo):
        self.ui.lbl_repo_name.setText(repo.name)
        self.ui.lbl_description.setText(repo.description)
        self.ui.lbl_language.setText(repo.language)
        self.ui.lbl_updated.setText(repo.last_days)
        self.ui.lbl_created_at.setText(str(repo.created_at))
        self.ui.lbl_stars.setText(str(repo.stars))


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RepoItem()
    window.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print(be)
##########################################
# END ==>
##########################################
