import sys

def fasd(event):
	if(chek.get_state()):
		frame.change_color('#F5BCA9')
	else:
		frame.reset_color()

def change(event):
		frame.change_title(t1.get_text())
	
if __name__ == '__main__':
	x=raw_input("Enter 1 for PyGTK, 2 for PyQT, 3 for WxPython, 4 for Tkinter : ")
	if x=='1':
		from P2010CS1038_PyGTK import *
	elif x=='2':
		from P2010CS1034_PyQt import *
	elif x=='3':
		from P2010CS1067_WxPython import *
	elif x=='4':
		from P2010CS1007_Tkinter import *	
	else:
		print "Please Enter a valid number."
		sys.exit()

	app =App()
	frame= Windows("What\'s up buddy!!!",250,250,400,400)
	frame.move_to_centre()
	a=Alignment(frame)
	
	st0=Statictext(frame,"Enter title to be changed")
	st1=Statictext(frame,"Which programming language you prefer?")
	st2=Statictext(frame,"What is your branch?")
	s1=Statictext(frame,"")
	
	t1=SingleTextBox(frame,1)
	a.add(t1,1,0,2)
	
	a.add(st0,0,0,2)
	b1=button(frame,"Submit")
	b1.bind(change)
	a.add(b1,1,2,2)
	
	a.add(st2,2,0,1)
	rb=RadioButtonList(frame,['Computer Science','Electrical','Mechanical','Civil'],0,2,s1,a,3)
	a.add(s1,7,0,1)
	
	combo=ComboBox(frame,'Select your choice',["C","C++","Java","Python"])
	chek=CheckBox(frame,'Change Background Color')
	
	chek.bind(fasd)
								
	value=combo.get_value()
	state=chek.get_state()
	a.add(st1,8,0,1)
	a.add(combo,9,0,1)
	a.add(chek,10,0,1)
	
	frame.show_window(a)
	
	app.loop()
	
