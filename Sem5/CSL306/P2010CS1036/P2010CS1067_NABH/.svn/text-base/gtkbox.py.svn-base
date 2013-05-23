import pygtk
pygtk.require('2.0')
import gtk

class TextBox:
	def enter_callback(auto, widget, entry):
		entry_text = entry.get_text()
		print "Entry contents: %s\n" % entry_text

	def __init__(auto):
		frame = gtk.Window(gtk.WINDOW_TOPLEVEL)
		frame.set_title("Sample")
		frame.connect("delete_event", lambda w,e: gtk.main_quit())
		vbox = gtk.VBox(False, 0)
		frame.add(vbox)
		vbox.show()
		entry = gtk.Entry(max=0)
		entry.connect("activate", auto.enter_callback, entry)
		entry.set_text("type")
		text=entry.get_text()
		a=len(text)
		entry.insert_text(" text", a)
		entry.select_region(0, a)
		vbox.pack_start(entry, True, True, 5)
		entry.show()		
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", lambda w: gtk.main_quit())
		vbox.pack_start(button, True, True, 1)
		button.set_flags(gtk.CAN_DEFAULT)
		button.grab_default()
		button.show()
		frame.show()
			
	def main(auto):
		gtk.main()
		return 0
if __name__ == "__main__":
	entry=TextBox()
	entry.main()


