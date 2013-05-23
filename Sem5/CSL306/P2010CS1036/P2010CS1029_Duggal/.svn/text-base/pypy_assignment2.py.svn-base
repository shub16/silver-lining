import gtk
#import adi


class App(gtk.Window):
    def __init__(self):
	super(App, self).__init__()
	
	#initializing the window dimensions and title
	#self.connect("destroy", gtk.main_quit)
        self.set_size_request(200, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.show()
	self.set_title("welcome :) ")
	
	# defining a textbox which would show "type here" on placing the cursor over it 
	fixed = gtk.Fixed()
	entry = gtk.Entry()
	entry.set_tooltip_text("type here")
	fixed.put(entry, 20, 50)
	
	# defining a button which would show "click here" on placing the cursor over it 
	btn2 = gtk.Button("Quit")
        fixed.put(btn2, 70, 100)
	btn2.set_tooltip_text("click here")
	btn2.connect("clicked",gtk.main_quit)
	
	#self.connect("destroy", gtk.main_quit)
	self.add(fixed)
	self.show_all()

class PyApp(gtk.Window):
	   	
	def hello(self,widget):
		import aditya_gujral_tkinter
	def helloworld(self,window):
		App()
				


	
	def __init__(self):
		super(PyApp, self).__init__()
	
		#initializing the window dimensions and title
		self.connect("destroy", gtk.main_quit)
		self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(6100,6400,6440))
		self.set_size_request(220,200)
		self.set_position(gtk.WIN_POS_CENTER)
		self.show()
		self.set_title("MAIN WINDOW ")
	
		# defining a CONTAINER on which buttons are placed 
		fix = gtk.Fixed()
		
		# defining a button's 
		btn1 = gtk.Button("PyGtk")
		btn1.connect("clicked",self.helloworld) 
		btn3 = gtk.Button("tkinter")
		btn3.connect("clicked",self.hello)	
		btn2 = gtk.Button("Quit")		
				
		# button position
		fix.put(btn1, 40,40)
		fix.put(btn3, 100,40)    
		fix.put(btn2, 80, 90)
		self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(6100,6400,6440))	#background color dark grey

		self.set_tooltip_text("MAIN WINDOW")
		btn1.set_tooltip_text("click here")
		btn3.set_tooltip_text("CliCK here")
		btn2.set_tooltip_text("for exit click here")
		btn2.connect("clicked",gtk.main_quit)
	
		self.connect("destroy", gtk.main_quit)
		self.add(fix)
		self.show_all()

PyApp()
gtk.main()

