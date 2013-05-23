#!/usr/bin/python

from gi.repository import Gtk, GObject, Gdk
import sys
import re
import time

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
	
def CreateImage(Path):
	return Path
		
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

	#Added a Multiline TextEditor in a ScrolledWindow
	def CreateTextArea(self, xPos, yPos):
		scrolledwindow=Gtk.ScrolledWindow()
		scrolledwindow.set_hexpand(True)
		scrolledwindow.set_vexpand(True)
		textview = Gtk.TextView()
		textview.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0.1, 0.1, 0.2) )
		textbuffer=textview.get_buffer()
		textbuffer.set_text("You can add text here!")
		textview.set_editable(True)
		textview.set_wrap_mode(True)
		scrolledwindow.add(textview)
		scrolledwindow.set_size_request(200,200)
		self.grid.attach(scrolledwindow,0,0,100,100)
		self.fixed.put(self.grid, xPos, yPos)
	
	#Added a Toggle Button	
	def CreateToggleButton(self, xPos, yPos, Title):
		toggleButton = Gtk.ToggleButton(label=Title)
		self.fixed.put(toggleButton, xPos, yPos )	
		return toggleButton
	
	#Added a Slider	
	def CreateSlider(self, xPos, yPos):
		hadjustment = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=10, page_size=0)
		hscale = Gtk.HScale(adjustment=hadjustment)
		hscale.set_size_request(250, -1)
		self.fixed.put(hscale, xPos, yPos)
	
	#Adding an image	
	def AddImage(self, xPos, yPos, Path):
		image = Gtk.Image()
		image.set_from_file(Path)
		self.fixed.put(image, xPos, yPos )
	
	#Added Calendar widget
	def CreateCalender(self, xPos, yPos, Title ):
		calendar = Gtk.Calendar()
		self.fixed.put(calendar, xPos, yPos )
		
	def CreateDialogBox(self, Text):
		dialog = dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.NONE, Text)
		dialog.set_default_size(300, 200)
		#response = dialog.run()
		dialog.show()
		
	# Added a Clock
	def CreateClock(self, xPos, yPos ):
		self.label = Gtk.Label()
		self.label.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0.1, 0.1, 0.2) )
		self.fixed.put(self.label, xPos, yPos)
		GObject.timeout_add(200, self.update)
	
	def update(self):
		self.label.set_markup("<span font_family='arial'weight='heavy' size='x-large'><big>" + time.strftime('%H:%M:%S') + "</big></span>")
		return True
		
	# Added a Spin Button
	def CreateSpinButton(self, xPos, yPos):
		spinner = Gtk.SpinButton()
		adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		spinner.set_adjustment(adjustment)
		spinner.set_wrap(True)
		self.fixed.put(spinner, xPos, yPos)
		
	# Added a Progress Bar
	def CreateProgressBar(self, xPos, yPos):
		progressBar = Gtk.ProgressBar()
		progressBar.set_fraction(0.1)
		#progressBar.start()
		self.fixed.put(progressBar, xPos, yPos)
		
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
		
