from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal
# from Systeminfo import Systeminfo


from CpuBenchmark import CpuBenchmark
from HarddiskBenchmark import HarddiskBenchmark
from MemoryBenchmark import MemoryBenchmark
from timeConvert import TimeConverter as tc
# import HarddiskBenchmark as HarddiskBenchmark
import time
# from pages.Systeminfo import pp


class BenchmarkPage(QMainWindow):
    def __init__(self):
        super(BenchmarkPage, self).__init__()
        loadUi("views/benchmarkpage.ui", self)
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
        self.main = Systeminfo()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def run(self):
        """Long-running task."""
        cpuBenchmark = CpuBenchmark()
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
