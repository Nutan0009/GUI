# grid making
from tkinter import *
root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name Is Nutan").grid(row=1, column=1)

root.mainloop()

