#!/usr/bin/python
    
import wx
from wxPython.wx import *
import re

def Validate(Values):
	#Checking if all fields are filled
	        for value in Values:
			if not value:
				print "Some fields are empty....Please fill up them"
				return
			else:
				continue
		if not Values[2] or not Values[3]:
			print "Fields are Empty"
					
		elif len(Values[2]) < 6 :
			print "Password is too short. Please use atleast 6 characters"		
		#Checking if the paswords match
		elif Values[2] != Values[3]:
			print "Passwords Do not Match"
		
		elif ((re.search("[A-Za-z]+", Values[2]) is None) or (re.search("[0-9]+", Values[2]) is None)) or not(str(Values[2]).isalnum()): 
			print "Passwords should contain both alpha-numeric characters"
		
		else:
			print "Passwords changed "

def GetValues( Event, TextBoxes):
		print "Hello"
		Values = []
		for item in TextBoxes:
			Values.append(item.GetValue())
		Validate(Values)




class CommonAPI(wx.Frame):
	def __init__(self, title, Length, Breadth):
            wx.Frame.__init__(self, None, -1, title, size=(Length, Breadth))

	
	def CreateButton(self,xPos,yPos,Title):
		button=wx.Button(self,1,Title,(xPos,yPos))
		#self.Bind( wx.EVT_BUTTON, self.OnButton_FrameHandler, button )
		return button		
		#self.Bind(wx.EVT_BUTTON, self.Clicked)
		#print "hama"	
		#self.b.Bind(wx.EVT_BUTTON, self.OnButton1Button,id=2)
	
	def CreateRadioButton(self,xPos,yPos,Title):
		self.rb=wx.RadioButton(self,100,Title,(xPos,yPos))

	def CreateCheckBox(self,xPos,yPos,Title):
		self.rb=wx.CheckBox(self,100,Title,(xPos,yPos))

      #def CreateTextBox(self,xPos,yPos,Title):
      #	self.tb=wx.TextCtrl(self,100,Title,(xPos,yPos))	

	def CreateTextBox(self,xPos,yPos,Password = "false"):
		#com['count'] += 1
		if Password == "false" :
			self.tb=wx.TextCtrl(self,100,pos=(xPos,yPos))	
			#lbl_username = wx.StaticText(self, -1, Title ,pos=(xPos,yPos-15),name = Title)
			
		else:
			self.tb=wx.TextCtrl(self,100,pos=(xPos,yPos),style = wxTE_PASSWORD)
			#lbl_username = wx.StaticText(self, -1, Title ,pos=(xPos,yPos-15),name = Title)
	        return self.tb	
	def CreateLabel(self, xPos, yPos, Title):
			lbl_username = wx.StaticText(self, -1, Title ,pos=(xPos,yPos-15),name = Title)

	def CreateTextArea(self,xPos,yPos,Title):
		self.ta = wx.TextCtrl(self, value= "Type Something here....",pos=(xPos,yPos), size=(100,100), style=wx.TE_MULTILINE)

	def CreateList(self,xPos,yPos,List):
		
		wx.ComboBox(self, -1, value= "TableTennis",pos=(xPos, yPos), size=(130, 30), choices=List, style=wx.CB_READONLY)
		

class aapp(wx.App):
        def OnInit(self):
        	 frame = CommonAPI("Assignment 5",350,350)
		 a=frame.CreateTextBox(15,35)
		 b=frame.CreateTextBox(15,85,"true")
		 c=frame.CreateTextBox(15,135,"true")
		 d=frame.CreateTextBox(15,185,"true")
		 frame.CreateLabel(15,35,"Username")
		 frame.CreateLabel(15,85,"Old Password")
		 frame.CreateLabel(15,135,"New Password")
		 frame.CreateLabel(15,185,"New Password(Repeat)")
		 button=frame.CreateButton(15,230,"Submit")
		 #button.Bind(wx.EVT_BUTTON, buttonClick)
		 #s,t = how(frame.GetValues,[c,d])
		 button.Bind(wx.EVT_BUTTON, lambda event, arg = [a,b,c,d] : GetValues(event, arg))
		 #button.callback("clicked",frame.GetValues,[a,b,c,d])	
		 frame.Show(True)
         	 
	         frame.Centre()
		 #print first_pass   	
         	 return True


if __name__ =='__main__':
	app = aapp(0)
	app.MainLoop()
