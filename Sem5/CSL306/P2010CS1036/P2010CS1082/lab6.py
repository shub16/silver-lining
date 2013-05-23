
from fltk import *
import sys
import re
import time



def Validate(Values, check = False):

		
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
			
		
		elif ((re.search("[A-Za-z]+", Values[0]) is None) or (re.search("[0-9]+", Values[0]) is None)) or not(str(Values[0]).isalnum()): 
			if (check == False):
				fl_alert("Passwords should contain both alpha-numeric characters")
		
		else:
			if (check == False):
				fl_alert( "Passwords changed sucessfully")
				sys.exit(0)



def CreateImage():
	img = Fl_GIF_Image("./smilingpython.gif")
	return img

class CommonAPI:


	def theCancelButtonCallback(self,ptr):
		sys.exit(0)

	
	
	def GetValues(self, widget, TextBoxes):
		Values = []
		for item in TextBoxes:
			Values.append(item.value())
		Validate(Values)

	
	
	def __init__(self, Title, xPos, yPos,):

		global window
		window = Fl_Window(xPos, yPos)
		window.label(Title)
		window.color(FL_RED)		
		

	def CreateSlider(self,xPos,yPos):
		Fl_Value_Slider(xPos,yPos,30,200)

	def CreateSpinButton(self,xPos,yPos):

		a= Fl_Counter(xPos,yPos,100,20)

	def CreateProgressBar(self,xPos,yPos):
		prog= Fl_Progress(xPos,yPos, 100,20)
		prog.value(50)
		prog.label("%")
		
	def CreateDialogBox(self,text):
		fl_message(text)

	def CreateClock(self,xPos, yPos):
		c1 = Fl_Clock(xPos,yPos,220,220,"clock")
		window.resizable(c1);
		
	
	def CreateButton(self, xPos, yPos, Title):

		button = Fl_Button(xPos, yPos,150,25)
		button.label(Title)
		return button

	def CreateTextBox(self, xPos, yPos, passwd = False):
		if passwd == False:
			textedit = Fl_Input(xPos, yPos, 180,25)
		else:
			textedit = Fl_Secret_Input(xPos,yPos,180,25)
		return textedit
		
	def CreateTextArea(self, xPos, yPos):
		textedit = Fl_Multiline_Input(xPos, yPos,180,60)
		return textedit
	
	def CreateCheckBox(self, xPos, yPos, Title):
		cbutton = Fl_Check_Button(xPos, yPos,100, 25,Title)
		return cbutton

	def CreateRadioButton(self, xPos, yPos, Title):
		rbutton = Fl_Round_Button(xPos, yPos, 100, 25,Title)
		return rbutton

	def CreateList(self, xPos, yPos,List):
		items = (( "&Name List", 0, 0, 0, FL_SUBMENU ),
    		( "&Tanvi",        0 ),
   	 	( "&Manisha",   0 ),
    		( "&Boni",   0),
    		( "&Jk",     0),
    		( None, 0 )
		)
		m = Fl_Menu_Bar(xPos, yPos, 100, 25);
		m.copy(items)
	
	def CreateLabel(self,xPos,yPos,Title):
		box = Fl_Button(xPos,yPos,100,30)
		box.label(Title)
		



	def AddImage(self,xPos,yPos,img):
		box = Fl_Button(470,80,100,100)
		box.image(img)
		

	def CreateToggleButton(self, xPos, yPos,Title):
		tbutton = Fl_Button( xPos, yPos,100,25,Title)
		tbutton.type(FL_TOGGLE_BUTTON)
		return tbutton

	def Show(self):
		global window
		window.end()
		window.show(len(sys.argv), sys.argv)
		Fl.run()
		
		

def main():
	app = CommonAPI("hello", 700,700)

	app.CreateLabel(20,100, "Username")
	d = app.CreateTextBox(150,100)

	button=app.CreateButton(150, 320, "Change Password !!")

	app.CreateLabel(20,150, "Passwrd")
	a=app.CreateTextBox(150,150, True)

	app.CreateLabel(20,200, "New Passwrd")	
	b=app.CreateTextBox(150,200, True)

	app.CreateLabel(20,250, "Re-enter")
	c=app.CreateTextBox(150,250, True)
	app.CreateLabel(20,20,"Text Area")
	f=app.CreateTextArea(150,20)
	List=[]
	e=app.CreateToggleButton(170,350,"Toggle")
	app.CreateClock(450,450)
	app.CreateSlider(100,490)
	app.CreateProgressBar(150,500)
	app.CreateSpinButton(150,450)
	app.CreateList(150,600,List)
	#app.CreateDialogBox("This is a dialog box!!!!!!")
	img = CreateImage()
	app.AddImage(0,0,img)
	button.callback(app.GetValues, [b,c])
	app.Show()



if __name__ == '__main__': main()


