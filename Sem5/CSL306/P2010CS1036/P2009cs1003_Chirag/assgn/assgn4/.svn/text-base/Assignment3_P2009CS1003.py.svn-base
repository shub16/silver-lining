#! /usr/bin/python
import wx

class Widgets(wx.Frame):
        parent = None
        def __init__(self):
                self.app = wx.App(False)
                
        def setWindow(self,x,y,height,width,title):
                wx.Frame.__init__(self, self.parent, -1, title, wx.DefaultPosition, wx.Size(width, height))
                self.panel = wx.Panel(self, -1) 
                self.Show(True)
                self.Centre()
                return

        def endWindow(self):
                self.app.MainLoop()
                return

        def createTextArea(self, x, y, height,width,name):
                TextArea(self,x,y,height,width,name)
        
        def createButton(self, x, y, height,width,name):
                Button(self,x,y,height,width,name)
        
        def createCheckBox(self,x,y,height,width,name):
                CheckBox(self,x,y,height,width,name)
        
        def createRadioButton(self,x,y,height,width,name):
                RadioButton(self,x,y,height,width,name)
                
        def createDropDownList(self,x,y,height,width,List,name):
                DropDownList(self,x,y,height,width,List,name)
        
class TextArea(wx.TextCtrl):
        def __init__(self, parent, x, y, height,width,name):
                wx.TextCtrl(parent.panel, -1, pos=(x,y), size=(height,width))

class Button(wx.Button):
        def __init__(self,parent,x,y,height,width,name):
                wx.Button(parent.panel,-1,name,pos=(x,y),size=(height,width))
                
class CheckBox(wx.CheckBox):
        def __init__(self,parent,x,y,height,width,name):
                wx.CheckBox(parent.panel, -1, name,  pos=(x,y),size=(height,width))
                
class RadioButton(wx.RadioButton):
        def __init__(self,parent,x,y,height,width,name):
                wx.RadioButton(parent.panel,-1,name,pos=(x,y),size=(height,width))


class DropDownList(wx.ComboBox):
#wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)
        def __init__(self,parent,x,y,height,width,List,name):
                wx.ComboBox(parent.panel,-1,"Select character",pos=(x,y),size=(height,width),choices=List)

if __name__ == '__main__':    
        widget = Widgets()
        widget.setWindow(300, 300, 300,400,"Running WIndow")
        widget.createTextArea(60,60,100,20,'Text Area')
        widget.createCheckBox(20,20,100,20,'check box')
        widget.createRadioButton(40,40,100,20,'radio button')
        List = ['First','Second','Third']
        widget.createDropDownList(80,80,100,20,List,"Country")
        
        widget.endWindow()
