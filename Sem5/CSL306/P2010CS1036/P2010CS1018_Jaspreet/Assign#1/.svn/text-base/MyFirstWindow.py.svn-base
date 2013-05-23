#!/usr/bin/python
from gi.repository import Gtk

class FirstWindow(Gtk.Window):
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
	
MyWindow = FirstWindow()

