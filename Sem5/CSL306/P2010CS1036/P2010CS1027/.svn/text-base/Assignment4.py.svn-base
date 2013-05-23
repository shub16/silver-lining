#!/usr/bin/python
    
import wx
from wxPython.wx import *


class CommonAPI(wx.Frame):
      def __init__(self, title, Length, Breadth):
            wx.Frame.__init__(self, None, -1, title, size=(Length, Breadth))

      def CreateButton(self,xPos,yPos,Title):
		self.b=wx.Button(self,1,Title,(xPos,yPos))
		
      def CreateRadioButton(self,xPos,yPos,Title):
		self.rb=wx.RadioButton(self,100,Title,(xPos,yPos))

      def CreateCheckBox(self,xPos,yPos,Title):
		self.rb=wx.CheckBox(self,100,Title,(xPos,yPos))

      def CreateTextBox(self,xPos,yPos):
		self.tb=wx.TextCtrl(self,100,pos=(xPos,yPos))	

      def CreateList(self,xPos,yPos,List):
		wx.ComboBox(self, -1, value= "TableTennis",pos=(xPos, yPos), size=(130, 30), choices=List, style=wx.CB_READONLY)

      
class aapp(wx.App):
        def OnInit(self):
	       	 frame = CommonAPI("Assignment 4",350,350)
		 frame.CreateButton(5,10,"Button")
		 frame.CreateRadioButton(15,50,"C")
		 frame.CreateRadioButton(15,70,"C++")
                 frame.CreateCheckBox(15,100,"Football")
              	 frame.CreateCheckBox(15,120,"BasketBall")
		 frame.CreateTextBox(15,150)
		 items=['Cricket','Football','BasketBall','BadMinton']
		 frame.CreateList(170,15,items)
		 frame.Show(True)
         	 frame.Centre()
         	 return True


if __name__ =='__main__':
	app = aapp(0)
	app.MainLoop()
