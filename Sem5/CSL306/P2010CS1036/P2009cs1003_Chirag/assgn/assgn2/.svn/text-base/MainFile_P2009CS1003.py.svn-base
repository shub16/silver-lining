import wx
import assg

class FirstAssignment(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(300, 250))
		wx.TextCtrl(self, -1, pos=(10, 10), size=(250,140))
		button1 = wx.Button(self, -1, 'First Button', pos=(70,152), size=(90, 28))
		self.Centre()
		self.Show(True)
app=wx.App(0)

def Main():
	print  " Enter choice of GUI"
	x = raw_input("Enter your choice. 1 for Wxpython and 2 for PyQT and pressing other keys will exit the program: ")
	if x == "1":
		FirstAssignment(None, -1, '')
		app.MainLoop()
	elif x == "2":
		assg.PyQt()
	else:
		print "Error in input"
		
if __name__ == '__main__':
    Main()