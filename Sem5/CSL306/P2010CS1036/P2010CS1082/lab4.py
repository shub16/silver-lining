from fltk import *
import sys


class CommonAPI:	
	
	def theCancelButtonCallback(self,ptr):
		sys.exit(0)
	
	#the constructor
	def __init__(self, Title, xPos, yPos,):
		global window
		window = Fl_Window(xPos, yPos)
		window.label(Title)
	
	#to create a button
	def CreateButton(self, xPos, yPos, Title):
		button = Fl_Button(xPos, yPos,80,25)
		button.label(Title)
		#window.end()
		#window.show(len(sys.argv), sys.argv)
		#Fl.run()
		return button

	#to create a text box
	def CreateTextBox(self, xPos, yPos):
		textedit = Fl_Input(xPos, yPos, 180,25,"Text:")
		return textedit
		
	#to create a checkbox
	def CreateCheckBox(self, xPos, yPos, Title):
		cbutton = Fl_Check_Button(xPos, yPos,80, 25,Title)
		return cbutton

	#to create a radiobutton
	def CreateRadioButton(self, xPos, yPos, Title):
		rbutton = Fl_Round_Button(xPos, yPos, 80, 25,Title)
		return rbutton
	#to create a list
	def CreateList(self, xPos, yPos):
		items = (( "&list here",              0, 0, 0, FL_SUBMENU ),
    		( "&list item 1",        0 ),
   	 	( "&list item 2",   0 ),
    		( "&list item 3",   0),
    		( "&list item 4",     0),
    		( None, 0 )
		)

		m = Fl_Menu_Bar(xPos, yPos, 100, 25);
		m.copy(items)
	
	def Show(self):
		global window
		window.end()
		window.show(len(sys.argv), sys.argv)
			


def main():

	#function calls
	app = CommonAPI("hello", 400, 400)
	app.CreateTextBox(50,150)
	app.CreateButton(250, 150, "CLICK")
	app.CreateCheckBox(250, 200, "Check")
	app.CreateRadioButton(250, 230, "Radio")
	app.CreateList(50,200)
	app.Show()
	#window.end()
	#window.show(len(sys.argv), sys.argv)
	Fl.run()

if __name__ == '__main__': main()

