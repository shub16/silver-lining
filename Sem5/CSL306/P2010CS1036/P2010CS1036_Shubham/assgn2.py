import gtk
import sys
from gtk import *
from PyQt4 import QtGui, QtCore
class PyApp(gtk.Window):
	def enter_callback(self, widget, entry):
		text=entry.get_text()
		a="HI "+text+" !"
		self.label.set_text(a)
	def on_click(self,widget,entry):	
		a="HI "+entry.get_text()+" !"
		self.label.set_text(a)
	def __init__(self):
		super(PyApp, self).__init__()
		self.set_title("Entry")
		self.set_size_request(250,200)
		self.set_position(gtk.WIN_POS_CENTER)
		fixed=gtk.Fixed()
		entry=gtk.Entry()
		entry.connect("activate", self.enter_callback,entry)
		btn=gtk.Button("ENTER")
		btn.set_size_request(60,40)
		btn.connect("clicked", self.on_click,entry)
		self.label = gtk.Label("Type a Name!")
		fixed.put(self.label, 60, 40)
		fixed.put(entry,60,100)
		fixed.put(btn,100,150)
		self.connect("destroy",gtk.main_quit)
		self.add(fixed)
		self.show_all()
	def main(self):
		gtk.main()
class MyFrame(gtk.Window):
	def on_button_clicked(self, widget):
		win=PyApp()
		win.main()
		return True
	def on_button(self, widget):
		import WX_canvas as w
		win=w.WX_Canvas(1, 'wxPython1' ,220,400)
		textArea = win.addTextArea("This is a demo text",0,0,200,200)
		win.addButton("MyButton",0,210,200,20)
		win.show()
		return True
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_size_request(250,200)
		self.set_position(gtk.WIN_POS_MOUSE)
		fixed=gtk.Fixed()
		btn=gtk.Button("PyGTK")
		btn.set_size_request(70,40)
		i=btn.connect("clicked", self.on_button_clicked)
		btn2=gtk.Button("WXPython")
		btn2.set_size_request(70,40)
		btn2.connect("clicked", self.on_button)
		btn3=gtk.Button("Quit")
		btn3.set_size_request(70,40)
		btn3.connect("clicked",gtk.main_quit)
		self.label = gtk.Label("Choose a button!")
		fixed.put(self.label, 60, 40)
		fixed.put(btn,60,90)
		fixed.put(btn2,140,90)
		fixed.put(btn3,100,150)
		self.add(fixed)
win = MyFrame()
win.show_all()
win.connect("destroy",gtk.main_quit)
gtk.main()
