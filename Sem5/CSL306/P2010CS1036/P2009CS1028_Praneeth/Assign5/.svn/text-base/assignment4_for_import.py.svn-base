#! /usr/bin/python
import Tkinter
from Tkinter import *
import sys

class Widgets(object):

        def __init__(self):
                self.window = Tk();
                
        def setWindow(self,height,width,title):
                self.window.title(title);
		# get screen width and height
	        ws = self.window.winfo_screenwidth();
	        hs = self.window.winfo_screenheight();
	        # calculate position x, y
	        x = (ws/2) - (width/2);  
	        y = (hs/2) - (height/2);
	        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y));
		return;
		

        def endWindow(self):
                self.window.mainloop();
                return;

        def createTextArea(self, x, y, height_in_lines,width_in_chars):
        	TextArea(self,x,y,height_in_lines,width_in_chars)
        
        def createButton(self, x, y, height_in_lines,width_in_chars,name):
                Button(self,x,y,height_in_lines,width_in_chars,name)

	def createLabel(self,x,y,width_in_chars,name):
		Label(self,x,y,width_in_chars,name)

	def createTextLine(self,x,y,width_in_chars, mode):
		TextLine(self,x,y,width_in_chars, mode)        	

        def createCheckBox(self,x,y,height,width,name):
                CheckBox(self,x,y,height,width,name)
        
        def createRadioGroup(self,x_list,y_list,name_list):
                RadioGroup(self,x_list,y_list,name_list)
                
        def createDropDownList(self,x,y,height,width,List,name):
                DropDownList(self,x,y,height,width,List,name)
	
class TextArea(object):
        def __init__(self, parent, x, y, height_in_lines,width_in_chars):
                self.text = Text(parent.window, height = height_in_lines, width = width_in_chars, bg = 'white');
		self.text.place(x = x, y = y);	

class Button(object):
        def __init__(self, parent, x, y, height_in_lines, width_in_chars, name):
                self.button = Tkinter.Button(parent.window, text = name, height = height_in_lines, width = width_in_chars);
		self.button.place(x = x, y = y);

class Label(object):
	def __init__(self, parent, x, y, width_in_chars, name):
		self.label = Tkinter.Label(parent.window, width = width_in_chars, text = name);
		self.label.place(x = x, y = y);

class TextLine(object):
	def __init__(self, parent, x, y, width_in_chars, mode):
		self.textline = Entry(parent.window, width = width_in_chars);
		if mode == "Password" or mode == "password":
			self.textline.config(show = "*");
		self.textline.place(x = x, y = y);
				
class CheckBox(object):
        def __init__(self,parent,x,y,height_in_lines,width_in_chars,name):
                self.CheckVar = IntVar();
		self.checkbutton = Checkbutton(parent.window, text = name, variable = self.CheckVar, \
                     onvalue = 1, offvalue = 0, height=height_in_lines, \
                     width = width_in_chars);
		self.checkbutton.place(x = x, y = y);
                
class RadioGroup(object):
        def __init__(self,parent,x_list,y_list,name_list):
		self.RadioVar = IntVar();
		for i in range(0, len(x_list)):
	                self.radiobutton = Radiobutton(parent.window, text = name_list[i], variable = self.RadioVar, value = i+1);
			self.radiobutton.place(x = x_list[i], y = y_list[i]);


class DropDownList(object):
        def __init__(self,parent,x,y,height_in_lines,width_in_chars,List,name):
		self.v = StringVar();
		self.v.set(name);
		self.optionMenu = OptionMenu(parent.window, self.v, *List );
		self.optionMenu.place(x= x, y = y);


'''----------------------------------------------------------------
	This is for demonstrating the power of the API
	and how to use it in an example case
   ----------------------------------------------------------------'''

if __name__ == '__main__':    

        widget = Widgets()
        widget.setWindow(300, 300, "Tkinter GUI")
        widget.createTextArea(40,100,4,30)
        widget.createCheckBox(10,20,1,0,'check box 1')
        widget.createCheckBox(10,40,1,0,'check box 2')
        widget.createCheckBox(10,60,1,0,'check box 3')
        widget.createRadioGroup((180, 180, 180),(20, 40, 60),('radio button 1','radio button 2','radio button 3'))
        dropDownList = ['Brazil','India','Pakistan','Russia', 'Iran']
        widget.createDropDownList(90,180,1,0,dropDownList,"Country Menu")
	widget.createButton(90,220,1,0,'This is a Buttton!')
        widget.endWindow()

