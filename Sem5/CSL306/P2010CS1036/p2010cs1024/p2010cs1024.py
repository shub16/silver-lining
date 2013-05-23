import pygtk
pygtk.require('2.0')
import gtk 

class textentry:
	
	# Call back function. 
	def enter_callback(self,widget,entry):
		entry_text = entry.get_text()
		print "Entered text is: %s\n" % entry_text
	
	# Call back for checkbutton editable.
	def entry_toggle_editable(self,checkbutton,entry):
		entry.set_editable(checkbutton.get_active())
	#	print "You can edit the content in textbox\n"
	#	print "Press enter to print the text\n"
      		print "%s is %s now" % ("Edit button", ("OFF","ON")[checkbutton.get_active()])
      		print "Press ENTER button to print text,works only if edit button is ON"

	def __init__(self):
		# Create a new window.
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)
			
		# Set the title of the window.
		window.set_title("GTK entry")

		# Set the size of the window.
		window.set_size_request(200,100)

		# Set a handler for delete_event that immediately exits GTK.
		window.connect("delete_event",gtk.main_quit)

		# Create a  vertical box.
		vbox = gtk.VBox()

		# Add this vertical box to the window.
		window.add(vbox)

		# Show the newly created vertical box.
		vbox.show()

		# Create a entry widget.
		entry = gtk.Entry()
			
		# Set the maximum length of the entry.
		entry.set_max_length(50)
  
  		# Set the signal handler for activate that calls the callback method. 
		entry.connect("activate",self.enter_callback,entry)

		# Set the contents of entry widget to "Hello" replacing the current contents.
		entry.set_text("Enter the text")

		# The region of the text is selected making it easy for the user to remove it.
		entry.select_region(0,len(entry.get_text()))
		
		# Packing the entry widget into the vertical box.
		vbox.pack_start(entry)

		# Show the entry widget created.
		entry.show()

		# Create a horizontal box.
		hbox = gtk.HBox()
			
		# Add the horizontal box to the vertical box.
		vbox.add(hbox)

		# Show the newly created horizontal box.
		hbox.show()

		# Create a check button with title editable.
		check = gtk.CheckButton("Edit")

		# Pack the checkbutton into the horizontal box.
		hbox.pack_start(check)
	
		# Set the signal handler for "toggled" that calls the entry_toggle_editable callback method.
		check.connect("toggled", self.entry_toggle_editable, entry)
                check.set_active(1)
		# Show the check button.
		check.show()
		
		# Create a 'close' button. 
		button = gtk.Button("CLICK to CLOSE")

		# gtk.main_quit to close the window.
		button.connect_object("clicked", gtk.main_quit, window)
		
		# Pack the button into the vertical box.
		vbox.pack_start(button)

		# Show the newly created button.
		button.show()

		# Show the window.
		window.show()


actresses = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'),
    ('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'),
    ('rachel weiss', 'london', '1971'), ('scarlett johansson', 'new york', '1984' )]



				
		
class textentry1:
	
	def destroy(self, widget, data=None):
                print "PYGTK has been selected"
                textentry()
        def destroy1(self, widget, data=None):
                print "TKINTER has been selected"
                import tk
         
         
        def callback(self,widget,data=None):
                print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
                
                
        def entry_toggle_editable(self,checkbutton,data=None):
	#	entry.set_editable(checkbutton.get_active())
	#	print "You can edit the content in textbox\n"
	#	print "Press enter to print the text\n"
      		print "%s is %s now" % (data, ("OFF","ON")[checkbutton.get_active()])
      	#	print "Press ENTER button to print text,works only if edit button is ON"        
                

	def __init__(self):
		# Create a new window.
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		
			
		# Set the title of the window.
		window.set_title("GTK entry")

		# Set the size of the window.
		window.set_size_request(350,450)

		# Set a handler for delete_event that immediately exits GTK.
		window.connect("delete_event",gtk.main_quit)

		# Create a  vertical box.
		vbox = gtk.VBox()

		# Add this vertical box to the window.
		window.add(vbox)

		# Show the newly created vertical box.
		vbox.show()

		# Create a horizontal box.
		hbox = gtk.HBox()
			
		# Add the horizontal box to the vertical box.
		vbox.add(hbox)

		# Show the newly created horizontal box.
		hbox.show()

		# Create a 'close' button. 
		button = gtk.Button("PYGTK")

		# gtk.main_quit to close the window.
                button.connect("clicked", self.destroy, None)
		
		# Pack the button into the vertical box.
		vbox.pack_start(button)

		# Show the newly created button.
		button.show()
		
		# Create a 'close' button. 
		button1 = gtk.Button("TKINTER")

		# gtk.main_quit to close the window.
		button1.connect("clicked", self.destroy1, window)
		
		# Pack the button into the vertical box.
		vbox.pack_start(button1)

                button1.show()





		# Create a check button with title editable.
		check1 = gtk.CheckButton("Checkbox1")

		# Pack the checkbutton into the horizontal box.
		vbox.pack_start(check1)
	
		# Set the signal handler for "toggled" that calls the entry_toggle_editable callback method.
		check1.connect("toggled", self.entry_toggle_editable, "Check box 1")
                check1.set_active(1)
		# Show the check button.
		check1.show()
		
		check2 = gtk.CheckButton("Checkbox2")

		# Pack the checkbutton into the horizontal box.
		vbox.pack_start(check2)
	
		# Set the signal handler for "toggled" that calls the entry_toggle_editable callback method.
		check2.connect("toggled", self.entry_toggle_editable, "Check box 2")
                #check2.set_active(1)
		# Show the check button.
		check2.show()

                button11 = gtk.RadioButton(None, "radio button1")
                button11.connect("toggled", self.callback, "radio button 1")
                vbox.pack_start(button11, True, True, 0)
                button11.show()
                
                button2 = gtk.RadioButton(button11, "radio button2")
                button2.connect("toggled", self.callback, "radio button 2")
                button2.set_active(True)
                vbox.pack_start(button2, True, True, 0)
                button2.show()

                button3 = gtk.RadioButton(button11, "radio button3")
                button3.connect("toggled", self.callback, "radio button 3")
                vbox.pack_start(button3, True, True, 0)
                button3.show()

                tree = gtk.TreeView()
                languages = gtk.TreeViewColumn()
                languages.set_title("Programming languages")
 
                cell = gtk.CellRendererText()
                languages.pack_start(cell, True)
                languages.add_attribute(cell, "text", 0)
 
                treestore = gtk.TreeStore(str)
 
                it = treestore.append(None, ["Scripting languages"])
                treestore.append(it, ["Python"])
                treestore.append(it, ["PHP"])
                treestore.append(it, ["Perl"])
                treestore.append(it, ["Ruby"])
 
                it = treestore.append(None, ["Compiling languages"])
                treestore.append(it, ["C#"])
                treestore.append(it, ["C++"])
                treestore.append(it, ["C"])
                treestore.append(it, ["Java"])
 
                tree.append_column(languages)
                tree.set_model(treestore)

                vbox.pack_start(tree)
                tree.set_size_request(350,250)
                tree.show()

		window.show()
		
def main():

	gtk.main()
	return 0



if __name__ == "__main__":
	textentry1()
	main()
