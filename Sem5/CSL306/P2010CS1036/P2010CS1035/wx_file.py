#!/usr/bin/python

# wxboxsizer.py

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), wx.Size(550, 550))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("#770000")
        box = wx.BoxSizer(wx.HORIZONTAL)
        
        box.Add(wx.TextCtrl(panel, style=wx.TE_MULTILINE), 2, wx.EXPAND | wx.ALL,10 )
        box.Add(wx.Button(panel, -1, 'Click Me !'), 1, wx.EXPAND | wx.ALL,10 )
       

        
        panel.SetSizer(box)
        self.Centre()

class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'wxboxsizer.py')
         frame.Center()
         frame.Show(True)
         return True

app = MyApp(0)
app.MainLoop()
