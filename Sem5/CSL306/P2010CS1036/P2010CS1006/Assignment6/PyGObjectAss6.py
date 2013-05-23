#!/usr/bin/python
from gi.repository import Gtk
import sys

#Main API
class Dashboard(Gtk.Window):							#Class responsible for making window
	def __init__(self, title, width, height):
		Gtk.Window.__init__(self, title = title)
		self.set_size_request(width, height)
		self.fix = Gtk.Fixed()
		self.grid = Gtk.Grid()
		self.add(self.fix)


	def Add(self, widget):									#Adding widgets based on their type
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
		


	def Display(self):										#Display - shows all the widgets
		self.connect("delete-event", Gtk.main_quit)
#		self.center()
		self.show_all()
		Gtk.main()

class Create_button(Gtk.Button):									#Creates  a button
	
	def __init__(self, posX, posY, title = "MyButton", length = 100, breadth = 30 ):   			#Initializes the button
		self.button2 = Gtk.Button(label = title)
		self.button2.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
					   		
	def Click_listener(self, method):								#A click listener function is passed as an argument
		self.button2.connect("clicked", method)



class Check_box(Gtk.CheckButton):								#creates a Checkbox
	def __init__(self, posX, posY, title, length, breadth):   
		self.button3 = Gtk.CheckButton(label = title)
		self.button3.set_size_request(length, breadth)
		self.button3.set_active(True)
		self.posX = posX
		self.posY = posY

	def Is_checked(self):										#returns if the checkbox is checked or not
		val = self.button3.get_active()
		if val == True:
			return True
		else:
			return False
	
	def Set_checked(self, value = True):								#Assigns value to the check box
		self.button3.set_active(value)

class Text_field(Gtk.Entry):							#A class for creating Text Field
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


class Password_field(Gtk.Entry):								#Creates a password field
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

class Drop_list(Gtk.ListStore):								#Creates a Drop_list
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


class Radio_button(Gtk.RadioButton):				#Creates a radio button
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


	def Add_radio_button(self, label, posX, posY):
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
	

class Static_text(Gtk.Label):							#Creates a static text
	def __init__(self, posX, posY, length = 150, breadth = 30, text = ""):
		self.mess = Gtk.Label(text)
		self.mess.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
		self.mess.set_text(text)

	def Set_value(self,text):									# Function to set text in the textbox
		self.mess.set_text(text)
	
	

class Spin_list(Gtk.SpinButton):							#Created spin list
	def __init__(self, posX, posY, length = 100, breadth = 25, minimum = 0, maximum = 100):
		self.hbox = Gtk.Box(spacing=6)
		self.posX = posX
		self.posY = posY
		adjustment = Gtk.Adjustment(0, minimum, maximum, 1, 10, 0)
		self.spinbutton = Gtk.SpinButton()
		self.spinbutton.set_adjustment(adjustment)
		self.spinbutton.set_size_request(length, breadth)
		self.hbox.pack_start(self.spinbutton, False, False, 0)

	def Get_value(self):
		return self.spinbutton.get_value_as_int()


	
class Text_area(Gtk.TextBuffer):								#Creates a Text Area
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
		
	def Set_text(self,text):
		self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
		self.textbuffer.set_text(text)

	def Append_text(self, text):
		self.textbuffer.insert(self.textbuffer.get_end_iter(), text)
	
	def Clear_area(self):
		self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
	
	def Get_text(self):
		a = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), 0)
		return a


def Submit(self):							#Submit function called while clicking submit button
     	text = " Your Favourite City is " + str(valuelist.Get_value())+"\n"
        if(checkbox1.Is_checked()):
		text = text + "You like  Cricket\n"
	else:
		text = text + "You don't like Cricket\n"
    
        if(checkbox2.Is_checked()):
            	text = text + "You like Football\n"
        else:
            	text = text + "You  don't like Football\n"
            		
        if(checkbox3.Is_checked()):
            	text = text + "You like Tennis\n"
       	else:
            	text = text + "You  don't like Tennis\n"
    
        text = text + "Your Gender is  "+rb1.Get_selected()+"\n"
	text = text + "Your lucky number is " + str(sp.Get_value()) + "\n"
       	textarea.Append_text("\n*************************\n"+text+"\n\n")
       	return True 


#----------------------Demonstration-------------------------------------------------------
frame = Dashboard( 'Naveen Qt4' ,550,500)
#fr = Dashboard( 'Naveen Qt4' ,550,300)
checkbox1 = Check_box(10,45,"Cricket",215,15)			#check boxes for selecting sport
checkbox2 = Check_box(10,70,"Football",215,15)
checkbox3 = Check_box(10,95,"Tennis",215,15)
#checkbox1.setValue(True)
submitBtn = Create_button(130,170,"Submit",120,30)		#Creates a submit button
submitBtn.Click_listener(Submit)
frame.Add(checkbox1)						#Adds the widget(check boxes and button) to the main frame
frame.Add(checkbox2)
frame.Add(checkbox3)
frame.Add(submitBtn)
cities = ['New Delhi', 'Pune', 'Ropar', 'Noida', 'Chandigarh', 'Kanpur','Aligarh', 'Lahore','Multan','Islamabad', ]
valuelist = Drop_list(10,10,"Cities",cities,150,20)		#Choose your favorite city
frame.Add(valuelist)
#rb1 = Radio_button("",10,350)
rb1=Radio_button("Male",10,300)					#Adds radio button
rb1.Add_radio_button("Female ",10,350)
   # 	rb1.setButtonTrue(0)
frame.Add(rb1)
textarea = Text_area(250,10,200,100," Click submit button")
password = Password_field(300,350)
textfield=Text_field(300,300)
#lb=Static_text(280,200,80,20,"naveen")	
sp=Spin_list(290,170,100,30,0,100)				#Choose your lucky no
lb2=Static_text(10,270,80,20,"Choose Gender")
frame.Add(lb2)
textfield.Set_text("Enter Password")
#textarea.Set_text(" window ")
textarea.Clear_area()
frame.Add(textarea)						#Adds all the widgets
frame.Add(password)
frame.Add(sp)
frame.Add(textfield)
frame.Display()							#Displays all the widgets

