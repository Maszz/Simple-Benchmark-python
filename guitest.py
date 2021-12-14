import tkinter as tk
import tkinter.font as tkFont
from tkinter import Button, messagebox
from Benchmark import Benchmark
from HarddiskBenchmark import HarddiskBenchmark
from MemoryBenchmark import MemoryBenchmark


class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_Benchmark=tk.Label(root)
        GLabel_Benchmark["bg"] = "#000000"
        GLabel_Benchmark["cursor"] = "circle"
        ft = tkFont.Font(family='Electrolize',size=10)
        GLabel_Benchmark["font"] = ft
        GLabel_Benchmark["fg"] = "#01aaed"
        GLabel_Benchmark["justify"] = "center"
        GLabel_Benchmark["text"] = "Benchmark"
        GLabel_Benchmark.place(x=250,y=30,width=92,height=46)

        GButton_Harddisk=tk.Button(root)
        GButton_Harddisk["bg"] = "#000000"
        GButton_Harddisk["activebackground"] = "#90ee90"
        ft = tkFont.Font(family='Electrolize',size=10)
        GButton_Harddisk["font"] = ft
        GButton_Harddisk["fg"] = "#01aaed"
        GButton_Harddisk["justify"] = "center"
        GButton_Harddisk["text"] = "Harddisk"
        GButton_Harddisk.place(x=260,y=180,width=70,height=25)
        GButton_Harddisk["command"] = self.GButton_Harddisk_command

        GButton_Memmory=tk.Button(root)
        GButton_Memmory["bg"] = "#000000"
        GButton_Memmory["activebackground"] = "#90ee90"
        ft = tkFont.Font(family='Electrolize',size=10)
        GButton_Memmory["font"] = ft
        GButton_Memmory["fg"] = "#01aaed"
        GButton_Memmory["justify"] = "center"
        GButton_Memmory["text"] = "Memmory"
        GButton_Memmory.place(x=480,y=180,width=70,height=25)
        GButton_Memmory["command"] = self.GButton_Memmory_command

        GButton_CPU=tk.Button(root)
        GButton_CPU["bg"] = "#000000"
        GButton_CPU["activebackground"] = "#90ee90"
        ft = tkFont.Font(family='Electrolize',size=10)
        GButton_CPU["font"] = ft
        GButton_CPU["fg"] = "#01aaed"
        GButton_CPU["justify"] = "center"
        GButton_CPU["text"] = "CPU"
        GButton_CPU.place(x=60,y=180,width=70,height=25)
        GButton_CPU["command"] = self.GButton_CPU_command

    def GButton_Harddisk_command(self):
        a = HarddiskBenchmark()


    def GButton_Memmory_command(self):
        a = MemoryBenchmark()
        print(a.cacheMemory(1000000))


    def GButton_CPU_command(self):
        a = Benchmark()
        a.multicoreBenchmark(50)
        print(a.excuteTime)
        messagebox.showinfo("showinfo", a.excuteTime)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
