# WX_canvas.py
'''
WX_Canvas class : currently support absolute layout
API

WX_Canvas(ID,Title,Width,Height)
        Constructor
        Parameter:
                Title : Title of window
                Width : Width of window
                Height : Height of window
        Return:
                Instance of object
        
                
addTextArea(Text,X,Y,Width,Height)
        Add text area to canvas
        Parameter
                Text : Initialise with text
                Width : Width of textarea
                Height : Height of textarea
                X,Y : Absolute position
        Return:
                Instance of object created

addButton(Text,X,Y,Width,Height)
        Add button to canvas
        Parameter
                Text : Initialise with text
                Width : Width of button
                Height : Height of button
                X,Y : Absolute position
        Return:
                Instance of object created

                '''

import wx
class WX_Canvas(wx.Frame):
        parent = None
        def __init__(self, id, title,width,height):
                self.app = wx.App(False)
                wx.Frame.__init__(self, self.parent, id, title, wx.DefaultPosition, wx.Size(width, height))
                self.panel = wx.Panel(self, -1)
                
        def addTextArea(self,title,X,Y,width,height):
                textArea = wx.TextCtrl(self.panel, -1, title,  (X,Y), wx.Size(width, height))
                print(type(textArea))
                return textArea

        def addButton(self,title,X,Y,width,height):
                wx.Button(self.panel, -1, title,  (X,Y), wx.Size(width, height))
                return True

                
        def show(self):
                self.Show(True)
                self.Centre()
                self.app.MainLoop()
                return True
        
        
if __name__ == '__main__':
        canvas = WX_Canvas(1, 'wxPython1' ,220,400)
        textArea = canvas.addTextArea("This is a demo text",0,0,200,200)
        #canvas.setText(textArea,"hello");
        canvas.addButton("MyButton",0,210,200,20)
        canvas.show()
