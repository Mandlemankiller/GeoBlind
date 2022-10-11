import re
import platform
import os
from tkinter import *

backgroundColor = "#ddfffb"
dialogColor = "#7b9e9a"
boxColor = "#cbd8d8"
operatingSystem = platform.system()
rootDirName = ".geoblind"
mediaDirName = "media"
homePath = os.path.expanduser("~")
geoblindPath = os.path.join(homePath, rootDirName)
regex = re.compile("[^a-zA-Z0-9_ěščřžýáíéóúůďťňÓĎŇŤŠČŘŽÝÁÍÉĚÚŮ]")
main = Tk() # define main window