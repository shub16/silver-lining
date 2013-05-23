#!/usr/bin/python

from gi.repository import Gtk, GObject
import sys

class FirstWindow(Gtk.Window):
	""" This class builds a window in pyGObject. 
	The constructor takes 0 arguments and is of the type: 
		MyWindow = FirstWindow()
	"""
	
	(NAME,
	BRANCH,
	ENTRY_NO) = range(3)
	
	def __init__(self):
		Gtk.Window.__init__(self, title="My First Window-GObject")
		self.set_size_request(500, 500)
		fixed = Gtk.Fixed()
		
		text_field = Gtk.Entry()
		
		button = Gtk.Button(label="Enter!")
		button.connect("clicked", self.on_button_clicked)
		
		checkbutton = Gtk.CheckButton( label ="Check Me" )
		checkbutton.connect("toggled", self.SetLabel, 0 )
		
		togglebutton = Gtk.ToggleButton( label = "Toggle Me" )
		togglebutton.connect("toggled", self.SetLabel, 1 )
		
		#Adding Two Radio button in here
		radiobutton1 = Gtk.RadioButton.new_with_label_from_widget(None, "Deselect Me")
		radiobutton2 = Gtk.RadioButton.new_with_label_from_widget(radiobutton1, "Select Me")
		radiobutton3 = Gtk.RadioButton.new_with_label_from_widget(radiobutton1, "Select Me")
		
		radiobutton1.connect("toggled", self.SetLabel, 2 )
		radiobutton2.connect("toggled", self.SetLabel, 2 )
		radiobutton3.connect("toggled", self.SetLabel, 2 )
		
		#Creating a model for treeview
		store = Gtk.ListStore(str, str, int)
		listiter = store.append(["Jaspreet Kaur", "CSE", 1018])
		listiter = store.append(["Bonani Hazarika", "CSE", 1010])
		listiter = store.append(["Tanvi Srivastava", "CSE", 1082])
		listiter = store.append(["Manisha Digra", "CSE", 1021])
		listiter = store.append(["Manisha Dudi", "CSE", 1022])
		listiter = store.append(["Neetu Soni", "CSE", 1027])
		
		# To view the list
		tree = Gtk.TreeView(store)
		
		#A box to hold the List to be inserted in Fixed
		vbox = Gtk.VBox( spacing = 3 )
		label = Gtk.Label('Demonstration of a List')
		vbox.pack_start(label, False, False, 0)
		vbox.pack_start(tree, False, False, 0)
   				
		#column for name
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Name", renderer, text = self.NAME)
		tree.append_column(column)
		
		#column for Branch
		column = Gtk.TreeViewColumn("Branch", renderer, text = self.BRANCH)
		tree.append_column(column)
		
		#column for EntryNo
		column = Gtk.TreeViewColumn("EntryNo", renderer, text=self.ENTRY_NO)
		tree.append_column(column)
		
		fixed.put(text_field, 100, 50)
		fixed.put(button, 300, 50)
		fixed.put(checkbutton, 100, 100)	#Adding Check Button
		fixed.put(togglebutton, 300, 100)	#Adding Toggle Button
		fixed.put(radiobutton1, 100, 150)	#Adding Radio Buttons
		fixed.put(radiobutton2, 100, 170)
		fixed.put(radiobutton3, 100, 190)
		fixed.put(vbox, 150, 250 )
		
		
				
		self.add(fixed)
		self.connect("delete-event", Gtk.main_quit)
		self.show_all()
		Gtk.main()    
  
	def on_button_clicked(self, widget):		
		print "You Entered the text"
		
	def SetLabel(self, widget, var):
		if( widget.get_active() ):
			if( var == 0 ):
				widget.set_label("Uncheck Me")
			elif( var == 1 ):
				widget.set_label("Untoggle Me")
			elif( var == 2 ):
				widget.set_label("Deselect Me")
		else:
			if( var == 0 ):
				widget.set_label("Check Me")
			elif( var == 1 ):
				widget.set_label("Toggle Me")
			elif( var == 2 ):
				widget.set_label("Select Me")
			
    
