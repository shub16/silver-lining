from Tkinter import *

#oka
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

	def move_to_centre(self):
		sw = self.frame.winfo_screenwidth()
		sh = self.frame.winfo_screenheight()
		x = (sw - self.w)/2
		y = (sh - self.h)/2
		self.frame.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
		
	def change_color(self,frm):
		self.frame.configure(background=frm)

	def reset_color(self):
		self.frame.configure(background="#D9D9D9")

#oka
class RadioButtonList():			#Widget class
	def __init__(self,frm, name, ch1, ch2,st,grid,i):
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
		x=1
		for txt in name:
			self.rb[r]=Radiobutton(frm.frame,text=txt,padx = 20,variable=v,value=x, command = self.onclick)
			self.rb[r].grid(row=i+r,column=0,sticky=W,pady=2)
			r= r+1
			x=x+1
			self.r=r

	def onclick(self):
		if(self.ch1==1):
			if(self.v.get()==self.ch2):
				self.st.set_text('true')
				v.add(self.st,self.i+self.r+1)
			else:
				self.st.set_text('false')
				v.add(self.st,self.i+self.r+1)
		else:
			self.st.set_text('Your choice:'+self.shuu[self.v.get()-1])
			#v.add(self.st,self.i+self.r+1)

#oka
class Statictext():
	def __init__(self,frm,text):
		self.frame = Frame(frm.frame)
		self.frame.grid()
		self.lab=StringVar()
		self.widget= Label(frm.frame,textvariable= self.lab)
		self.lab.set(text)

	def set_text(self,name):
		self.lab.set(name)
#oka

class button():
	def __init__(self,frm,name):
		self.frame = Frame(frm.frame)
		self.frame.grid()
		self.widget = Button(frm.frame)
		self.widget.configure(text=name,fg="red")

	def bind(self,fn,*arc):
		self.widget.bind("<Button-1>",fn)
#oka
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

#oka
class CheckBox():
	def __init__(self,frm,name):
		self.frame = Frame(frm.frame)
		self.frame.grid()		
		self.var=IntVar()
		self.widget= Checkbutton(frm.frame,text=name,variable=self.var)

	def get_state(self):
		return not self.var.get()

	def bind(self,fn,*arc):
		self.widget.bind("<Button-1>",fn)

class ComboBox():
	def __init__(self,frm,hello,arg):
		self.arg=arg
		self.frame = Frame(frm.frame)
		self.frame.grid()
		var = IntVar()
		var.set(hello)
		self.widget = OptionMenu(frm.frame, var, *self.arg)
		self.widget.state = []
	def get_value(self):
		pass
    

class Alignment():
	def __init__(self,frm):
		self.frame = Frame(frm.frame)
		self.frame.grid()		

	def add(self,widget,i,j,span):
		self.widget=widget.widget
		self.widget.grid(row=i,column=j,sticky=N,columnspan=span, rowspan=1,pady=2)

class App():
	def __init__(self):
		pass
	def loop(self):
		mainloop()	



'''
win=Windows('None',400,200,500,530)
win.show_window(None)
win.change_title('waheguru')
win.move_to_center()

stat = Statictext(win)

v=Alignment()

text=SingleTextBox(win,1)

check=CheckBox(win,'do u love someone')

check1=CheckBox(win,'i am smart')

option=ComboBox(win,'chose one',['satnam','waheguru','dhan','guru','nanak'])

stat.set_text("Write your name")
v.add(stat,0,0,1)
v.add(text,1,0,1)

stat2 = Statictext(win)
stat2.set_text("chose your fav language:")
v.add(stat2,2,0,1)

stat1 = Statictext(win)

app = RadioButtonList(win,['Python','Perl','Java','C++'],0,1,stat1,3)
v.add(stat1,8,0,1)
v.add(option,9,0,1)

stat3 = Statictext(win)
stat3.set_text("chose the option u like")
v.add(stat3,10,0,1)

v.add(check,11,0,1)
v.add(check1,12,0,1)

stat4 = Statictext(win)

stat4.set_text("Write something about yourself")
v.add(stat4,13,0,1)
text1=MultiTextBox(win)
v.add(text1,14,0,1)

but=button(win,'OKAY')
v.add(but,15,0,1)
but.bind(exit,None)

mainloop()
'''


