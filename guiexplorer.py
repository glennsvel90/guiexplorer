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
aEntry.grid(column=0, row=2)

button2Action = ttk.Button(win, text = "Click2 Me", command=click2Me)
button2Action.grid(column=1, row=2)

aEntry.focus() # make the mouse cursor appear on this widget at the start of the application

def click3Me():
    button3Action.configure(text="Hello " + name3.get() + ' ' + numberChosen.get())
    buttonAction.configure(state='disabled') # make the click3me disable the top button


ttk.Label(win, text="Enter a name:").grid(column=0, row=3)

name3 = tk.StringVar()
a3Entry = ttk.Entry(win, textvariable=name3)
a3Entry.grid(column=0, row=4)

button3Action = ttk.Button(win, text = "Click3 Me", command=click3Me)
button3Action.grid(column=1, row=4)

ttk.Label(win, text="Choose a number:").grid(column=2, row=3)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, textvariable=number, state='readonly')
numberChosen["values"] = (1,10,50,100,500,1000)
numberChosen.grid(column=2,row=4)
numberChosen.current(0)


























win.mainloop()
