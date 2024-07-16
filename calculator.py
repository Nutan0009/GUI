from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=10, border=5, font=('Helvetica', 24))
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

def add_button(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear_button():
    e.delete(0,END)  

def add2_button():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def equal_button():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num+int(second_number))

button_1=Button(root,text="1",padx=30,pady=20,command=lambda: add_button(1))
button_2=Button(root,text="2",padx=30,pady=20,command=lambda: add_button(2)) 
button_3=Button(root,text="3",padx=30,pady=20,command=lambda: add_button(3))
button_4=Button(root,text="4",padx=30,pady=20,command=lambda: add_button(4))
button_5=Button(root,text="5",padx=30,pady=20,command=lambda: add_button(5))
button_6=Button(root,text="6",padx=30,pady=20,command=lambda: add_button(6))
button_7=Button(root,text="7",padx=30,pady=20,command=lambda: add_button(7))
button_8=Button(root,text="8",padx=30,pady=20,command=lambda: add_button(8))
button_9=Button(root,text="9",padx=30,pady=20,command=lambda: add_button(9))
button_0=Button(root,text="0",padx=30,pady=20,command=lambda: add_button(0))
button_add=Button(root,text="+",padx=29,pady=20,command=add2_button)
button_equal=Button(root,text="=",padx=71,pady=20,command=equal_button)
button_clear=Button(root,text="Clear",padx=59,pady=20,command=clear_button)

button_1.grid(row= 3,column=0)
button_2.grid(row= 3,column=1)
button_3.grid(row= 3,column=2)

button_4.grid(row= 2,column=0)
button_5.grid(row= 2,column=1)
button_6.grid(row= 2,column=2)

button_7.grid(row= 1,column=0)
button_8.grid(row= 1,column=1)
button_9.grid(row= 1,column=2)

button_0.grid(row= 4,column=0)
button_clear.grid(row= 4,column=1,columnspan=2)
button_add.grid(row= 5,column=0)
button_equal.grid(row= 5,column=1,columnspan=2)

#myButton = Button(root, text="Enter Your Stock Quote", command=myClick)
#myButton.pack()

root.mainloop()

