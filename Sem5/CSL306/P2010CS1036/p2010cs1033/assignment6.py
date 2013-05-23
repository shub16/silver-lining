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
			widget.controller.set_size_request(widget.width,widget.height)
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
submitBtn = Create_button(130,170,"Submit",30,120)		#Creates a submit button
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
