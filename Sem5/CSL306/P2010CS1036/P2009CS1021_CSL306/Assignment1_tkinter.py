#!/usr/bin/python 
#Python program for implementing two GUIs - Tkinter and wxpython (P2009Cs1034)
#Tkinter toolkit implements five widgets: Checkbox, Radiobutton, Listbox, Button and Entryfield

#Importing wxpython module
import wxmodule
from Tkinter import *

s = "Anonymous"			#Global string
class Widget:			#Widget class
	def print_this(self):				#Function which will be called when the button is pressed
		global s
		if(self.entry.get()!=""):
			s = self.entry.get()		#Getting the entry from the entry field
		items = self.listbox.curselection()
		if(len(items)!=0):			#Getting the number of items selected (It could be 0 or 1)
			data = self.listbox.get(items)
		else:
			data = "Tkinter"
		print "Hello "+s
		print "You are using "+data+" GUI toolkit. Great! I am using Tkinter"
		radio_output = self.radio_v.get()	#By default it assumes that the person is not enjoying working on its toolkit
		if(radio_output=="Yes"):
			print "Good to know that you enjoy working on your toolkit"
		else:
			print "It's bad that you don't enjoy working on your toolkit"
		checkbox_output = self.check_v.get()
		if(checkbox_output=="No"):
			print "Ok then! Happy programming."
		else:
			print "Good! You want to learn Tkinter. Contact me any time for any help."

	def entry_widget(self,entryf):			#Creating a single line entry field widget
		#Create a label in entry frame
	        self.entryLabel = Label(entryf)
                self.entryLabel["text"] = "Enter your name:"
                self.entryLabel.pack(side=LEFT)
		    
   		self.entry = Entry(entryf,text="Enter your choice")	
		self.entry.pack(side= TOP,padx=10,pady=12)

	def list_widget(self,listf):			#Creating a list of values using Listbox widget
		#Create a label in list frame
		self.listLabel = Label(listf)
                self.listLabel["text"] = "Choose your GUI:"
                self.listLabel.pack(side=LEFT)

		self.listbox = Listbox(listf)
		self.listbox.pack(side=TOP,padx=10,pady=12)
		for item in ["Tkinter", "PyGUI", "PyQT", "PyGtk", "wxPython", "pyjs", "pygame", "Microsoft Windows", "easyGUI", "fxpy","pygobject"]:
			self.listbox.insert(END, item)
		
	def radio_widget(self,radiof):			#Creating a group of radio-buttons pointing to the same variable
		#Create a label in radio frame
		self.radioLabel = Label(radiof)
                self.radioLabel["text"] = "Do you enjoy working on your GUI?"
                self.radioLabel.pack(side=LEFT)

		self.radio_v = StringVar()
		Radiobutton(radiof, text="Yes", variable=self.radio_v, value="Yes").pack(anchor=W)
		Radiobutton(radiof, text="No", variable=self.radio_v, value="No").pack(anchor=W)

	def checkbox_widget(self,checkf):		#Creating a checkbox
		
		self.check_v = StringVar()
    		c = Checkbutton(checkf, text="Want ot try my Tkinter GUI toolkit?", variable=self.check_v,onvalue="Yes",offvalue="No")
		c.pack()
	
	def __init__(self,parent):			#Initializing function for creating all widgets within a parent frame				
		entryf = Frame(parent)			#Entryfield widget
		entryf.pack(padx=15,pady=15)
		self.entry_widget(entryf)
		
		listf = Frame(parent)			#Listbox widget
		listf.pack(padx=15,pady=15)
		self.list_widget(listf)		

		radiof = Frame(parent)			#Radiobutton widget
		radiof.pack(padx=15,pady=15)
		self.radio_widget(radiof)

		checkf = Frame(parent)			#Checkbox widget
		checkf.pack(padx=15,pady=15)
		self.checkbox_widget(checkf)
	
		self.button = Button(parent, text="Go",command=self.print_this)	#Creating a "Go" button which will call "print_this" function when pressed
		self.button.pack(side=BOTTOM,padx=10,pady=10)

#Taking input from user regarding which GUI (Tkinter or wxPython) need to be executed
var = raw_input("Enter 1 for Tkinter GUI and 2 for WxPython GUI:\n")
var = int(var)

#Calling Tkinter GUI
if var == 1:
	root = Tk()
	root.title('Tkwidgets application')
	app = Widget(root)
	root.mainloop()
#Calling wxPython GUI
if var == 2:
	wxmodule.app.MainLoop()
