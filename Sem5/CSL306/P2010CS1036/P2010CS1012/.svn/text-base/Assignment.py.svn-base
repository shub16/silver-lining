#!/usr/bin/env python
import gtk

def Tkinter(widget,data = None ):
   import tkinter
def PyGTK(widget,data = None ):
   EntryExample() 
      

class EntryExample:
 
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.set_position(gtk.WIN_POS_CENTER)
        window.set_usize(200, 100)
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
        button = gtk.Button("Close")
        button.connect_object("clicked", gtk.mainquit, window)
        vbox.pack_start(button, gtk.TRUE, gtk.TRUE, 0)
        button.show()
	window.show()
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

