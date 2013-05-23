from fltk import *
import sys

# my FLTK code 
class ex1(Fl_Widget):

	def theCancelButtonCallback(self,ptr):
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
	var= raw_input("enter 1 for FLTK window, 2 for pyQT window\n")
	var=int(var)
	if (var==1):	
		ex=ex1()
	elif(var==2):
		#importing pyqt code
		import A1
		
	else: print "wrong input\n"
	                                                            

if __name__ == '__main__': main()
	
	




