import gtk
import sys
from gtk import *
from PyQt4 import QtGui, QtCore
people = [('Shubham', 'Delhi', '1991'), ('Mohan', 'Rajasthan', '1990'),('Sam', 'Delhi', '1985'), ('natalie', 'new york', '1981'),('rachel', 'london', '1971'), ('john', 'California', '1984' )]
class App(gtk.Window):
	def enter_callback(self, widget, entry):
		text=entry.get_text()
		a="HI "+text+" !"
		self.label.set_text(a)
	def on_click(self,widget,entry):	
		a="HI "+entry.get_text()+" !"
		self.label.set_text(a)
	def __init__(self):
		super(App, self).__init__()
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
# This creates a new window with list of values with a statusbar at the bottom
class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_size_request(350, 250)
        self.set_position(gtk.WIN_POS_CENTER)
        
#        self.connect("destroy", gtk.main_quit)
        self.set_title("ListView")

        vbox = gtk.VBox(False, 8)
        
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)

        store = self.create_model()

        treeView = gtk.TreeView(store)
        treeView.connect("row-activated", self.on_activated)
        treeView.set_rules_hint(True)
        sw.add(treeView)

        self.create_columns(treeView)
        self.statusbar = gtk.Statusbar()
        
        vbox.pack_start(self.statusbar, False, False, 0)

        self.add(vbox)
        self.show_all()


    def create_model(self):
        store = gtk.ListStore(str, str, str)

        for act in people:
            store.append([act[0], act[1], act[2]])

        return store


    def create_columns(self, treeView):
    
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Name", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Place", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Year", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)


    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)
class MyFrame(gtk.Window):
	def callback(self,widget,data = None):
		print "%s was toggled %s" % (data,("OFF","ON")[widget.get_active()])
	def button_toggled(self,widget):
		win=PyApp()
		win.show_all()
		return True
	def on_button_toggled(self, widget):
		win=App()
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
		self.set_size_request(300,250)
		self.set_position(gtk.WIN_POS_MOUSE)
		fixed=gtk.Fixed()
		btn1=gtk.CheckButton("LIST")
		btn1.set_size_request(60,40)
		btn1.connect("toggled", self.button_toggled)
		btn3=gtk.RadioButton(None,"Rb1")
		btn3.set_size_request(60,40)
		btn3.connect("toggled", self.callback,"RadioButton1")
		btn4=gtk.RadioButton(btn3,"Rb2")
		btn4.set_size_request(60,40)
		btn4.connect("toggled", self.callback,"RadioButton2")
		btn=gtk.CheckButton("PyGTK")
		btn.set_size_request(60,40)
		btn.connect("toggled", self.on_button_toggled)
		btn2=gtk.CheckButton("WXPython")
		btn2.set_size_request(80,40)
		btn2.connect("toggled", self.on_button)
		button = gtk.Button("Close")
		button.connect("clicked",gtk.main_quit)
		button.set_size_request(60,40)
		self.label = gtk.Label("Choose a button!")
		fixed.put(self.label, 60, 25)
		fixed.put(btn,60,130)
		fixed.put(btn2,140,130)
		fixed.put(button,120,180)
		fixed.put(btn1,60,75)
		fixed.put(btn3,140,55)
		fixed.put(btn4,140,90)
		self.add(fixed)	
win = MyFrame()
win.show_all()
win.connect("destroy",gtk.main_quit)
gtk.mainloop()