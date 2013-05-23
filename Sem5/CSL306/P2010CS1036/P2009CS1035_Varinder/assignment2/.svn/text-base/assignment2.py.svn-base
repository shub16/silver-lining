from fltk import *
import sys


def fltk_code(ptr):
    import assig1
    sys.exit(0)

def other_code(ptr):
    import tkinte
    sys.exit(0)

window = Fl_Window(100,100,400,200)
window.label("assingment 2")
#textdis = Fl_Tile(50, 50,300,30)
#textdis.label("click on button to run code")

button1 = Fl_Button(50,150,100,30)
button1.label("pyFltk")

button2 = Fl_Button(250,150,100,30)
button2.label("Tkinter")

button1.callback(fltk_code)
button2.callback(other_code)

window.show()

Fl.run()
    
    
    
    
