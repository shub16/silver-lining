#!/usr/bin/env python



import gtk

class EntryExample:

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_usize(200, 100)
        window.set_title("GTK Entry")
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
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show()

def main():
    gtk.mainloop()
    return 0

if __name__ == "__main__":
    EntryExample()
    main()


