import gtk
class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()
		self.set_title("Entry")
		self.set_size_request(250, 200)
		self.set_position(gtk.WIN_POS_CENTER)
		fixed = gtk.Fixed()
		btn=gtk.Button("ENTER")
		btn.set_size_request(60,40)
		self.label = gtk.Label("Type anything!!!")
		fixed.put(self.label, 60, 40)
		entry = gtk.Entry()
		entry.add_events(gtk.gdk.BUTTON_PRESS_MASK)
		fixed.put(entry, 60, 100)
		fixed.put(btn,100,150)
		entry.connect("button-press-event", self.on_button_press)
		self.connect("destroy", gtk.main_quit)
		self.add(fixed)
		self.show_all()
	def on_button_press(self, widget, event):
		self.label.set_text("HI "+widget.get_text()+" !")
PyApp()
gtk.main()
