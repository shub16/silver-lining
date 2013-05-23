import wx
WIDTH = 300
HEIGHT = 400
class Panel(wx.Frame):

	def __init__(make):
		wx.Frame.__init__(make, None, title = 'What\'s up buddy!!! ',
		pos = (200,100), size = (WIDTH, HEIGHT))
		make.backgrnd = wx.Panel(make)
		
		make.submission = wx.Button(make.backgrnd, label = 'Submit')
		make.submission.Bind(wx.EVT_BUTTON, make.submitEvent)
		make.input = wx.TextCtrl(make.backgrnd, style=wx.TE_PROCESS_ENTER)
		make.input.Bind(wx.EVT_TEXT_ENTER, make.submitEvent)
		make.submitArea = wx.TextCtrl(make.backgrnd, style = wx.TE_READONLY | wx.TE_MULTILINE)
		make.horizontal = wx.BoxSizer()
		make.horizontal.Add(make.input, proportion = 1, border = 0)
		make.horizontal.Add(make.submission, proportion = 0, border = 0)
		
		make.vertical = wx.BoxSizer(wx.VERTICAL)
		make.vertical.Add(make.horizontal, proportion = 0, flag = wx.EXPAND, border = 0)
		make.vertical.Add(make.submitArea, proportion = 1, flag = wx.EXPAND, border = 0)
		make.backgrnd.SetSizer(make.vertical)
		make.Show()
	
	def submitEvent(make, event):
		make.submitArea.SetValue(make.input.GetValue())
app = wx.App(redirect=False)
window = Panel()
app.MainLoop()

