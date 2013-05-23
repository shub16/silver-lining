#import tkinter library
from Tkinter import *

#import pyqt library
import sys
from PyQt4.QtGui import *

#class to add widgets to tkinter gui
class App:
#constructor of app class
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

def Main():
    print " Enter Your Choice:  "
    print " 1 for TKinter GUI"
    print " 2 for PYQT GUI"
    
    try:
        x = int(raw_input())
    except ValueError:
        print 'Enter a valid number!!'
        
    if x == 1:
        root.mainloop()
    elif x == 2:
        import tryqt              
    else:
        sys.exit(0)

if __name__ == '__main__':
    Main()




