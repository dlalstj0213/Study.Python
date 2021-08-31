import sys
import os
from view.repository import Repository
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

#############################################
# IMPORT GUI FILE
from ui_interface import Ui_MainWindow
from view.home import Home
from view.browser import Browser
#############################################


#########################################
# MAIN WINDOW CLASS
#########################################

PREV_BUTTON = None


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##############################################
        # Remove window tittle bar
        ##############################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        ##############################################
        # Set main background to transparent
        ##############################################
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #############################################
        # Shadow effect style
        #############################################
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))

        ##############################################
        # Apply shadow to central widget
        ##############################################
        # self.ui.centralwidget.setGraphicsEffect(self.shadow) # This code gives 'UpdateLayeredWindowIndirect failed' when move toggle menu

        ###############################################################################################
        # Set window Icon
        # This icon and title will not appear on our app main window because we removed the title bar
        ###############################################################################################
        self.setWindowIcon(QtGui.QIcon(u":/icons/icons/github.svg"))
        # Set window title
        self.setWindowTitle("My Github")

        ##############################################
        # WIndow Size grip to resize window
        ##############################################
        QtWidgets.QSizeGrip(self.ui.size_grip)

        ##############################################
        # Minimize window
        ###############################################################################################
        self.ui.minimize_window_button.clicked.connect(
            lambda: self.showMinimized())
        # Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        #self.ui.exit_button.clicked.connect(lambda: self.close())
        # Restore / Maximize window
        self.ui.restore_window_button.clicked.connect(
            lambda: self.restore_or_maximize_window())

        ###############################################################################################
        # Function to Move window on mouse drag event on the title bar
        ###############################################################################################
        def moveWindow(e):
            # Detect if the window is normal size
            ###############################################################################################
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                ###############################################################################################
                # If left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == QtGui.Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        ###############################################################################################

        ###############################################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        ###############################################################################################
        self.ui.header_frame.mouseMoveEvent = moveWindow

        ###############################################################################################
        # Left Menu toggle button
        ###############################################################################################
        self.ui.open_close_side_bar_btn.clicked.connect(
            lambda: self.slideLeftMenu())

        buttons = self.ui.toolBox.findChildren(QtWidgets.QPushButton)
        for button in buttons:
            button.clicked.connect(self.click_button)

        self.views = {"total": 0}
        self.ui.stackedWidget.removeWidget(self.ui.page)
        self.ui.stackedWidget.removeWidget(self.ui.page_2)
        self.change_current_stackwidget("home", Home())

        def mouseClicked(e):
            if e.buttons() == QtGui.Qt.LeftButton:
                self.change_current_stackwidget("home")

        self.ui.lbl_app_name.mousePressEvent = mouseClicked
        self.ui.lbl_app_icon.mousePressEvent = mouseClicked

    ###############################################################################################
    # Update restore button icon on maximizing or minimizing the window
    ###############################################################################################

    def restore_or_maximize_window(self):
        # If window is maximized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u":/icons/icons/minimize-2.svg"))
        # Get current left menu width
        width = self.ui.slide_menu_container.width()
        if width != 0:
            current_height = self.ui.slide_menu_items.height()
            newheight = self.ui.slide_menu_container.height() - self.ui.app_frame.height() - \
                self.ui.exit_frame.height()
            # Animate the transition
            self.menu_item_animation = QtCore.QPropertyAnimation(
                self.ui.slide_menu_items, b"maximumHeight")  # Animate minimumWidth
            self.menu_item_animation.setDuration(250)
            # Start value is the current menu width
            self.menu_item_animation.setStartValue(current_height)
            # end value is the new menu width
            self.menu_item_animation.setEndValue(newheight)
            self.menu_item_animation.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.menu_item_animation.start()

    ###############################################################################################
    # Add mouse events to the window
    ###############################################################################################
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        ###############################################################################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # This value will be used to move the window
        ###############################################################################################

    ###############################################################################################
    # Slide left menu function
    ###############################################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.slide_menu_container.width()

        # If minimized
        if width == 0:
            # Expand menu
            newwidth = 200
            self.ui.open_close_side_bar_btn.setIcon(
                QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            newwidth = 0
            self.ui.open_close_side_bar_btn.setIcon(
                QtGui.QIcon(u":/icons/icons/align-left.svg"))

        # Animate the transition
        self.slide_menu_animation = QtCore.QPropertyAnimation(
            self.ui.slide_menu_container, b"maximumWidth")  # Animate minimumWidth
        self.slide_menu_animation.setDuration(250)
        # Start value is the current menu width
        self.slide_menu_animation.setStartValue(width)
        self.slide_menu_animation.setEndValue(
            newwidth)  # end value is the new menu width
        self.slide_menu_animation.setEasingCurve(
            QtCore.QEasingCurve.InOutQuart)
        self.slide_menu_animation.start()

        self.slideDownMenuItems()

    def slideDownMenuItems(self):
        # Get current left menu width
        current_height = self.ui.slide_menu_items.height()

        # If minimized
        if current_height == 0:
            # Expand menu
            newheight = self.ui.slide_menu_container.height() - self.ui.app_frame.height() - \
                self.ui.exit_frame.height()
        # If maximized
        else:
            newheight = 0

        # Animate the transition
        self.menu_item_animation = QtCore.QPropertyAnimation(
            self.ui.slide_menu_items, b"maximumHeight")  # Animate minimumWidth
        self.menu_item_animation.setDuration(250)
        # Start value is the current menu width
        self.menu_item_animation.setStartValue(current_height)
        # end value is the new menu width
        self.menu_item_animation.setEndValue(newheight)
        self.menu_item_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.menu_item_animation.start()

    def click_button(self):
        global PREV_BUTTON
        sender = self.sender()
        self.load_view(sender)
        if sender is PREV_BUTTON:
            return
        sender.setStyleSheet("""
            QPushButton{
                background-color: rgb(24, 24, 36);
            }
            QPushButton::hover {
                color: rgb(0, 0, 0);
                background-color: rgb(255, 255, 255);
            }
        """)
        if PREV_BUTTON is not None:
            PREV_BUTTON.setStyleSheet("""
                QPushButton {
                    background-color: rgb(9, 5, 13);
                }
                QPushButton::hover {
                    color: rgb(0, 0, 0);
                    background-color: rgb(255, 255, 255);
                }
            """)
        PREV_BUTTON = sender

    def load_view(self, button_object):
        if button_object.objectName() == "github_browser_button":
            self.change_current_stackwidget("browser", Browser())
        elif button_object.objectName() == "repository_button":
            # print("RUN")
            # self.views.get("browser").get("view").browser.setUrl(
            #     QtCore.QUrl("http://www.google.com"))
            self.change_current_stackwidget("repository", Repository())
            pass

    def change_current_stackwidget(self, kwrg: str, view=None):
        if self.views.get(kwrg) is None:
            self.views.update({
                str(kwrg): {"view": view, "index": self.views.get("total")}})
            self.views["total"] += 1
            self.ui.stackedWidget.addWidget(
                self.views.get(kwrg).get("view"))
        self.ui.stackedWidget.setCurrentWidget(
            self.views.get(kwrg).get("view"))
        self.ui.stackedWidget.setCurrentIndex(
            self.views.get(kwrg).get("index"))


##########################################
# EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        window.views.get("browser").get("view").browser.close()

##########################################
# END ==>
##########################################
