from tkinter import*
root = Tk()
#to add single menu
'''m1 = Menu(root)
m1.add_command(label="exit",command=quit)
root.config(menu=m1)'''
#to add multiple menu or submenu
m2 = Menu(root)
m1 = Menu(m2)
m1.add_command(label="jupiter")
m1.add_command(label="saturn")
#add a line bw menu
m1.add_separator()
m1.add_command(label="earth")
m1.add_command(label="venus")
root.config(menu=m2)
m2.add_cascade(label="planets",menu=m1)
''

root.mainloop()