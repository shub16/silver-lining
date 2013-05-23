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

if __name__ == '__main__':
    OuterPanel.Display()
