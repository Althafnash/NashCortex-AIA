import tkinter as tk
import tkinter.ttk as ttk
from time import strftime

def Clock():

    root = tk.Tk()
    root.title("clock")

    def time():
        string = strftime('%H:%M:%S %p')
        lable.config(text=string)
        lable.after(1000,time)

    lable = tk.Label(root ,font=("ds-digital", 80) , bg="black" ,fg="lightgreen" )
    lable.pack(anchor="center")
    time()

    root.mainloop()