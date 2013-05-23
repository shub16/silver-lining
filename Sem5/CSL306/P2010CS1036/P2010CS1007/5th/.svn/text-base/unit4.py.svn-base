from Tkinter import *

class SingleTextBox():
	def __init__(self,frm,visibilty):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()		
		self.v = StringVar()
		if visibilty==1:
			self.widget=Entry(width=30,background='white',textvariable=self.v)
		if visibilty==0:
			self.widget=Entry(width=30,background='white', show="*",textvariable=self.v)

	def set_text(self,text):
		self.v.set(text)

	def get_text(self):
		x = self.widget.get()
		return x

class MultiTextBox():
	def __init__(self,frm):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.widget=Text(frm.frame,height=10,width=30,background='white')

class button():
	def __init__(self,frm,name,fn):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.widget = Button(frm.frame,text=name, fg="red",command=fn,padx=20)

	def color_change(self):
		self.widget.configure(fg = "blue")

class CheckBox():
	def __init__(self,frm,name):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()	
    		self.widget= Checkbutton(frm.frame,text=name)

class ComboBox():
	def __init__(self,frm,hello,arg):
		self.arg=arg
	        self.frame = Frame(frm.frame)
	        self.frame.grid()		
		optionvalue = IntVar()
        	optionvalue.set(hello)
        	self.widget = OptionMenu(frm.frame,self.frame, optionvalue, *self.arg)
        	self.widget.state = []

class RadioButton():			#Widget class
	def __init__(self,frm,i,st, ch1, ch2, name):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.ch1=ch1
		self.ch2=ch2
		self.i=i
		self.st=st
		v = IntVar()
		self.v=v
		self.shuu=name
		self.length = len(name)
		self.rb={}
		r=0
		self.r=r
		for txt, val in name:
			self.rb[r]=Radiobutton(frm.frame,text=txt,padx = 20,variable=v,value=val, command = self.onclick)
			self.rb[r].grid(row=i+r,column=0,sticky=W,pady=2)
			r= r+1
		self.r=r

	def onclick(self):
		if(self.ch1==1):
			if(self.v.get()==self.ch2):
				self.st.set_text('true')
				h.add(self.st,self.i+self.r+1)
			else:
				self.st.set_text('false')
				h.add(self.st,self.i+self.r+1)
		else:
			self.st.set_text('Your choice:'+self.shuu[self.v.get()-1][0])
			h.add(self.st,self.i+self.r+1)

class Valignment():
	def __init__(self,frm):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()		

	def add(self,widget,i,j,span):
		self.widget=widget.widget
		self.widget.grid(row=i,column=j,columnspan=span,sticky=W,pady=2)

class Statictext():
	def __init__(self,frm):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.lab=StringVar()
		self.widget= Label(frm.frame,textvariable= self.lab)

	def set_text(self,name):
		self.lab.set(name)
class Windows():
	def __init__(self,titl,px,py,x,y):
		self.titl=titl
		self.w=x
		self.h=y
		self.frame=Tk()
		self.frame.geometry('%dx%d+%d+%d'%(x,y,px,py))
		self.frame.title(titl)
	def show_window(self,box):
		pass

	def change_title(self,tit):
		self.frame.title(tit)

	def move_to_center(self):
	        sw = self.frame.winfo_screenwidth()
	        sh = self.frame.winfo_screenheight()
	        x = (sw - self.w)/2
	        y = (sh - self.h)/2
	        self.frame.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))

	def change_color(self,frm):
	        self.frame.configure(background=frm)

	def reset_color(self):
	        self.frame.configure(background="#D9D9D9")

