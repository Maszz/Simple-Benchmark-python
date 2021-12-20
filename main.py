from os import error
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication


from pages.AppUI import LoadingScreen

###############


if __name__ == '__main__':

    app = QApplication(sys.argv)
    welcome = LoadingScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)

    # Remove title bar
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    widget.show()
    try:
        sys.exit(app.exec_())
    except error as e:
        print("Exiting")
