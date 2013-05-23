#! /usr/bin/python

import wx
import slider

class Window(wx.Frame):
    parent = None
    def __init__(self, x,y,height,width,title):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, -1, title, wx.DefaultPosition, wx.Size(height,width))
        self.panel = wx.Panel(self, -1)


    def displayWindow(self):
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return

    def createTextArea(self,x, y, height,width,mode,name):
        self.createLabel(name,5,y)
        return TextArea(self,x,y,height,width,mode)

    def createButton(self,x, y, height,width,name):
        return Button(self,x,y,height,width,name)

    def createCheckBox(self,name,value,x,y,height,width):
        CheckBox(self,name,x,y,height,width)

    def createRadioButton(self,name,value,x,y,height,width):
        RadioButton(self,name,x,y,height,width)

    def createDropDownList(self,List,x,y,height,width):
        DropDownList(self,List,x,y,height,width)
        
    def createLabel(self,message,x,y):
        return Label(self,message,x,y)
    
    def createDialogBox(self,message,x,y):
        return DialogBox(self,message,x,y)
    
    def createSlider(self,x,y,height,width,minimum,maximum):
        slider.Slider(self,x,y,height,width,minimum,maximum)

    def InitUI(self,x,y,height,width):   
        wx.StaticText(self, label='Convert Fahrenheit temperature to Celsius', 
            pos=(20,20))
        wx.StaticText(self, label='Fahrenheit: ', pos=(20, 80))
        wx.StaticText(self, label='Celsius: ', pos=(20, 150))
        
        self.celsius = wx.StaticText(self, label='', pos=(150, 150))
        self.sc = wx.SpinCtrl(self, value='0', pos=(150, 75), size=(60, -1))
        self.sc.SetRange(-459, 1000)
        
        btn = wx.Button(self, label='Compute', pos=(70, 230))
        btn.SetFocus()
        cbtn = wx.Button(self, label='Close', pos=(185, 230))
        btn.Bind(wx.EVT_BUTTON, self.OnCompute)
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)         
        
    def OnClose(self, e):
        
        self.Close(True)    
        
    def OnCompute(self, e):
        
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))      
    
class DialogBox(wx.MessageDialog):
    def __init__(self, parent, message,x,y):
        self.controller=wx.MessageDialog(parent.panel,message,caption="Chirag",style=wx.ICON_ERROR,pos=(x,y))

class Label(wx.StaticText):
    def __init__(self,parent,message,x,y):
            self.controller=wx.StaticText(parent.panel,-1, message,pos=(x,y))
            
    def setTextColour(self,colour):
            self.controller.SetBackgroundColour(colour)
            
    def setText(self,message):
        self.controller.SetLabel(message)

class TextArea(wx.TextCtrl):
    def __init__(self,parent,x, y, height,width,mode):
        if(mode=="Password"):
            mode=wx.TE_PASSWORD
        else:
            mode=wx.TE_LEFT
        self.controller = wx.TextCtrl(parent.panel, -1, pos=(x,y),style=mode)

    def setValue(self,text):
        self.controller.SetValue(text)
    def getValue(self):
        return self.controller.GetValue()
    def textLength(self):
        return self.controller.GetLineLength(1)

class CheckBox(wx.CheckBox):
    def __init__(self,parent,name,x,y,height,width):
        wx.CheckBox(parent.panel, -1, name,  pos=(x,y),size=(height,width))

class RadioButton(wx.RadioButton):
    def __init__(self,parent,name,x,y,height,width):
        wx.RadioButton(parent.panel,-1,name,pos=(x,y),size=(height,width))


class DropDownList(wx.ComboBox):
#wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)
    def __init__(self,parent,List,x,y,height,width):
        wx.ComboBox(parent.panel,-1,"Select character",pos=(x,y),size=(height,width),choices=List)

class Button(wx.Button):
    def  __init__(self, parent, label, x,y, height,width):
        self.controller=wx.Button(parent.panel,-1,label,pos=(x,y),size=(height,width),style=0)

    def pressed(self,method):
        if(self.controller == None):
            self.callback = method
        else:
            self.controller.Bind(wx.EVT_BUTTON, method)
            return True
                                                                
if __name__ == '__main__':

    widget = Window(-1,-1,350,310,"Chirag Gupta-Assignment 6")

    widget.InitUI(150,75,60,-1)

    widget.displayWindow()
