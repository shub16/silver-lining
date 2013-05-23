#!/usr/bin/python
# assignment.py
import wx
import lab
class Frame(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title)
		panel = wx.Panel(self, -1)
		wx.TextCtrl(panel, -1, pos=(10, 10), size=(305,150))
		button = wx.Button(panel,-1,'Submit',(200,180))
		self.Show(True)
class PivotFrame(wx.Frame)	:
	def __init__(self,parent,id,title):
        	wx.Frame.__init__(self,parent,id,title)
			panel =wx.Panel(self,-1)
        	button1=wx.Button(panel,-1,'WxPython',(200,120))
        	button2=wx.Button(panel,-1,'PyQT',(200,180))
        	self.Bind(wx.EVT_BUTTON,self.onWxPython,id=button1.GetId())
        	self.Bind(wx.EVT_BUTTON,self.onPyQT,id=button2.GetId())
        	self.Show(True)
       
	def onPyQT(self,event):
		lab.main()   
        def onWxPython(self,event):
                Frame(None,-1,'WxPython')
               


def main():
       
	app = wx.App()
	PivotFrame(None,-1,'assignment')
	app.MainLoop()
if __name__=='__main__':
	main()

