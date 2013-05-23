#!/usr/bin/python
from gi.repository import Gtk
import sys


#-----------Main Class-----------------------------------
class Dashboard(Gtk.Window):
	def __init__(self, title, width, height):
		Gtk.Window.__init__(self, title = title)
		self.set_size_request(width, height)
		self.fix = Gtk.Fixed()
		self.grid = Gtk.Grid()
		self.add(self.fix)


	def Add(self, widget):					#Adds all the widgets
		widget_type = type(widget)
		if widget_type == Gtk.Entry:
			self.fix.put(widget.entry, widget.posX, widget.posY )
			self.set_size_request(Length, Breadth)
		if widget_type == Create_button:
			self.fix.put(widget.button2, widget.posX, widget.posY )
		if widget_type == Check_box:
			self.fix.put(widget.button3, widget.posX, widget.posY )
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
		


	def Display(self):					#Displays the function
		self.connect("delete-event", Gtk.main_quit)
#		self.center()
		self.show_all()
		Gtk.main()

class Create_button(Gtk.Button):						#Creates the button
	
	def __init__(self, posX, posY, title = "MyButton", length = 100, breadth = 30 ):   
		self.button2 = Gtk.Button(label = title)
		self.button2.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
					   		
	def Click_listener(self, method):
		self.button2.connect("clicked", method)



class Check_box(Gtk.CheckButton):						#Creates the Check box
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

class Text_field(Gtk.Entry):							#Text_field
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


class Password_field(Gtk.Entry):						#Password field
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


class Radio_button(Gtk.RadioButton):				#Radio Button
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
	

class Static_text(Gtk.Label):							#Displays the Static_text
	def __init__(self, posX, posY, length = 150, breadth = 30, text = ""):
		self.mess = Gtk.Label(text)
		self.mess.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
		self.mess.set_text(text)

	def Set_value(self,text):									# Function to set text in the textbox
		self.mess.set_text(text)



class Text_area(Gtk.TextBuffer):							#The text_area
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


def Submit(self):			#Called when the button is clicked and prints the the text in Text area
     	text = ""
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
       	textarea.Append_text("\n*************************\n"+text+"\n\n")
       	return True 



#------------------------------Demonstration--------------------------------------------------------------------------------
frame = Dashboard( 'Naveen Qt4' ,550,500)
checkbox1 = Check_box(10,45,"Cricket",215,15)			#check boxes for selecting sport
checkbox2 = Check_box(10,70,"Football",215,15)
checkbox3 = Check_box(10,95,"Tennis",215,15)
submitBtn = Create_button(130,160,"Submit",120,30)		#Creates a submit button
submitBtn.Click_listener(Submit)
frame.Add(checkbox1)						#Adds the widget(check boxes and button) to the main frame
frame.Add(checkbox2)
frame.Add(checkbox3)
frame.Add(submitBtn)
rb1=Radio_button("Male",10,300)					#Adds radio button
rb1.Add_radio_button("Female ",10,350)
frame.Add(rb1)
textarea = Text_area(250,10,200,100," Click submit button")
password = Password_field(300,350)
textfield=Text_field(300,300)
lb=Static_text(3,10,80,20,"Choose")
lb2=Static_text(10,270,80,20,"Choose Gender")			#Choose the Gender
frame.Add(lb)
frame.Add(lb2)
textfield.Set_text("Enter Password")
textarea.Clear_area()						#Adds all the widgets
frame.Add(textarea)
frame.Add(password)
frame.Add(textfield)
frame.Display()						#Displays all the widgets

