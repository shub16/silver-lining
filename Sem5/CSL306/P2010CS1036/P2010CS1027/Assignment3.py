#!/usr/bin/python
    
import wx
    
class MyCheckBox(wx.Frame):
      def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(300, 300))
	   
   	    self.cb=wx.TextCtrl(self,-1,'Name  ',(30,20))	
            self.cb=wx.Button(self,1,'Submit ',(130,20))
	    self.cb=wx.StaticBox(self,-1,'Current Job ',(35, 45), size=(210, 90))
            self.cb = wx.CheckBox(self, -1, 'Software Engineer', (70, 70))
            self.cb = wx.CheckBox(self, -1, 'Other', (70, 90))
	    self.cb=wx.StaticBox(self,-1,'Want to code in ',(35, 135), size=(210, 90))	   
            self.cb = wx.RadioButton(self, -1, 'C', (70, 150))
	    self.cb = wx.RadioButton(self, -1, 'C++', (70, 170))	
	    self.cb = wx.RadioButton(self, -1, 'Java', (70, 190))
	    self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)	
  	    #wx.EVT_CHECKBOX(self, self.cb.GetId(), self.ShowTitle)
   	    fruits = [ 'Apple', 'Banana', 'Papaya' , 'Grapes', 'Watermelon' ]
	    self.cb=wx.ComboBox(self,-1,value="Select one fruit",pos=(100,250),size=(150,30),choices=fruits,style=wx.CB_READONLY,name="Select your favourite fruit")
           
      def OnClose(self,event):
		if self.cb.GetValue():
			self.Close()

      def ShowTitle(self, event):
           if self.cb.GetValue():
               self.SetTitle('assignment 3')
           else: self.SetTitle('')
  
class aapp(wx.App):
        def OnInit(self):
        	 frame = MyCheckBox(None, -1, 'Assignment 3')
              	 frame.Show(True)
         	 frame.Centre()
         	 return True



x=raw_input("Press 0 if you want to execute code in wxPython(contains new widgets like radiobutton) and 1 for pyQT(imported module)");
x=int(x)
if(x==0):
	app = aapp(0)
	app.MainLoop()
else:
	import A1
