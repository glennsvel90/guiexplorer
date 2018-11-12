import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
# win.resizable(0,0)


alabel = ttk.Label(win, text="A Label")
alabel.grid(column=0, row=0)



def clickMe():
    buttonAction.configure(text="** I have been clicked! **")
    alabel.configure(forground='red')
    alabel.configure(text='A Red Label')

buttonAction = ttk.Button(win, text = "Click Me", command=clickMe).grid(column=1, row=0)

ttk.Label(win, text="A Label").grid(column=0, row=0)






















win.mainloop()
