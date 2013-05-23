#!/usr/bin/python
# Button and Text-Area
import sys
import wx
class WindowFrame(wx.Frame): #This is a window class named WindowFrame
	
	controller = None
	def __init__(self,id, title,width,height):# Constructor for the WindowFrame class
		global app    # A global App has been initialized
		app = wx.App()  # App starts
		wx.Frame.__init__(self, None, id, title, wx.DefaultPosition, wx.Size(width, height))  #Constructor for the Frame class is called
		self.panel = wx.Panel(self, -1) # A panel is initialized
	
	def center(self):# Using this function the WindowFrame is put at the center of the Screen
		self.Centre()	

	def show(self):# Makes the instance of the window visible
		global app
		self.Show(True)
		app.MainLoop()
				
		
	def add(self,widget,field=None): # This function adds widgets to the window considered
		WidgetName = type(widget)
	        if(WidgetName==TextArea or isinstance(widget,TextArea)):
			widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_MULTILINE)#Constructor of TextArea is called
		elif(WidgetName==Password or isinstance(widget,Password)):      
			widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_PASSWORD)#Constructor of Password is called
		elif(WidgetName==TextLine or isinstance(widget,TextLine)):      
			widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=0) #Constructor of TextLine is called
		elif(WidgetName==Slider or isinstance(widget,Slider)):
			widget.controller = wx.Slider(self.panel, -1, value = -1,minValue=widget.start,maxValue=widget.end,pos=widget.pos,size=widget.size)	
				#Constructor of Slider is called
		elif(WidgetName==SpinBox or isinstance(widget,SpinBox)):
			widget.controller = wx.SpinButton(self.panel, -1,  widget.pos, widget.size)#Constructor of SpinBox is called			
		elif(WidgetName==Button or isinstance(widget,Button)):
        		widget.controller = wx.Button(self.panel, -1, widget.title,  widget.position, widget.size)#Constructor of Button is called
          		if(widget.callBackMethod is not None):
                		widget.controller.Bind(wx.EVT_BUTTON,widget.callBackMethod,id = widget.controller.GetId())#Constructor of CheckBox is called
        	elif(WidgetName==CheckBox or isinstance(widget,CheckBox)):
          		widget.controller = wx.CheckBox(self.panel, -1, widget.title,  widget.position)#Constructor of Radio Group is called
        	elif(WidgetName==RadioGroup or isinstance(widget,RadioGroup)):
            		widget.controller = []
          		radio_controller = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            		widget.controller.append(radio_controller)
            		for i in range(1,len(widget.labels)):
                		radio_controller = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                		widget.controller.append(radio_controller)# All the radio buttons are added to a single group
                        if(widget.selected_index != None):
                		widget.controller[widget.selected_index].SetValue(True)
		elif(WidgetName==SelectList or isinstance(widget,SelectList)):
         		widget.controller = wx.ListCtrl(self.panel,-1,widget.position,widget.size, style=wx.LC_REPORT | wx.SUNKEN_BORDER)#Constructor of Select List is called
			widget.controller.Bind(wx.EVT_LIST_ITEM_ACTIVATED,widget.onConnect)#Bind the widget with onConnect function
			widget.controller.InsertColumn(0, 'Options',width=400)
			for i in widget.choices:
				index = widget.controller.InsertStringItem(sys.maxint,i[0])
				widget.controller.SetStringItem(index,0,i)

		elif(WidgetName==DropDownList or isinstance(widget,DropDownList)):#Constructor of Drop Down Box Value is called
         		widget.controller = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)
			widget.controller.Bind(wx.EVT_COMBOBOX,widget.onConnect)# Bind Drop Down Box With onConnect Function 
		elif(WidgetName==Label or isinstance(widget,Label)):
			widget.controller = wx.StaticText(self.panel,-1,widget.name,widget.position,widget.size)
		
class SelectList(wx.ListCtrl):# Defines a list
	controller = None
	callBackMethod = None
	choices = []		
        def __init__(self,choices,X,Y,width,height):# this function initializes all the variables
	
            self.choices = choices
	
            self.position = (X,Y)
	
            self.size = (width,height)

	def clickListener(self,method):# Assign an event associated function
	
		self.callBackMethod = method
	        return True
	def append(self,item):
		self.controller.Append(item)
	def clickListener(self,method):
     		if(self.controller == None):
        		self.callBackMethod = method
        	else:
			self.callBackMethod = method
	         	
	def onConnect(self,event):#Connected function
		if self.callBackMethod != None:
			self.callBackMethod(event.GetItem().GetText())				

	
class Password(wx.TextCtrl):# defines a password field
	controller = None
	def __init__(self,X,Y,width,height):# this function initializes all the variables
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text=""
	def setText(self,text):# set the text in the text region
		self.controller.text = text		
	def appendText(self,text):# append the text
		self.controller.text = self.controller.text + text
	def clearText():
		self.controller.text = ""	
	def getText(self):
		return self.controller.GetValue()


class TextArea(wx.TextCtrl):# defines a text area
	controller = None
	def __init__(self,string,X,Y,width,height):# this function initializes all the variables
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text = string
	def setText(self,text):# set the text in the text region
        	if(self.controller == None):
        	    self.text = text
        	else:
        	    self.controller.SetValue(text)
        	return True
	def appendText(self,text):# append the text
	        if(self.controller == None):
	            self.text = self.controller.GetValue() + text
	        else:
	            self.controller.AppendText(text)
	        return True              

	def clear(self):
		self.setText("")	
	def getText(self):
		return self.controller.GetValue()

	def AppendBefore(self,string1,string2):# append string2 just before string1  
		if string1== ",":
			n = self.controller.GetNumberOfLines()
			st=""	
			count =0
			for i in range(0,n):
				line = self.controller.GetLineText(i)
				buf=""	
				for i in line:
					if i==',' and count==0:
						count = count +1
						buf+=" "+string2 +"," 
					else:
						buf+=i	
				st = st +buf+"\n"
			self.setText(st)
		elif string1=="Yours sincerely,":
			n = self.controller.GetNumberOfLines()
			lineNo=0 	
			st1 =""
			st2 ="" 
			tag = 0
			for i in range(0,n):
				line = self.controller.GetLineText(i)
				if line == "Yours sincerely," :
					tag = 1
				else :	
					if tag== 0:
						st1 =st1 + line+"\n"
					elif tag==1:
						st2 =st2 +line+"\n"
			st1=st1+"\n"+string2+"\n"
			st1=st1+"\n"+string1+"\n"+st2+"\n"
			self.setText(st1) 
		
		elif string1=="Dear":
			n = self.controller.GetNumberOfLines()
			lineNo=0 	
			st1 =""
			tag = 0
			for i in range(0,n):
				line = self.controller.GetLineText(i)
				if len(line)>4 and line[0]=="D"  and line[1]=="e" and line[2]=="a" and line[3]=="r"  :
					st1 = st1+string2+"\n"
					st1 = st1+ line+"\n"
					#print"hiii"
					
				else :	
					st1 =st1 + line+"\n"
			self.setText(st1)
		
	

class TextLine(wx.TextCtrl):# Class for  text area
	controller = None
	def __init__(self,X,Y,width,height):#initializes all the variables
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text=""
	def setText(self,text):
		self.controller.text = text		
	def appendText(self,text):# append the text
		self.controller.text = self.controller.text + text
	def clear():# clears the TextLine
		self.controller.text = ""	
	def getText(self):# returns the text
		return self.controller.GetValue()
		

class Slider(wx.Slider):# class for Slider
	controller = None
	callBackMethod = None
	def __init__(self,start,end,X,Y,width,height):# initialize all the variables
		self.start=start
		self.end=end
        	self.pos = (X,Y)
		self.size = (width,height)
	def getValue(self):# returns the value of the slider
		if(self.controller == None):
			return ''
		else:	
	    		return self.controller.GetValue()


class Label(wx.StaticText):#Class for Static text
	controller =  None
	def __init__(self,name, X,Y, width,height):
		self.position = (X,Y)
       		self.size = (width,height)
		self.name = name

class SpinBox(wx.SpinButton):#Class for Spin Box
	controller = None
	callBackMethod = None
	def __init__(self,start,end,X,Y,width,height):# initialize the variables
	
		self.start=start
		self.end=end
        	self.pos = (X,Y)
        	self.size = (width,height)
    
    	def getValue(self):# returns the value for the spin box
		if(self.controller == None):
	       		return ''
		else:	
	    		return self.controller.GetValue()

class Button(wx.Button):# class for button
	controller = None
	callBackMethod = None	
	def __init__(self,string,X,Y,width,height):	# initialize the variables
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.title = string

	def clickListener(self,method):# add an event triggered function to the button
     		if(self.controller == None):
        		self.callBackMethod = method
        	else:
         		self.controller.Bind(wx.EVT_BUTTON, method)
       		return True

class CheckBox(wx.CheckBox):# Class for a Check Box
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):#initialize the variables
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setValue(self,value):# set the value for the check box
        if(self.controller == None):
            self.value = value
        else:
            self.controller.SetValue(value)

    def getValue(self):# returns value for  the check box 
        if(self.controller == None):
            return self.value
        else:
            return self.controller.IsChecked()

class RadioGroup(object):# Class for radio Group
	controller = None
   	selected_index = None
    
	def __init__(self,width,height):#initialise all the variables
	        self.labels = []
	        self.positions = []
	        self.size = wx.Size(width, height)

        def addRadioButton(self,label,X,Y):# add radio buttons to the group
	        self.labels.append(label)
	        self.positions.append((X,Y))
	        return True

	def getValue(self):# get current values of the radiobuttons in the group
        	for i in range(len(self.controller)):
        	    if(self.controller[i].GetValue()):
        	        return self.labels[i]
        	return None

    	def setButtonTrue(self,index):# function to set the true button
    	    if(self.controller == None):
    	        self.selected_index = index
    	    else:
    	        button_controller = self.controller[index]
    	        button_controller.SetValue(True)

		
class DropDownList(wx.ComboBox):# A drop Down Box
	controller = None
	callBackMethod =None		
    	def __init__(self,choices,X,Y,width,height,value=""):# initialise all the variables
        	self.choices = choices
        	self.position = (X,Y)
        	self.size = (width,-1)
        	self.value = value

    	def getValue(self): # returns the value of the dropDownlist 
        	if(self.controller == None):
                	return self.value
            	else:
                	return self.controller.GetValue()
    	def clickListener(self,method):# add an event associated function
     		if(self.controller == None):
        		self.callBackMethod = method
        	else:
			self.callBackMethod = method
	         	
	def onConnect(self,event):# action associated with connected function
		if self.callBackMethod != None:
			self.callBackMethod(self.controller.GetValue())				

	
	
