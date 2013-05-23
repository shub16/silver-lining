import gtk

class gtkwork():
	
	def enter_callback(self,widget,entry):
		entry_text=entry.get_text()
		print "Entered text is: %s\n" % entry_text
		
	
	def __init__(self):
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("pyGTK Env")
		window.set_size_request(300,100)
		window.connect("delete_event",gtk.main_quit)
		
		vbox=gtk.VBox()
		window.add(vbox)
		vbox.show()
		
		entry= gtk.Entry()
		entry.connect("activate",self.enter_callback,entry)
		entry.set_text("Enter the text")
		
		button=gtk.Button("Click to close")
		button.connect("clicked", gtk.main_quit, window)
		
		vbox.pack_start(entry)
		vbox.pack_start(button)
		
		entry.show()
		button.show()
			
		window.show()
		

class anygui():
	
	def forwardgtk(self,widget,data=None):
		gtkwork()
		
		
	def forwardtkinter(self,widget,data=None):
		import tk
	
	
	def __init__(self):
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("AnyGUI")
		window.set_size_request(500,200)
		window.connect("delete_event",gtk.main_quit)
			
		vbox=gtk.VBox()
		window.add(vbox)
		vbox.show()
	
		button1=gtk.Button("pyGTK World")
		button2=gtk.Button("Tkinter World")
	
		button1.connect("clicked",self.forwardgtk,None)
		button2.connect("clicked",self.forwardtkinter,None)
		
		vbox.pack_start(button1)
		vbox.pack_start(button2)
	
		button1.show()
		button2.show()
	
		window.show()
		
	
anygui()

gtk.main()
