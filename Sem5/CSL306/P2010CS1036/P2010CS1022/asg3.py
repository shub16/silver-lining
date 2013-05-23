from Tkinter import *

import sys
from PyQt4.QtGui import *
from fltk import *

class App:
#constructor of app class
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
	
	self.label=Label (text='Enter Username')
	self.label.pack(side=TOP,padx=10,pady=6)
	self.entry=Entry(root, width=15)
	self.entry.pack(side=TOP,padx=10,pady=10)

    def say_hi(self):
        print "hi there, everyone!"
    
    def sel(self):
        selection = "You selected the option " + str(var.get())
        label.config(text = selection)

root = Tk()
app = App(root)


var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1 )
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2 )
R2.pack( anchor = W )

label = Label(root)
label.pack()
	
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Check 1", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=0, \
                 width = 8)
C2 = Checkbutton(root, text = "Check 2", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=0, \
                 width = 8)
C1.pack(anchor = W)
C2.pack(anchor = W)

Lb1 = Listbox(root)
Lb1.insert(1, "Algorithm Design")
Lb1.insert(2, "Software Engineering")
Lb1.insert(3, "Opertaing Systems")
Lb1.insert(4, "Artificial Intelligence")
Lb1.insert(5, "Special Topics")
Lb1.insert(6, "Database Systems")

Lb1.pack()
root.geometry("240x310+300+300")
def Main():
    print " Enter Your Choice:  "
    print " 1 for TKinter GUI"
    print " 2 for PYQT GUI"
    print " 3 for FLTK GUI"
    
    try:
        x = int(raw_input())
    except ValueError:
        print 'Enter a valid number!!'
        
    if x == 1:
        root.mainloop()
    elif x == 2:
        import tryqt    
    elif x == 3:
        import flt 	          
    else:
        sys.exit(0)

if __name__ == '__main__':
    Main()




