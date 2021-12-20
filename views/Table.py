
from tkinter import *


class Table:

    def __init__(self, root, datalst):

        # code for creating table
        self.total_rows = len(datalst)
        self.total_columns = len(datalst[0])
        self.flm = Frame(master=root)
        if not(len(datalst) < 1):
            for i in range(self.total_rows):
                if isinstance(datalst[i], dict):
                    j = 0
                    for k in datalst[i]:

                        self.e = Label(self.flm, fg='black', width=11,
                                       font=('Arial', 15, 'normal'), text=f'{datalst[i][k]}')

                        self.e.grid(row=i, column=j)
                        j += 1
                else:
                    for j in range(self.total_columns):

                        self.e = Label(self.flm, fg='black', width=11,
                                       font=('Arial', 15, 'bold'), text=f'{datalst[i][j]}')

                        self.e.grid(row=i, column=j)
