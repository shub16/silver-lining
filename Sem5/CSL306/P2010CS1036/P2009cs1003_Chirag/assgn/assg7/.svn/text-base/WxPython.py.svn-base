#! /usr/bin/python
import wx
import  wx.calendar
import wx.lib.buttons as buttons
import wx.lib.platebtn as platebtn
class Window(wx.Frame):
    parent = None
    def __init__(self, height,width,title):
        self.app = wx.App(False)
        #wx.Frame.__init__(self, None, title="Simple Notebook Example")
        wx.Frame.__init__(self, self.parent, -1, title, wx.DefaultPosition, wx.Size(height,width))
        
    def displayWindow(self,notebook):
        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return

class Page(wx.Panel):
    def __init__(self, x,y,height,width,name,parent):
        wx.Panel.__init__(self, parent)
    def setPage(self,*args):
        pass

class TabPanel(wx.Notebook):
    def __init__(self,x,y,height,width,parent):
        super(TabPanel, self).__init__(parent)
    def addPage(self,page,pageName):
        self.AddPage(page,pageName)
##    def setPanel(self):
##        sizer = wx.BoxSizer()
##        sizer.Add(notebook, 1, wx.EXPAND)
##        self.p.SetSizer(sizer)

class GroupBox(wx.Panel):
    def __init__(self, x,y,height,width,name,parent):
        pass
        '''wx.Panel.__init__(self, parent, -1,pos=(x,y),size=(height,width))
        self.border = wx.BoxSizer()
        self.box = wx.StaticBox(self, -1, name)
        self.bsizer = wx.StaticBoxSizer(self.box, wx.VERTICAL)
        self.border.Add(self.bsizer, 1000, wx.ALL, 10)
        self.SetSizer(self.border)
        #self.bsizer.Add(self.rtext, 0, flag=wx.ALL, border=5)
        #self.rtext = wx.TextCtrl(self, 1, "", size=(80, -1), style=wx.ALL)'''
    def setLayouts(self,layoutstyle,*widgets):
        pass
        '''if(layoutstyle=='Horizontal'):
                self.bsizer = wx.StaticBoxSizer(self.box, wx.HORIZONTAL)
        elif(layoutstyle=='Vertical'):
                self.bsizer = wx.StaticBoxSizer(self.box, wx.VERTICAL)
        else:
                self.bsizer = wx.StaticBoxSizer(self.box, wx.VERTICAL)
        for widget in widgets:
                self.bsizer.Add(widget, 0, flag=wx.ALL, border=5)
        self.border = wx.BoxSizer()
        self.border.Add(self.bsizer, 1000, wx.ALL, 10)
        self.SetSizer(self.border)'''
                    

class Slider(wx.Slider):
    def __init__(self,x,y,height,width,name,mode,minval,maxval,orientation,parent):
        avg=(minval+maxval)/2
        if(mode==1):
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_HORIZONTAL)
        if(mode==2):
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_AUTOTICKS)
        if(mode==3):
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_LABELS)
        if(mode==4):
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_VERTICAL)
        if(mode==5):
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_AUTOTICKS | wx.SL_VERTICAL)
        if(mode==6):
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_VERTICAL)
        else:
            sld = wx.Slider(parent, value=avg, minValue=minval, maxValue=maxval, pos=(x, y), size=(height, width), style=wx.SL_HORIZONTAL)


class SpinBox(wx.SpinCtrl):
    def __init__(self,x,y,height,width,name,mode,parent):   
        '''wx.StaticText(self, label='Convert Fahrenheit temperature to Celsius', pos=(x,y))
        wx.StaticText(self, label='Fahrenheit: ', pos=(20, 80))
        wx.StaticText(self, label='Celsius: ', pos=(20, 150))
        
        self.celsius = wx.StaticText(self, label='', pos=(150, 150))'''
        self.sc = wx.SpinCtrl(parent, value='0', pos=(x, y), size=(height, width))
        if(mode==1):
            self.sc = wx.SpinCtrl(parent, value='0', pos=(x, y), size=(height, width),style=wx.SP_ARROW_KEYS)
        self.sc.SetRange(-459, 1000)
        
        '''btn = wx.Button(self, label='Compute', pos=(70, 230))
        btn.SetFocus()
        cbtn = wx.Button(self, label='Close', pos=(185, 230))
        btn.Bind(wx.EVT_BUTTON, self.OnCompute)
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)         
        
    def OnClose(self, e):
        
        self.Close(True)    
        
    def OnCompute(self, e):
        
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))'''
                
class Label(wx.StaticText):
        def __init__(self,x,y,str,parent):
                wx.StaticText(parent,label=str , pos=(x,y))

class TextArea(wx.TextCtrl):
        def __init__(self, x, y, height,width,name,parent):
                wx.TextCtrl(parent, -1, pos=(x,y), size=(height,width),style=wx.TE_MULTILINE)

class TextLine(wx.TextCtrl):
        def __init__(self, x, y, height,width,mode,name,parent):
                if(mode=="Normal"):
                        wx.TextCtrl(parent, -1, pos=(x,y), size=(height,width))
                if(mode=="Password"):
                        wx.TextCtrl(parent, -1, pos=(x,y), size=(height,width),style=wx.TE_PASSWORD)

class Button(wx.Button):
        def __init__(self,x,y,height,width,name,mode,parent):
                if(mode==1):    #Flat Button
                        wx.Button(parent,-1,name,pos=(x,y),size=(height,width),style=wx.NO_BORDER)
                elif(mode==2):
                        buttons.GenToggleButton(parent, -1,label=name,pos=(x,y))
                elif(mode==4):
                        btn = platebtn.PlateButton(parent, label=name, pos=(x,y),size=(height,width),style=platebtn.PB_STYLE_GRADIENT)
                else:   #Normal Button
                        wx.Button(parent,-1,name,pos=(x,y),size=(height,width))
                
class CheckBox(wx.CheckBox):
        def __init__(self,x,y,height,width,name,state,parent,*args):
                wx.CheckBox(parent, -1, name,  pos=(x,y),size=(height,width))
                
class RadioButton(wx.RadioButton):
        def __init__(self,x,y,height,width,name,parent):
                wx.RadioButton(parent,-1,name,pos=(x,y),size=(height,width))


class DropDownList(wx.ComboBox):
        def __init__(self,x,y,height,width,List,name,parent):
                wx.ComboBox(parent,-1,"Select character",pos=(x,y),size=(height,width),choices=List)
                                
class Calendar(wx.calendar.CalendarCtrl):
    def __init__(self, x,y,parent):
        cal = wx.calendar.CalendarCtrl(parent, -1, wx.DateTime_Now(), pos = (x, y),
                                       style=wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SUNDAY_FIRST |
                                       wx.calendar.CAL_SEQUENTIAL_MONTH_SELECTION)

        '''parent.Bind(wx.calendar.EVT_CALENDAR, self.OnCalSelected, id=cal.GetId())

        # Set up control to display a set of holidays:
        self.Bind(wx.calendar.EVT_CALENDAR_MONTH, self.OnChangeMonth, cal)
        self.holidays = [(1,1), (10,31), (12,25)]    # (these don't move around)
        self.OnChangeMonth()

        cal2 = wx.calendar.CalendarCtrl(self, -1, wx.DateTime_Now(), pos = (325,50))
        self.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnCalSelChanged, cal2)


    def OnCalSelected(self, evt):

        print 'OnCalSelected: %s' % evt.GetDate()


    def OnChangeMonth(self, evt=None):

        cur_month = self.cal.GetDate().GetMonth() + 1   # convert wxDateTime 0-11 => 1-12
        for month, day in self.holidays:
            if month == cur_month:
                self.cal.SetHoliday(day)

        if cur_month == 8:
            attr = wx.calendar.CalendarDateAttr(border=wx.calendar.CAL_BORDER_SQUARE, colBorder="blue")
            self.cal.SetAttr(14, attr)
        else:
            self.cal.ResetAttr(14)


    def OnCalSelChanged(self, evt):

        cal = evt.GetEventObject()
        print "OnCalSelChanged:\n\t%s: %s\n\t%s: %s\n\t%s: %s\n\t" % ("EventObject", cal, "Date       ", cal.GetDate(),
                                                                      "Ticks      ", cal.GetDate().GetTicks())'''
