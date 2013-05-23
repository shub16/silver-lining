#!/usr/bin/env python
import pygtk
import gtk

def PyQT(widget,data = None ):
	import A1
def PyGTK(widget,data = None ):
	Hello()
def Tkinter(widget, data = None):
	import dudi

Students = [('Bonani Hazarika', '2010CS1010', 'CSL_306'), ('Jaspreet Kaur', '2010CS1018', 'CSL_306'),
    ('Manisha Digra', '2010CS1021', 'CSL_306'), ('Manisha Dudi', '2010CS1022', 'CSL_306'),
    ('Tanvi Srivastava', '2010CS1082', 'CSL_306'), ('Neetu Soni', '2010CS1027', 'CSL_306' )]


class Hello :

	def destroy(self, widget, data=None):
		gtk.main_quit()

	def create_model(self):
        	store = gtk.ListStore(str, str, str)
        	for act in Students:
        		store.append([act[0], act[1], act[2]])
        	return store

	def on_activated(self, widget, row, col):
		model = widget.get_model()
		text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
		self.statusbar.push(0, text)
	


	def create_columns(self, treeView):
		rendererText = gtk.CellRendererText()
        	column = gtk.TreeViewColumn("Name", rendererText, text=0)
        	column.set_sort_column_id(0)    
        	self.treeView.append_column(column)

		rendererText = gtk.CellRendererText()
        	column = gtk.TreeViewColumn("Entry Number", rendererText, text=1)
        	column.set_sort_column_id(1)
        	self.treeView.append_column(column)
	
		rendererText = gtk.CellRendererText()
        	column = gtk.TreeViewColumn("Course Taken", rendererText, text=2)
        	column.set_sort_column_id(2)
        	self.treeView.append_column(column)




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
		self.button2 = gtk.RadioButton(None, "Radio Button")
		self.hbox.pack_start(self.button2, True, True, 0)
		self.button2.show()
		self.button3 = gtk.CheckButton("Check Button")
		self.hbox.pack_start(self.button3, True, True, 0)
		self.button3.show()

		self.sw = gtk.ScrolledWindow()
        	self.sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        	self.sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.vbox.pack_start(self.sw, True, True, 0)
		store = self.create_model()
		self.treeView = gtk.TreeView(store)
        	self.treeView.connect("row-activated", self.on_activated)
        	self.treeView.set_rules_hint(True)
        	self.sw.add(self.treeView)
		self.create_columns(self.treeView)
        	self.statusbar = gtk.Statusbar()
		self.vbox.pack_start(self.statusbar, False, False, 0)

		self.sw.show()
		self.window.show_all()

class Option:

	def destroy(self, widget, data=None):
		gtk.main_quit()

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Window 3")
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
		self.button6 = gtk.Button("Tkinter")
		self.button6.connect_object("clicked", Tkinter, self.window)
		self.box2.pack_start(self.button6, True, True, 0)
		self.button6.show()
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
