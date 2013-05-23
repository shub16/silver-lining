import gtk
from VirtualTerminal import VirtualTerminal

class PyApp(gtk.Window):
	def on_clicked1(self,widget):
		self.myTerminal.terminal.run_command("perl init.pl ")
	def on_clicked2(self,widget):
		self.myTerminal.terminal.run_command("snort -c /etc/snort/snort.conf")
	def on_clicked3(self,widget):
		self.myTerminal.terminal.run_command("perl alert.pl")
	def on_clicked4(self,widget):
		self.myTerminal.terminal.run_command("chmod +x tcpclient.sh")
		self.myTerminal.terminal.run_command("./tcpclient.sh")
	def on_clicked(self,widget):
		if self.rb1.get_active():
			#self.ip=self.wins.get_text()
			self.myTerminal.terminal.run_command("./prevent.sh ")
		if self.rb2.get_active():
			#self.ip=self.wins.get_text()
			self.myTerminal.terminal.run_command("./syn_prevent.sh ")
		if self.rb3.get_active():
			#self.ip=self.wins.get_text()
			self.myTerminal.terminal.run_command("./port_prevent.sh ")
		if self.rb4.get_active():
			self.myTerminal.terminal.run_command("./worm_prevent.sh ")
		if self.rb5.get_active():
			#self.ip1=self.wins.get_text()
			#self.ip2=self.wins2.get_text()
			self.myTerminal.terminal.run_command("./smurf_prevent.sh ")
	def __init__(self):
		super(PyApp, self).__init__()
		self.set_title("Buttons")
		self.set_size_request(650, 500)
		self.set_position(gtk.WIN_POS_CENTER)
		self.wins = gtk.Entry()
		self.wins.set_editable(True)
		self.wins.set_size_request(200,30)
		self.wins2 = gtk.Entry()
		self.wins2.set_editable(True)
		self.wins2.set_size_request(200,30)
		self.wins2.set_text("Source IP (only for Smurf Attack)")
		self.wins.set_text("Destination IP")
		self.btn1 = gtk.Button("INITIALIZE")
		self.btn1.connect("clicked",self.on_clicked1)
		self.btn1.set_size_request(120, 40)
		self.btn2 = gtk.Button("Snort ON")
		self.btn2.connect("clicked",self.on_clicked2)
		self.btn2.set_size_request(90, 40)
		self.btn3 = gtk.Button("Snort OFF")
		self.btn3.connect("clicked",self.on_clicked3)
		self.btn3.set_size_request(90, 40)
		self.btn5 = gtk.Button("TCP Client")
		self.btn5.connect("clicked",self.on_clicked4)
		self.btn5.set_size_request(90, 40)
		self.btn4 = gtk.Button("Prevent!!!")
		self.btn4.connect("clicked",self.on_clicked)
		self.btn4.set_size_request(100, 40)
		self.rb1=gtk.RadioButton(None,"Ping Flood")
		self.rb2=gtk.RadioButton(self.rb1,"Syn Flood")
		self.rb3=gtk.RadioButton(self.rb1,"PortScan Attack")
		self.rb4=gtk.RadioButton(self.rb1,"Worm Attack")
		self.rb5=gtk.RadioButton(self.rb1,"Smurf Attack")
		fixed = gtk.Fixed()
		fixed.put(self.btn1,80,50)
		fixed.put(self.btn2,80,150)
		fixed.put(self.btn3,180,150)
		fixed.put(self.btn5,190,300)
		fixed.put(self.btn4,200,400)
		fixed.put(self.rb1,150,200)
		fixed.put(self.rb2,150,220)
		fixed.put(self.rb3,150,240)
		fixed.put(self.rb4,150,260)
		fixed.put(self.rb5,150,280)
		self.myTerminal = terminal()
		self.connect("destroy", gtk.main_quit)
		self.set_tooltip_text("Target Window")
		self.btn1.set_tooltip_text("Initialize Button")
		self.add(fixed)
		self.show_all()
class terminal(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        #self.set_title(self.settings.application_name)
        self.connect('destroy', lambda w: gtk.main_quit())
 
        self.terminal = VirtualTerminal()
 
        #self.child_pid = self.terminal.fork_command()
 
        self.add(self.terminal)
        self.show_all()
	
PyApp()
gtk.main()

