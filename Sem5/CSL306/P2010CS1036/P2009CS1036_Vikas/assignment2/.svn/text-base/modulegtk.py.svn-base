import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("Harmandeep Singh")
        self.set_size_request(500,200)
        self.set_position(gtk.WIN_POS_CENTER)
	label=gtk.Label("Enter Text Here")
        btn2 = gtk.Button("Exit on Click")
        entry = gtk.Entry()
        entry.set_text("text")
        entry.show()
        fixed = gtk.Fixed()
	fixed.put(label, 180, 60)
        fixed.put(btn2, 185, 110)
        fixed.put(entry,150,80)
        btn2.connect("clicked", gtk.main_quit)
        self.connect("destroy", gtk.main_quit)        
        self.add(fixed)
        self.show_all()
