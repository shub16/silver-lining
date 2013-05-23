import gtk
class PyApp1(gtk.Window):
    def __init__(self):
        super(PyApp1, self).__init__()
        self.set_title("Harmandeep Singh")
        self.set_size_request(500,200)
        self.set_position(gtk.WIN_POS_CENTER)
	label=gtk.Label("Enter Text Here")
        btn2 = gtk.Button("Button")
        entry = gtk.Entry()
        entry.set_text("text")
        entry.show()
        fixed = gtk.Fixed()
	fixed.put(label, 180, 60)
        fixed.put(btn2, 200, 110)
        fixed.put(entry,150,80)
        #btn2.connect("clicked", gtk.main_quit)
        #self.connect("destroy", gtk.main_quit)        
        self.add(fixed)
        self.show_all()


actresses = [('Anubhav', 'pomona', '1981'), ('Harmandeep', 'Bathinda', '1992'),
    ('Gurpreet', 'los angeles', '1975'), ('Kshitij', 'jerusalem', '1981'),
     ]


class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_size_request(400, 800)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)
        self.connect("destroy", gtk.main_quit)
        self.set_title("ListView")
	vbox = gtk.VBox(False, 0)
	
	# For Adding Scroll Bar
        
        sw = gtk.ScrolledWindow()
        sw.set_border_width(50)
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

	
	
	#for check Boxes
        button = gtk.CheckButton("check button 1")
        button.connect("toggled", self.callback, "check button 1")
        vbox.pack_start(button, True, True, 2)
        button.show()
        
        button = gtk.CheckButton("check button 2")
        button.connect("toggled", self.callback, "check button 2")
        vbox.pack_start(button, True, True, 2)
        button.show()
	
	# For Adding Buttons
	btn1 = gtk.Button("Py GTK")
        btn1.connect("clicked", self.fun , None )
    	vbox.pack_start(btn1, True, True, 0)
        vbox.add(btn1)
        btn2 = gtk.Button("Py tkinter")
        btn2.connect("clicked", self.fun1 , None )
    	vbox.pack_start(btn1, True, True, 0)
    	vbox.add(btn2)
    	vbox.show()
    	btn1.show()
    	btn2.show()
        
        
        
        #For adding Radio Buttons
        
        button = gtk.RadioButton(None, "radio button1")
        button.connect("toggled", self.callback, "radio button 1")
        vbox.pack_start(button, True, True, 0)
        button.show()
        button = gtk.RadioButton(button, "radio button2")
        button.connect("toggled", self.callback, "radio button 2")
        #button.set_active(True)
        vbox.pack_start(button, True, True, 0)
        button.show()
	self.add(vbox)
        self.show_all()


    def create_model(self):
        store = gtk.ListStore(str, str, str)
        for act in actresses:
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

    def fun1(self, widget,data = None ):
    	import tkinter

    def fun(self, widget,data = None ):
	PyApp1()

    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)
	
    def callback(self, widget, data=None):
        print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])



PyApp()
gtk.main()
