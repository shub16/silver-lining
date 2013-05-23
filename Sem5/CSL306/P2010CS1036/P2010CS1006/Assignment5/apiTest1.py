#!/usr/bin/python
from gi.repository import Gtk
import sys



class Dashboard(Gtk.Window):						#Class which creates the main window
	def __init__(self, title, width, height):
		Gtk.Window.__init__(self, title = title)
		self.set_size_request(width, height)
		self.fix = Gtk.Fixed()
		self.grid = Gtk.Grid()
		self.add(self.fix)


	def Add(self, widget):							#Adds widget
		widget_type = type(widget)
		if widget_type == Gtk.Entry:
			self.fix.put(widget.entry, widget.posX, widget.posY )
			self.set_size_request(Length, Breadth)
		if widget_type == Create_button:
			self.fix.put(widget.button2, widget.posX, widget.posY )
		if widget_type == Check_box:
			self.fix.put(widget.button3, widget.posX, widget.posY )
		if widget_type == Drop_list:
			self.fix.put(widget.vbox, widget.posX, widget.posY )
		if widget_type == Radio_button:
			pos2 = 0
			for k in widget.track:
				self.fix.put(k, widget.pos[pos2][0], widget.pos[pos2][1] )	
				pos2 = pos2 + 1	
		if widget_type == Static_text:
			self.fix.put(widget.mess, widget.posX, widget.posY )
		if widget_type == Text_field:
			self.fix.put(widget.entry, widget.posX, widget.posY )
		if widget_type == Password_field:
			self.fix.put(widget.entry, widget.posX, widget.posY )
		if widget_type == Text_area:
			self.fix.put(widget.scrolledwindow, widget.posX, widget.posY )
		if widget_type == Spin_list:
			self.fix.put(widget.hbox, widget.posX, widget.posY )
		if widget_type == Progress_bar:
			self.fix.put(widget.vbox, widget.posX, widget.posY )
		


	def Display(self):
		self.connect("delete-event", Gtk.main_quit)
#		self.center()
		self.show_all()
		Gtk.main()

class Create_button(Gtk.Button):								#Creates a Button
	
	def __init__(self, posX, posY, title = "MyButton", length = 100, breadth = 30 ):   
		self.button2 = Gtk.Button(label = title)
		self.button2.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
					   		
	def Click_listener(self, method):
		self.button2.connect("clicked", method)



class Check_box(Gtk.CheckButton):
	def __init__(self, posX, posY, title, length, breadth):   
		self.button3 = Gtk.CheckButton(label = title)
		self.button3.set_size_request(length, breadth)
		self.button3.set_active(True)
		self.posX = posX
		self.posY = posY

	def Is_checked(self):
		val = self.button3.get_active()
		if val == True:
			return True
		else:
			return False
	
	def Set_checked(self, value = True):
		self.button3.set_active(value)

class Text_field(Gtk.Entry):							#Creates a Text_field
	def __init__(self, posX, posY, text = "", length = 250, breadth = 25):   
		self.entry = Gtk.Entry()
		self.posX = posX
		self.posY = posY
		self.entry.set_text(text)
		self.entry.set_size_request(length, breadth)
	
	def Clear_field(self):
		 self.entry.set_text("")

	def Set_text(self,text):
		self.entry.set_text(text)

	def Get_text(self):
		return self.entry.get_text()


class Password_field(Gtk.Entry):						#A password field
	def __init__(self, posX, posY, text = "", length = 250, breadth = 25):   
		self.entry = Gtk.Entry()
		self.posX = posX
		self.posY = posY
		self.entry.set_text(text)
		self.entry.set_size_request(length, breadth)
		self.entry.set_visibility(False)
	
	def Clear_field(self):
		 self.entry.set_text("")

	def Set_text(self,text):
		self.entry.set_text(text)

	def Get_text(self):
		return self.entry.get_text()

class Drop_list(Gtk.ListStore):							#Creates a Drop List with options
	def __init__(self, posX, posY, name1, values, length = 100, breadth = 27):
		self.posX = posX
		self.posY = posY
		self.store = Gtk.ListStore(str)
		self.name = name1
		for i in values:
			treeiter = self.store.append([i])	
		self.name_combo = Gtk.ComboBox.new_with_model(self.store)
		self.name_combo.set_size_request(length, breadth)
		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		renderer_text = Gtk.CellRendererText()
		self.name_combo.pack_start(renderer_text, True)
		self.name_combo.add_attribute(renderer_text, "text", 0)
		self.vbox.pack_start(self.name_combo, False, False, 0)

	def Get_value(self):
		tree_iter = self.name_combo.get_active_iter()
		model = self.name_combo.get_model()
		return model[tree_iter][:1]



class Progress_bar(Gtk.Window):
	def __init__(self, posX, posY, length = 100, breadth = 20):
		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.progressbar = Gtk.ProgressBar()
		self.progressbar.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY	
		self.vbox.pack_start(self.progressbar, True, True, 0)
	
	def Set_fraction(self, value = 0.5):
		self.value = self.progressbar.set_fraction(value)
	
	def Ret_fraction(self):
		return self.value


class Radio_button(Gtk.RadioButton):						#Creates a Radio Button
	def __init__(self,label1, posX, posY):
		self.track = []	
		self.names = []
		self.pos = []	
		self.names.append(label1)
		self.choose1 = Gtk.RadioButton.new_with_label_from_widget(None, label1)
		self.track.append(self.choose1)
		self.posX = posX
		self.posY = posY
		self.pos.append((posX, posY))


	def Add_radio_button(self, label, posX, posY):					#Adds another radio_button
		self.label2 = Gtk.RadioButton.new_with_label_from_widget(None, label)
		self.posX = posX
		self.posY = posY
		self.names.append(label)
		self.track.append(self.label2)
		self.pos.append((posX, posY))
		self.choose1.join_group(self.label2)
	
	
	def Get_selected(self):
		k = 0
		for i in self.track:
			if(i.get_active() == True):
				return self.names[k]
			k = k + 1
	

class Static_text(Gtk.Label):								#Creates a Label
	def __init__(self, posX, posY, length = 150, breadth = 30, text = ""):
		self.mess = Gtk.Label(text)
		self.mess.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
		self.mess.set_text(text)

	def Set_value(self,text):									# Function to set text in the textbox
		self.mess.set_text(text)
	
	

class Spin_list(Gtk.SpinButton):								#Creates a spinButton
	def __init__(self, posX, posY, length = 100, breadth = 25, minimum = 0, maximum = 100):
		self.hbox = Gtk.Box(spacing=6)
		self.posX = posX
		self.posY = posY
		adjustment = Gtk.Adjustment(0, minimum, maximum, 1, 10, 0)
		self.spinbutton = Gtk.SpinButton()
		self.spinbutton.set_adjustment(adjustment)
		self.spinbutton.set_size_request(length, breadth)
		self.hbox.pack_start(self.spinbutton, False, False, 0)

	def Get_value(self):									#returns the value
		return self.spinbutton.get_value_as_int()



class Text_area(Gtk.TextBuffer):							#Creates Text Area
	def __init__(self, posX, posY, length = 300, breadth = 200, text = ""):
		self.scrolledwindow = Gtk.ScrolledWindow()
		self.scrolledwindow.set_size_request(length, breadth)
		self.scrolledwindow.set_hexpand(True)
		self.scrolledwindow.set_vexpand(True)
		self.posX = posX
		self.posY = posY
		self.length = length
		self.breadth = breadth
		self.textview = Gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		self.textbuffer.set_text(text)
		self.textview.set_size_request(length, breadth)
		self.textview.set_wrap_mode(True)
		self.scrolledwindow.add(self.textview)
		
	def Set_text(self,text):							#Sets its Text
		self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
		self.textbuffer.set_text(text)

	def Append_text(self, text):
		self.textbuffer.insert(self.textbuffer.get_end_iter(), text)
	
	def Clear_area(self):
		self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
	
	def Get_text(self):
		a = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), 0)
		return a



#--------------------------------------------------UNIT Test Demonstration--------------------------------#

def Check(self):					#Checks if the password is set satisfactorily
    password1 = NewPassEntry.Get_text();
    password2 = ReNewPassEntry.Get_text();
    if(Is_valid_pass(password1,password2)):		#calls Is_valid_pass
        print ("Password Successfully Changed ! ");
        OldPassEntry.Clear_field();
        NewPassEntry.Clear_field();
        ReNewPassEntry.Clear_field();
    else:
        print ("Retry by Entering new Password!  ");
        OldPassEntry.Clear_field();
        NewPassEntry.Clear_field();
        ReNewPassEntry.Clear_field();
 

def Is_valid_pass(pass1, pass2):		#Checks if the passwords satisfy all the criteria
    if pass1 != pass2:
       print("Error in Password! --> Passwords do not match! ")
       return False
    
    if(len(pass1)<=6):               # Check the length of the password
       print("Error in Password! --> Password Length should be more than 6. ")
       return False    
    
    if(str(pass1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(pass1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print("Error in Password!--> Password cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(pass1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print("Error in Password!--> Password cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            print ("Password Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print ("Error in Password!--> Password should contain only alphabets and digits.");
       return False


#----------------Unit Test Window------------------------------------------------------------------
#------------------Creates a Login Window-------------------------------------------------------
OuterPanel = Dashboard("Unit Test",400, 300)
NameLabel = Static_text( 15, 30, 80, 30,  "Name :")
OuterPanel.Add(NameLabel)
OldPassLabel = Static_text( 10, 75,140, 30, "Old Password :",)
OuterPanel.Add(OldPassLabel)
NewPassLabel = Static_text( 4, 120,160, 30, "New Password :",)
OuterPanel.Add(NewPassLabel)
ReTypeLabel = Static_text( 14, 170, 160, 30, "Re-Type Password :")
OuterPanel.Add(ReTypeLabel)
NameEntry = Text_field(180, 30, "", 150, 30)
OuterPanel.Add(NameEntry)
OldPassEntry = Password_field(180, 75, "", 150, 30)
OuterPanel.Add(OldPassEntry)
NewPassEntry = Password_field(180, 120, "", 150, 30)
OuterPanel.Add(NewPassEntry)
ReNewPassEntry = Password_field(180, 170, "", 150, 30)
OuterPanel.Add(ReNewPassEntry)
SubmitButton = Create_button(150, 230, "Log In", 100, 35)
OuterPanel.Add(SubmitButton)
SubmitButton.Click_listener(Check) 
OuterPanel.connect("delete-event", Gtk.main_quit))
OuterPanel.show_all()
if __name__ == '__main__':
    Gtk.main()
