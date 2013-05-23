#!/usr/bin/python 

import pygtk
pygtk.require('2.0')
import gtk
import text_box_qt as qt
import text_box_wx as wx
import gtk_gui as gui

def echo(button, text):
	"""This function prints the message in the text box."""
	
#	getting the string in the buffer
	msg=text.getValue()
	if msg!="":
		print "The message on the text box was \n", msg
	else:
		print "There was no message!\n"

def make_changes(button, cbtn1, cbtn2, cbtn3, window, Title, text_box):
	"""This function executes some modifications in the window based on the selections of the checkbuttons."""
	
#	If the first checkbutton is selected, then show the title of the window as given in the parameter
	if cbtn1.getValue():
		window.set_title(Title)
	else:
		window.set_title("Untitled!")
			
#	If the second checkbutton is selected, then clear the buffer in the text box
	if cbtn2.getValue():
		text_box.setValue("")
			
#	If the third checkbox is selected then display the message in the text box as the title of the window
	if cbtn3.getValue():
		window.set_title(text_box.getValue())
	else:
		window.set_title("Untitled!")

def switch_gui(button, r_buttons):
	"""This function displays another window in the selected GUI toolkit."""

#	Check which radio button is active out of the list of radio buttons
	a=0
	for i in r_buttons.getWidget():
		a=a+1
		if i.get_active():
			break
	
#	If pyGTK is selected, then display the same window again
	if a==1:
		gtk.main()
			
#	If wxPython is selected, then import the wxPython file and execute the main function
	elif a==2:
		import text_box_wx as WX
		WX.main()

#	If pyQT is selected, then import the pyQT module and execute its main function
	else:
		import text_box_qt as QT
		QT.main()
		
def close(button):
	"""This function closes the window and exists from the program."""
	gtk.main_quit()
			
def createWidgets(obj):		
	"""This function would be written by the user to create and return the list of widgets he wants to have in the window."""

#	All the widgets would be added to this list and this list of widgets is then returned
	lstWidgets=[]

	obj.checkVar = ""
	obj.radioVar = ""	
		
	title="Untitled!"		
		
#	Create the text box, button and a separator
	#text="Enter your message here!"
	
	obj.txt=gui.TextBoxWidget("")
	lstWidgets.append(obj.txt.getWidget())

#	obj.txt=gui.TextLineWidget("")
#	lstWidgets.append(obj.txt.getWidget())
		
	btn1_Label="Print the Message"
	obj.btn1=gui.ButtonWidget( "", btn1_Label, echo, obj.txt)
	lstWidgets.append(obj.btn1.getWidget())
		
	obj.sep1=obj.createHSeparator()
	lstWidgets.append(obj.sep1)
	
#	Create a label, checkbuttons, button and a separator
	obj.label1=gui.LabelWidget("", "Want to Modify this window?")
	lstWidgets.append(obj.label1.getWidget())
		
	obj.cbtn1=gui.CheckBoxWidget("", "Show Title",obj.checkVar)
	lstWidgets.append(obj.cbtn1.getWidget())
		
	obj.cbtn2=gui.CheckBoxWidget("", "Clear the Text Box", obj.checkVar)
	lstWidgets.append(obj.cbtn2.getWidget())
		
	obj.cbtn3=gui.CheckBoxWidget("", "Show the message in the Text Box as the title", obj.checkVar)
	lstWidgets.append(obj.cbtn3.getWidget())
		
	btn2_Label="Ok! Modify now."
	obj.btn2=gui.ButtonWidget("", btn2_Label, make_changes, obj.cbtn1, obj.cbtn2, obj.cbtn3, obj.window, title, obj.txt) 
	lstWidgets.append(obj.btn2.getWidget())
		
	obj.sep2=obj.createHSeparator()
	lstWidgets.append(obj.sep2)

#	Create a label, radio buttons, button and a separator
	obj.label2=gui.LabelWidget("", "View a window in another GUI")
	lstWidgets.append(obj.label2.getWidget())
		
	obj.rbtn=gui.RadioButtonWidget("", ["Open the window in PyGTK", "Open the window using wxPython", "Open the window in PyQT"],obj.radioVar)
	for i in obj.rbtn.getWidget():
		lstWidgets.append(i)
		
	btn3_Label="Show in this GUI"
	obj.btn3=gui.ButtonWidget("", btn3_Label, switch_gui, obj.rbtn)		
	lstWidgets.append(obj.btn3.getWidget())
		
	obj.sep3=obj.createHSeparator()
	lstWidgets.append(obj.sep3)

#	Create a label, combo-box and a separator
	obj.label3=gui.LabelWidget("", "Which GUI are you working on?")
	lstWidgets.append(obj.label3.getWidget())
		
	obj.list_box=gui.ListWidget("", ["pyGTK", "pyQT", "Tkinter", "wxPython", "pyjs", "pygame", "easyGUI", "pyGUI", "fxpy", "pyfltk", "pyGObject"])
	lstWidgets.append(obj.list_box.getWidget())
	
	obj.sep4=obj.createHSeparator()
	lstWidgets.append(obj.sep4)

#	Create a "exit" button
	btn4_Label="Exit"
	obj.btn4=gui.ButtonWidget("", btn4_Label, close)
	lstWidgets.append(obj.btn4.getWidget())
		
	return lstWidgets
		
def main():
	"""This is the main function of the program."""

#	the parameters for the window
	title="Hello!"
	width=300
	height=200

#	create an object of the class i.e. create the window
	obj=gui.windowLayout("", title, width, height)

#	create the list of widgets to be present in the window
	wgt=createWidgets(obj)

#	place the widgets
	obj.createLayout(wgt)
	
	gtk.main()
	return 0

if __name__=="__main__":
        main()
