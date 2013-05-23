import gtk
class App(gtk.Window):
	def __init__(self):
		super(App, self).__init__()
		self.set_title("Text-Box")
		self.set_size_request(350, 200)
		self.set_position(gtk.WIN_POS_CENTER)
		fixed = gtk.Fixed()
		btn=gtk.Button("OK")
		btn.set_size_request(80,40)
		entry = gtk.Entry()
		entry.set_text("Type anything!")
		fixed.put(entry, 100, 80)
		fixed.put(btn,125,150)
		self.connect("destroy", gtk.main_quit)
		self.add(fixed)
		self.show_all()
App()
gtk.main()
