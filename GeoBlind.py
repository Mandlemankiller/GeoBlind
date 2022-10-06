from tkinter import *
import os

# Local imports
import NewMap
import Widgets
import Constants

class c:  # define colors and text styles
    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Info = "\033[32m\033[1m[INFO] \033[34m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    Bold = "\033[1m"
    Underlined = "\033[4m"
    END = '\033[0m'

def dg(msg): # info function
    print(c.Info + msg + c.END)

if not os.path.exists(Constants.geoblindPath): # check and create root dir
    os.mkdir(Constants.geoblindPath)
    dg("Made root directory")

# Main Window
backgroundColor = Constants.backgroundColor
main = Constants.main
geoblindPath = Constants.geoblindPath

main.title("GEOBLIND") 
main['background']=backgroundColor
main.attributes('-fullscreen',True) # fullscreen

label = Label(main,text ="Welcome to GEOBLIND!",font=("Ubuntu",40))
label['background']=backgroundColor
label.pack(pady = 10)

newBtn = Widgets.Butonek(main, "new", lambda: NewMap.newMap()) # New Map button
newBtn.pack(pady=20)

# openBtn = butonek.Butonek(main, "open")
# openBtn.pack(pady=20)

# exportBtn = butonek.Butonek(main, "export")
# exportBtn.pack(pady=20)

exitBtn = Widgets.Butonek(main, "exit", main.destroy) # Exit program button

exitBtn.pack(pady=20)

# mainloop, runs infinitely
mainloop()