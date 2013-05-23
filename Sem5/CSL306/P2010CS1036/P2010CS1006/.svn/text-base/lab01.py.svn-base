#!/usr/bin/python
from gi.repository import Gtk
import sys
from Tkinter import *

#A class which would be used incase GTK-3.0 is installed in the users computer
class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
		#Creates a Window
		#Heirarchy -> window ->mainbox->(topBox->(middlebox->(radiobuttons,checkBox)),entry, Button))
		self.mainbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 3)
		self.add(self.mainbox)

		self.topbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 3)
		self.mainbox.pack_start(self.topbox, True, True, 0)
		
		self.middlebox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 3)
		self.topbox.pack_start(self.middlebox, True, True, 0)
		
		#RadioGroup
		self.choose1 = Gtk.RadioButton.new_with_label_from_widget(None, "Choice1")
		self.choose1.connect("toggled", self.button_toggled, "1")
		self.middlebox.pack_start(self.choose1, True, True, 0)
		self.choose2 = Gtk.RadioButton.new_with_label_from_widget(self.choose1, "Choice2")
		self.choose2.connect("toggled", self.button_toggled, "2")
                self.middlebox.pack_start(self.choose2, True, True, 0)
		
		#checkBox1
		self.check = Gtk.CheckButton("Tick1")
		self.check.set_active(True)
		self.check.connect("toggled", self.checkToggle, "1")
		self.middlebox.pack_start(self.check, True, True, 0)

		 #checkBox2
                self.check = Gtk.CheckButton("Tick2")
#                self.check.set_active(True)
                self.check.connect("toggled", self.checkToggle, "2")
                self.middlebox.pack_start(self.check, True, True, 0)


		#ListView
#		self.scrolledwindow = Gtk.ScrolledWindow()
		self.listbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 3)
		self.mainbox.pack_start(self.listbox, True, True, 0)
		self.store = Gtk.ListStore(str)
		treeiter = self.store.append(["Name 1"])	
		treeiter = self.store.append(["Name 2"])
		treeiter = self.store.append(["Name 3"])
		self.treeview = Gtk.TreeView(model = self.store)
		renderer_text = Gtk.CellRendererText()
		column_text = Gtk.TreeViewColumn("Friends", renderer_text, text=0)
		self.treeview.append_column(column_text)
#		self.scrolledwindow.add(self.treeview)
#		self.listbox.pack_start(self.scrolledwindow, True, True, 0)
		self.listbox.pack_start(self.treeview, True, True, 0)
		
		#Entry
		self.entry = Gtk.Entry()
		self.topbox.pack_start(self.entry, True, True, 0)	
		
		#Button
		self.button = Gtk.Button(label = "Send")
		self.button.connect("clicked", self.on_button_clicked)
		#function on_button_clicked called when the button is clicked
		self.topbox.pack_start(self.button, True, True, 0)
	
	#prints the text present in Entry on to the Terminal
	def on_button_clicked(self, widget):
		text = self.entry.get_text()
		if text != "":
			print text
		else:
			print "Hello"

	#Prints the name of the active button
	def button_toggled(self, button, name):
		if button.get_active():
			print "Button", name, "is turned on"

	#Prints the state of the active button
	def checkToggle(self, widget, name):
		value = widget.get_active()
		if value == True:
			print "CheckBox", name,  "has the State -  On"
		else:
			print "CheckBox", name,  "has the State -  Off"
	
#Opening/Home Window
class MyFrame(Gtk.Window):
	
	def __init__(self):
		self.flag = 1
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
		self.button3 = Gtk.Button(label = "Exit")
                self.button3.connect("clicked", self.back_off)
		self.topbox.pack_start(self.button3, True, True, 0)

	def on_button_clicked(self, widget):
		win = MyWindow()
		win.connect("delete-event", Gtk.main_quit)
		#to quit the application when the user clicks the close button
		win.show_all()
		Gtk.main()
	
	def on_button(self, widget):
#		root = Tk()
#		app = tk1.App(root)
#		root.mainloop()
		execfile("hello1.py")
#		top1 = Tkinter.Tk() 
#		hello1.top.mainloop()
#		sys.exit()
	
	def back_off(self, widget):
		sys.exit()
				
			

#tk is a file, containing GUI code based on Tkinter, present in the same location
win = MyFrame()
#calls MyFrame so as to present the user with the optionwin.connect("delete-event", Gtk.main_quit)
#to quit the application when the user clicks the close button
win.show_all()
if __name__ == '__main__':
	Gtk.main()


