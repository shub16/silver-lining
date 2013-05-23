"""
This code generates the GUI for the attacker. The attacker can attack the target just by inputing its IP address in GUI.  

"""

import gtk
from VirtualTerminal import VirtualTerminal


class PyApp(gtk.Window):					
	def on_clicked(self,widget):					# It executes script for a particular attack on receiving a button click signal.
		if self.rb2.get_active():
			self.ip=self.wins.get_text()
			self.myTerminal.terminal.run_command("./syn.sh "+self.ip)
		if self.rb3.get_active():
			self.ip=self.wins.get_text()
			self.myTerminal.terminal.run_command("./port.sh "+self.ip)
		if self.rb4.get_active():
			self.myTerminal.terminal.run_command("./worm.sh ")
		if self.rb5.get_active():
			self.ip1=self.wins.get_text()
			self.ip2=self.wins2.get_text()
			self.myTerminal.terminal.run_command("./smurf.sh "+self.ip2+" "+self.ip1+" 0")
	def __init__(self):
		super(PyApp, self).__init__()				# It generates the GUI window
		self.set_title("Attacker")
		self.set_size_request(350, 300)
		self.set_position(gtk.WIN_POS_CENTER)
		self.wins = gtk.Entry()
		self.wins.set_editable(True)
		self.wins.set_size_request(200,30)
		self.wins2 = gtk.Entry()
		self.wins2.set_editable(True)
		self.wins2.set_size_request(200,30)
		self.wins2.set_text("Source IP (only for Smurf Attack)")
		self.wins.set_text("Destination IP")
		self.btn4 = gtk.Button("ATTACK")
		self.btn4.connect("clicked",self.on_clicked)
		self.btn4.set_size_request(90, 40)
		self.rb2=gtk.RadioButton(None,"Syn Flood")
		self.rb3=gtk.RadioButton(self.rb2,"PortScan Attack")
		self.rb4=gtk.RadioButton(self.rb2,"Worm Attack")
		self.rb5=gtk.RadioButton(self.rb2,"Smurf Attack")
		fixed = gtk.Fixed()
		fixed.put(self.wins,60,190)
		fixed.put(self.wins2,60,145)
		fixed.put(self.btn4,130,230)
		fixed.put(self.rb2,50,50)
		fixed.put(self.rb3,50,70)
		fixed.put(self.rb4,50,90)
		fixed.put(self.rb5,50,110)
		self.myTerminal = terminal()
		self.connect("destroy", gtk.main_quit)
		self.set_tooltip_text("Attack window")
		self.btn4.set_tooltip_text("Attack Button")
		self.add(fixed)
		self.show_all()
class terminal(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect('destroy', lambda w: gtk.main_quit())
        self.terminal = VirtualTerminal()
        self.add(self.terminal)
        self.show_all()
PyApp()
gtk.main()
