#!/usr/bin/env python
import pygtk
import gtk

class Hello :

	def destroy(self, widget, data=None):
		gtk.main_quit()

	

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Window 1")
		self.window.set_border_width(10)
		self.window.connect("destroy", self.destroy)
		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)
		self.vbox.show()
		self.entry = gtk.Entry()
		self.entry.set_max_length(50)
		self.vbox.pack_start(self.entry, True, True, 0)
		self.entry.show()
		self.hbox=gtk.HBox(False, 0)
		self.vbox.add(self.hbox)
		self.button1=gtk.Button("Button")
		self.hbox.pack_start(self.button1, True, True, 0)
		self.button1.show()
		self.hbox.show()
		self.window.show()

def main():
		gtk.main()

if __name__ == "__main__":
		hello=Hello()
		main()
