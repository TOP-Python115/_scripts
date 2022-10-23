import tkinter as tk
from tkinter.constants import BOTH, SUNKEN

from typing import Literal


class Notebook:
    def __init__(self):
        self.root = tk.Frame(None)
    
    def start(self):
        self.root.pack()
        self.root.mainloop()

class Factory:
    def __init__(self, pages: Literal[1, 2, 4]):
        self.app = Notebook()
        if pages == 2:
            self.two_page()
        elif pages == 4:
            self.four_page()
        else:
            self.one_page()
        self.app.start()
        
    def one_page(self):
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).pack(fill=BOTH)
    
    def two_page(self):
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).grid(row=0, column=0, sticky='nsew', padx=(1, 2))
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).grid(row=0, column=1, sticky='nsew', padx=(2, 1))
        self.app.root.rowconfigure(0, weight=1)
        self.app.root.columnconfigure(0, weight=1)
        self.app.root.columnconfigure(1, weight=1)

    def four_page(self):
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).grid(row=0, column=0, sticky='nsew', padx=(1, 2), pady=(1, 2))
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).grid(row=0, column=1, sticky='nsew', padx=(2, 1), pady=(1, 2))
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).grid(row=1, column=0, sticky='nsew', padx=(1, 2), pady=(2, 1))
        tk.Text(
            self.app.root,
            relief=SUNKEN,
            font=16
        ).grid(row=1, column=1, sticky='nsew', padx=(2, 1), pady=(2, 1))
        self.app.root.rowconfigure(0, weight=1)
        self.app.root.rowconfigure(1, weight=1)
        self.app.root.columnconfigure(0, weight=1)
        self.app.root.columnconfigure(1, weight=1)


Factory(1)
