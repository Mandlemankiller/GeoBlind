import re
import platform
import os
from tkinter import *

backgroundColor = "#ddfffb"
dialogColor = "#7b9e9a"
rootDirName = "geoblind"
homePath = os.path.expanduser("~")
geoblindPath = os.path.join(homePath, rootDirName)
operatingSystem = platform.system()
regex = re.compile("[^a-zA-Z0-9_ěščřžýáíéóúůďťňÓĎŇŤŠČŘŽÝÁÍÉĚÚŮ]")

main = Tk() # define main window