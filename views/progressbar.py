from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


class progressionbar:
    def __init__(self, root):
        # root window

        self.tl = tk.Toplevel(master=root)
        self.pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        self.tl.grid(WIDTHINC=300, HEIGHTINC=100)
        self.value_label = ttk.Label(
            self.tl, text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)

    def update_progress_label(self):
        return f"Current Progress: {self.pb['value']}%"

    def progress(self):
        if self.pb['value'] < 100:
            self.pb['value'] += 20
            self.value_label['text'] = self.update_progress_label()
        else:
            showinfo(message='The progress completed!')

    # place the progressbar

    # label
