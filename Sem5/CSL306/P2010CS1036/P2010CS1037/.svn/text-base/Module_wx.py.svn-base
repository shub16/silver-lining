#!/usr/bin/env python
import wx

class frame(wx.Frame):  
      def __init__(self):
                wx.Frame.__init__(self, None, wx.ID_ANY, pos=(300, 150), size=(620,550))                
                panel = wx.Panel(self, wx.ID_ANY)
                self.text=wx.TextCtrl(panel,pos=(168,48), size=(285,148))
                self.button=wx.Button(panel,id=1,label='press me and i will dissappar ',pos=(168,228), size=(285,48))
                self.button.Bind(wx.EVT_BUTTON, self.buttonClick)
                
                self.Show(True)

       
      def buttonClick(self,event):
                self.button.Hide()
                self.SetTitle("Button clicked")
                
               
application=wx.PySimpleApp()
windows=frame()  
application.MainLoop()       

