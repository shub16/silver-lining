#!/usr/bin/python

from gi.repository import Gtk
from Assign1_P2010CS1082 import ex1

class FirstWindow(Gtk.Window):
	""" This class builds a window in pyGObject. 
	The constructor takes 0 arguments and is of the type: 
		MyWindow = FirstWindow()
	"""
	def __init__(self):
		Gtk.Window.__init__(self, title="My First Window-GObject")
		self.set_size_request(270, 100)
		fixed = Gtk.Fixed()
		text_field = Gtk.Entry()
		button = Gtk.Button(label="Enter!")
		button.connect("clicked", self.on_button_clicked)
				
		fixed.put(text_field, 20, 40)
		fixed.put(button, 200, 40)
		self.add(fixed)
		self.connect("delete-event", Gtk.main_quit)
		self.show_all()
		Gtk.main()    
  
	def on_button_clicked(self, widget):		
		print "You Entered the text"
	
def main():
    print "Enter 1 for pyGObject\nEnter 2 for pyfltk\nEnter 3 for Tkinter"
    value = raw_input("-->");
    value = int(value)
    if( value == 1 ):
        MyWindow = FirstWindow()
        MyWindow.connect("delete-event", Gtk.main_quit)
        MyWindow.show_all()
        Gtk.main()
    elif( value == 2):
        MyWindow = ex1()
    elif( value == 3 ):
		import Assign1_P2010CS1022
        
        
if __name__ == '__main__': main()
    
