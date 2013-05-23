#!/usr/bin/python
from gi.repository import Gtk

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
		#Creates a Window
		#Heirarchy -> window ->(topBox->(entry, Button))
		self.topbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
		self.add(self.topbox)
		self.entry = Gtk.Entry()
		self.topbox.pack_start(self.entry, True, True, 0)	
		self.button = Gtk.Button(label = "Send")
		self.button.connect("clicked", self.on_button_clicked)
		#function on_button_clicked called when the button is clicked
		self.topbox.pack_start(self.button, True, True, 0)
	
	def on_button_clicked(self, widget):
		print "Hello"

class MyFrame(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
		#Creates a Window
		#Heirarchy -> window ->(topBox->(entry, Button))
		self.topbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
		self.add(self.topbox)
		self.label = Gtk.Label("Choose the option")
		self.topbox.pack_start(self.label, True, True, 0)
		self.button1 = Gtk.Button(label = "GTK")
		self.button1.connect("clicked", self.on_button_clicked)
		self.topbox.pack_start(self.button1, True, True, 0)
		#function on_button_clicked called when the button is clicked
		self.button2 = Gtk.Button(label = "Tkinter")
		self.button2.connect("clicked", self.on_button)
		self.topbox.pack_start(self.button2, True, True, 0)

	def on_button_clicked(self, widget):
		win = MyWindow()
		win.connect("delete-event", Gtk.main_quit)
		#to quit the application when the user clicks the close button
		win.show_all()
		Gtk.main()
	
	def on_button(self, widget):
		import text
		
			

#decides which GUI library to be used based on the value of flag
#tk is a file, containing GUI code based on Tkinter, present in the same location
win = MyFrame()
#calls MyFrame so as to present the user with the option
win.connect("delete-event", Gtk.main_quit)
#to quit the application when the user clicks the close button
win.show_all()
Gtk.main()

