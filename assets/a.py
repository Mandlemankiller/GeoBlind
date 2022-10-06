from tkinter import *   

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Button Background Example')

button = Button(tkWindow, text = 'Submit')  
button.grid()
# button.place(relx=0.8, rely=0.8, anchor=CENTER)
button.grid_forget()
  
tkWindow.mainloop()