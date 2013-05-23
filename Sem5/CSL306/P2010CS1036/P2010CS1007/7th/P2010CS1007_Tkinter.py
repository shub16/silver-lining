import tkFileDialog 
from Tkinter import *
import ttk
import Image 
import ImageTk
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class SingleTextBox():
	def __init__(self,frm,visibilty):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()		
		self.v = StringVar()
		if visibilty==1:
			self.widget=Entry(width=25,background='white',textvariable=self.v)
		if visibilty==0:
			self.widget=Entry(width=25,background='white', show="*",textvariable=self.v)

	def set_text(self,text):
		self.v.set(text)

	def get_text(self):
		x = self.widget.get()
		return x

class MultiTextBox():
	def __init__(self,frm):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.widget=Text(frm.frame,height=5,width=30,background='white')

class button():
	def __init__(self,frm,name):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.widget = Button(frm.frame)
		self.widget.configure(text=name,fg="red")

	def bind(self,fn,*arc):
		self.widget.bind("<Button-1>",fn)

class CheckBox():
	def __init__(self,frm,name):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()	
    		self.widget= Checkbutton(frm.frame,text=name)

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

class ComboBox():
	def __init__(self,frm,hello,arg):
		self.arg=arg
	        self.frame = Frame(frm.frame)
	        self.frame.grid()		
		optionvalue = IntVar()
        	optionvalue.set(hello)
        	self.widget = OptionMenu(frm.frame, optionvalue, *self.arg)
        	self.widget.state = []

class RadioButtonList():			#Widget class
	def __init__(self,frm, name, ch1, ch2,st,i):
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
				#v.add(self.st,self.i+self.r+1)
			else:
				self.st.set_text('false')
				#v.add(self.st,self.i+self.r+1)
		else:
			self.st.set_text('Your choice:'+self.shuu[self.v.get()-1][0])
			#v.add(self.st,self.i+self.r+1)

class Halignment():
	def __init__(self):
	        self.frame = Frame()
	        self.frame.grid()		

	def add(self,widget,i,j):
		self.widget=widget.widget
		self.widget.grid(row=i,column=j,sticky=W,pady=2)

class Alignment():
	def __init__(self,frame):
	        self.frame = Frame()
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

class Slider():
	def __init__(self,frm,value,mini,maxi):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.var = DoubleVar()
		self.var.set(value)
		self.widget = Scale(frm.frame,variable = self.var,from_=mini, to=maxi,length=200, sliderlength=8 , orient=HORIZONTAL)

	def get_value(self):
		return 'Value = ', self.var.get()	

class SpinCtrl():
	def __init__(self,frm,val,mini,maxi):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.var = IntVar()
		self.var.set(5)
		self.widget = Spinbox(frm.frame,from_=mini, to=maxi)
	
	def get_value(self):
		print 'spin= ', self.widget.get()
		return	self.widget.get()


class ProgressBar():
	def __init__(self,frm,value,rang,wid,hite):
	        self.frame = Frame(frm.frame)
	        self.frame.grid()
		self.var = IntVar()
		self.var.set(value)
		self.widget = ttk.Progressbar(frm.frame,variable=self.var,orient=HORIZONTAL, length=wid, mode='determinate')
		self.widget.start()

	def stop(self):	
		self.widget.stop()

class image():
	def __init__(self,frm):
		self.frm=frm.frame
		self.widget = Label(self.frm, image=None)

	def set_image(self,path):
		self.bard = Image.open(path)
		self.bard=self.bard.resize((500,500))
		ba = ImageTk.PhotoImage(self.bard)
		self.widget.configure(image = ba)
		self.widget.image = self.ba
		self.widget.pack()

class FileDialog(Frame):
	def __init__(self, parent,text):
		self.sukh=parent
		self.text=text
		self.frame = Frame(parent.frame)
		self.frame.grid()
		
	def get_value(self):
		ftypes = [(self.text, '*.jpg')]
		dlg = tkFileDialog.Open(filetypes = ftypes)
		fl = dlg.show()
		return fl		

class App():
	def __init__(self):
		pass

	def loop(self):
		mainloop()


