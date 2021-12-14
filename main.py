import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import Benchmark


class App:
    def __init__(self, root):
        # setting title
        root.title("Benchmark")
        # setting window size
        frm = ttk.Frame(root, padding=10)
        ft = tkFont.Font(family='Times', size=10)
        frm.grid()
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Label(frm, text="CPU bench!",
                  foreground="#333333", justify="center").grid(column=0, row=1)
        ttk.Button(frm, text="start", command=self.GButton_35_command).grid(
            column=1, row=1)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(
            column=1, row=0)
        width = 763
        height = 685
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # GListBox_304 = tk.Listbox(root)
        # GListBox_304["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times', size=10)
        # GListBox_304["font"] = ft
        # GListBox_304["fg"] = "#333333"
        # GListBox_304["justify"] = "center"
        # GListBox_304.place(x=0, y=790, width=80, height=25)

        # GLabel_882 = tk.Label(root)
        # ft = tkFont.Font(family='Times', size=10)
        # GLabel_882["font"] = ft
        # GLabel_882["fg"] = "#333333"
        # GLabel_882["justify"] = "center"
        # GLabel_882["text"] = "CPU bench"
        # GLabel_882.place(x=20, y=30, width=88, height=49)

        # GButton_35 = tk.Button(root)
        # GButton_35["bg"] = "#efefef"
        # ft = tkFont.Font(family='Times', size=10)
        # GButton_35["font"] = ft
        # GButton_35["fg"] = "#000000"
        # GButton_35["justify"] = "center"
        # GButton_35["text"] = "Start"
        # GButton_35.place(x=30, y=80, width=70, height=25)
        # GButton_35["command"] = self.GButton_35_command

    def GButton_35_command(self):
        a = Benchmark.Benchmark()
        a.multicoreBenchmark(50)
        print(a.excuteTime)
        # win32api.MessageBox(0, a.excuteTime, 'CPU')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
