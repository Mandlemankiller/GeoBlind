from tkinter import *
import os

# Local imports
import NewMap
import Widgets
import Constants
import TerminalColors

c = TerminalColors.Color # Define colors

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