#!/usr/bin/python
import wx

class DialogNew(wx.Frame):
  
    def __init__(self, parent, title):
        super(DialogNew, self).__init__(parent, title=title,size=(500, 300))  
        self.Interface()
        self.Centre()
        self.Show()     
        
    def Interface(self):

        panel = wx.Panel(self)
        panel.SetBackgroundColour("#367588")
        verticalbox = wx.BoxSizer(wx.VERTICAL)

        wxPython = wx.Button(panel, label='wxPython', size=(80, 30))
        pyQT = wx.Button(panel, label='pyQT', size=(80, 30))
        exit = wx.Button(panel, label='Exit', size=(80, 30))
        horizontalbox = wx.BoxSizer(wx.HORIZONTAL)
        horizontalbox.Add(wxPython,proportion=1)
        horizontalbox.Add(pyQT,proportion=1)
        horizontalbox.Add(exit,proportion=1)
        verticalbox.Add(horizontalbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=30)

        radiobox = wx.StaticBoxSizer(wx.StaticBox(panel, -1, 'Type'), orient=wx.VERTICAL)
        radiobox.Add(wx.RadioButton(panel, -1, 'Qwerty', style=wx.RB_GROUP))
        radiobox.Add(wx.RadioButton(panel, -1, 'Touch Screen'))
        checkbox = wx.StaticBoxSizer(wx.StaticBox(panel, -1, 'Features'), orient=wx.VERTICAL)
        checkbox.Add(wx.CheckBox(panel, 1, 'Camera'))
        checkbox.Add(wx.CheckBox(panel, 2, 'WiFi'))
        checkbox.Add(wx.CheckBox(panel, 3, 'Bluetooth'))
        sampleList = ["Apple","Samsung","Nokia","Blackberry","HTC","Sony","Motorola"]
        list_box = wx.ListBox(panel,size=wx.DefaultSize,choices=sampleList)
        widgets = wx.BoxSizer(wx.HORIZONTAL)
        widgets.Add(radiobox, 1, wx.ALL, 5)
        widgets.Add(checkbox, 1, wx.ALL, 5)
        widgets.Add(list_box, 1, wx.ALL, 5)
        verticalbox.Add(widgets, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=30)

        panel.SetSizer(verticalbox)
		
	self.Bind(wx.EVT_BUTTON, self.OnClickwxPython, id=wxPython.GetId())
	self.Bind(wx.EVT_BUTTON, self.OnClickpyQT, id=pyQT.GetId())
	self.Bind(wx.EVT_BUTTON, self.OnClick, id=exit.GetId()) 

    def OnClickwxPython(self,event):
	self.Close()
	Dialog(None, title='Text Box And Button')

    def OnClickpyQT(self,event):
	self.Close()
	import textAndButton
	
    def OnClick(self,event):
	self.Close()

class Dialog(wx.Frame):
  
    def __init__(self, parent, title):
        super(Dialog, self).__init__(parent, title=title, size=(400, 100))
        self.Interface()
        self.Centre()
        self.Show()     
        
    def Interface(self):
       
        panel = wx.Panel(self)
        verticalbox = wx.BoxSizer(wx.VERTICAL)
        horizontalbox1 = wx.BoxSizer(wx.HORIZONTAL)
        textbox = wx.TextCtrl(panel)
        horizontalbox1.Add(textbox, proportion=1)
        verticalbox.Add(horizontalbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        verticalbox.Add((-1, 9))
        horizontalbox2 = wx.BoxSizer(wx.HORIZONTAL)
        button = wx.Button(panel, label='Exit', size=(200, 30))
        horizontalbox2.Add(button)
        verticalbox.Add(horizontalbox2, flag=wx.ALIGN_CENTER|wx.CENTER, border=10)
        panel.SetSizer(verticalbox)
        
	self.Bind(wx.EVT_BUTTON, self.OnClick, id=button.GetId()) 
	
    def OnClick(self,event):
	self.Close()

if __name__ == '__main__':
  
    application = wx.App()
    DialogNew(None, title='Select The GUI')
    application.MainLoop()
