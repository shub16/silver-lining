#!/usr/bin/env python



import pygtk
pygtk.require('2.0')
import gtk
choice=int(raw_input("Enter the choice:\n1 for running \"PyGTK\" code or 2 for running \"wxpython\" code:"))

if choice==1:
	class Textbox:
    		def sample(self, widget, 	textbox):						#definfing function Sample (to be executed when the button is pressed)
        		self.text = textbox.get_text()
        		print "Entry contents: %s\n" % text
    
   	 	def callback(self, widget, data=None):
   	   		print "The button - %s was pressed" % data
		def check(self,widget,data=None):
			print"%s was toggled %s "%(data,("OFF", "ON")[widget.get_active()])
		
   	 
   	 	def __init__(self):
   	   
   	     		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)				#Creating  a Window
   	     		self.window.set_size_request(400, 300)
   	     		self.window.set_title("Text-Box Window")					#Setting the title of the Window
   	     		self.window.connect("delete_event", lambda w,e: gtk.main_quit())
	
   	     		self.hbox = gtk.VBox(True, 20)						#Adding a Horizontal Box
   	     		self.window.add(self.hbox)
   	     		self.hbox.show()
			self.hbox1 = gtk.HBox(True, 20)						#Adding a Horizontal Box
   	     		self.window.add(self.hbox1)
   	     		self.hbox1.show()
		
			
   	     		self.textbox = gtk.Entry()							#Creating the textbox 
   	     		self.textbox.set_max_length(20)						#Setting the maximum length of input string to be entered in the textbox
   	     		self.textbox.connect("activate", self.sample, self.textbox)
   	     		self.textbox.set_text("type the text here")					#Default String to be displayed
   	     		self.textbox.select_region(0, len(self.textbox.get_text()))
   	     		self.hbox.pack_start(self.textbox, True, True, 0)
   	     		self.textbox.show()
			
			self.button1=gtk.CheckButton("checkbutton")
			self.button1.connect("toggled", self.check,"checkbutton")
			self.hbox.pack_start(self.button1,True, True, 2)
			self.button1.show()
			
			self.button2=gtk.RadioButton(None,"radio button1")
			self.button2.connect("toggled",self.check,"radiobutton1")
			self.hbox.pack_start(self.button2,True, True, 0)
			self.button2.show()

			self.button3=gtk.RadioButton(self.button2,"radio button2")
			self.button3.connect("toggled",self.check,"radiobutton2")
			self.hbox.pack_start(self.button3,True, True, 0)
			self.button3.show()

			self.combo=gtk.Combo()
			sdf="enter the contents of the list"
			self.combo.entry.set_text(sdf)
			slist=["string1", "String 2", "String 3"]
			self.combo.set_popdown_strings(slist)
			self.hbox.pack_start(self.combo,True,True,0)
			self.combo.show()
			
        
			self.button = gtk.Button(stock=gtk.STOCK_OK)					#Creating the Button 
					
			self.button.connect("clicked", self.callback, "OK")				#Setting the Stock to "OK" and specifying to call the function Callback when the button is pressed
			
			self.hbox.pack_start(self.button, True, True, 0)
        		self.button.set_flags(gtk.CAN_DEFAULT)
        		self.button.grab_default()
			self.button.show()
        
        		self.window.show()								#Displaying the Window


        
		def main(self):
    			gtk.main()
 		

	if __name__ == "__main__":
    		tex=Textbox()
    		tex.main()
elif choice==2:
	import Module_wx

else:
	print("wrong choice")		                                  
        
    
        
                                   
        



