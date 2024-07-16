from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('My Image')
#root.iconbitmap(r'C:\Users\HP\OneDrive\Desktop\nutan.ico')


my_img = ImageTk.PhotoImage(Image.open(r'C:\Users\HP\OneDrive\Desktop\nutan.jpg'))
my_label = Label(image=my_img)
my_label.pack()












button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()






root.mainloop()