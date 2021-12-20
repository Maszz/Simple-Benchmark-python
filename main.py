import tkinter as tk

#################################
import tkinter.font as tkFont
from tkinter import ttk, messagebox
##############################

#ใช้progress table
import Benchmark as cpuBench
import HarddiskBenchmark as ioBench

#import for creat table
from views import Table as T
from views import progressbar as P

from views import systeminfo as S
import time
import MemoryBenchmark as M


class App:
    def __init__(self, root):
        # setting title
        self.app_root = root
        self.app_root.title("Benchmark")
        self.app_root.resizable(width=False, height=False)
        self.results = dict()

        #declare variable
        self.resultstable = [[]]
        self.thead = [
            ["round", "cpu", "create", "read", "write", "delete", "memory"]]


        #create window
        width = 763
        height = 685
        screenwidth = self.app_root.winfo_screenwidth()
        screenheight = self.app_root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.app_root.geometry(alignstr)
        
        self.__render__()
        self.app_root.bind_all("<Motion>", func=self.state)
        self.iter = 1
        self.tbody = None





    def __render__(self):
        self.header()
        self.cpu_benchmark_frame()
        self.IOBenchmarkFrame()
        self.result_table()
        self.app_root_canvas()

    def state(self, event=None):
        if not(self.tbody == None):
            self.tbody.flm.destroy()
        self.tbody = T.Table(self.app_root, self.resultstable)
        self.tbody.flm.pack(pady=5, fill=tk.X)

    #creat table
    def result_table(self):
        self.thead = T.Table(self.app_root, self.thead)
        self.thead.flm.pack(pady=5, fill=tk.X)
        self.tbody = T.Table(self.app_root, self.resultstable)
        self.tbody.bind_all("<Destroy>", func=self.state)

    def ioBenchamrk(self):
        bench = ioBench.HarddiskBenchmark()
        self.resultstable[self.iter]["create"] = bench.result[0]
        self.resultstable[self.iter]["read"] = bench.result[1]
        self.resultstable[self.iter]["write"] = bench.result[2]
        self.resultstable[self.iter]["delete"] = bench.result[3]

    def app_root_canvas(self):
        btn_quit = tk.Button(master=self.app_root, text="quit",
                             command=self.app_root.destroy)
        btn_quit.place(x=700, y=650, )

    def header(self,):
        lbl_top = tk.Frame(master=self.app_root, width=300, relief=tk.RAISED)
        lbl_app = tk.Label(master=lbl_top, text="Super Benchmark")

        lbl_app.pack()
        lbl_top.pack(pady=20)

        lbl_sys = tk.Label(master=lbl_top, text="System information")
        flm_sys = S.SysteminfoFrame(lbl_top)
        lbl_sys.pack()
        flm_sys.flm.pack()

    def cpu_benchmark_frame(self):
        frm_cpu_bench = tk.Frame(master=self.app_root, relief=tk.RAISED)
        lbl_cpu_bench = tk.Label(master=frm_cpu_bench,
                                 text="CPU bench!", width=10)

        btn_start_cpu_bench = tk.Button(master=frm_cpu_bench, text="start",
                                        command=self.cpu_benchmark)
        lbl_cpu_bench.grid(row=0, column=0,)
        btn_start_cpu_bench.grid(row=0, column=1,)
        frm_cpu_bench.pack()

    def IOBenchmarkFrame(self):
        frm_io_bench = tk.Frame(master=self.app_root, relief=tk.RAISED)

        lbl_io_bench = tk.Label(master=frm_io_bench, text="I/O bench!")
        btn_start_io_bench = tk.Button(master=frm_io_bench, text="start",
                                       command=self.ioBenchamrk)
        dooall = tk.Button(master=frm_io_bench, text="doall",
                           command=self.doallbenchwithupdatestate)

        lbl_io_bench.grid(row=0, column=0,)
        btn_start_io_bench.grid(row=0, column=1,)
        dooall.grid(row=0, column=2,)

        frm_io_bench.pack()

    def cpu_benchmark(self):
        a = cpuBench.Benchmark()
        a.multicoreBenchmark()
        self.resultstable[self.iter]["cpu"] = a.excuteTime
        messagebox.showinfo(title="result", message=a.excuteTime)


    #Program run DOALL
    def doallbenchmark(self):
        self.resultstable.append(
            {"round": self.iter, "cpu": None, "create": None, "read": None, "write": None, "delete": None})
        self.cpu_benchmark()
        time.sleep(4)
        self.ioBenchamrk()
        self.iter += 1

    def doallbenchwithupdatestate(self):
        self.resultstable.append(
            {"round": self.iter, "cpu": None, "create": None, "read": None, "write": None, "delete": None, "mem": None})
        a = cpuBench.Benchmark()
        a.multicoreBenchmark()
        self.resultstable[self.iter]["cpu"] = a.excuteTime
        self.state()
        self.app_root.update()
        time.sleep(4)
        self.app_root.update()
        bench = ioBench.HarddiskBenchmark()
        bench.createFilesOs()
        self.resultstable[self.iter]["create"] = bench.result[0]
        self.state()
        self.app_root.update()

        bench.sequentialRead_os()
        self.resultstable[self.iter]["read"] = bench.result[1]
        self.state()
        self.app_root.update()

        bench.sequentialWrite_os()
        self.resultstable[self.iter]["write"] = bench.result[2]
        self.state()
        self.app_root.update()

        bench.deleteTempFile()
        self.resultstable[self.iter]["delete"] = bench.result[3]
        self.state()
        self.app_root.update()

        m = M.MemoryBenchmark()
        m.memoryBenchmark()
        self.resultstable[self.iter]["mem"] = m.result
        self.state()
        self.app_root.update()

        self.iter += 1
        messagebox.showinfo(title="result", message="BenchmarkComplete")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
