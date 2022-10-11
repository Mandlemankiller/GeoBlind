from tkinter import *
import PIL.Image as PIM
import os
import shutil

# Local imports
import Constants
import Widgets
import Add

def createMap(newMapWin, mapName, mapFilePath):
    newMapWin.destroy()
    # Save constants localy
    main = Constants.main
    geoblindPath = Constants.geoblindPath
    win = Toplevel(main)

    main.withdraw()

    mapFileWorkspaceName = "map.png"
    workspaceName = "workspace"

    workspacePath = os.path.join(geoblindPath, workspaceName)
    mapFileName = os.path.basename(mapFilePath)
    mapFileWorkspacePath = os.path.join(workspacePath, mapFileWorkspaceName)
    
    if os.path.exists(workspacePath):
        shutil.rmtree(workspacePath)

    os.mkdir(os.path.join(workspacePath)) # Make workspace directory
    shutil.copy(mapFilePath, workspacePath) # Copy mapfile to workspace dir
    os.rename(os.path.join(workspacePath, mapFileName), mapFileWorkspacePath) # rename it to map.png

    win.title(mapName)
    win['background']=Constants.backgroundColor
    win.attributes('-fullscreen',True)
    win.geometry("1700x900")

    canvas = Canvas(win, bg=Constants.backgroundColor)
    win.update()
    canvas.pack(anchor='nw', fill='both', expand=1)
    canvas.update()
    btn = Widgets.Butonek(canvas, "add", lambda: Add.addPoint(win, canvas))
    btn.pack(side="bottom")
    
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # btn.place(width=width/2, height=height/2)

    mapWorkspaceFile = PIM.open(mapFileWorkspacePath)
    if (int(height * mapWorkspaceFile.width / mapWorkspaceFile.height) <= width):
        mapWorkspaceFile = mapWorkspaceFile.resize((int(height * mapWorkspaceFile.width / mapWorkspaceFile.height), height))
    else:
        mapWorkspaceFile = mapWorkspaceFile.resize((width, int(width * mapWorkspaceFile.height / mapWorkspaceFile.width)))
    mapWorkspaceFileScaledPath = os.path.join(workspacePath, mapFileWorkspaceName + "_scaled.png")
    mapWorkspaceFile.save(mapWorkspaceFileScaledPath)

    mapPhIm = PhotoImage(file=mapWorkspaceFileScaledPath)
    # So the image doesn't get garbage collected
    win.img = mapPhIm

    canvas.create_image(width/2, height/2, image=mapPhIm, anchor="center")
    canvas.bind("<Button-1>", lambda event: Add.canvasClick(event, win))

