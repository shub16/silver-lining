from fltk import *
import sys



class ex1(Fl_Widget):

	def theCancelButtonCallback(self, ptr):
		sys.exit(0)
	
	def __init__ (self):
		window = Fl_Window(400,200,400,100)
		window.label("welcome :)")
		textedit = Fl_Input(130, 20, 100, 25,"enter text here:")
		button = Fl_Button(300,20,80,25)
		button.label("Click here")
		button.callback(self.theCancelButtonCallback)
		window.end()
		window.show(len(sys.argv), sys.argv)
		Fl.run()
	
def main():
	ex=ex1()
	                                                            

if __name__ == '__main__': main()
	
	




