import gtk
#import P2009cs1026_Asn2_text_Editor as py_fltk

class PyApp(gtk.Window):
# enter_callback function executes when user presses enter
	def enter_callback(self, widget, entry):
		text=entry.get_text()
		a="HI "+text+" !"
		self.label.set_text(a)
# on_click functions executes when user clicks on the button
	def on_click(self,widget,entry):	
		a="HI "+entry.get_text()+" !"
		self.label.set_text(a)
	def __init__(self):
		super(PyApp, self).__init__()
		self.set_title("Entry")
		self.set_size_request(250,200)
		self.set_position(gtk.WIN_POS_CENTER)
		fixed=gtk.Fixed()
		entry=gtk.Entry()
		entry.connect("activate", self.enter_callback,entry)
		btn=gtk.Button("ENTER")
		btn.set_size_request(60,40)
		btn.connect("clicked", self.on_click,entry)
		self.label = gtk.Label("Type a Name!")
		fixed.put(self.label, 60, 40)
		fixed.put(entry,60,100)
		fixed.put(btn,100,150)
		self.connect("destroy",gtk.main_quit)
		self.add(fixed)
		self.show_all()
		
def main() :
	PyApp()
	gtk.main()

if __name__ == "__main__":
	main()

"""
if __name__ == "__main__":

	x = int(raw_input("\tPlease enter :\n\t1 for Pyfltk window\n\t2 for pyGtk Window\n > "))
	if x == 1:
		main()												# RUN pyGTK App
	elif x == 2:
		py_fltk.main()										# RUN Py_fltk App
	else :
		print "\t Please, Enter 1 or 2 \nEXIT\n"
"""
