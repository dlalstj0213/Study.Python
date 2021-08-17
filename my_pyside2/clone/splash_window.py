import sys
import os
import platform
from PySide2 import *
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_splash_window import *
from main_window import MainWindow

# Global value
progressBarValue = 0


class SplashWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

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

        # code QTIMER to delay the progressBar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)
        # Time interval in Milliseconds for the progressbar to change value
        self.timer.start(100)

    # appProgress fuction : update the progressBar value
    def appProgress(self):
        global progressBarValue
        # Apply progressBarValue to the progressBar
        self.ui.my_progressBar.setValue(progressBarValue)

        # View progressBarValue and update status text or close splash screen and open main window
        loading_progress_status_text = "Please wait..."
        loading_status_text = "Initializing Desk App"
        if progressBarValue > 100:

            # reset / stop timer
            self.timer.stop()

            # Close the splash screen after the progress is complete
            # self.close()

            loading_progress_status_text = "Loading completed successfully"
            loading_status_text = "Now Open Desk App"
            # self.close()
            self.open_main_window()

        elif progressBarValue < 10:
            pass
        elif progressBarValue < 20:
            loading_progress_status_text = "Connecting to App server"
        elif progressBarValue < 35:
            loading_progress_status_text = "Logging in..."
        elif progressBarValue < 55:
            loading_progress_status_text = "Logging in succesfully. Requesting Data..."
        elif progressBarValue < 65:
            loading_progress_status_text = (
                "Data set to design. Requesting design data information"
            )
        elif progressBarValue < 85:
            loading_progress_status_text = "Finalizing data setup"
        else:
            loading_progress_status_text = "Almost done..."
            loading_status_text = "Minseo Design"

        # change the loading status text
        QtCore.QTimer.singleShot(
            0,
            lambda: self.ui.loading_progress_status.setText(
                loading_progress_status_text
            ),
        )
        QtCore.QTimer.singleShot(
            0,
            lambda: self.ui.loading_status.setText(loading_status_text),
        )

        # increase progressBarValue by 1 after every time interval we set of 100 milliseconds;
        progressBarValue += 1

    # open new window which is the main window and close previous window which is splash window when the progressBar reach 100 value
    def open_main_window(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.close()


# Execute
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SplashWindow()
    main.show()
    try:
        sys.exit(app.exec_())
    except BaseException as be:
        print(type(be), str(be))
