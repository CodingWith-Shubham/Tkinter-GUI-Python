from tkinter import *
#to know about background,foreground,padding,font,fillx,filly
root = Tk()
root.geometry("300x250+300+300")
a = Label(text="The Indian Space Research Organisation[a] (ISRO /ˈɪsroʊ/) \nor (IAST : Bhāratīya Antrikṣ \nAnusandhān Saṅgaṭhan) is the national \nspace agency of India, headquartered in \nBengaluru. It operates under the \nDepartment of Space (DOS) which is \ndirectly overseen by the Prime Minister \nof India, while Chairman of ISRO acts as \nexecutive of DOS as well. ISRO is the \nprimary agency in India to perform \ntasks related to space based \napplications, space exploration and \ndevelopment of related technologies.[6] \nIt is one of six government space \nagencies in the world which possess \nfull launch capabilities, deploy \ncryogenic engines, launch extra-\nterrestrial missions and operate large \nfleets of artificial satellites.",bg='blue',fg='white' , padx=23,pady=23,font="arial 10 italic",border=3,relief=GROOVE)
a.pack(fill=X)
a.pack(fill=Y)

root.mainloop()