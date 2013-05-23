'''
WX_Canvas class : support absolute layout wxPython Evn
Dialog_box class : support box layout QtPy EVN

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
                return textArea

        def addButton(self,title,X,Y,width,height):
                button = wx.Button(self.panel, -1, title,  (X,Y), wx.Size(width, height))
                return button
        
        def show(self):
                self.Show(True)
                self.Centre()
                self.app.MainLoop()
                return True
        
        
if __name__ == '__main__':
        ''' Set GUI environment from [wxPython] or [PyQt] '''
        ENV = "wxPython"
        #ENV = "PyQt"

        if(ENV == "wxPython"):
            Input_box = WX_Canvas(1,"Input",220,400)
            Input_box.addTextArea("This is a demo text",0,0,200,200)
            Input_box.addButton("MyButton",0,210,200,20)
            Input_box.show()

        if(ENV == "PyQt"):
            import sys
            from PyQt4 import QtGui
            from QtPyGUI import Dialog_box
            app = QtGui.QApplication(sys.argv)
            Input_box = Dialog_box(None,"Input",220,400)
            Input_box.addTextArea("This is a demo text")
            Input_box.addButton("MyButton")
            Input_box.show()
            app.exec_()

