import tkinter as tk
import tkinter.font as tkFont
import multiprocessing
import time
from timeConvert import TimeConverter as tc
import random
import numpy as np
import win32api


class Benchmark:
    def __init__(self):
        """
        Initialize worker and mulltiprocessing varable .
        ** In multiprocessor we can't get the returnValue in direct way, using manager in Multiprocess to get the output.

        """
        self.results = []
        self.returnValue = dict()
        self.worker = multiprocessing.cpu_count()
        self.excuteTime = None

    def multicoreBenchmark(self, job):
        """
        Main algorithm to assigning job to process.
        Multiprocessing is module to create multiple of process intredsof one process.
        to efficiently using CPU, This function assigning job to process depends on CPU_COUNT
        assign process to every thread of cpu.
        :param : Job amount to assign to process .
        :return :None
        """
        start = time.time()
        process = list()
        iterations = job // self.worker
        fractionOfJob = job % self.worker
        # stressMemory = os.urandom(psutil.virtual_memory().total)

        for worker in range(self.worker):
            if fractionOfJob != 0:
                p = multiprocessing.Process(
                    target=self.benchmarkProcess, args=(self.returnValue, worker, iterations+1))
                fractionOfJob -= 1
                process.append(p)
                p.start()
            else:
                p = multiprocessing.Process(
                    target=self.benchmarkProcess, args=(self.returnValue, worker, iterations))
                process.append(p)
                p.start()
        for p in process:
            p.join()
        stop = time.time()
        self.excuteTime = tc(stop - start).toString()

    def benchmarkProcess(self, returnDict, workerNumber, iterations):
        """
        Process target function that comfortable form to :meth:`multicoreBenchmark` .
        This function calls :meth:`benchmark algorithm` .
        :param:returnDict, workerNumber, iteration to process algorithm.
        :return: None ,**using multiprocessing manager to get return Value.
        """
        temp = list()
        for _ in range(iterations):
            a = self.benchMarkAlgorithms()
            temp.append(a[0])

        returnDict[workerNumber] = temp

    def benchMarkAlgorithms(self, ):
        """
        Algorithm for benchmarking.
        """
        start = time.time()
        x = np.array([[random.getrandbits(32) for _ in range(1000)]
                      for _ in range(1000)])

        y = np.array([[random.getrandbits(32) for _ in range(1000)]
                      for _ in range(1000)])
        z = x@y
        stop = time.time()
        return (stop - start, z)

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=763
        height=685
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_304=tk.Listbox(root)
        GListBox_304["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_304["font"] = ft
        GListBox_304["fg"] = "#333333"
        GListBox_304["justify"] = "center"
        GListBox_304.place(x=0,y=790,width=80,height=25)

        GLabel_882=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_882["font"] = ft
        GLabel_882["fg"] = "#333333"
        GLabel_882["justify"] = "center"
        GLabel_882["text"] = "CPU bench"
        GLabel_882.place(x=20,y=30,width=88,height=49)

        GButton_35=tk.Button(root)
        GButton_35["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_35["font"] = ft
        GButton_35["fg"] = "#000000"
        GButton_35["justify"] = "center"
        GButton_35["text"] = "Start"
        GButton_35.place(x=30,y=80,width=70,height=25)
        GButton_35["command"] = self.GButton_35_command
       


    def GButton_35_command(self):
        a = Benchmark()
        a.multicoreBenchmark(50)
        print(a.excuteTime)
        win32api.MessageBox(0, a.excuteTime , 'CPU')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
