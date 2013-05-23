#!/usr/bin/python
# simple.py
import wx
import lab

class Frame(wx.Frame):
	
	def __init__(self,parent,id,title):
	
		wx.Frame.__init__(self,parent,id,title)  # initialize the frame
		
		panel = wx.Panel(self, -1)  
		
		wx.TextCtrl(panel, -1, pos=(20, 20), size=(150,150)) # text area is defined

		button = wx.Button(panel,-1,'ok',(200,150)) # button is initialized

		checkBox1 = wx.CheckBox(panel,-1,'GAMES',(100,200))

		checkBox2 = wx.CheckBox(panel,-1,'BOOKS',(200,200))

		radioButton1 = wx.RadioButton(panel,-1,"King Khan",(100,250))

		radioButton2 = wx.RadioButton(panel,-1,"Aamir Khan",(200,250))

		sins = ['Greed', 'Lust', 'Gluttony', 'Pride', 'Sloth', 'Envy', 'Wrath']

         	combo = wx.ComboBox(panel, pos=(100,300), choices=sins, style = wx.CB_READONLY)

#       		if dlg.ShowModal() == wx.ID_OK:
#
#			self.SetStatusText('You chose: %s\n' % dlg.GetStringSelection())

 #        		dlg.Destroy()
		
		self.Show(True)
	
class MainFrame(wx.Frame):
	
	def __init__(self,parent,id,title):
	
		wx.Frame.__init__(self,parent,id,title)  # initialize the frame
		
		panel = wx.Panel(self, -1)  
		
		button1 = wx.Button(panel,-1,'WxPython',(200,150))

		button2 = wx.Button(panel,-1,'PyQt',(200,250))		
		
		self.Bind(wx.EVT_BUTTON,self.onWxPython,id=button1.GetId()) # button1's functionality gets associated with onWxPython function

		self.Bind(wx.EVT_BUTTON,self.onPyQt,id=button2.GetId())	#button2's functionality gets associated with onPyQt function	

		self.Show(True)
	
	def onWxPython(self,event):
		
		Frame(None,-1,'WxPython')

	def onPyQt(self,event):
	
		lab.main()  # lab's main function is called (this is a different file)

def main():
	
	app = wx.App()

	MainFrame(None,-1,'Welcome to my GUI Application')

	app.MainLoop()

if __name__ == '__main__':
    main()
