#!/usr/bin/python
import wx
class updated(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300,260))
        panel=wx.Panel(self,-1)
        
        vbox=wx.BoxSizer(wx.VERTICAL)

        hbox1=wx.BoxSizer(wx.HORIZONTAL)
        cb1=wx.CheckBox(panel, -1, 'Hockey')
        hbox1.Add(cb1)
        cb2=wx.CheckBox(panel, -1, 'Cricket')
        hbox1.Add(cb2, 0, wx.LEFT, 70)
        vbox.Add(hbox1, 0, wx.ALIGN_CENTER|wx.ALL, 10)

        hbox2=wx.BoxSizer(wx.HORIZONTAL)
        r1=wx.RadioButton(panel, -1, 'Male')
        hbox2.Add(r1)
        r2=wx.RadioButton(panel, -1, 'Female')
        hbox2.Add(r2, 0, wx.LEFT, 80)
        vbox.Add(hbox2, 0, wx.ALIGN_CENTER|wx.ALL, 10)

        hbox3=wx.BoxSizer(wx.HORIZONTAL)
        t1=wx.StaticText(panel, -1, 'City')
        hbox3.Add(t1)
        c1=wx.ComboBox(panel, -1, size=(100, -1))
        hbox3.Add(c1)
        t2=wx.StaticText(panel, -1, 'State')
        hbox3.Add(t2, 0, wx.LEFT, 20)
        c2=wx.ComboBox(panel, -1, size=(100, -1))
        hbox3.Add(c2)
        vbox.Add(hbox3, 0, wx.ALIGN_CENTER|wx.ALL, 10)

        textarea=wx.TextCtrl(panel, -1, size=(265,50))
        vbox.Add(textarea, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        B1=wx.Button(panel, -1, 'ok')
        B1.Bind(wx.EVT_BUTTON, self.onclick)
        vbox.Add(B1, 0, wx.ALIGN_CENTER|wx.TOP, 10)

        panel.SetSizer(vbox)
        panel.SetAutoLayout(True)
        vbox.Fit(panel)
        self.Centre()
        self.Show(True)

    def onclick(self, event):
        self.Close(True)

app=wx.App()
updated(None, -1, 'Assignment3')
app.MainLoop()
