from tkinter import *

# Local imports
import Widgets
import Constants

pointing = False
label = None
x = 0
y = 0
pointSize = 8

def addPoint(mapWin, canvas):
    global pointing
    global label
    if pointing == True:
        pointing = False
        label.destroy()
    else:
        pointing = True
        label = Widgets.Lab(mapWin, "CIRCLE: TOGGLED", Constants.dialogColor, 20)
        # win = Widgets.ModalWin(Constants.main, "Add", "400x400", False, 0.9, False, True)
        
        label.pack()
        label.place(relx=0.5, rely=0.15, anchor=CENTER)

def canvasClick(event):
    if pointing == True:
        global x, y
        x = event.x
        y = event.y
        x1, y1 = x - pointSize/2, y - pointSize/2
        x2, y2 = x + pointSize/2, y + pointSize/2
        event.widget.create_oval(x1, y1, x2, y2, fill="red")