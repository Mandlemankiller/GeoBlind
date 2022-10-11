from time import sleep
from tkinter import *
from tkinter import ttk
from threading import Thread
import os

# Local imports
import Constants

class Butonek(Button, ttk.Button):
    def __init__(self, window, fileName, command, modalStarter=False):
        self.img = PhotoImage(master=Constants.main, file=os.path.join(Constants.geoblindPath, fileName + ".png"))
        self.imgHover = PhotoImage(file=os.path.join(Constants.geoblindPath, fileName + "_hover" + ".png"))
        super().__init__(window)
        self["command"] = command
        self["bg"] = Constants.backgroundColor
        self["image"] = self.img

        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)
        
        if modalStarter == True:
            self.bind("<Button-1>", self.thread)
    
    def enter(self, e):
        self["image"] = self.imgHover
    
    def leave(self, e):
        self["image"] = self.img
    
    def thread(self, e):
        Thread(target = self.click).start()

    def click(self):
        sleep(0.3)
        try:
            if self.winfo_exists() == 1:
                self["image"] = self.img
        except: # This means that the program shut down completely and the mainloop in geoblind.py stopped
            pass
    
class ModalWin(Toplevel):
    def __init__(self, main, title, geometry, resizable, opacity, movable, centered):
        super().__init__(main)
        self.title(title)
        self.geometry(geometry)
        self.transient(main)
        self["bg"] = Constants.dialogColor

        if resizable == False:
            self.resizable(False, False)
        else:
            self.resizable(True, True)
        
        if movable == False:
            self.overrideredirect(True)
        else:
            self.overrideredirect(False)
        
        self.attributes("-type", "normal")

        if opacity < 1:
            self.attributes("-alpha", opacity)
        else:
            self.attributes("-alpha", 1)

        if centered == True:
            self.centerWin()
        
        self.wait_visibility()
        self.grab_set()
            
    def centerWin(self):
        self.update_idletasks()
        width = self.winfo_width()
        frmWidth = self.winfo_rootx() - self.winfo_x()
        winWidth = width + 2 * frmWidth
        height = self.winfo_height()
        titlebarHeight = self.winfo_rooty() - self.winfo_y()
        winHeight = height + titlebarHeight + frmWidth
        x = self.winfo_screenwidth() // 2 - winWidth // 2
        y = self.winfo_screenheight() // 2 - winHeight // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()
    
class Lab(Label):
    def __init__(self, win, text, bgColor, fontSize, font=None):
        super().__init__(win)
        self["text"] = text
        if font == None:
            font = "Ubuntu"
        self["font"] = font, fontSize
        self["bg"] = bgColor