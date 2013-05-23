#!/usr/bin/python
import wx

class Box(wx.Frame):
  
    def __init__(self, parent, head):									
        super(Box, self).__init__(parent, title=head, size=(300, 80))
            
        self.Interface()
        self.Centre()
        self.Show()     
        
    def Interface(self):
       
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#360523")

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
 
        tbox = wx.TextCtrl(panel)
        button = wx.Button(panel, label='Exit', size=(80, 27))
	self.Bind(wx.EVT_BUTTON, self.OnClick, id=button.GetId())  

        hbox.Add(tbox, proportion=1)
      	hbox.Add(button)

        vbox.Add(hbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=20)

        panel.SetSizer(vbox)

    def OnClick(self,event):
	self.Close()

class Dialog(wx.Frame):
  
    def __init__(self, parent, title):
        super(Dialog, self).__init__(parent, title=title, size=(310, 280))
            
        self.Interface()
        self.Centre()
        self.Show()     
        
    def Interface(self):
       
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#770000")

	verticalbox = wx.BoxSizer(wx.VERTICAL)

        horizontalbox1 = wx.BoxSizer(wx.HORIZONTAL)
	horizontalbox2 = wx.BoxSizer(wx.HORIZONTAL)

        verticalbox12 = wx.BoxSizer(wx.VERTICAL)
        verticalbox22 = wx.BoxSizer(wx.VERTICAL)
        verticalbox32 = wx.BoxSizer(wx.VERTICAL)
	
	verticalbox.Add(horizontalbox1, 0, wx.ALL|wx.EXPAND, 5)
	verticalbox.Add(horizontalbox2, 0, wx.ALL|wx.EXPAND, 5)

        horizontalbox2.Add(verticalbox12, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        horizontalbox2.Add(verticalbox22, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        horizontalbox2.Add(verticalbox32, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        wxPython = wx.Button(panel, label='wxPython', size=(100, 30))
        pyQt = wx.Button(panel, label='pyQt', size=(100, 30))
        exit = wx.Button(panel, label='Exit', size=(100, 30))
	self.Bind(wx.EVT_BUTTON, self.OnClick, id=exit.GetId())  
	self.Bind(wx.EVT_BUTTON, self.OnClickWx, id=wxPython.GetId())
	self.Bind(wx.EVT_BUTTON, self.OnClickQt, id=pyQt.GetId())



        radiofield = wx.StaticBoxSizer(wx.StaticBox(panel, -1, 'Year'), orient=wx.VERTICAL)
        checkfield = wx.StaticBoxSizer(wx.StaticBox(panel, -1, 'Electives'), orient=wx.VERTICAL)

        radiofield.Add(wx.RadioButton(panel, -1, '2009', style=wx.RB_GROUP))
        radiofield.Add(wx.RadioButton(panel, -1, '2010'))
        radiofield.Add(wx.RadioButton(panel, -1, '2011'))

        checkfield.Add(wx.CheckBox(panel, 1, 'CSL 111'))
        checkfield.Add(wx.CheckBox(panel, 2, 'CSL 222'))
        checkfield.Add(wx.CheckBox(panel, 3, 'CSL 333'))
        checkfield.Add(wx.CheckBox(panel, 4, 'CSL 444'))
        checkfield.Add(wx.CheckBox(panel, 5, 'CSL 555'))

        halls = ["L_1","L_2","L_3","L_4","L_5","L_6","L_7","L_8","L_9"]
        listbox = wx.ListBox(panel,size=wx.DefaultSize,choices=halls)

        horizontalbox1.Add(wxPython)
        horizontalbox1.Add(pyQt)
        horizontalbox1.Add(exit)

        verticalbox12.Add(radiofield, 1, wx.ALL, 5)
        verticalbox22.Add(checkfield, 1, wx.ALL, 5)
        verticalbox32.Add(listbox, 2, wx.TOP, 15)


        panel.SetSizer(verticalbox)


    def OnClick(self,event):
	self.Close()

    def OnClickWx(self,event):
	self.Close()
	Box(None, head='Text box+Button')

    def OnClickQt(self,event):
	self.Close()
	import textAndButton


if __name__ == '__main__':
  
    application = wx.App()
    Dialog(None, title='Choose Your GUI')
    application.MainLoop()
