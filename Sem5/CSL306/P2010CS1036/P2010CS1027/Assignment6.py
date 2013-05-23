#!/usr/bin/python
    
import wx
from wxPython.wx import *
import cStringIO
import re
import wx.calendar as cal
from wx.lib import analogclock as ac
from wx.lib.analogclock import *
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
def CreateImage(Path):
	return Path

class CommonAPI(wx.Frame):
	def __init__(self, title, Length, Breadth):
            wx.Frame.__init__(self, None, -1, title, size=(Length, Breadth))

	def CreateTextArea(self,xPos,yPos,Title):
		self.ta = wx.TextCtrl(self, value= "Type Something here....",pos=(xPos,yPos), size=(100,100), style=wx.TE_MULTILINE)

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

        def CreateSpinButton(self,xPos,yPos):
      		self.sc = wx.SpinCtrl(self, -1, '',  (xPos,yPos), (60, -1))
                self.sc.SetRange(-459, 1000)
                self.sc.SetValue(0)

	def CreateTextBox(self,xPos,yPos,passwd = False):
		#com['count'] += 1
		if passwd == False :
			self.tb=wx.TextCtrl(self,100,pos=(xPos,yPos))	
			#lbl_username = wx.StaticText(self, -1, Title ,pos=(xPos,yPos-15),name = Title)
			
		else:
			self.tb=wx.TextCtrl(self,100,pos=(xPos,yPos),style = wxTE_PASSWORD)
			#lbl_username = wx.StaticText(self, -1, Title ,pos=(xPos,yPos-15),name = Title)
	        return self.tb	

	def CreateLabel(self, xPos, yPos, Title):
			lbl_username = wx.StaticText(self, -1, Title ,pos=(xPos,yPos-15),name = Title)


	def CreateTextArea(self,xPos,yPos):
		self.ta = wx.TextCtrl(self, value= "Type Something here....",pos=(xPos,yPos), size=(100,100), style=wx.TE_MULTILINE)

	def CreateList(self,xPos,yPos,List):
		
		wx.ComboBox(self, -1, value= "TableTennis",pos=(xPos, yPos), size=(130, 30), choices=List, style=wx.CB_READONLY)

	def CreateToggleButton(self,xPos,yPos,Title):
		#wx.Colour(0,0,0) = wx.Colour(0, 0, 0)
		wx.ToggleButton(self, 1, 'me..ToggleButton', (xPos, yPos))
		#wx.ToggleButton(self, 2, 'green', (20, 60))
        	#wx.ToggleButton(self, 3, 'blue', (20, 100))

	
	def CreateCalender(self,xPos,yPos):
           vbox = wx.BoxSizer(wx.VERTICAL)
   
           calend = cal.CalendarCtrl(self, -1, wx.DateTime_Now(),
           style = cal.CAL_SHOW_HOLIDAYS|cal.CAL_SEQUENTIAL_MONTH_SELECTION)
           vbox.Add(calend, 0, wx.EXPAND | wx.ALL, 200)
           #self.Bind(cal.EVT_CALENDAR, self.OnCalSelected, id=calend.GetId())
  
           vbox.Add((-1, 200))
   
  
	def OnQuit(self, event):
           self.Destroy()

	def CreateSlider(self,xPos,yPos):
	   vbox = wx.BoxSizer(wx.VERTICAL)
           hbox = wx.BoxSizer(wx.HORIZONTAL)
           self.sld = wx.Slider(self, -1, 450, 150, 500, (xPos,yPos), (xPos,yPos),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
           
           vbox.Add(self.sld, 1, wx.ALIGN_CENTRE)
           
           vbox.Add(hbox, 0, wx.ALIGN_CENTRE | wx.ALL, 20)
           self.SetSizer(vbox)
	

	def OnOk(self, event):
        	   if self.count >= 50:
        		       return
        	   self.timer.Start(100)
        	   #self.text.SetLabel('Task in Progress')
   
	def OnStop(self, event):
           if self.count == 0 or self.count >= 50 or not self.timer.IsRunning():
        	       return
           self.timer.Stop()
           #self.text.SetLabel('Task Interrupted')
           wx.Bell()
   
	def OnTimer(self, event):
        	   self.count = self.count +1
        	   self.gauge.SetValue(self.count)
        	   if self.count == 50:
        	       self.timer.Stop()
        	       self.text.SetLabel('Task Completed')

	def AddImage(self,xPos,yPos,Path):
		data = open(Path, "rb").read()
		stream = cStringIO.StringIO(data)
		bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
		wx.StaticBitmap(self, -1, bmp, (xPos, yPos))

	def CreateScrolledBar(self,xPos,yPos):
		self.scroll = wx.ScrolledWindow(self, -1)
       		self.scroll.SetScrollbars(1, 1, 600, 400)
        	self.button = wx.Button(self.scroll, -1, "Scroll Me", pos=(50, 20))
        	self.Bind(wx.EVT_BUTTON,  self.OnClickTop, self.button)
        	self.button2 = wx.Button(self.scroll, -1, "Scroll Back", pos=(500, 350))
        	self.Bind(wx.EVT_BUTTON, self.OnClickBottom, self.button2)
	
	def CreateClock(self,xPos,yPos):

		clock = AnalogClockWindow(self)
		clock.SetBackgroundColour("yellow")
		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(clock, 2,wx.SHAPED,30)
		#box.Add(clock, 1, wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL|wx.SHAPED, 10)
		self.SetAutoLayout(True)
		self.SetSizer(box)
		self.Layout()
		#self.ShowModal()
		#self.Destroy()

	def OnPopupDisplay(self, evt):
	        self.popup.Show(True)
	        evt.Skip()

	def OnPopupHide(self, evt):
	        self.popup.Show(False)
	        evt.Skip()


	def CreateDialogBox(self,Text):
		 #txton = wx.TextCtrl(self, -1, pos=(20,20), size=(100,20))
        	 txton=wx.Button(self,1,"Click on this for pop up menu to appear",(515,15))
       		 
       
       		 self.popup = wx.PopupWindow(self, wx.RAISED_BORDER)

       		 self.popup.SetPosition((100,120))
       		 self.popup.SetSize((100,200))
       		 button = wx.Button(self.popup, -1, "Hide me!", pos=(10,40))
       		 button2 = wx.Button(self.popup, -1, Text, pos=(10,80))
       		 txton.Bind(wx.EVT_BUTTON, self.OnPopupDisplay)
       		 txton.Bind(wx.EVT_BUTTON, self.OnPopupHide)
       		 self.Bind(wx.EVT_BUTTON, self.OnPopupHide, button)

	def CreateProgressBar(self,xPos,yPos):
		wx.StaticText(self, -1, "Showing Progress Bar" ,pos=(1100,15),name = "Progress Bar")

		self.timer = wx.Timer(self, 1)
  	        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
		self.count = 0
		vbox = wx.BoxSizer(wx.VERTICAL)
  	        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
          	hbox2 = wx.BoxSizer(wx.HORIZONTAL)
           	hbox3 = wx.BoxSizer(wx.HORIZONTAL)
   
           	self.gauge = wx.Gauge(self, -1, 50, size=(250, 25))
          	self.btn1 = wx.Button(self, wx.ID_OK)
         	self.btn2 = wx.Button(self, wx.ID_STOP)
           	#self.text = wx.StaticText(self, -1, 'Task to be done')
   
           	self.Bind(wx.EVT_BUTTON, self.OnOk, self.btn1)
           	self.Bind(wx.EVT_BUTTON, self.OnStop, self.btn2)
   
           	hbox1.Add(self.gauge, 1, wx.ALIGN_CENTRE)
           	hbox2.Add(self.btn1, 1, wx.RIGHT, 10)
           	hbox2.Add(self.btn2, 1)
           	#hbox3.Add(self.text, 1)
           	vbox.Add((0, 50), 0)
           	vbox.Add(hbox1, 0, wx.ALIGN_RIGHT)
           	vbox.Add((0, 30), 0)
           	vbox.Add(hbox2, 1, wx.ALIGN_RIGHT)
           	#vbox.Add(hbox3, 1, wx.ALIGN_RIGHT)
		self.SetSizer(vbox)
          	self.Centre()


	

	def OnClickTop(self, event):
	        self.scroll.Scroll(600, 400)
        
	def OnClickBottom(self, event):
	        self.scroll.Scroll(1, 1)
		
		
	   
class aapp(wx.App):
        def OnInit(self):
        	 frame = CommonAPI("Assignment 6",350,350)
		 items=['Cricket','Football','BasketBall','BadMinton']		 
		 a=frame.CreateTextBox(515,185)
		 b=frame.CreateTextBox(515,235,"true")
		 c=frame.CreateTextBox(515,285,"true")
		 d=frame.CreateTextBox(515,335,"true")
		 frame.CreateLabel(515,185,"Username")
		 frame.CreateLabel(515,235,"Old Password")
		 frame.CreateLabel(515,285,"New Password")
		 frame.CreateLabel(515,335,"New Password(Repeat)")
		
		 button=frame.CreateButton(515,385,"Submit")
		 button.Bind(wx.EVT_BUTTON, lambda event, arg = [a,b,c,d] : GetValues(event, arg))
		 frame.CreateToggleButton(515,435,"Toggle Button")
		 #frame.CreateCalender(195,190)
		 frame.CreateSlider(515,35)
		 x = CreateImage("logo.jpg")
		 frame.AddImage(15,295,x)	
		 frame.CreateTextArea(515,535)
		 frame.CreateSpinButton(515,485);	 
		 #frame.CreateScrolledBar(15,555)
                 frame.CreateClock(139,15)
		 frame.CreateDialogBox("hi everyone")
		 frame.CreateProgressBar(15,11)
		 frame.Show(True)
         	 
	         frame.Centre()
		 
         	 return True


if __name__ =='__main__':
	app = aapp(0)
	app.MainLoop()
