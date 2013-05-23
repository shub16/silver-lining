#!/usr/bin/python

from gi.repository import Gtk, GObject, Gdk
import sys

class CommonAPI(Gtk.Window):
	
	def __init__ (self, Title, Length, Breadth):
		Gtk.Window.__init__(self, title = Title )
		self.set_size_request(Length, Breadth)
		self.fixed = Gtk.Fixed()
		self.grid = Gtk.Grid()
		self.radioButton1 = None
		#self.Show()
			
	def CreateButton(self, xPos, yPos, Title ):
		button = Gtk.Button( label = Title )
		self.fixed.put(button, xPos, yPos )
	
	def CreateRadioButton(self, xPos, yPos, Title ):
		radioButton = Gtk.RadioButton.new_with_label_from_widget(self.radioButton1, Title)
		self.radioButton1 = radioButton
		self.fixed.put(radioButton, xPos, yPos )
	
	def CreateCheckBox(self, xPos, yPos, Title ):
		checkButton = Gtk.CheckButton( label = Title )
		self.fixed.put(checkButton, xPos, yPos)
	
	def CreateTextBox(self, xPos, yPos):
		textField = Gtk.Entry()
		self.fixed.put(textField, xPos, yPos)

	def CreateList(self, xPos, yPos, List):
		#Creating a model from treeview
		store = Gtk.ListStore(str)
		for i in range(len(List)):
			listiter = store.append([List[i]])
		tree = Gtk.TreeView(store)
		
		vbox = Gtk.VBox(spacing = 1)
		label = Gtk.Label("Your list is here");
		vbox.pack_start(label, False, False, 0)
		vbox.pack_start(tree, False, False, 0)
		   				
		#column for name
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn(" ", renderer, text = 0)
		tree.append_column(column)
		self.fixed.put(vbox, xPos, yPos)	
		
	def Show(self):
		self.add(self.fixed)
		self.connect("delete-event", Gtk.main_quit)
		self.show_all()
		Gtk.main()
		
		
	
