
from PyQt5.uic import loadUi

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from pages.Systeminfo import Systeminfo


class LoadingScreen(QMainWindow):
    def __init__(self):
        self.counter = 0
        super(LoadingScreen, self).__init__()
        loadUi("views/loadingScreen.ui", self)
        self.splashframe.setStyleSheet("background-color: transparent;")

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(10)

    def progress(self):

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Systeminfo()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 1
