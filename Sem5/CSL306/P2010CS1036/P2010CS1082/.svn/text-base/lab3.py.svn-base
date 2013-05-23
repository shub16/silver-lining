from fltk import *
import sys

# my FLTK code 
class ex1(Fl_Widget):

	def theCancelButtonCallback(self,ptr):
		sys.exit(0)

	
	def __init__ (self):

		window = Fl_Window(400,200,500,400)
		window.label("welcome :)")
		
		textedit = Fl_Input(240, 20, 200, 25,"NAME (single line text here) :")
		textedit = Fl_Multiline_Input(240, 60, 200,60,"ADDRESS (multiline text here) :")

		lbutton = Fl_Light_Button(300,200, 100, 25,"light button");
		
		rbutton = Fl_Round_Button(170, 140, 80, 25,"option1");
		rbutton2 = Fl_Round_Button(170, 160, 80, 25,"option2");
		rbutton.type(100)
		rbutton2.type(100)

		cbutton = Fl_Check_Button(300, 140, 80, 25,"check it..!!");
		
		items = (( "&list here",              0, 0, 0, FL_SUBMENU ),
    		( "&list item 1",        0 ),
   	 	( "&list item 2",   0 ),
    		( "&list item 3",   0),
    		( "&list item 4",     0),
    		( None, 0 )
		)

		m = Fl_Menu_Bar(170, 200, 100, 25);
		m.copy(items)
		
		button = Fl_Button(230,240,80,25)
		button.label("submit")
		button.labelcolor(FL_BLUE);
		button.box(FL_PLASTIC_UP_BOX)
		button.color(FL_WHITE);
		button.callback(self.theCancelButtonCallback)

		lbutton.type(FL_TOGGLE_BUTTON);
		rbutton.type(FL_RADIO_BUTTON);
		rbutton2.type(FL_RADIO_BUTTON);

		window.end()
		window.show(len(sys.argv), sys.argv)
		Fl.run()
	
def main():
	var= raw_input("ENTER 1 for FLTK window with added widgets,\n2 for pyQT window (txtbox-button), \n3 for tkinter window(txtbox-button) \n")
	var=int(var)
	if (var==1):	
		ex=ex1()
	elif(var==2):
		#importing pyqt code
		import A1
	elif (var==3):
		#importing tkinter code
		import asg	
	else: print "wrong input\n"
	                                                            

if __name__ == '__main__': main()
	
	




