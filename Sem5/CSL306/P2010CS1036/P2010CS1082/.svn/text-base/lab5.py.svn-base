
from fltk import *
import sys
import re



def Validate(Values,check =False):

	#Checking if any field is left empty
	for value in Values:
		if not value:
			if (check == False):
				fl_alert("Enter all the fields!!")
				return
		else:
			continue
	#Checking if the paswords match
	if len(Values[0]) < 6 :
		if (check == False):
				fl_alert("Password is too short. Please use atleast 6 characters")
			
			
	#Checking if the paswords match
	elif Values[0] != Values[1]:
		if (check == False):
			fl_alert("Passwords Do not Match")
			
		
	elif ((re.search("[A-Za-z]+", Values[0]) is None) or (re.search("[0-9]+", Values[1]) is None)) or not(str(Values[1]).isalnum()): 
		if (check == False):
			fl_alert("Passwords should contain both alpha-numeric characters")
		
	else:
		if (check == False):
			fl_alert( "Passwords changed sucessfully")
		#sys.exit(0)

class CommonAPI:


	def theCancelButtonCallback(self,ptr):
		sys.exit(0)

	#to retrieve values from textboxes
	def GetValues(self, widget, TextBoxes):
		Values = []
		for item in TextBoxes:
			Values.append(item.value())
		Validate(Values)

	
	#constructor
	def __init__(self, Title, xPos, yPos,):
		global window
		window = Fl_Window(xPos, yPos)
		window.label(Title)
	
	#to create a button
	def CreateButton(self, xPos, yPos, Title):
		button = Fl_Button(xPos, yPos,150,25)
		button.label(Title)
		return button

	#to create a textbox
	def CreateTextBox(self, xPos, yPos, Title, passwd = False):
		if passwd == False:
			textedit = Fl_Input(xPos, yPos, 180,25,Title)
		else:
			textedit = Fl_Secret_Input(xPos,yPos,180,25,Title)
		return textedit
		
	#to create a checkbox
	def CreateCheckBox(self, xPos, yPos, Title):
		cbutton = Fl_Check_Button(xPos, yPos,100, 25,Title)
		return cbutton

	#to create a radio button
	def CreateRadioButton(self, xPos, yPos, Title):
		rbutton = Fl_Round_Button(xPos, yPos, 100, 25,Title)
		return rbutton

	#to create a list
	def CreateList(self, xPos, yPos):
		items = (( "&list here", 0, 0, 0, FL_SUBMENU ),
    		( "&list item 1",        0 ),
   	 	( "&list item 2",   0 ),
    		( "&list item 3",   0),
    		( "&list item 4",     0),
    		( None, 0 )
		)
		m = Fl_Menu_Bar(xPos, yPos, 100, 25);
		m.copy(items)
	
	#to show the window
	def Show(self):
		global window
		window.end()
		window.show(len(sys.argv), sys.argv)


def main():
	global window

	#constuctin th class & making function calls
	app = CommonAPI("hello", 400, 400)
	d = app.CreateTextBox(150,100, "Username :")


	button=app.CreateButton(150, 320, "Change Password !!")
	a=app.CreateTextBox(150,150,"Current Password:", True)
	b=app.CreateTextBox(150,200,"New Password:", True)
	c=app.CreateTextBox(150,250,"Re-enter Password:", True)
	button.callback(app.GetValues, [b,c]);
	app.Show()
	window.end()
	Fl.run()


if __name__ == '__main__': main()

