import wx
class Windows(wx.Frame):
	def __init__(self, title,x,y, width, height):
		#self.app = wx.App(redirect=False)
		wx.Frame.__init__(self,None , wx.NewId(), title, pos=(x, y), size= (width, height))
		self.panel=wx.Panel(self)
			
	def show_window(self,box):
		self.panel.SetSizer(box.widget)												
		self.Show()
		
	def change_title(self,title):
		self.SetTitle(title)
		
	def change_color(self,color):
		self.panel.SetBackgroundColour(color) 
		
	def reset_color(self):
		self.panel.SetBackgroundColour(wx.NullColor) 
		
	def move_to_centre(self):
		self.Centre()
	
	def close_window(self):
		self.Destroy()
	
class RadioButtonList():
	def __init__(self,frm,group,ch1,ch2,st,grid,start):
		self.ch1=ch1
		self.ch2=ch2
		self.num=len(group)
		self.group=group
		self.st=st.widget
		self.grid=grid
		self.start=start
		self.rb={}
		
		for i in range(0,self.num):
			self.rb[i]=wx.RadioButton(frm.panel, label=group[i])
			self.rb[i].Bind(wx.EVT_RADIOBUTTON, self.onclick)
			self.grid.widget.Add(self.rb[i],pos=(start+i,0) )
			
	def onclick(self,event):
		if(self.ch1==1):
			if(self.rb[self.ch2-1].GetValue()):
				self.st.SetLabel('true')
			else:
				self.st.SetLabel('false')
		else:
			for i in range(0,self.num):
				if(self.rb[i].GetValue()):
					self.st.SetLabel('Your choice:'+self.group[i])
					
		
class Statictext(wx.StaticText):
	def __init__(self,frm,text):
		self.widget=wx.StaticText(frm.panel,label='')
		self.widget.SetLabel(text)
	def set_text(self,text):
		self.widget.SetLabel(text)
		
	
class button(wx.Button):
	def __init__(self,frm,text):
		self.widget=wx.Button(frm.panel,label=text)
		#self.b=l
		#self.tcb=textctrlbox.widget
		#self.multcb=multcb.widget
		
		#self.multcb.SetValue(self.tcb.GetValue())
		#@ color_change: changes color of button on mouse hovering
		#def colour_change(color)
	def	bind(self,fn,*args):
		self.widget.Bind(wx.EVT_BUTTON, fn)
		
			
			
class SingleTextBox(wx.TextCtrl):
	def __init__(self,frm,visibility):
		self.panel=frm.panel
		if(visibility==1):
			self.widget=wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
		if(visibility==0):
			self.widget=wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
		
	def set_text(self,text):
		self.widget.SetValue(text)
		
	def get_text(self):
		return self.widget.GetValue()
	
class MultiTextBox(wx.TextCtrl):
	def __init__(self,frm):		
		self.panel=frm.panel
		self.widget=wx.TextCtrl(self.panel, style = wx.TE_READONLY | wx.TE_MULTILINE)
		
	def set_text(self,text):
		self.widget.SetValue(text)
		
	def get_text(self):
		return self.widget.GetValue()

class Halignment(wx.BoxSizer):
	def __init__(self):
		'''if(alignment=="right"):
			self.widget=wx.BoxSizer(wx.HORIZONTAL)	
		else if(alignment=="move_to_centre"):
			self.widget=wx.BoxSizer(wx.HORIZONTAL)
		else:'''
		self.widget=wx.BoxSizer(wx.HORIZONTAL)
			
	def add(self,field,border):
		self.border=border
		self.widget.Add(field.widget, proportion = 0, flag = wx.EXPAND|wx.BOTTOM|wx.TOP, border=self.border)
		

class Valignment(wx.BoxSizer):
	def __init__(self):
		self.widget=wx.BoxSizer(wx.VERTICAL)
	def add(self,field,border):
		self.border=border
		self.widget.Add(field.widget, proportion = 0, flag = wx.EXPAND|wx.BOTTOM|wx.TOP, border=self.border)	
		
	
class Alignment(wx.StaticBoxSizer):
	def __init__(self,frm):
		self.widget = wx.GridBagSizer(5, 5)
		
	def add(self,field,row,column,columnspan):
		#boxsizer.Add(wx.CheckBox(panel, label="Generate Default Constructor"),
         #   flag=wx.LEFT, border=5)
		self.widget.Add(field.widget, pos=(row,column), span=(1,columnspan), flag=wx.EXPAND, border=5)

class ComboBox(wx.ComboBox):
	def __init__(self,frm,name,group):
		self.widget=wx.ComboBox(frm.panel, choices=group, style=wx.CB_READONLY)	
		self.widget.SetValue(name)
	
	def get_value(self):
		return self.widget.GetValue()
	
class CheckBox(wx.CheckBox):
	def __init__(self,frm,text):	
		self.widget=wx.CheckBox(frm.panel, label=text)	
	
	def bind(self,fn,*args):
		 self.widget.Bind(wx.EVT_CHECKBOX, fn)
	
	def get_state(self):
		return self.widget.GetValue()
	
	#def bind(self,fn):
	#		self.fn=fn
	#		self.widget.Bind(wx.EVT_CHECKBOX, self.fn)
			
	
class App(wx.App):
	def __init__(self):
		self.app = wx.App(redirect=False)
	def loop(self):
		self.app.MainLoop()	
		

class SpinCtrl(wx.SpinCtrl):
	def __init__(self,frm,val,minv,maxv):
		self.widget = wx.SpinCtrl(frm.panel, value=str(val), size=(250, -1))
		self.widget.SetRange(minv, maxv)
		
	def get_value(self):
		return self.widget.GetValue() 

class Slider(wx.Slider):
	def __init__(self,frm,val,minv,maxv):
		self.widget=wx.Slider(frm.panel, value=val, minValue=minv, maxValue=maxv, size=(250, -1), style=wx.SL_HORIZONTAL)
		
	def get_value(self):
		return self.widget.GetValue()
		# self.widget.GetValue()
	
class ProgressBar(wx.Gauge):
	def __init__(self,frm,val,rang,width,height):
		self.widget = wx.Gauge(frm.panel, range=rang, size=(width, height))
		self.widget.SetValue(val)
	def get_value(self):
		return self.widget.GetValue()
	
	def set_value(self,val):
		self.widget.SetValue(val)	
		
		
		
class image:
	def __init__(self,frm):
		#__init__(self, String name, long type=BITMAP_TYPE_ANY, int index=-1)
		#self.widget=wx.Image("/home/nchy13/Desktop/1.png",BITMAP_TYPE_ANY,-1)	
		#self.widget.Create(100,200,clear=True)
		
		self.panel=frm.panel
		#self.bit=wx.Bitmap(path)
		#self.depth=self.bit.GetDepth()
		#self.height=self.bit.GetHeight()
		self.PhotoMaxSize = 500
		self.img = wx.EmptyImage(550,550)
		
		self.inter=wx.BitmapFromImage(self.img)
		
		self.widget=wx.StaticBitmap(frm.panel,-1,self.inter)
		#self.path='/home/nchy13/Desktop/samsung75es9000rosegoldblush750000.jpg'
	
	def set_image(self,path):
		self.img = wx.Image(path, wx.BITMAP_TYPE_ANY)
		W = self.img.GetWidth()
		       
		H = self.img.GetHeight()
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		self.img = self.img.Scale(NewW,NewH)
		self.widget.SetBitmap(wx.BitmapFromImage(self.img))
		
		
		
class FileDialog:
	def __init__(self,frm,text):
		wildcard = "JPEG files (*.jpg)|*.jpg"
		self.widget = wx.FileDialog(None, text,wildcard=wildcard,style=wx.OPEN)
        
	def get_value(self):
		if self.widget.ShowModal() == wx.ID_OK:
			return self.widget.GetPath()
	#def set_size(self,x,y):
	#	self.bit.SetSize((x,y))
	#	self.widget.Create(self.panel,-1,self.bit)

		
	

	
