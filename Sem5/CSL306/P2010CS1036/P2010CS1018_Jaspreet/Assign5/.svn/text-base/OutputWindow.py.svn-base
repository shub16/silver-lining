#!/usr/bin/python

from gi.repository import Gtk, GObject, Gdk
import sys
import re

def AreFieldsEmpty(Values):
	#Checking if all fields are filled
	for value in Values:
		if not value:
			print "Enter all the fields"
			return
		else:
			continue
	PasswdValid(Values[2], Values[3])

def PasswdValid(passwd1, passwd2):
	if not passwd1 or not passwd2:
		print "Fields are Empty"					
	elif len(passwd1) < 6 :
		print "Password is too short. Please use atleast 6 characters"		
	#Checking if the paswords match
	elif passwd1 != passwd2:
		print "Passwords Do not Match, Re-Enter Passwords"
	
	elif ((re.search("[A-Za-z]+", passwd1) is None) or (re.search("[0-9]+", passwd1) is None)) or not(str(passwd1).isalnum()): 
		print "Passwords should contain both alpha-numeric characters"
	
	else:
		print "Passwords changed sucessfully"
		Gtk.main_quit()

def GetValues(widget, TextBoxes):
	Values = []
	for item in TextBoxes:
		Values.append(item.get_text())
	AreFieldsEmpty(Values)
		
class CommonAPI(Gtk.Window):
	
	def __init__ (self, Title, Length, Breadth):
		Gtk.Window.__init__(self, title = Title )
		self.set_size_request(Length, Breadth)
		self.fixed = Gtk.Fixed()
		self.grid = Gtk.Grid()
		self.radioButton1 = None
			
	def CreateButton(self, xPos, yPos, Title):
		button = Gtk.Button( label = Title )
		self.fixed.put(button, xPos, yPos )
		return button
	
	def CreateRadioButton(self, xPos, yPos, Title ):
		radioButton = Gtk.RadioButton.new_with_label_from_widget(self.radioButton1, Title)
		self.radioButton1 = radioButton
		self.fixed.put(radioButton, xPos, yPos )
	
	def CreateCheckBox(self, xPos, yPos, Title ):
		checkButton = Gtk.CheckButton( label = Title )
		self.fixed.put(checkButton, xPos, yPos)
	
	def CreateTextBox(self, xPos, yPos, passwd=False):
		textField = Gtk.Entry()
		if passwd == True:
			textField.set_visibility(0)
		self.fixed.put(textField, xPos, yPos)
		return textField
	
	def CreateLabel(self, xPos, yPos, Title):
		label = Gtk.Label(Title)
		self.fixed.put(label, xPos, yPos)

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
		


	
