import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
# win.resizable(0,0)





def clickMe():
    buttonAction.configure(text="** I have been clicked! **")
    alabel.configure(foreground='red')
    alabel.configure(text='A Red Label')


alabel = ttk.Label(win, text="A Label")
alabel.grid(column=0, row=0)

buttonAction = ttk.Button(win, text = "Click Me", command=clickMe)
buttonAction.grid(column=1, row=0)

def click2Me():
    button2Action.configure(text="Hello " + name.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=1)

name = tk.StringVar()
aEntry = ttk.Entry(win, textvariable=name)
aEntry.grid(column=0, row=1)

button2Action = ttk.Button(win, text = "Click2 Me", command=click2Me)
button2Action.grid(column=1, row=1)






















win.mainloop()
