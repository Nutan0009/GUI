from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()

def popup():
	response = messagebox.showinfo("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()
mainloop()