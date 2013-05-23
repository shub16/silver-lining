#!/usr/bin/env python
import wx
class frame(wx.Frame):  
      def __init__(self):
                wx.Frame.__init__(self, None, wx.ID_ANY, pos=(300, 150), size=(620,550))                
                panel = wx.Panel(self, wx.ID_ANY)
                self.text=wx.TextCtrl(panel,pos=(168,48), size=(285,148))
                self.button1=wx.Button(panel,id=1,label='wxPYTHON ',pos=(168,228), size=(285,48))
                self.button2=wx.Button(panel,id=2,label='PyGTK ',pos=(168,288), size=(285,48))
                self.button1.Bind(wx.EVT_BUTTON, self.button1Click)
                self.button2.Bind(wx.EVT_BUTTON, self.button2Click)
                self.Show(True)

       
      def button1Click(self,event):
                self.button1.Hide()
                self.SetTitle("Button clicked")
      
      def button2Click(self,event):
                import pyGTK
                
               
application=wx.PySimpleApp()
windows=frame()  
application.MainLoop()       

