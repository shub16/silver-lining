import wx

class Vista(wx.Frame):
    parent = None
    def __init__(self, id, title,width,height):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, id, title, wx.DefaultPosition, wx.Size(width, height))
        self.panel = wx.Panel(self, -1)

    def show(self):
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return

    def addWidget(self,widget):
        widget_type = type(widget)
        print widget_type
        if(widget_type==Button or isinstance(widget,Button)):
            widget.controller = wx.Button(self.panel, -1, widget.title,  widget.position, widget.size)
            if(widget.callback != None ):
                widget.controller.Bind(wx.EVT_BUTTON, widget.callback)     
        elif(widget_type==TextBuffer or isinstance(widget,TextBuffer)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_MULTILINE)
        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = wx.CheckBox(self.panel, -1, widget.title,  widget.position,widget.size)
            widget.controller.SetValue(widget.value)
        elif(widget_type==RadioButton or isinstance(widget,RadioButton)):
            widget.controller = []
            radio_controller = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                widget.controller.append(radio_controller)
            if(widget.selected_index != None):
                widget.controller[widget.selected_index].SetValue(True)
        elif(widget_type==List or isinstance(widget,List)):
            widget.controller = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)                                           
        elif(widget_type==TextArea or isinstance(widget,TextArea)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size)
        elif(widget_type==PasswordField or isinstance(widget,PasswordField)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_PASSWORD)            
        elif(widget_type==ShowText or isinstance(widget,ShowText)):
            widget.controller = wx.StaticText(self.panel, -1,widget.text,widget.position,widget.size)       
            
class Button(wx.Button):
    controller = None
    callback = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def clickTrigger(self,method):
        if(self.controller == None):
            self.callback = method
        else:
            self.controller.Bind(wx.EVT_BUTTON, method)
        return True

class TextBuffer(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.SetValue(text)
        return True

    def concatText(self,text):
        if(self.controller == None):
            self.text = self.controller.GetValue() + text
        else:
            self.controller.AppendText(text)
        return True              

    def clearBuffer(self):
        self.controller.Clear()
        return True

class CheckBox(wx.CheckBox):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setBox(self,value):
        if(self.controller == None):
            self.value = value
        else:
            self.controller.SetValue(value)

    def getBox(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.IsChecked()

class RadioButton(wx.RadioButton):
    controller = None
    selected_index = None
    def __init__(self,width,height):
        self.labels = []
        self.positions = []
        self.size = wx.Size(width, height)

    def addButton(self,label,X,Y):
        self.labels.append(label)
        self.positions.append((X,Y))
        return True

    def getButton(self):
        for i in range(len(self.controller)):
            if(self.controller[i].GetValue()):
                return self.labels[i]
        return None

    def setButton(self,index):
        if(self.controller == None):
            self.selected_index = index
        else:
            button_controller = self.controller[index]
            button_controller.SetValue(True) 

class List(wx.ComboBox):
    controller = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.choices = choices
        self.position = (X,Y)
        self.size = (width,-1)
        self.value = value

    def getValue(self):
            if(self.controller == None):
                return self.value
            else:
                return self.controller.GetValue()

class TextArea(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, -1)

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.SetValue(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.GetValue()
            
class PasswordField(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, -1)

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.SetValue(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.GetValue()

class ShowText(wx.StaticText):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)
