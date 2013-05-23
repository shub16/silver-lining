import gtk

class List(gtk.Window): 
    def __init__(self):
		super(List, self).__init__()
		self.set_size_request(350,200)
		self.set_position(gtk.WIN_POS_CENTER)
		self.set_title("ListView")
		
		vbox = gtk.VBox(False, 10)
		sw = gtk.ScrolledWindow()
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

        for act in actresses:
            store.append([act[0], act[1], act[2]])

        return store
	
	#defining different coloumns
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
        column = gtk.TreeViewColumn("Entry Number", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)

# when doubly clicked on the items on list this will print 
    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)

actresses = [('Nitish Duggal', 'Chandigarh', '2010CS1029'), ('Shubham Upadhyay', 'New Delhi', '2010CS1036'),
    ('Gurpreet Singh', 'Chandigarh', '2010CS1015'), ('Bonani Hazarika', 'Guwahati', '2010CS1010'),
    ('Kshitij Gupta', 'Jaipur', '2010CS1019'), ('Manisha  Digra', 'Pathankot', '2010CS1020' ),('Abhisaar Sharma','Jalandhar','2010CS1001')]


class App(gtk.Window):
    def __init__(self):
	super(App, self).__init__()
	#initializing the window dimensions and titles
	self.set_size_request(200, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("welcome :) ")
	
	# defining a textbox which would show "type here" on placing the cursor over it 
	fixed = gtk.Fixed()
	entry = gtk.Entry()
	entry.set_tooltip_text("type here")
	fixed.put(entry, 20, 50)
	
	# defining a button which would show "click here" on placing the cursor over it 
	btn = gtk.Button("Quit")
	fixed.put(btn, 70, 100)
	btn.set_tooltip_text("click here")
	btn.connect("clicked",gtk.main_quit)
		
	self.add(fixed)
	self.show_all()

class PyApp(gtk.Window):
	   	
	def hello(self,widget):
		import aditya_gujral_tkinter
	def helloworld(self,window):
		App()
	def ListHello(self,window):
		List()			
	def __init__(self):
		super(PyApp, self).__init__()
	
		#initializing the window dimensions and title
		self.connect("destroy", gtk.main_quit)
		self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(6100,6400,6440))
		self.set_size_request(330,330)
		self.set_position(gtk.WIN_POS_CENTER)
		self.set_title("MAIN WINDOW ")
	
		# defining a CONTAINER on which buttons are placed 
		fixed = gtk.Fixed()
		
		# defining a button's
		btn1 = gtk.Button("PyGtk")
		btn2 = gtk.Button("tkinter")
		btn3 = gtk.Button("Quit")	
		btn4 = gtk.Button("List")	
		
		btn1.connect("clicked",self.helloworld) 
		btn2.connect("clicked",self.hello)	
		btn3.connect("clicked",gtk.main_quit)
		btn4.connect("clicked",self.ListHello)		
	
		# button position
		fixed.put(btn1, 85,220)
		fixed.put(btn4, 165,220)    
		fixed.put(btn3, 165, 260)
		fixed.put(btn2, 85,260)
	
		self.set_tooltip_text("MAIN WINDOW")
		btn1.set_tooltip_text("Assignment 1")
		btn2.set_tooltip_text("Assignment 3")
		btn3.set_tooltip_text("Assigment 2")
		btn4.set_tooltip_text("for exit click here")
		
		cbtn1=gtk.CheckButton("CHECK ME 1")
		cbtn2=gtk.CheckButton("CHECK ME 2")
		cbtn3=gtk.CheckButton("CHECK ME 3")
				
		fixed.put(cbtn1,30,50)
		fixed.put(cbtn2,30,100)
		fixed.put(cbtn3,30,150)
		
		rbtn1=gtk.RadioButton(None,"Radio One")
		rbtn2=gtk.RadioButton(rbtn1,"Radio Two")
		rbtn3=gtk.RadioButton(rbtn2,"Radio Three")
		
		fixed.put(rbtn1,150,50)
		fixed.put(rbtn2,150,100)
		fixed.put(rbtn3,150,150)
		
		self.add(fixed)
		self.show_all()

PyApp()
gtk.main()
