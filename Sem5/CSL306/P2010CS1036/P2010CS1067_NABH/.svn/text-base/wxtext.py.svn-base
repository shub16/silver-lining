import wx
import gtkbox
WIDTH = 500
HEIGHT = 450
class Panel(wx.Frame):

	def __init__(make):
		wx.Frame.__init__(make, None, title = 'What\'s up buddy!!! ',
		pos = (200,100), size = (WIDTH, HEIGHT))
		make.backgrnd = wx.Panel(make)
		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(11)
		
		make.submission = wx.Button(make.backgrnd, label = 'Submit')
		make.submission.Bind(wx.EVT_BUTTON, make.submitEvent)
		make.input = wx.TextCtrl(make.backgrnd, style=wx.TE_PROCESS_ENTER)
		make.input.Bind(wx.EVT_TEXT_ENTER, make.submitEvent)
		make.submitArea = wx.TextCtrl(make.backgrnd, style = wx.TE_READONLY | wx.TE_MULTILINE)
		make.horizontal = wx.BoxSizer(wx.HORIZONTAL)
		make.horizontal.Add(make.input, proportion = 1, flag=wx.RIGHT, border = 5)
		make.horizontal.Add(make.submission, proportion = 0, flag=wx.RIGHT, border = 5)
		
		make.cb = wx.CheckBox(make.backgrnd, label='Change Background Color')
		make.cb.SetValue(False)
		make.cb.Bind(wx.EVT_CHECKBOX, make.OnCheck)
		
		lang=['C++','C','Java','Objective C','Visual Basics','C#','Python','Perl','Ruby']
		make.lb = wx.ComboBox(make.backgrnd, choices=lang, style=wx.CB_READONLY)
		make.lb.Bind(wx.EVT_COMBOBOX, make.OnSelect)
		
		make.st3 = wx.StaticText(make.backgrnd, label='In which continent is Turkey?')
		make.rb1 = wx.RadioButton(make.backgrnd, label='Europe', style=wx.RB_GROUP)
		make.rb2 = wx.RadioButton(make.backgrnd, label='Asia')
		make.rb1.Bind(wx.EVT_RADIOBUTTON, make.Onright)
		make.rb2.Bind(wx.EVT_RADIOBUTTON, make.Onwrong)
		make.st4 = wx.StaticText(make.backgrnd, label='')
		
		make.st1 = wx.StaticText(make.backgrnd, label='Which language do you prefer?')
		make.st2 = wx.StaticText(make.backgrnd, label='')
		make.st1.SetFont(font)
		
		make.h2 = wx.BoxSizer(wx.HORIZONTAL)
		make.h2.Add(make.st1, flag=wx.RIGHT, border=5)
		make.h2.Add(make.lb, proportion=1, flag=wx.RIGHT, border=30)
		
		make.vertical = wx.BoxSizer(wx.VERTICAL)
		make.vertical.Add(make.horizontal, proportion = 0, flag = wx.EXPAND|wx.BOTTOM|wx.TOP, border = 10)
		make.vertical.Add(make.submitArea, proportion = 1, flag = wx.EXPAND|wx.BOTTOM, border = 5)
		make.vertical.Add(make.cb, proportion=1, flag=wx.EXPAND|wx.LEFT, border=100)
		make.vertical.Add(make.h2, proportion=0, flag=wx.EXPAND)
		make.vertical.Add(make.st2, flag=wx.LEFT, border=100)
		make.vertical.Add(make.st3,flag=wx.EXPAND|wx.TOP, border=20)
		make.vertical.Add(make.rb1,flag=wx.EXPAND)
		make.vertical.Add(make.rb2,flag=wx.EXPAND)
		make.vertical.Add(make.st4,flag=wx.EXPAND|wx.BOTTOM, border=20)
		
		make.backgrnd.SetSizer(make.vertical)
		make.Show()
	
	def submitEvent(make, event):
		make.submitArea.SetValue(make.input.GetValue())
		
	def OnSelect(make, e):
		i = e.GetString()
		make.st2.SetLabel('Your choice:'+i)
		
	def OnCheck(make, e):
		sender = e.GetEventObject()
		isChecked = sender.GetValue()

		if isChecked:
			make.backgrnd.SetBackgroundColour('DARKGREY')            
		else: 
			make.backgrnd.SetBackgroundColour(wx.NullColor)     
			       
	def Onright(make, e):
		make.st4.SetLabel('It\'s correct. Good guess!!!')

	def Onwrong(make, e):
		make.st4.SetLabel('Don\'t be surprised. It is one of the four muslim countries in Europe.')	
		
app = wx.App(redirect=False)
input= raw_input("Enter 1 for Wxpython, 2 for PyQT or 3 for Tkinter. Program will quit otherwise. ")
if input=="1":
	window = Panel()
	app.MainLoop()
elif input=="2":
	entry=gtkbox.TextBox()
	entry.main()
elif input=="3":
	import tkin
else:
	print("invalid input")

