from Tkinter import *

#oka
class TextBox():
	def __init__(self,frm):
	        self.frame = Frame()
	        self.frame.grid()		

	def singleline(self):
		self.widget=Text(height=1,width=30,background='white')
#		self.widget.insert(INSERT, name)
#		self.widget.grid(row=i,column=1,pady=2)

	def multiline(self):
		self.widget=Text(height=10,width=30,background='white')
#		self.widget.insert(INSERT, name)
#		self.widget.grid(row=i,column=1,pady=2)

class button():
	def __init__(self,name, action):
	        self.frame = Frame()
	        self.frame.grid()
		self.widget = Button(text=name, fg="red",command= action,padx=20)

	def color_change(self):
		self.widget.configure(fg = "blue")

#oka
class check_box():
	def __init__(self,frm,name):
	        self.frame = Frame()
	        self.frame.grid()	
    		self.widget= Checkbutton(text=name)

#	def make_checkbox(self,name):		#Creating a checkbox
#    		self.widget= Checkbutton(text=name)
#		widget.grid(row=i,column=1,sticky=W,pady=2)
#oka
class ComboBox():
	def __init__(self,hello,*arg):
	        self.frame = Frame()
	        self.frame.grid()		
		optionvalue = IntVar()
        	optionvalue.set(hello)
        	self.widget = OptionMenu(self.frame, optionvalue, *arg)
        	self.widget.state = []




class window(Frame):
	def __init__(self,master=None):
#		Frame.__init__(self,master)
	        self.frame = Frame()
	        self.frame.grid()

	def show_window(self):
	        self.frame = Frame()
	        self.frame.grid(column=2)

	def title(self,master=None):
		self.frame.title("hello")

class RadioButton():			#Widget class
	def __init__(self,i,st, ch1, ch2, name):
	        self.frame = Frame()
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
			self.rb[r]=Radiobutton(text=txt,padx = 20,variable=v,value=val, command = self.onclick)
			self.rb[r].grid(row=i+r,column=0,sticky=W,pady=2)
			r= r+1
		self.r=r

	def onclick(self):
		if(self.ch1==1):
			if(self.v.get()==self.ch2):
				self.st.set_text('true')
				h.add(self.st,self.i+self.r)
			else:
				self.st.set_text('false')
				h.add(self.st,self.i+self.r)
		else:
			self.st.set_text('Your choice:'+self.shuu[self.v.get()-1][0])
			h.add(self.st,self.i+self.r)

class Halignment():
	def __init__(self):
	        self.frame = Frame()
	        self.frame.grid()		

	def add(self,widget,i):
		self.widget=widget.widget
		self.widget.grid(row=i,column=0,sticky=W,pady=2)

class Valignment():
	def __init__(self):
	        self.frame = Frame()
	        self.frame.grid()		

	def add(self,widget,i,j):
		self.widget=widget.widget
		self.widget.grid(row=i,column=j,sticky=W,pady=2)

class Statictext():
	def __init__(self,frm):
	        self.frame = Frame()
	        self.frame.grid()
		self.lab=StringVar()
		self.widget= Label(textvariable= self.lab)

	def set_text(self,name):
#		self.widget.grid(column=1,sticky=W,pady=2)
		self.lab.set(name)

win=window()

win.show_window()
#win.master.title("waheguru")

stat = Statictext(10)


text=TextBox(10)

but=button('OKAY', exit)

check=check_box(10,'do u love someone')
check1=check_box(10,'i am smart')

option=ComboBox('chose one','satnam','waheguru','dhan','guru','nanak')

h=Halignment()

stat.set_text("Write your name")
h.add(stat,0)

text.singleline()
h.add(text,1)

stat2 = Statictext(10)
stat2.set_text("chose your fav language:")
h.add(stat2,2)

stat1 = Statictext(10)
app = RadioButton(3,stat1,0,1,[("Python",1),("Perl",2),("Java",3),("C++",4)])

stat3 = Statictext(10)
stat3.set_text("chose the option u like")
h.add(stat3,9)

#check.make_checkbox('do u love someone')
h.add(check,10)

#check.make_checkbox('i am smart')
h.add(check1,11)

#option.value_list('chose one','satnam','waheguru','dhan','guru','nanak')
#h.add(option,0)

stat4 = Statictext(10)
stat4.set_text("Write something about yourself")
h.add(stat4,13)

text.multiline()
h.add(text,14)


#but.make_button()
h.add(but,15)
#but.make_button('EXIT', exit)
#h.v_Halignment(but,15,1)

mainloop()

