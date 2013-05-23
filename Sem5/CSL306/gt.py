from gi.repository import Gtk

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
		#Creates a Window
		#Heirarchy -> window ->(topBox->(entry, Button))
		self.topbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
		self.add(self.topbox)
		self.entry = Gtk.Entry()
		self.topbox.pack_start(self.entry, True, True, 0)	
		self.button = Gtk.Button(label = "Send")
		self.button.connect("clicked", self.on_button_clicked)
		#function on_button_clicked called when the button is clicked
		self.topbox.pack_start(self.button, True, True, 0)
	
	def on_button_clicked(self, widget):
		print "Hello"
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
#to quit the application when the user clicks the close button
win.show_all()
Gtk.main()
