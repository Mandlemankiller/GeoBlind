from tkinter import *

# Local imports
import Widgets
import Constants

pointing = False
label = None
x = 0
y = 0
pointSize = 10

def addPoint(mapWin, canvas):
    global pointing
    global label
    if pointing == True:
        pointing = False
        label.destroy()
    else:
        pointing = True
        label = Widgets.Lab(mapWin, "Click on the map to add a point.", Constants.dialogColor, 20)
        # win = Widgets.ModalWin(Constants.main, "Add", "400x400", False, 0.9, False, True)
        
        label.pack()
        label.place(relx=0.5, rely=0.15, anchor=CENTER)

def canvasClick(event, mapWin):
    if pointing == True:
        global x, y
        x = event.x
        y = event.y
        x1, y1 = x - pointSize/2, y - pointSize/2
        x2, y2 = x + pointSize/2, y + pointSize/2
        point = event.widget.create_oval(x1, y1, x2, y2, fill="red")
        # Open Add point win
        win = Widgets.ModalWin(mapWin, "Add a point", "600x300", False, 0.8,  False, True)

        # Main label
        updateLabel = Label(win, text="Add a point",font=("Ubuntu",30), bg=Constants.dialogColor)
        updateLabel.grid(row=0)

        # Name
        nameLabel = Label(win, text="Name: ", font=("Ubuntu",20), bg=Constants.dialogColor)
        nameLabel.grid(row=1)
        # Map name input
        sv = StringVar()
        createBtn = Widgets.Butonek(win, "create", lambda: createPoint())
        # sv.trace("w", lambda name, index, mode, sv=sv: mapNameEntryEvent(sv, createBtn, mapFilePath))
        nameEntry = Entry(win, font=("Ubuntu",20), textvariable=sv)
        nameEntry.grid(row=1, column=1)

        exitBtn = Widgets.Butonek(win, "exit_small", lambda: exitWin(win, event.widget, point))
        exitBtn.grid(row=3)

        createBtn.grid(row=3, column=1)
    
        # Try to center everything (very poorly)
        updateLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
        nameLabel.place(relx=0.15, rely=0.45, anchor=CENTER)
        nameEntry.place(relx=0.65, rely=0.45, anchor=CENTER)
        exitBtn.place(relx=0.2, rely=0.8, anchor=CENTER)
        createBtn.place(relx=0.8, rely=0.8, anchor=CENTER)
        # createBtn.place_forget()

def createPoint():
    print("hola")

def exitWin(win, canvas, shape):
    canvas.delete(shape)
    win.destroy()