from tkinter import*
#TO IMPORT THE MESSAGE BOX
import tkinter.messagebox as tmsg
root = Tk()
#TMSG WILL SHOW DIALOG BOX , WE CAN DO ANYTHING WITH IT LIKE SHOWING WARNIGN , SHOWING INFO , SHOWING IMAGE ETC.......
def jupiter():
	tmsg.showinfo("ABOUT JUPITER","Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but slightly less than one-thousandth the mass of the Sun. Jupiter is the third-brightest natural object in the Earth's night sky after the Moon and Venus. It has been observed since pre-historic times and is named after the Roman god Jupiter, the king of the gods, because of its observed size.")
#to add single menu
def saturn():
	a = tmsg.askquestion("ALERT", "Do you wish to know about saturn?")
	if a == "yes":
		tmsg.showinfo("saturn" , "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.[22][23] It only has one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive.[24][25][26] Saturn is named after the Roman god of wealth and agriculture. Its astronomical symbol (♄) has been traced back to the Greek Oxyrhynchus Papyri, where it can be seen to be a Greek kappa-rho with a cross-bar, as an abbreviation for Κρονος (Cronos), the Greek name for the planet.[27] It later came to look like a lower-case Greek eta, with the cross added at the top in the 16th century.")
	else:
		None 
def venus():
	b = tmsg.askquestion("ALERT", "Do you wish to know about venus?")
	if b == "yes":
		tmsg.showinfo("VENUS","Venus is the second planet from the Sun. It is named after the Roman goddess of love and beauty. As the brightest natural object in Earth's night sky after the Moon, Venus can cast shadows and can be, on rare occasions, visible to the naked eye in broad daylight.[17][18] Venus lies within Earth's orbit, and so never appears to venture far from the Sun, either setting in the west just after dusk or rising in the east a little while before dawn. Venus orbits the Sun every 224.7 Earth days.[19] It has a synodic day length of 117 Earth days and a sidereal rotation period of 243 Earth days. As a consequence, it takes longer to rotate about its axis than any other planet in the Solar System, and does so in the opposite direction to all but Uranus. This means the Sun rises in the west and sets in the east.[20] Venus does not have any moons, a distinction it shares only with Mercury among the planets in the Solar System")
	else:
		None
'''m1 = Menu(root)
m1.add_command(label="exit",command=quit)
root.config(menu=m1)'''
#to add multiple menu or submenu
m2 = Menu(root)
m1 = Menu(m2)
m1.add_command(label="jupiter", command=jupiter)
m1.add_command(label="saturn", command=saturn)
#add a line bw menu
m1.add_separator()
m1.add_command(label="earth")
m1.add_command(label="venus", command=venus)
root.config(menu=m2)
m2.add_cascade(label="planets",menu=m1)



root.mainloop()