from tkinter import *
import os
import urllib.request
from threading import Thread
import json

# Local imports
import NewMap
import Widgets
import Constants
import TerminalColors

c = TerminalColors.Color # Define colors

def info(msg): # info function
    print(c.Info + msg + c.END)

def error(msg): # info function
    print(c.Error + msg + c.END)

def updateTextures(win):
    urllib.request.urlretrieve("https://skladu.jeme.cz/geoblind/textures.zip", "textures.zip")
    win.destroy()


if not os.path.exists(Constants.geoblindPath): # check and create root dir
    os.mkdir(Constants.geoblindPath)
    info("Made root directory")

# Main Window

# os checkBob
if Constants.operatingSystem != "Linux": # OS not supported
    error("OS not supported!")
    exit()

backgroundColor = Constants.backgroundColor
main = Constants.main
geoblindPath = Constants.geoblindPath

main.title("GEOBLIND") 
main['background']=backgroundColor
main.attributes('-fullscreen',True) # fullscreen


label = Label(main,text ="Welcome to GEOBLIND!",font=("Ubuntu",40))
label['background']=backgroundColor
label.pack(pady = 10)

newBtn = Widgets.Butonek(main, "new", lambda: NewMap.newMap(), True) # New Map button
newBtn.pack(pady=20)

# openBtn = butonek.Butonek(main, "open")
# openBtn.pack(pady=20)

# exportBtn = butonek.Butonek(main, "export")
# exportBtn.pack(pady=20)

exitBtn = Widgets.Butonek(main, "exit", main.destroy) # Exit program button

exitBtn.pack(pady=20)


# updateWin = Widgets.ModalWin(main, "Updating...", "800x100", False, 1, False, True)
# updateLabel = Label(updateWin, text="Updating textures...",font=("Ubuntu",40), bg=Constants.dialogColor)
# updateLabel.pack()

try:
    response = urllib.request.urlopen("https://api.github.com/repos/Mandlemankiller/CustomCapes/releases/latest")
    jsonObj = json.load(response)

    f = open(os.path.join(Constants.geoblindPath, "version"), "r")

    if f.readline() != jsonObj["tag_name"]:
        info("Update availible!")
        # f = open(os.path.join(Constants.geoblindPath, "version"), "w")
        # f.write(jsonObj["tag_name"])
    else:
        info("No updates availible!")
    f.close()
except:
    error("Unable to check for updates!")

mainloop()