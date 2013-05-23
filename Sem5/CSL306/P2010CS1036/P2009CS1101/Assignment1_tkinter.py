#!/usr/bin/python 
#Implementing tkinter entry and button widgets
#Here the entry-field expects name of the user and when the user clicks on the button it will display a hello message

from Tkinter import *

s = ""			#Global empty string
class Widget:		#Widget class

	#Callback function which will be called when user clicks the button	
	def print_this(self):
		global s
		s = self.entry.get()	#Getting the entry from the entry field
		print "Hello "+s

	def __init__(self,parent):	#Constructor taking parent frame as a parameter
		#Creating and padding a frame
		f = Frame(parent)
		f.pack(padx=15,pady=15)

		#Create a Label in Frame f
	        self.entryLabel = Label(f)
                self.entryLabel["text"] = "Enter your name:"
                self.entryLabel.pack(side=LEFT)
		    
		#Creating an entry widget and putting it within the frame
		#Afterwards content of entry widgets are fetched and it is cleared for storing new entries
   		self.entry = Entry(f,text="enter your choice")	#Creating a single line entry field
		self.entry.pack(side= TOP,padx=10,pady=12)		
		
		#Creating a button which when clicked call print_this function and pass
		#contents of entry field as parameter
		self.button = Button(parent, text="Go",command=self.print_this)	#Creating a "Go" button which will call "print_this" function when pressed
		self.button.pack(side=BOTTOM,padx=10,pady=10)

	
#Calling Tkinter GUI
root = Tk()	#Creating a parent container
root.title('Tkwidgets application')
app = Widget(root)	#Creating an object of the class Widget
