#!/usr/bin/python

import pygtk
import gtk
import re
import clock

Students = [('Bonani Hazarika', '2010CS1010', 'CSL_306'), ('Jaspreet Kaur', '2010CS1018', 'CSL_306'),
    ('Manisha Digra', '2010CS1021', 'CSL_306'), ('Manisha Dudi', '2010CS1022', 'CSL_306'),
    ('Tanvi Srivastava', '2010CS1082', 'CSL_306'), ('Neetu Soni', '2010CS1027', 'CSL_306' )]


def AreFieldsEmpty(Values) :
	for value in Values:
		if not value:
			print "Enter all the fields!!"
			return
		else:
			continue
	PasswdValid(Values[2], Values[3])

def PasswdValid(passwd1, passwd2):

	if not passwd1 or not passwd2:
		print "Fields are Empty...Enter again!!"
	elif len(passwd1) < 6:
	    	print "Password should contain more than 6 characters!!"
	elif passwd1 != passwd2 :
		print "Passwords Do not Match!!"
	elif ((re.search("[A-Za-z]+", passwd1) is None) or (re.search("[0-9]+", passwd1) is None)) or not(str(passwd1).isalnum()):
		print "Passwords should contain both alpha-numeric characters!!"
	else:
		print "Password changed successfully!!"


def GetValues( widget, TextBoxes):
		Values = []
		for item in TextBoxes:
			Values.append(item.get_text())
		AreFieldsEmpty(Values)

def CreateImage(Path):
	return Path


class CommonAPI:
	def __init__ (self, Title, Length, Breadth):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		color = gtk.gdk.color_parse('grey')
           	self.window.modify_bg(gtk.STATE_NORMAL, color)
		self.window.set_title(Title)
		self.window.set_border_width(10)
		self.window.set_size_request(Length, Breadth)
		self.window.fixed = gtk.Fixed()
		#self.window.grid = gtk.Grid()
		self.radioButton1 = None
		#self.Show()

	def CreateClock(self, xPos, yPos):
		clk = clock.PyGtkWidget()
		self.window.fixed.put(clk, xPos, yPos)
	
	def CreateDialogBox(self, xPos, yPos, Title):
		dialog = gtk.MessageDialog(parent=None, flags=0, type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_NONE, message_format=Title)
		dialog.show()
	

	
	def CreateButton(self, xPos, yPos, Title ):
		button = gtk.Button( label = Title )
		self.window.fixed.put(button, xPos, yPos )
		return button
		

	def CreateProgressBar(self, xPos, yPos):
		progressbar = gtk.ProgressBar(adjustment=None)
		progressbar.set_fraction(0.5)
		self.window.fixed.put(progressbar, xPos, yPos )

	def CreateToggleButton(self, xPos, yPos, Title):
		toggle_button = gtk.ToggleButton(label="Toggle Button")
		#toggle_button.connect("clicked", self.CreateDialog)
		self.window.fixed.put(toggle_button, xPos, yPos )

	def AddImage(self, xPos, yPos, Title):
		i = gtk.Image()
		i.set_from_file(Title)
		self.window.fixed.put(i, xPos, yPos )

	def CreateRadioButton(self, xPos, yPos, Title ):
		radioButton = gtk.RadioButton(self.radioButton1, Title)
		self.radioButton1 = radioButton
		self.window.fixed.put(radioButton, xPos, yPos )
	
	def CreateCheckBox(self, xPos, yPos, Title ):
		checkButton = gtk.CheckButton( label = Title )
		self.window.fixed.put(checkButton, xPos, yPos)
	
	def CreateTextBox(self, xPos, yPos, passwd = "FALSE" ):
		textField = gtk.Entry()
		if (passwd == 'FALSE'):
			textField.set_visibility(gtk.TRUE)
		else:
			textField.set_visibility(gtk.FALSE)
			
		#textField.set_visibility(gtk.FALSE)
		self.window.fixed.put(textField, xPos, yPos)
		return textField

	

	def CreateSlider(self, xPos, yPos):
		#adjustment = gtk.Adjustment(0, 0, 100, 5, 10, 0)
		scale = gtk.HScale(adjustment = None)
		scale.set_range(0, 100)
		scale.set_digits(0)
		scale.set_update_policy(gtk.UPDATE_DELAYED)
		
		
		scale.set_size_request(320, -1)
		self.window.fixed.put(scale, xPos, yPos)

		

	def CreateTextArea(self,xPos,yPos):
		textView = gtk.TextView()
		textView.set_size_request(100, 100)
		self.window.fixed.put(textView, xPos, yPos)

	
		
	def CreateList(self, xPos, yPos, List):
		store = self.CreateModel(List)
		self.treeView = gtk.TreeView(store)
		self.CreateColumns(self.treeView)
		self.window.fixed.put(self.treeView, xPos, yPos)

	def CreateColumns(self, treeView):
		rendererText = gtk.CellRendererText()
        	column = gtk.TreeViewColumn("Name", rendererText, text=0)
        	column.set_sort_column_id(0)    
        	self.treeView.append_column(column)

	def CreateLabel(self, xPos, yPos, Title):
		label = gtk.Label(Title)
		self.window.fixed.put(label, xPos, yPos)

	def CreateSpinButton(self, xPos, yPos):
		adj = gtk.Adjustment(1.0, 1.0, 31.0, 1.0, 5.0, 0.0)
   	        spinner = gtk.SpinButton(adj, 0, 0)
   	        spinner.set_wrap(True)
		self.window.fixed.put(spinner, xPos, yPos)
		
		
	def CreateModel(self, Students):
        	store = gtk.ListStore(str, str, str)
        	for act in Students:
        		store.append([act[0], act[1], act[2]])
        	return store

	def GetValues( self,widget, TextBoxes):
		Values = []
		for item in TextBoxes:
			Values.append(item.get_text())
		AreFieldsEmpty(Values)
		


	def Show(self):
		self.window.add(self.window.fixed)
		self.window.connect("delete-event", gtk.main_quit)
		self.window.show_all()
		gtk.main()

			
if __name__ == "__main__":

	api = CommonAPI("Unit Testing", 650, 650)
	T1 = api.CreateTextBox(220,50, "FALSE")
	T2 = passwd = api.CreateTextBox(220,80, "TRUE")
	T3 = api.CreateTextBox(220,110, "TRUE")
	T4 = api.CreateTextBox(220,140, "TRUE")
	toggle = api.CreateToggleButton( 20,170, "Toggle Button")
	api.CreateLabel(20, 50, "Enter username: ")
	api.CreateLabel(20, 80, "Enter old password: ")
	api.CreateLabel(20, 110, "Enter new password: ")
	api.CreateLabel(20, 140, "Enter new password(repeat): ")
	button = api.CreateButton(300, 170, "Submit")
	button.connect("clicked", api.GetValues, [T1,T2,T3,T4] )
	slider = api.CreateSlider(0,500)
	i = CreateImage("1.gif")
	image = api.AddImage(250,200,i)
	area = api.CreateTextArea(0,230)
	spin = api.CreateSpinButton(170,170)
	progress = api.CreateProgressBar(0,480)
	clok = api.CreateClock(0,360)
	dialog = api.CreateDialogBox(0,500, "Dialog Box")
	l = api.CreateList(120, 240, Students)
	api.Show()
