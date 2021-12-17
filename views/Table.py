
from tkinter import *
import configparser
from config import CONFIG


class Table:

    def __init__(self, root, datalst):

        # code for creating table
        config = CONFIG()
        self.width = config.WIDTH
        self.fontsize = config.FONT_SIZE
        self.total_rows = len(datalst)
        self.total_columns = len(datalst[0])
        self.flm = Frame(master=root)
        if not(len(datalst) < 1):
            for i in range(self.total_rows):
                if isinstance(datalst[i], dict):
                    j = 0
                    for k in datalst[i]:

                        self.e = Label(self.flm, fg='black', width=self.width,
                                       font=('Arial', self.fontsize, 'normal'), text=f'{datalst[i][k]}')

                        self.e.grid(row=i, column=j)
                        j += 1
                else:
                    for j in range(self.total_columns):

                        self.e = Label(self.flm, fg='black', width=self.width,
                                       font=('Arial', self.fontsize, 'bold'), text=f'{datalst[i][j]}')

                        self.e.grid(row=i, column=j)
