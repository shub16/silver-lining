#!/usr/bin/env python
import gtk
people = [('deepak','1992'),('isha',1989),('ravish','1985')]
def Tkinter(widget,data = None ):
   import tkinter
def PyGTK(widget,data = None ):
   EntryExample() 
      

class EntryExample:
    def callback(self, widget, data=None):
	print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
 
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.set_position(gtk.WIN_POS_CENTER)
        window.set_usize(300, 400)
        window.set_title("2010CS1012")
        window.connect("delete_event", gtk.mainquit)
        vbox = gtk.VBox(gtk.FALSE, 0)
        window.add(vbox)
        vbox.show()
        entry = gtk.Entry(1000)
        entry.set_text("hello")
        entry.append_text(" world")
        vbox.pack_start(entry, gtk.TRUE, gtk.TRUE, 0)
        entry.show()
	
	label = gtk.Label("Check button")
	vbox.pack_start(label, True, True, 2)
	label.show()
	button = gtk.CheckButton("check button 1")
	# When the button is toggled, we call the "callback" method
	# with a pointer to "button" as its argument
	button.connect("toggled", self.callback, "check button 1")
	# Insert button 1
	vbox.pack_start(button, True, True, 2)
	button.show()
	# Create second button
	button = gtk.CheckButton("check button 2")
	button.connect("toggled", self.callback, "check button 2")
	#Insert button 2
	vbox.pack_start(button, True, True, 2)
	button.show()
	separator = gtk.HSeparator()
	vbox.pack_start(separator, False, True, 0)
	separator.show()
	label = gtk.Label("Radio button")
	vbox.pack_start(label, True, True, 2)
	label.show()
	button = gtk.RadioButton(None,"radio button 1")
	# When the button is toggled, we call the "callback" method
	# with a pointer to "button" as its argument
	button.connect("toggled", self.callback, "radio button 1")
	# Insert button 1
	vbox.pack_start(button, True, True, 3)
	button.show()
	# Create second button
	button = gtk.RadioButton(button,"radio button 2")
	button.connect("toggled", self.callback, "radio button 2")
	#Insert button 2
	vbox.pack_start(button, True, True, 3)
	button.show()                           
        button = gtk.Button("Close")
        button.connect_object("clicked", gtk.mainquit, window)
        vbox.pack_start(button, gtk.TRUE, gtk.TRUE, 0)
        button.show()
	store = self.create_model()

        treeView = gtk.TreeView(store)
	vbox.pack_start(treeView, gtk.TRUE, gtk.TRUE, 0)
	treeView.connect("row-activated", self.on_activated)
	self.create_columns(treeView)
	treeView.show()
	window.show()
    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1]
        print text
    def create_columns(self, treeView):
    
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Name", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Place", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)
    def create_model(self):
        store = gtk.ListStore(str,str)

        for act in people:
            store.append([act[0], act[1]])

        return store
class Option:
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.set_position(gtk.WIN_POS_CENTER)
        window.set_usize(200, 100)
        window.set_title("2010CS1012")
        window.connect("delete_event", gtk.mainquit)
        vbox = gtk.HBox(gtk.FALSE, 0)
        window.add(vbox)
        vbox.show()
        button1 = gtk.Button("PyGTK")
        button1.connect_object("clicked",PyGTK ,None)
        vbox.pack_start(button1, gtk.TRUE, gtk.TRUE, 0)
        button1.show() 
	button2 = gtk.Button("Tkinter")
        button2.connect_object("clicked",Tkinter , window)
        vbox.pack_start(button2, gtk.TRUE, gtk.TRUE, 0)
        button2.show()                                  
        button = gtk.Button("Close")
        button.connect_object("clicked", gtk.mainquit, window)
        vbox.pack_start(button, gtk.TRUE, gtk.TRUE, 0)
        button.show()
	window.show()
def main():
    gtk.mainloop()
    return 0
if __name__ == "__main__":
    Option()
    main()

