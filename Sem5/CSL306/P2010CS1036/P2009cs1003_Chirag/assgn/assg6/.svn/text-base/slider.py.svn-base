import wx
class Slider(wx.Slider):
           
    def __init__(self,parent,x,y,height,width,minimum,maximum):
        sld = wx.Slider(parent.panel, value=(minimum+maximum)/2, minValue=minimum, maxValue=maximum, pos=(x, y), 
            size=(250, -1), style=wx.SL_HORIZONTAL)
        
        sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        
        self.txt = wx.StaticText(parent.panel, label='Middle', pos=(x, y+25))               
    def OnSliderScroll(self, e):
        
        obj = e.GetEventObject()
        val = obj.GetValue()
        
        self.txt.SetLabel(str(val)) 

		
		
#__init__(self, parent, id=-1, date=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=wxCAL_SHOW_HOLIDAYS|wxWANTS_CHARS, name=CalendarNameStr) 
'''class Calendar(wx.CalendarCtrl):
    def __init__(self,parent,x,y,height,width):
        self.controller=wx.CalendarCtrl(parent.panel,-1,date=DefaultDateTime,pos=(x,y),size=(height,width),style=wxCAL_SHOW_HOLIDAYS|wxWANTS_CHARS'''

#TASK_RANGE = 50

class Gauge():
    def InitUI(self,parent,TASK_RANGE):   
        
        parent.frame.timer = wx.Timer(self, 1)
        self.count = 0

        parent.frame.Bind(wx.EVT_TIMER, parent.frame.OnTimer, parent.frame.timer)

        pnl = wx.Panel(parent.frame)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        parent.frame.gauge = wx.Gauge(pnl, range=TASK_RANGE, size=(250, 25))
        parent.frame.btn1 = wx.Button(pnl, wx.ID_OK)
        parent.frame.btn2 = wx.Button(pnl, wx.ID_STOP)
        parent.frame.text = wx.StaticText(pnl, label='Task to be done')

        parent.frame.Bind(wx.EVT_BUTTON, parent.frame.OnOk, self.btn1)
        parent.frame.Bind(wx.EVT_BUTTON, parent.frame.OnStop, self.btn2)

        hbox1.Add(parent.frame.gauge, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox2.Add(parent.frame.btn1, proportion=1, flag=wx.RIGHT, border=10)
        hbox2.Add(parent.frame.btn2, proportion=1)
        hbox3.Add(parent.frame.text, proportion=1)
        vbox.Add((0, 30))
        vbox.Add(hbox1, flag=wx.ALIGN_CENTRE)
        vbox.Add((0, 20))
        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox3, proportion=1, flag=wx.ALIGN_CENTRE)

        pnl.SetSizer(vbox)

    def OnOk(self, e):
        
        if self.count >= TASK_RANGE:
            return

        self.timer.Start(100)
        self.text.SetLabel('Task in Progress')

    def OnStop(self, e):
        
        if self.count == 0 or self.count >= TASK_RANGE or not self.timer.IsRunning():
            return

        self.timer.Stop()
        self.text.SetLabel('Task Interrupted')
        
    def OnTimer(self, e):
        
        self.count = self.count + 1
        self.gauge.SetValue(self.count)
        
        if self.count == TASK_RANGE:

            self.timer.Stop()
            self.text.SetLabel('Task Completed')