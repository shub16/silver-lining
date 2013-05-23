import pygtk
pygtk.require('2.0')
import gtk


class Dashboard(object):
	parent=None
	
	def __init__(self, title, width, height):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", gtk.main_quit)
		self.window.set_title(title)
		self.window.set_size_request(width, height)
		self.fix = gtk.Fixed()
		self.window.add(self.fix)
		self.fix.show()
	
	def Add(self, widget):
		widget_type = type(widget)
		if widget_type == gtk.Entry:
			self.fix.put(widget.entry, widget.posX, widget.posY )
			self.set_size_request(Length, Breadth)
			widget.entry.show()

		elif widget_type == Create_button:
			widget.controller = gtk.Button(widget.label)
			widget.controller.set_size_request(widget.height,widget.width)
			self.fix.put(widget.controller, widget.posX, widget.posY)
 	                widget.controller.show()
		
		elif (widget_type == Check_box):
			self.fix.put(widget.button3, widget.posX, widget.posY )
			widget.button3.show()
			
		elif (widget_type==Drop_list):
			widget.controller = gtk.OptionMenu()
			widget.controller.set_size_request(widget.length,widget.width)
			menu = gtk.Menu()
			for name in widget.values:
				item = gtk.MenuItem(name)
				item.show()
				menu.append(item)
			widget.controller.set_menu(menu)
			self.fix.put(widget.controller,widget.posX, widget.posY)
			widget.controller.show()
			
		elif widget_type == Radio_button:
			widget.controller = []
			radio_controller = gtk.RadioButton(None, widget.names[0])
			self.fix.put(radio_controller,widget.postnX[0], widget.postnY[0])
			radio_controller.show()
			widget.controller.append(radio_controller)
			for i in range(1,len(widget.track)):
				radio_controller = gtk.RadioButton(widget.controller[0], widget.names[i])
				self.fix.put(radio_controller,widget.postnX[i], widget.postnY[i])
				radio_controller.show()
				widget.controller.append(radio_controller)

		elif widget_type == Static_text:
			self.fix.put(widget.mess, widget.posX, widget.posY )
			widget.mess.show()
			
		elif widget_type == Text_field:
			self.fix.put(widget.entry, widget.posX, widget.posY )
			widget.entry.show()
			
		elif (widget_type == Text_area):
			widget.controller = gtk.TextView(widget.buffer)
			widget.controller.set_size_request(widget.width,widget.height)
			self.fix.put(widget.controller, widget.postnX, widget.postnY)            
			widget.controller.show()
			if(widget.callbackMethod != None ):
				widget.controller.connect('clicked',widget.callbackMethod)
 
		elif widget_type == Spin_list:
			widget.controller = gtk.SpinButton()
			widget.controller.set_range(widget.minimum,widget.maximum)
			widget.controller.set_increments(1, 1)
			widget.controller.set_size_request(widget.length,widget.width)
			self.fix.put(widget.controller, widget.posX, widget.posY)
			widget.controller.show()

		elif widget_type == Password_field:
			self.fix.put(widget.entry, widget.posX, widget.posY )
			widget.entry.show()
            
	def Display(self):
		self.window.show()
		gtk.main()
		return
		
class Create_button(object):
	controller=None
	callbackMethod=None
	
	def __init__(self, posX, posY, title, length, breadth):   
		self.label=title
#		self.button2 = gtk.Button(self.label)
#		self.button2.set_size_request(length, breadth)
		self.posX = posX
		self.posY = posY
		self.width = breadth
		self.height = length
					   		
	def Click_listener(self, method):
		if(self.controller == None):
			self.callbackMethod = method
		else:
			self.controller.connect("clicked", method)
		return True
		
class Check_box(gtk.CheckButton):
	def __init__(self, posX, posY, title,length=50,breadth=100):   
		self.button3 = gtk.CheckButton(label = title)
		self.button3.set_size_request(length, breadth)
		self.button3.set_active(True)
		self.posX = posX
		self.posY = posY
					   		
	def Click_listener(self, method, *args):
		self.button3.connect("toggled", method, self.button3, *args)

	def ismarked(self, widget):
		val = widget.button3.get_active()
		if val == True:
			return True
		else:
			return False
	
	def setmarked(self, widget):
		widget.button3.set_active(True)
		
class Text_field(gtk.Entry):
	def __init__(self, posX, posY, text = "", length = 250, breadth = 25):   
		self.entry = gtk.Entry()
		self.posX = posX
		self.posY = posY
		self.entry.set_text(text)
		self.entry.set_size_request(length, breadth)
	
	def Clear_field(self):
		 self.entry.set_text("")

	def Set_text(self,text):									# Funtion to set text in the textbox
		self.entry.set_text(text)

	def Get_text(self):
		return self.entry.get_text()
		
class Static_text(gtk.Label):
	def __init__(self, posX, posY, length = 150, breadth = 30, text= ""):
		self.mess = gtk.Label(text)
		self.mess.set_size_request(length,breadth)
		self.posX = posX
		self.posY = posY
		self.mess.set_text(text)
		
class Spin_list(gtk.SpinButton):
	controller=None
	callback= None
	def __init__(self, posX, posY, length, breadth, minimum = 0, maximum = 100):
		self.posX = posX
		self.posY = posY
		self.width = breadth
		self.length = length
		self.minimum= minimum
		self.maximum = maximum
		adjustment = gtk.Adjustment(0, minimum, maximum, 1, 10, 0)
		self.spinbutton = gtk.SpinButton(adjustment)
		self.spinbutton.set_increments(1, 1)
		self.spinbutton.get_value_as_int()
		
	def Get_value(self):
		return self.spinbutton.get_value_as_int()


class Text_area(object):
	controller = None
	callbackMethod = None
	buffer = gtk.TextBuffer()
	
	def __init__(self, posX, posY, length, breadth, text=""):
		self.title = text
		self.postnX = posX
		self.postnY = posY
		self.width = length
		self.height = breadth
        
	def Set_Text(self,text):
		self.buffer.set_text(text)
		return True
	
	def Get_text(self,text):
		return self.text
		
	def Append_Text(self,text):
		self.buffer.insert(self.buffer.get_end_iter(),text)
		return True              
		
	def Clear_area(self):
		self.buffer.set_text("")
		return True
	
class Drop_list(object):
	controller = None
	def __init__(self,posX,posY,name1, values,length,breadth):
		self.name = name1
		self.posX = posX
		self.posY = posY
		self.width = breadth
		self.length = length
		temp = values
		self.values = temp
	
	def Get_value(self):
		if(self.controller == None):
			return self.value
		else:
			IntValue = self.controller.get_history()
			if(IntValue < 0):
				return None
			return self.name1[IntValue]
			
class Password_field(gtk.Entry):
	def __init__(self, posX, posY, text = "", length = 250, breadth = 25):   
		self.entry = gtk.Entry()
		self.posX = posX
		self.posY = posY
		self.entry.set_text(text)
		self.entry.set_size_request(length, breadth)
		self.entry.set_visibility(False)
	
	def Clear_field(self):
		 self.entry.set_text("")

	def Set_text(self,text):									# Funtion to set text in the textbox
		self.entry.set_text(text)

	def Get_text(self):
		return self.entry.get_text()
		


class Radio_button(object):
	controller=  None
	def __init__(self,label1, posX, posY):
		self.track = []	
		self.names = []
		self.postnX = []	
		self.postnY = []
		self.names.append(label1)
		self.choose1 = gtk.RadioButton(None, label1)
		self.track.append(self.choose1)
		self.posX = posX
		self.posY = posY
		self.postnX.append(posX)
		self.postnY.append(posY)

	def Add_radio_button(self, label, posX, posY):
		self.label2 = gtk.RadioButton(None, label)
		self.posX = posX
		self.posY = posY
		self.names.append(label)
		self.track.append(self.label2)
		self.postnX.append(posX)
		self.postnY.append(posY)
		self.choose1.set_group(self.label2)
	def Get_selected(self):
		k = 0
		for i in self.track:
			if(i.get_active() == True):
				return self.names[k]
			k = k + 1




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
OuterPanel.Display()
gtk.main()
#if __name__ == '__main__':
#   Gtk.main()
