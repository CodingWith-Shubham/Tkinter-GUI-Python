from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
def rating():
	tmsg.showinfo("RATING BY USER", "THANKS FOR YOUR RATING !!! HAVE A WONDERFUL DAY")
	
a = Label(root,text="RATE YOUR EXPERIENCE").pack()
slider = Scale(root , from_=0 , to=10 , tickinterval=10, orient=HORIZONTAL).pack()
B1 = Button(root, text="SUBMIT", command=rating).pack()



root.mainloop()