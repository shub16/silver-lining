import gtk
import pygtk

class PyApp(gtk.Window):
    def __init__(self):
	super(PyApp, self).__init__()
	
	#initializing the window dimensions and title
	self.connect("destroy", gtk.main_quit)
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
	
	self.connect("destroy", gtk.main_quit)
	self.add(fixed)
	self.show_all()

PyApp()
gtk.main()

