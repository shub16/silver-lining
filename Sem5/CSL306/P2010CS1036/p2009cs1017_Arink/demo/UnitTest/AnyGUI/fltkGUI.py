#! usr/bin/python

from fltk import *
import sys

''' WX_Canvas : On it widget can be added '''
class Canvas(Fl_Widget):
	parent = None
	def __init__(self, id, title,width,height):
		self.window = Fl_Window(0,0,width,height,title)
		self.window.position((Fl.w() - self.window.w())/2, (Fl.h() - self.window.h())/2);

	def show(self):
		self.window.end()
		self.window.show(sys.argv)
		Fl.run()
		return

	def add(self,widget):
		widget_type = type(widget)
		if(widget_type==TextArea or isinstance(widget,TextArea)):
			widget.controller = Fl_Multiline_Input(widget.position_X, widget.position_Y, widget.width, widget.height)
			widget.controller.value(widget.title)
		elif(widget_type==Button or isinstance(widget,Button)):
			widget.controller = Fl_Button(widget.position_X, widget.position_Y, widget.width, widget.height, widget.title)
			if(widget.callbackMethod != None ):
				widget.controller.callback(widget.callbackMethod)

		elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
			widget.controller = Fl_Check_Button(widget.position_X, widget.position_Y, widget.width, widget.height, widget.title)
			widget.controller.type(FL_TOGGLE_BUTTON)
			widget.controller.value(widget.value)
		elif(widget_type==RadioGroup or isinstance(widget,RadioGroup)):
			widget.GroupController = Fl_Group(widget.position_X[0], widget.position_Y[0], len(widget.labels)*widget.width, 2*widget.height, "")
			widget.controller = []
			radio_controller = Fl_Round_Button(widget.position_X[0], widget.position_Y[0], widget.width, widget.height, widget.labels[0]);
			radio_controller.type(FL_RADIO_BUTTON);
			widget.controller.append(radio_controller)
			for i in range(1,len(widget.labels)):
				radio_controller = Fl_Round_Button(widget.position_X[i], widget.position_Y[i], widget.width, widget.height, widget.labels[i]);
				radio_controller.type(FL_RADIO_BUTTON);
				widget.GroupController.add(radio_controller)
				widget.controller.append(radio_controller)
			widget.GroupController.end()
			if(widget.selected_pos != None):
				widget.controller[widget.selected_pos].value(True)
		elif(widget_type==ValueList or isinstance(widget,ValueList)):
			widget.controller = Fl_Choice (widget.position_X, widget.position_Y, widget.width, widget.height, widget.title)
			widget.controller.copy(widget.choices)
        	

''' WIDGETS: Button '''
class Button(Fl_Button):
	controller = None
	callbackMethod = None
	def __init__(self,title,X,Y,width,height):
		self.title = title
		self.position_X = X
		self.position_Y = Y
		self.width = width
		self.height = height

	def clickListener(self,method):
		if(self.controller == None):
			self.callbackMethod = method
		else:
			self.controller.callback(method)
		return True

class TextArea(Fl_Multiline_Input):
	controller = None
	callback = None
	def __init__(self,title,X,Y,width,height):
		self.title = title
		self.position_X = X
		self.position_Y = Y
		self.width = width
		self.height = height

	def setText(self,text):
		if(self.controller == None):
			self.text = text
		else:
			self.controller.value(text)
		return True

	def appendText(self,text):
		if(self.controller == None):
			self.text = self.text+text
		else:
			self.text = self.controller.value() + text
			self.controller.value(text)
		return True              

	def clear(self):
		self.controller.Clear()
		return True


class CheckBox(Fl_Check_Button):
	controller = None
	value = False
	def __init__(self,title,X,Y,width,height):
		self.title = title
		self.position_X = X
		self.position_Y = Y
		self.width = width
		self.height = height

	def setValue(self,value):
		if(self.controller == None):
			self.value = value
		else:
			self.controller.value(value)

	def getValue(self):
		if(self.controller == None):
			return self.value
		else:
			return self.controller.value()


class RadioGroup(Fl_Round_Button):
	GroupController = None
	controller = None
	selected_pos = None
	def __init__(self,width,height):
		self.labels = []
		self.position_X = []
		self.position_Y = []
		self.width = width
		self.height = height
		self.GroupController = None

	def addRadioButton(self,label,X,Y):
		self.labels.append(label)
		self.position_X.append(X)
		self.position_Y.append(Y)
		return True

	def getValue(self):
		for i in range(len(self.controller)):
			if(self.controller[i].value()):
				return self.labels[i]
		return "None"

	def setButtonTrue(self,pos):
		if(self.controller == None):
			self.selected_pos = pos
		else:
			button_controller = self.controller[pos]
			button_controller.value(True)

class ValueList(Fl_Choice):
	controller = None
	def __init__(self,choices,X,Y,width,height,value=""):
		self.title = ""
		self.position_X = X
		self.position_Y = Y
		self.width = width
		self.height = height
		self.value = value

		temp = [(value,)]
		for i in range(len(choices)):
			temp.append((choices[i],))
		self.choices = tuple(temp)

	def getValue(self):
		if(self.controller == None):
			return self.value
		else:
			IntValue = self.controller.value()
			if(IntValue < 0):
				return None
			return self.choices[IntValue][0]

''' ----------------------------------------------------------------
        This is just demo! 
        IT IS NOT THE PART OF LIB '''

if __name__ == '__main__':

	#Functions bind to button events
	def SubmitButtonClick(event):
		report = " Your city is "+valuelist.getValue()+"\n"
		if(checkbox1.getValue()):
		    report = report + " you have read the code\n"
		else:
		    report = report + " you have not read the code\n"

		if(checkbox2.getValue()):
		    report = report + " you have read the documentation\n"
		else:
		    report = report + " you have not read the documentation\n"

		report = report + " you are "+rb1.getValue()+"\n"
		report = report + " you need "+rb2.getValue()+"\n"

		textarea.appendText("_______________________\n"+report+"\n\n")
		return True 

	def AboutButtonClick(event):
		textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
		return True



	#Constructor canvas
	canvas = Canvas(1, 'wxGUI -v1.0 | ArinkVerma' ,510,300)

	#Dropdown valuelist
	cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
	valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
	canvas.add(valuelist)

	#checkboxs
	checkbox1 = CheckBox("I have read the code.",10,45,215,15)
	checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
	checkbox1.setValue(True)
	canvas.add(checkbox1)
	canvas.add(checkbox2)

	#radioGroup1
	rb1 = RadioGroup(60,50)
	rb1.addRadioButton("Nice",10,110)
	rb1.addRadioButton("Good",70,110)
	rb1.addRadioButton("Great",140,110)
	rb1.setButtonTrue(2)
	canvas.add(rb1)

	#radioGroup2
	rb2 = RadioGroup(100,50)
	rb2.addRadioButton("Option #1",10,160)
	rb2.addRadioButton("Option #2",110,160)
	rb2.setButtonTrue(0)
	canvas.add(rb2)

	#TextArea
	textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
	canvas.add(textarea)

	#Creating Buttons
	submitBtn = Button("Submit",130,230,120,30)
	aboutBtn = Button("About",260,230,120,30)

	#Callback methods on buttons click
	submitBtn.clickListener(SubmitButtonClick)
	aboutBtn.clickListener(AboutButtonClick)

	#Adding buttons to canvas
	canvas.add(aboutBtn)
	canvas.add(submitBtn)

	canvas.show()
