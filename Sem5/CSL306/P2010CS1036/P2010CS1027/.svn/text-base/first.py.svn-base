#!/usr/bin/python
 
import wx
 
class fframe(wx.Frame):
        def __init__(self, parent, id, title):
        	wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(250, 50))
 		self.logger = wx.TextCtrl(self, pos=(110,10), size=(100,30), style=wx.TE_MULTILINE)
		self.button =wx.Button(self, label="Name", pos=(20, 10))
		

class aapp(wx.App):
        def OnInit(self):
        	 frame = fframe(None, -1, 'First Assignment')
              	 frame.Show(True)
         	 frame.Centre()
         	 return True
 

app = aapp(0)
app.MainLoop()

 
