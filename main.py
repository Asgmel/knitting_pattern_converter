from tkinter import *
from tkinter import ttk
import sv_ttk

root = Tk()
root.title("Marits Knitting Tool")
root.geometry("500x500")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

sv_ttk.set_theme("dark")
root.mainloop()
