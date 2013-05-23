import gtk
import sys
from gtk import *
from PyQt4 import QtGui, QtCore
class MyFrame(gtk.Window):
	def on_button_clicked(self, widget):
		import text
		text.gtk.main()
	def on_button(self, widget):
		import qt
		qt.main()
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_size_request(250,200)
		self.set_position(gtk.WIN_POS_MOUSE)
		fixed=gtk.Fixed()
		btn=gtk.Button("PyGTK")
		btn.set_size_request(60,40)
		btn.connect("clicked", self.on_button_clicked)
		btn2=gtk.Button("PyQT")
		btn2.set_size_request(60,40)
		btn2.connect("clicked", self.on_button)
		self.label = gtk.Label("Choose a button!")
		fixed.put(self.label, 60, 40)
		fixed.put(btn,60,125)
		fixed.put(btn2,140,125)
		self.add(fixed)	
win = MyFrame()
#calls MyFrame so as to present the user with the option
#to quit the application when the user clicks the close button
win.show_all()
win.connect("destroy",gtk.main_quit)
gtk.main()
