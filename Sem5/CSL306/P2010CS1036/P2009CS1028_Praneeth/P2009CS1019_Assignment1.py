import gtk

#This class will use gtk Window class to show gui
class PyApp(gtk.Window):

    def __init__(self):
        #initializing
        super(PyApp, self).__init__()
        #setting title
        self.set_title("Calculator")
        #assigning size
        self.set_size_request(250, 250)
        self.set_position(gtk.WIN_POS_CENTER)

        #this will request a vertical box
        vbox = gtk.VBox(False, 2)
        
        
        table = gtk.Table(4, 4, True)
        #this will attach a button to table 
        table.attach(gtk.Button("Submit"), 1, 2, 1, 2)
        #this will add a textbox to start of vertical box
        vbox.pack_start(gtk.Entry(), False, False, 0)
        vbox.pack_end(table, True, True, 0)

        self.add(vbox)
        
        #this will link close button and Alt+F4 to close the program 
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
#initialize PyAPP class
PyApp()
#initailize gtk
gtk.main()