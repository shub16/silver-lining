import gtk

class gtkwork():
	
	def enter_callback(self,widget,entry):
		entry_text=entry.get_text()
		print "Entered text is: %s\n" % entry_text
		
	def call_back(self, widget,data=None):
		print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
		
	def prntxt(self, widget,data=None):
		print"%s is selected" % (data [widget.get_text()])
		
		
	def  widgts(self,widget,entry):
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("pyGTK additional WIDGETS")
		window.set_size_request(200,200)
		window.connect("delete_event",gtk.main_quit)
		
		vbox=gtk.VBox()
		window.add(vbox)
		vbox.show()
		
		chkbutton=gtk.CheckButton("click to activate")
		chkbutton.connect("toggled",self.call_back,"click to activate")
		
		
		rdiobutton1=gtk.RadioButton(None,"Switch me1")
		rdiobutton1.connect("toggled",self.call_back,"Switch me1")
		rdiobutton2=gtk.RadioButton(rdiobutton1,"Switch me2")
		rdiobutton2.connect("toggled",self.call_back,"Switch me2")
		
		combobox=gtk.Combo()
		slist=["pyGTK","pyQT","Tkinter","pyGame"]
		combobox.set_popdown_strings(slist)
		combobox.set_use_arrows(True)
		combobox.entry.connect("activate", self.prntxt)
		
		vbox.pack_start(chkbutton)
		vbox.pack_start(rdiobutton1)
		vbox.pack_start(rdiobutton2)
		vbox.pack_start(combobox)
		chkbutton.show()
		rdiobutton1.show()
		rdiobutton2.show()
		combobox.show()
		
		window.show()
	
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
		
		button1=gtk.Button("Click to close")
		button1.connect("clicked", gtk.main_quit, window)
		
		button2=gtk.Button("Click for additional widgets")
		button2.connect("clicked", self.widgts,None)

		vbox.pack_start(entry)
		vbox.pack_start(button1)
		vbox.pack_start(button2)
		
		entry.show()
		button1.show()
		button2.show()
			
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
