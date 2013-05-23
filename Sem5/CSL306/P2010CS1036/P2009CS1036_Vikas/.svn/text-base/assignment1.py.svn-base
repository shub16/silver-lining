#!/usr/bin/python
# sizer.py
import wx 

class Sizer(wx.Frame):
        def __init__(self, parent, id, title):
                wx.Frame.__init__(self, parent, id, title, size=(300, 250))
                panel=wx.Panel(self, -1)
                wx.TextCtrl(panel, -1, pos=(10, 10), size=(260,140))
                button1 = wx.Button(panel, -1, 'Exit', pos=(90,152), size=(90, 28))
                self.Bind(wx.EVT_BUTTON,self.press)
                self.Centre()
                self.Show(True)
        def press(self,event):
            self.Close(True)

app=wx.App(0)
Sizer(None, -1, 'Assign2')
app.MainLoop()
