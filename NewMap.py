from glob import glob
from tkinter import *
from threading import Thread
from tkinter import filedialog
from time import sleep
import os

# Local imports
import Widgets
import Constants
import Create

mapFilePath = None
mapName = None

def newMap(): # Function called after pressing NEW button in main
    global mapFilePath
    global mapName

    main = Constants.main
    dialogColor = Constants.dialogColor
    # from geoblind import Butonek
    win = Widgets.ModalWin(main, "Create New Blind Map", "1000x400", False, 1, False, True)
    # Label
    mapLabel = Label(win, text="Create New Blind Map", font=("Ubuntu",30), bg=dialogColor)
    mapLabel.grid(row=0)

    # Map name label
    nameLabel = Label(win, text="Map Name: ", font=("Ubuntu",20), bg=dialogColor)
    nameLabel.grid(row=1)
    # Map name input
    sv = StringVar()
    createBtn = Widgets.Butonek(win, "create", lambda: Create.createMap(win, mapName, mapFilePath))
    sv.trace("w", lambda name, index, mode, sv=sv: mapNameEntryEvent(sv, createBtn, mapFilePath))
    nameEntry = Entry(win, font=("Ubuntu",20), textvariable=sv, bg=Constants.boxColor)
    nameEntry.grid(row=1, column=1)
    # Path name label
    pathLabel = Label(win, text="Map Image: ", font=("Ubuntu",20), bg=dialogColor)
    pathLabel.grid(row=2)
    # Path name button
    pathBtn = Button(win, text="Click Here To Select", font=("Ubuntu",20), bg=Constants.boxColor)
    pathBtn.grid(row=2, column=1)
    # The command is configured here, because the "file" def requires the button as a parameter, which is not possible before .grid or .pack
    pathBtn.configure(command = lambda: selectMapImg(win, pathBtn, sv, createBtn, main))

    exitBtn = Widgets.Butonek(win, "cancel_small", lambda: exitWin(win))
    exitBtn.grid(row=3)

    createBtn.grid(row=3, column=1)
   
    # Try to center everything (very poorly)
    mapLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
    nameLabel.place(relx=0.35, rely=0.35, anchor=CENTER)
    nameEntry.place(relx=0.65, rely=0.35, anchor=CENTER)
    pathLabel.place(relx=0.35, rely=0.5, anchor=CENTER)
    pathBtn.place(relx=0.65, rely=0.5, anchor=CENTER)
    exitBtn.place(relx=0.2, rely=0.8, anchor=CENTER)
    createBtn.place(relx=0.8, rely=0.8, anchor=CENTER)
    createBtn.place_forget()
    # createBtn["state"] = "disabled"



def mapNameEntryEvent(sv, btn, path):
    global mapName
    if sv.get() == "" or os.path.exists(os.path.join(Constants.geoblindPath, sv.get())): # if emptied, remove create button
        btn.place_forget()
    elif path != None: # if filled and image filled in, show create button
        btn.place(relx=0.8, rely=0.8, anchor=CENTER)
    
    sv.set(sv.get().replace(" ", "_")) # replace all spaces with underscores
    sv.set(Constants.regex.sub("", sv.get())) # replace all nonregex chars with question mark

    if len(sv.get()) > 20:
        sv.set(sv.get()[0:20])
    
    mapName = sv.get()

def selectMapImg(win, btn, sv, createBtn, main):
    global mapFilePath
    win.withdraw() # hide the new map window, so it doesnt get in the way
    pathValid = False
    while not pathValid: # untill the selected file is valid (window was not closed) ask
        Thread(target = resize).start() # call a new thread to resize the filedialog window
        # open filedialog for image selection
        path = filedialog.askopenfilename(title="Open Map Image", filetypes=[("Image Files", ".png .jpeg .jpg .svg .pdf")], parent=main, initialdir=Constants.homePath)

        if not os.path.isfile(str(path)): # if the path it returned is not valid
            win.deiconify()
            win.grab_set() # transfer all events, keybinds and click from the application to this window
            return
        else: # path is valid
            pathValid = True
    displayPath = os.path.basename(path)
    if len(displayPath) > 23:
        displayPath = "..." + displayPath[-20:] # save ... and the last 20 chars

    btn.configure(text=displayPath) # change the button text

    if sv.get() != "" and not os.path.exists(os.path.join(Constants.geoblindPath, sv.get())):
        createBtn.place(relx=0.8, rely=0.8, anchor=CENTER)

    mapFilePath = path
    win.deiconify() # show the window again
    win.grab_set() # transfer all events, keybinds and click from the application to this window

def resize(): # resize the window, ONLY WORKS ON LINUX
    if Constants.operatingSystem == "Linux":
        sleep(0.2)
        os.system("wmctrl -r Open Map Image -e 1,200,50,1500,900")

def exitWin(win):
    global mapFilePath
    mapFilePath = None
    win.destroy()