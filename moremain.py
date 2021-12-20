from os import close
import sys
from time import clock
from typing import Counter
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal

###############
import platform

import psutil
import time
import re
import uuid
###############


from Benchmark import Benchmark
from HarddiskBenchmark import HarddiskBenchmark
from MemoryBenchmark import MemoryBenchmark
from timeConvert import TimeConverter as tc

# Globals
counter = 0


class pp(QMainWindow):
    def __init__(self):
        super(pp, self).__init__()
        loadUi("pp.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.gridLayout_2.setStyleSheet("background: transparent;")


####################################################
        self.exitButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.doAllbotton)

        self.data_animate()

        # output data system
    def data_animate(self):
        self.platform_2.setText(platform.system())

        self.arcitecture.setText(platform.machine())
        self.host_name_2.setText(platform.node())

        self.address_2.setText(':'.join(re.findall('..',
                                                   '%012x' % uuid.getnode())))

        self.processor_2.setText(platform.processor())
        self.ram_2.setText(str(
            round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB")

        # self.platform_2.setText(platform.system())
        # self.arcitecture.setText(platform.machine())
        # self.host_name_2.setText(platform.node())

        # self.address_2.setText(platform.machine())##

        # self.processor_2.setText(platform.processor())
        # self.ram_2.setText(ram)

    def doAllbotton(self):

        # SHOW MAIN WINDOW
        self.main = doAll()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()


class doAll(QMainWindow):
    def __init__(self):
        super(doAll, self).__init__()
        loadUi("doAll.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.exitButton.clicked.connect(lambda: self.close())
        self.pushButton_2.clicked.connect(self.backbotton)
        self.pushButton_3.clicked.connect(self.runLongTask)

        # bench varable
        self.counter = 0

        # set new type data

        self.lbl_cpu_bench.setText("CPU Bench")
        self.lbl_create_bench.setText("Create Bench")
        self.lbl_write_bench.setText("Write Bench")

        self.lbl_read_bench.setText("Read Bench")

        self.lbl_delete_bench.setText("Delete Bench")
        self.lbl_memory_bench.setText("Memory Bench")
        # self.reset_score()

        # self.benchmarkAllWithUpdateState()
    def reset_score(self):
        self.cpu_bench.setText("-")
        self.create_bench.setText("-")
        self.write_bench.setText("-")
        self.read_bench.setText("-")
        self.delete_bench.setText("-")
        self.memory_bench.setText("-")

    def runLongTask(self):
        self.reset_score()
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.pushButton_3.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.pushButton_2.setEnabled(True)
        )

    def reportProgress(self, score):
        if self.counter == 0:
            self.cpu_bench.setText(score)
            self.counter += 1
        elif self.counter == 1:
            self.create_bench.setText(score)
            self.counter += 1
        elif self.counter == 2:
            self.write_bench.setText(score)
            self.counter += 1
        elif self.counter == 3:
            self.read_bench.setText(score)
            self.counter += 1
        elif self.counter == 4:
            self.delete_bench.setText(score)
            self.counter += 1
        else:
            self.memory_bench.setText(score)
            self.counter = 0

    def backbotton(self):

        # SHOW MAIN WINDOW
        self.main = pp()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def run(self):
        """Long-running task."""
        cpuBenchmark = Benchmark()
        cpuBenchmark.multicoreBenchmark()
        self.progress.emit(tc(cpuBenchmark.excuteTime).toString())

        time.sleep(4)
        ioBenchmark = HarddiskBenchmark()
        ioBenchmark.createFilesBench()
        self.progress.emit(tc(
            ioBenchmark.result[0]).toString())

        ioBenchmark.writeFileBench()

        self.progress.emit(tc(
            ioBenchmark.result[1]).toString())

        ioBenchmark.readFilesBench()

        self.progress.emit(tc(
            ioBenchmark.result[2]).toString())

        ioBenchmark.deleteTempFile()

        self.progress.emit(tc(
            ioBenchmark.result[3]).toString())

        memoryBenchmark = MemoryBenchmark()
        memoryBenchmark.memoryBenchmark()
        self.progress.emit(tc(memoryBenchmark.result).toString())

        self.finished.emit()


############################################

class splashprogram(QMainWindow):
    def __init__(self):
        self.counter = 0
        super(splashprogram, self).__init__()
        loadUi("splashprogram.ui", self)
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
            self.main = pp()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 1


# main
app = QApplication(sys.argv)
welcome = splashprogram()
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
except:
    print("Exiting")
