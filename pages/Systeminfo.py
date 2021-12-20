from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import platform
import psutil
import re
import uuid
from pages.BenchmarkPage import BenchmarkPage


class Systeminfo(QMainWindow):
    def __init__(self):
        super(Systeminfo, self).__init__()
        loadUi("views/systemInfo.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.gridLayout_2.setStyleSheet("background: transparent;")


####################################################
        self.exitButton.clicked.connect(lambda: self.close())
        self.pushButton_2.clicked.connect(self.goToBenchmarkPage)

        self.showSystemData()

        # output data system
    def showSystemData(self):
        self.platform_2.setText(platform.system())

        self.arcitecture.setText(platform.machine())
        self.host_name_2.setText(platform.node())

        self.address_2.setText(':'.join(re.findall('..',
                                                   '%012x' % uuid.getnode())))

        self.processor_2.setText(platform.processor())
        self.ram_2.setText(
            f"{str(round(psutil.virtual_memory().total / (1024.0 ** 3)))}GB")

    def goToBenchmarkPage(self):

        # SHOW MAIN WINDOW
        self.main = BenchmarkPage()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()
