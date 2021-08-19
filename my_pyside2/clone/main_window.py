import sys
from PySide2 import QtCore, QtGui
from ui_main_window import *

# Global value for the window status
WINDOW_SIZE = 0
# This variable will be used to determine if the window is minimize or maximize

# ###
# Main Window Class
# ###
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window tittle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 상단에 있는 윈도우 기본 바를 제거

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to top bar buttons
        #
        # Minimize window
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        # Restore/Maximize window
        self.ui.restore_btn.clicked.connect(lambda: self.restore_or_maximize_window())
        # Close window
        self.ui.close_btn.clicked.connect(lambda: self.close())

        # ###
        # Move window on mouse drag event on the tittle bar
        # ###
        def moveWindow(e):
            # Detect if the window is normal size
            if not self.isMaximized():  # Not maximized
                # Move window only when window is normal size
                # If left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Add click/mouse move/drag events to the top header to move the window
        # self.ui.main_header.mouseMoveEvent = moveWindow
        self.ui.titlebar.mouseMoveEvent = moveWindow

        # Slidable left MENU
        # Left Menu toggle button
        self.ui.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())

    # ###
    # Restore or maximize window function
    # ###
    def restore_or_maximize_window(self):
        # Global window state
        global WINDOW_SIZE

        # 1 == True
        if WINDOW_SIZE:
            # If the window is on its default size
            WINDOW_SIZE = 0
            self.showNormal()
            # Update button icon
            self.ui.restore_btn.setIcon(
                QtGui.QIcon(
                    u":/icons/icons/cil-window-maximize.png"
                )  # show minimized icon
            )

        else:
            # If the window is not maximized
            WINDOW_SIZE = 1
            self.showMaximized()
            # Update button icon
            self.ui.restore_btn.setIcon(
                QtGui.QIcon(
                    u":/icons/icons/cil-window-restore.png"
                )  # show maximized icon
            )

    # ###
    # Add mouse events to the window
    # ###
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # This value will be used to move the window

    # ###
    # Slide left menu
    # ###
    def slideLeftMenu(self):
        # Get Current left menu width
        width = self.ui.left_side_menu.width()

        if width == 0:
            # Expand menu
            newwidth = 160
        else:
            newwidth = 0

        # Animate the transition
        # self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


# Execute
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
