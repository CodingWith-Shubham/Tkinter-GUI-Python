from tkinter import *
root = Tk()
#to give width and hieght of box
root.geometry("300x250+300+300")
#to give min size of window
root.minsize(width = 400, height = 400)
#to give max size of window
root.maxsize(width = 500, height = 600)
#to print text on empty window
a = Label(text="hello world nice to meetu")
a.pack()
root.mainloop()
#to obtain a white blank screen 

