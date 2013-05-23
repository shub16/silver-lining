from fltk import *
import sys


def theCancelButtonCallback(ptr):
		sys.exit(0)

class ex1(Fl_Widget):

	window = Fl_Window(400,200,400,100)
	window.label("welcome :)")
	textedit = Fl_Input(130, 20, 100, 25,"enter text here:")
	button = Fl_Button(300,20,80,25)
	button.label("Click here")
	button.callback(theCancelButtonCallback)
	window.end()
	window.show(len(sys.argv), sys.argv)
	Fl.run()


def pyFLTK():
	a=ex1();
	
	




