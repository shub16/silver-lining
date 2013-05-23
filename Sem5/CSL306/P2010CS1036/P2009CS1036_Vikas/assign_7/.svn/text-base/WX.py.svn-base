import wx

class LabelText(wx.StaticText):
    handle = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)


class TextView(wx.TextCtrl):
    handle = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def getText(self):
        if(self.handle == None):
            return self.text
        else:
            return self.handle.GetValue()

class Button(wx.Button):
    handle = None
    callback = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def clickListener(self,method):
        if(self.handle == None):
            self.callback = method
        else:
            self.handle.Bind(wx.EVT_BUTTON, method)
        return True

class CheckBox(wx.CheckBox):
    handle = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setValue(self,value):
        if(self.handle == None):
            self.value = value
        else:
            self.handle.SetValue(value)

class Radio(wx.RadioButton):
    handle = None
    selected_index = None
    def __init__(self,width,height):
        self.labels = []
        self.positions = []
        self.size = wx.Size(width, height)

    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.positions.append((X,Y))
        return True


class DropDownList(wx.ComboBox):
    handle = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.choices = choices
        self.position = (X,Y)
        self.size = (width,-1)
        self.value = value


class Widget:
    pass



class Xwindow(wx.Frame):
    parent = None
    def __init__(self, id, title,width,height):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, id,title, wx.DefaultPosition, wx.Size(width, height))
        self.panel = wx.Panel(self, -1)

    def show(self):
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return

    def add(self,widget):
        widget_type = type(widget)
        if(widget_type==TextView):
            widget.handle = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_MULTILINE)

        elif(widget_type==Radio):
            widget.handle = []
            radio_handle = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            widget.handle.append(radio_handle)
            for i in range(1,len(widget.labels)):
                radio_handle = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                widget.handle.append(radio_handle)
        
            if(widget.selected_index != None):
                widget.handle[widget.selected_index].SetValue(True)

        elif(widget_type==DropDownList):
            widget.handle = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)

        elif(widget_type==LabelText):
            widget.handle = wx.StaticText(self.panel, -1,widget.text,widget.position,widget.size)

        elif(widget_type==TextView):
            widget.handle = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size)

        elif(widget_type==Button):
            widget.handle = wx.Button(self.panel, -1, widget.title,  widget.position, widget.size)
            if(widget.callback != None ):
                 widget.handle.Bind(wx.EVT_BUTTON, widget.callback)

        elif(widget_type==CheckBox):
            widget.handle = wx.CheckBox(self.panel, -1, widget.title,  widget.position,widget.size)
            widget.handle.SetValue(widget.value)
