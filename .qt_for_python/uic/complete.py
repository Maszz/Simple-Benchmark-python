# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mawinsukmongkol/Desktop/CN212/complete.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1098, 768))
        self.frame.setStyleSheet("background-color: rgba(20, 20, 20, 150);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 330, 1078, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.closeBotton = QtWidgets.QPushButton(self.frame)
        self.closeBotton.setGeometry(QtCore.QRect(0, -3, 1090, 771))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.closeBotton.setFont(font)
        self.closeBotton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: none;")
        self.closeBotton.setText("")
        self.closeBotton.setObjectName("closeBotton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -1, 1081, 761))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("/Users/mawinsukmongkol/Desktop/CN212/finishedImage.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.emptybox3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.emptybox3.setFont(font)
        self.emptybox3.setStyleSheet("background-color: rgba(46, 46, 140, 150);\n"
"color: rgb(255, 255, 255);")
        self.emptybox3.setText("")
        self.emptybox3.setAlignment(QtCore.Qt.AlignCenter)
        self.emptybox3.setObjectName("emptybox3")
        self.gridLayout_3.addWidget(self.emptybox3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(46, 46, 140, 150);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.timetobenchmark = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.timetobenchmark.setFont(font)
        self.timetobenchmark.setStyleSheet("background-color: rgba(46, 46, 140, 150);\n"
"color: rgb(255, 255, 255);")
        self.timetobenchmark.setAlignment(QtCore.Qt.AlignCenter)
        self.timetobenchmark.setObjectName("timetobenchmark")
        self.gridLayout_3.addWidget(self.timetobenchmark, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 7)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 4)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.emtpybox1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.emtpybox1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.emtpybox1.setText("")
        self.emtpybox1.setObjectName("emtpybox1")
        self.gridLayout.addWidget(self.emtpybox1, 3, 2, 1, 1)
        self.emtpybox2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.emtpybox2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.emtpybox2.setText("")
        self.emtpybox2.setObjectName("emtpybox2")
        self.gridLayout.addWidget(self.emtpybox2, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.closeBotton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "seconds to complete"))
        self.timetobenchmark.setText(_translate("MainWindow", "0"))