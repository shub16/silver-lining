import wx
import sys
''' Frame-widget class'''
class Dashboard(wx.Frame):
    def __init__(self, title, length,breadth):							# Contructor of the Dashboard class
	self.app = wx.App(False)				
	wx.Frame.__init__(self, None, -1, title)						# Initializing a Dashboard
	self.SetSize(wx.Size(length,breadth))								# Setting size of the Dashboard
	self.panel = wx.Panel(self, -1)								# Initializing a panel

    def Display(self):
	self.Centre()
	self.Show()
	self.app.MainLoop()
 
    def Add(self,widget):								# Function to add widgets in the frame
	if(isinstance(widget,Create_button)):								# To add a button
		widget.controller = wx.Button(self.panel, -1, widget.label,  widget.pos, widget.size, widget.style)
	elif(isinstance(widget,Text_field)):							# To add a Text field
		widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.pos, widget.size, widget.style)
	elif(isinstance(widget,Password_field)):							# To add a Password field
		widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.pos, widget.size, widget.style)
	elif(isinstance(widget,Text_area)):							# To add a Text area
		widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.pos, widget.size, widget.style)
	elif(isinstance(widget,Drop_list)):							# To add a Drop down list
		widget.controller = wx.ComboBox(self.panel, -1, widget.value,widget.pos,widget.size,widget.choices,widget.style)
	elif(isinstance(widget,Static_text)):							# To add a Static Text
		widget.controller = wx.StaticText(self.panel, -1, widget.label, widget.pos)
	elif(isinstance(widget,Spin_list)):							# to add a spin list
		widget.controller = wx.SpinCtrl(self.panel, id = -1, value = widget.value,  pos = widget.pos,size = widget.size, min=widget.minimum, max=widget.maximum)
	elif(isinstance(widget,Radio_button)):						# To add a radio button set
		widget.controller = []
		radio_controller = wx.RadioButton(self.panel, -1, widget.labels[0], pos = widget.pos[0], style =widget.style)
		widget.controller.append(radio_controller)
		for i in range(1,len(widget.labels)):
			radio_controller = wx.RadioButton(self.panel, -1, widget.labels[i], pos = widget.pos[i])   # To inidividual radio buttons
			widget.controller.append(radio_controller)
		widget.controller[widget.default_pos].SetValue(True)
 	elif(isinstance(widget,Check_box)):							# To add a check box 
		widget.controller = wx.CheckBox(self.panel, -1, widget.label,  widget.pos)
		


''' Button - widget class '''

class Create_button(wx.Button):
    controller = None
    def __init__(self, posX, posY, title = "", length = 100, breadth = 30):            	# Constructor for button class
	self.label = title								    	# Assigning name to the button	
	self.pos = (posX,posY)								     	# Setting position of the button
	self.size = wx.Size(length, breadth)								# Setting size of the button
	self.style = wx.BU_EXACTFIT									# Setting the button style
    def Click_listener(self, method):	
	if( self.controller != None):							# Function to handle button click
		self.controller.Bind(wx.EVT_BUTTON, method)

''' Text-Field widget class'''

class Text_field(wx.TextCtrl):
    def __init__(self, posX, posY, text = "", length = 250, breadth = 25):				# Constructor for text field class
	self.text = text									# Setting text in the text field
	self.pos = (posX, posY)									# Setting position of the text field
	self.size = (length , breadth)									# Setting size of the text field
	self.style = wx.DEFAULT									# Setting the style of the text field
    def Clear_field(self):										# Funtion to clear the contents in text field
	self.controller.Clear()
    def Set_text(self,text):									# Funtion to set text in the text field
	self.controller.SetValue(text)
    def Get_text(self):								# Function to get complete text from the text field
	return self.controller.GetString(0,self.controller.GetLastPosition()) 

'''Password-Field widget class'''

class Password_field(wx.TextCtrl):
    def __init__(self, posX, posY, text = "",length = 250, breadth = 25):				# Constructor for password field class
	self.text = text									# Setting text in the password field
	self.pos = (posX, posY)									# Setting position of the password field
	self.size = (length , breadth)									# Setting size of the password field
	self.style = wx.TE_PASSWORD									# Setting the style of the password field
    def Clear_field(self):									# Funtion to clear the contents in password field
	self.controller.Clear()
    def Set_text(self,text):									# Funtion to set text in the password field
	self.controller.SetValue(text)
    def Get_text(self):								# Function to get complete text from the password field
	return self.controller.GetString(0,self.controller.GetLastPosition()) 

''' Text-area widget class'''

class Text_area(wx.TextCtrl):
    def __init__(self, posX, posY, length = 300, breadth = 200, text = ""):				# Constructor for text area class
	self.text = text									# Setting text in the text area
	self.pos = (posX,posY)									# Setting position of the text area
	self.size = (length,breadth)									# Setting size of the text area
	self.style = wx.TE_MULTILINE									# Setting the style of the text area
    def Clear_area(self):										# Funtion to clear the contents in text area
	self.controller.Clear()
    def Set_text(self,text):									# Funtion to set text in the text area
	self.controller.SetValue(text)
    def Append_text(self,text):									# Function to append text in the text area
	self.controller.AppendText(text)
    def Get_text(self):								# Function to get complete text from the text area
	return self.controller.GetString(0,self.controller.GetLastPosition())

''' Drop-list class '''
class Drop_list(wx.ComboBox):
    controller = None	
    def __init__(self, posX , posY, name1, values, length = 100 , breadth= 27):		# Constructor of the Drop-list class
	self.pos = (posX, posY)									# Setting position of the drop down list
	self.choices = values								# Setting the list in the drop down list
	self.style = wx.CB_READONLY								# Setting the style of the drop down list
	self.size = (length , breadth)								# Setting the size of the drop down list
	self.value = name1									# Setting the default value in the drop down list
    def Get_value(self):									# Function to get selected value in drop down list
	if (self.controller == None):
		return self.value
	else:
		text = self.controller.GetValue()
		return text

''' Static - text class '''

class Static_text(wx.StaticText):
    controller = None					
    def __init__(self, posX, posY,length =150, breadth=30, text = ""):				# Constructor of the Static-text class
	self.pos = (posX,posY)									# Setting the position of the static-text
	self.label = text									# Setting the text in static-text 
    def Set_value(self, text):
	if( self.controller == None):
		self.label = text
	else:
		self.controller.SetLabel(text)


''' Radio - Button Group Class '''

class Radio_button(wx.RadioButton):
    default_pos = 0										
    controller = None
    def __init__(self, label, posX, posY):							# Constructor of the Radio-Button group class
	self.labels = []									# Initializing the list of labels
	self.pos = []										# Initializing the list of positions
	self.style = wx.RB_GROUP									# Setting the style of the radio buttons
	self.labels.append(label)
	self.pos.append((posX,posY))		

    def Add_radio_button(self, label, posX, posY):							# Function to add radio buttons in the group
	self.labels.append(label)
	self.pos.append((posX,posY))		
        
    def Get_selected(self):									# Function to return the selected value
	for i in range(len(self.controller)):
		if(self.controller[i].GetValue()):
			return self.labels[i]
	

''' Check - box class '''

class Check_box(wx.CheckBox):								
    controller = None
    def __init__(self,posX,posY, title = "", length = 20, breadth = 20):			# Constructor of checkbox class
	self.label = title									# Setting label
	self.pos = (posX, posY)									# Setting position 

    def Set_checked(self, value=True):								# Function to set a check box checked or unchecked
	if(self.controller == None):
		self.value = value
	else:
		self.controller.SetValue(value)

    def Is_checked(self):									#Function to Check if a check box is checked
        if(self.controller == None):
		return self.value
	else:
		return self.controller.IsChecked()


''' Spin-Box Class'''

class Spin_list(wx.SpinCtrl):
    controller = None
    def __init__(self, posX , posY, length = 100, breadth = 25 , minimum = 0, maximum = 100):	# Constructor of Spin_list class		
	self.pos = (posX, posY)									# Setting position
	self.size = (length , breadth)								# Setting size		
	self.value = ""										# Setting Value
	self.minimum = minimum									# Setting minimum limit
	self.maximum = maximum									# Setting maximum limit
    def Get_value(self):									# Function to get the selected value
	if (self.controller == None):
		return self.value
	else:
		return self.controller.GetValue()

if __name__=='__main__':
	name_field1 = ""
	phoneno_field1 = ""
	rbgender1 = ""
	spin_day1 = 0
	drop_month1 = ""
	spin_year1 = 0
	def OnClickSave(self):								
		name_field1 = name_field.Get_text()
		name_field.Clear_field()	
		phoneno_field1 = phoneno_field.Get_text() 
		phoneno_field.Clear_field()
		rbgender1 = rbgender.Get_selected()
		spin_day1 = spin_day.Get_value()
		drop_month1 = drop_month.Get_value()
		spin_year1 = spin_year.Get_value()
		
		

	byname_field1 = ""
	byphoneno_field1 = ""
	def OnClickSearch():
		if( check_byname.Is_checked()):
			byname_field1 = byname_field.Get_text() 
		if( check_byphoneno.Is_checked()):
			byphoneno_field1 = byphoneno_field.Get_text() 
		byname_field.Clear_field()
		check_byname.Set_checked(False)
		byphoneno_field.Clear_field()
		check_byphoneno.Set_checked(False)


	send_name_field1 = ""
	send_message_area1 = ""
	def OnClickSend():
		send_name_field1 = send_name_field.Get_text()
		send_name_field.Clear_field()
		send_message_area1 = send_message_area.Get_text()
		send_message_area.Clear_area()


	def OnClickClear():
		messages_area.Clear_area()


	window = Dashboard('Application', 1000, 670)	

	a_contacts = Static_text(25, 25, text = "Add Contacts ---> ")			# Creating static text1
	window.Add(a_contacts)
	name = Static_text(25, 65, text = "Name")
	window.Add(name)

	phoneno = Static_text(25, 105, text = "Phone No")
	window.Add(phoneno)

	gender = Static_text( 25, 150, text = "Gender")
	window.Add(gender)

	dob = Static_text(25, 195, text = "Date of Birth")
	window.Add(dob)

	name_field = Text_field( 130, 60, length = 270)
	window.Add(name_field)
	
	phoneno_field = Text_field(130, 100, length = 270)
	window.Add(phoneno_field)

	rbgender = Radio_button("Male",130, 150)					# Creating a Radio Button Set1			
	rbgender.Add_radio_button("Female", 210, 150)
	window.Add(rbgender)

	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']			 # List of entries in combo-box
	drop_month = Drop_list(130, 190, "January", months, 125, 25)	# Creating a Combo box
	window.Add(drop_month)

	spin_day = Spin_list(265, 190, 50, 25, 1, 31)
	window.Add(spin_day)

	spin_year = Spin_list(325, 190, 75, 25,1950,2012)
	window.Add(spin_year)

	save_btn = Create_button(170, 250, "Save", 85, 25)						# Creating Submit Button
	window.Add(save_btn)								# Adding it to frame1
	save_btn.Click_listener(OnClickSave)

	messages = Static_text(25, 300, text = "Messages Recieved --->")
	window.Add(messages)

	messages_area = Text_area(25, 330, 375, 250)
	window.Add(messages_area)

	clear_btn = Create_button(170, 600, "Clear", 85, 25)						# Creating Submit Button
	window.Add(clear_btn)								# Adding it to frame1
	clear_btn.Click_listener(OnClickClear)


	s_contacts = Static_text(500, 25, text = "Search Contacts ---> ")			# Creating static text1
	window.Add(s_contacts)

	byname = Static_text(500, 65, text = "By Name")
	window.Add(byname)

	byphoneno = Static_text(500, 105, text = "By Phone No")
	window.Add(byphoneno)
	
	select = Static_text(890, 25, text = "Select")
	window.Add(select)

	byname_field = Text_field( 605, 60)
	window.Add(byname_field)
	
	byphoneno_field = Text_field(605, 100)
	window.Add(byphoneno_field)

	check_byname = Check_box(900, 60, "", 20, 20)		# Adding entries
	window.Add(check_byname)								# Adding it to frame1		

	check_byphoneno = Check_box(900, 100, "" , 20, 20)		# Adding entries
	window.Add(check_byphoneno)								# Adding it to frame1		

	search_btn = Create_button(690, 160, "Search", 85, 25)						# Creating Submit Button
	window.Add(search_btn)								# Adding it to frame1
	search_btn.Click_listener(OnClickSearch)

	results = Static_text(500, 200, text = "Results --->")
	window.Add(results)

	results_area = Text_area(500, 230, 450, 125)
	window.Add(results_area)

	message = Static_text(500, 370, text = "Send Message --->")
	window.Add(message)

	send_name = Static_text(500, 410, text = "Name")
	window.Add(send_name)

	send_message = Static_text(500, 450, text = "Message")
	window.Add(send_message)

	send_name_field = Text_field( 605, 405, length = 270)
	window.Add(send_name_field)

	send_message_area = Text_area( 605, 445, 270, 140)
	window.Add(send_message_area)

	send_btn = Create_button(690, 600, "Send", 85, 25)						# Creating Submit Button
	window.Add(send_btn)								# Adding it to frame1
	send_btn.Click_listener(OnClickSend)


	window.Display()	


