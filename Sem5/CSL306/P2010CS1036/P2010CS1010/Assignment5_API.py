#!/usr/bin/python

import pygtk
import gtk
import re

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


class CommonAPI():
	#Creating Window
	def __init__ (self, Title, Length, Breadth):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title(Title)
		self.window.set_border_width(10)
		self.window.set_size_request(Length, Breadth)
		self.window.fixed = gtk.Fixed()
		self.radioButton1 = None
			
	#Creating Button
	def CreateButton(self, xPos, yPos, Title,  ):
		button = gtk.Button( label = Title )
		self.window.fixed.put(button, xPos, yPos )
		return button
	
	#Creating Text Box
	def CreateTextBox(self, xPos, yPos, passwd = "FALSE" ):
		textField = gtk.Entry()
		if (passwd == 'FALSE'):
			textField.set_visibility(gtk.TRUE)
		else:
			textField.set_visibility(gtk.FALSE)
			
		self.window.fixed.put(textField, xPos, yPos)
		return textField

	#Create Label
	def CreateLabel(self, xPos, yPos, Title):
		label = gtk.Label(Title)
		self.window.fixed.put(label, xPos, yPos)
	
	#Adding values for comparing
	def GetValues( self,widget, TextBoxes):
		Values = []
		for item in TextBoxes:
			Values.append(item.get_text())
		AreFieldsEmpty(Values)

	#The show function	
	def Show(self):
		self.window.add(self.window.fixed)
		self.window.connect("delete-event", gtk.main_quit)
		self.window.show_all()
		gtk.main()

			
#The Main function
if __name__ == "__main__":

	api = CommonAPI("Unit Testing", 500, 500)
	T1 = api.CreateTextBox(220,20, "FALSE")
	T2 = passwd = api.CreateTextBox(220,50, "TRUE")
	T3 = api.CreateTextBox(220,80, "TRUE")
	T4 = api.CreateTextBox(220,110, "TRUE")
	api.CreateLabel(20, 20, "Enter username: ")
	api.CreateLabel(20, 50, "Enter old password: ")
	api.CreateLabel(20, 80, "Enter new password: ")
	api.CreateLabel(20, 110, "Enter new password(repeat): ")
	button = api.CreateButton(200, 250, "Submit")
	button.connect("clicked", api.GetValues, [T1,T2,T3,T4] )
	api.Show()
