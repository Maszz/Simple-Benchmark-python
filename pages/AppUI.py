
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from CpuBenchmark import CpuBenchmark
from HarddiskBenchmark import HarddiskBenchmark
from MemoryBenchmark import MemoryBenchmark
from timeConvert import TimeConverter as tc

###############
import platform
import psutil
import time
import re
import uuid
###############


class LoadingScreen(QMainWindow):
    def __init__(self):
        self.counter = 0
        super(LoadingScreen, self).__init__()
        loadUi("loadingScreen.ui", self)
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


class Systeminfo(QMainWindow):
    def __init__(self):
        super(Systeminfo, self).__init__()
        loadUi("systemInfo.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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


class BenchmarkPage(QMainWindow):
    def __init__(self):
        super(BenchmarkPage, self).__init__()
        loadUi("benchmarkpage.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.exitButton.clicked.connect(lambda: self.close())
        self.pushButton_2.clicked.connect(self.backbotton)
        self.pushButton_3.clicked.connect(self.runLongTask)

        # bench varable
        self.counter = 0
        self.totalScore = 0

        # set new type data

        self.lbl_cpu_benchmark.setText("CPU Benchmark")
        self.lbl_io_benchmark.setText("IO Benchmark")

        self.lbl_memory_benchmark.setText("Memory Benchmark")
        self.lbl_total.setText("Total")

    def reset_score(self):
        self.cpu_benchmark_score.setText("-")
        self.io_benchmark_score.setText("-")
        self.memory_benchmark_score.setText("-")
        self.total_score.setText("-")
        self.totalScore = 0

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
        self.thread.finished.connect(lambda: self.pushButton_3.setEnabled(True)
                                     )
        self.thread.finished.connect(
            lambda: self.pushButton_2.setEnabled(True))

        self.thread.finished.connect(self.complete_message)
        self.thread.finished.connect(lambda: self.total_score.setText(f'{self.totalScore:.2f}')
                                     )

    def reportProgress(self, score):
        self.totalScore += float(score)
        if self.counter == 0:
            self.cpu_benchmark_score.setText(score)
            self.counter += 1
        elif self.counter == 1:
            self.io_benchmark_score.setText(score)
            self.counter += 1
        else:
            self.memory_benchmark_score.setText(score)
            self.counter = 0

    def backbotton(self):

        # SHOW MAIN WINDOW
        self.main = Systeminfo()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()

    def complete_message(self):

        self.main = Complete()
        self.main.label_2.setText(
            f'{tc(benchmark_stop).toString()} to complete Benchmark')
        self.main.show()


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def run(self):
        """Long-running task."""
        start = time.time()
        cpuBenchmark = CpuBenchmark()
        cpuBenchmark.multicoreBenchmark()
        self.progress.emit(
            f'{((1 - (cpuBenchmark.excuteTime/1000)) * 1000): .2f}')

        time.sleep(4)
        ioBenchmark = HarddiskBenchmark()

        ioBenchmark.startBenchmark()
        self.progress.emit(
            f'{((1 - (ioBenchmark.benchmarkTime/600)) * 1000): .2f}')
        memoryBenchmark = MemoryBenchmark()
        memoryBenchmark.memoryBenchmark()
        self.progress.emit(
            f'{((1 - (memoryBenchmark.result/400)) * 1000): .2f}')
        global benchmark_stop
        benchmark_stop = time.time() - start
        self.finished.emit()


class Complete(QMainWindow):
    def __init__(self):
        super(Complete, self).__init__()
        loadUi("complete.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.closeBotton.clicked.connect(lambda: self.close())
