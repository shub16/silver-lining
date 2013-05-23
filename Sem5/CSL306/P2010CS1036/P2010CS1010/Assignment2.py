#!/usr/bin/env python
import pygtk
import gtk

def PyQT(widget,data = None ):
	import A1
def PyGTK(widget,data = None ):
	Hello()


class Hello :

	def destroy(self, widget, data=None):
		gtk.main_quit()

	

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Window 1")
		self.window.set_border_width(10)
		#self.window.connect("destroy", self.destroy)
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



class Option:

	def destroy(self, widget, data=None):
		gtk.main_quit()

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Window 2")
		self.window.connect("destroy", self.destroy)
		self.window.set_border_width(10)
		self.box2=gtk.HBox(False, 0)
		self.window.add(self.box2)
		self.button4 = gtk.Button("PyGTK")
		self.button4.connect_object("clicked",PyGTK ,None)
		self.box2.pack_start(self.button4, True, True, 0)
		self.button4.show()
		self.button5 = gtk.Button("PyQT")
		self.button5.connect_object("clicked",PyQT , self.window)
		self.box2.pack_start(self.button5, True, True, 0)
		self.button5.show()
		self.button7 = gtk.Button("Close")
		self.button7.connect_object("clicked", gtk.main_quit, self.window)
		self.box2.pack_start(self.button7, True, True, 0)
		self.button7.show()
		self.box2.show()
		self.window.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	Option()
	main()
