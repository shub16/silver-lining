#Implementing tkinter entry and button widget and putting them together in a frame
#Here the entry-field expects name of the user and when the user clicks on the button it will display a hello message
from Tkinter import *

class Widget:
	def __init__(self,parent):

		#Creating and padding a frame
		f = Frame(parent)			
		f.pack(padx=15,pady=15)
		
		#Creating an entry widget and putting it within the frame
		#Afterwards content of entry widgets are fetched and it is cleared for storing new entries
    
   		self.entry = Entry(f,text="Enter your Name")
		self.entry.pack(side= TOP,padx=10,pady=12)
		s = self.entry.get()
		self.entry.delete(0, END)
		
		
		#Creating a button which when clicked call print_this function and pass
		#contents of entry field as parameter
		
		self.button = Button(f, text="Go",command=self.print_this(s))
		self.button.pack(side=BOTTOM,padx=10,pady=10)

	#Callback function which will be called when user clicks the button	
	def print_this(self,s):
		print "Hello"
		print s




