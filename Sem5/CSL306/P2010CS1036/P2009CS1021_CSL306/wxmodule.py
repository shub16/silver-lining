import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Simple GUI', size=(250, 170))    #creating a wx.Frame widget which is parent for all other widgets. Its parent is none.
        
        
    def Addbutton(self,panel):
        button=wx.Button(panel, label='Close', pos=(10, 105))   #creates a wx.Button widget with panel as parent
        button.Bind(wx.EVT_BUTTON, self.OnClose)                #binds an event with the button when pressed which is defined by the function OnClose

    def Addtextbox(self,panel):
        multiText = wx.TextCtrl(panel, -1,"Enter your text here", size=(230, 100), style=wx.TE_MULTILINE) #adds a wx.Textctrl multiline widget with panel as parent
        multiText.SetInsertionPoint(0)
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)  #Adds the scroll bar or the FlexGridSizer
        sizer.AddMany([multiText])  #Adds the Textctrl to the FlexGridSizer widget
        panel.SetSizer(sizer)       #Sets the FlexGridSizer to the panel
        
    def OnClose(self, e):
        self.Close(True)     #predefined function in wx.Frame that closes the application
            

def DefineGui():
    frame = TextFrame()     #creates an instance of TextFrame class which creates an instance of wx.Frame  
    panel = wx.Panel(frame) #to create a panel
    frame.Addbutton(panel)  #call to the TextFrame class function that adds a button widget with panel as the parent
    frame.Addtextbox(panel) #call to the TextFrame class function that adds a textctrl widget with panel as the parent
    frame.Centre()          #predefined function in wx.Frame to position it in the centre
    frame.Show()            #to view the wx.Frame
    
app = wx.App()
DefineGui()     #function call to construct the GUI
