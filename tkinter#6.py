import tkinter
from tkinter import *
root = Tk()
root.geometry("300x250+300+300")
def getvalue():
	print("the value is: ",user1.get())
	print("the value is ", user2.get())
	
'''f = Frame(root,borderwidth=10,bg="blue")
f.pack()
b = Button(f,text="press this")
b.pack()'''
l = Label(root,text="Name in block letters:")
l.grid(row=0,column=1)
m = Label(root,text="Surname in block letters:")
m.grid(row=1,column = 1)
user1 = StringVar()
user2 = StringVar() 
a = Entry(root,textvariable=user1)
b = Entry(root,textvariable=user2)
a.grid(row=0,column=2)
b.grid(row=1,column=2)
q = Button(text="submit",command=getvalue)
q.grid(row=2,column=1)






root.mainloop()

#from tkinter import *  


