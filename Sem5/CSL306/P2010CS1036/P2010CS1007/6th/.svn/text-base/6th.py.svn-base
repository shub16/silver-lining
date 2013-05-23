from Tkinter import *
import ttk

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
		self.var=IntVar()
    		self.widget= Checkbutton(frm.frame,text=name,variable=self.var)

	def get_state(self):
		return not self.var.get()

	def bind(self,fn,*arc):
		self.widget.bind("<Button-1>",fn)



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
			self.rb[r]=Radiobutton(frm.frame,text=txt,variable=v,value=val, command = self.onclick)
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

class Alignment():
	def __init__(self):
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
		#self.widget = Label(self.frm, image=self.ba)
		self.widget.image = self.ba
		self.widget.pack()

class FileDialog(Frame):
	def __init__(self, parent,text):
		self.sukh=parent
		self.frame = Frame(parent.frame)
		self.text=text
		self.frame.grid()

	def get_value(self):
		ftypes = [(self.text, '*.jpg')]
		dlg = tkFileDialog.Open(filetypes = ftypes)
		fl = dlg.show()
		if fl !='':
			return fl		


def main():
	win=Windows('None',0,0,500,600)
	win.show_window(None)
	win.change_title('waheguru')

	stat = Statictext(win)

	v=Alignment()

	text=SingleTextBox(win,1)

	check=CheckBox(win,'do u love someone')
	'''
	def printf(event):
		a= check.get_state()
		print a
	check.bind(printf)
	'''

	check1=CheckBox(win,'i am smart')

	option=ComboBox(win,'chose one',['satnam','waheguru','dhan','guru','nanak'])

	stat.set_text("Write your name")
	v.add(stat,0,0,1)
	v.add(text,1,0,1)

	stat2 = Statictext(win)
	stat2.set_text("chose your fav language:")
	v.add(stat2,2,0,1)

	stat1 = Statictext(win)
	app = RadioButtonList(win,[("Python",1),("Perl",2),("Java",3),("C++",4)],0,1,stat1,3)
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

	scale=Slider(win,0,0,200)
	v.add(scale,15,0,1)

	spn=SpinCtrl(win,0,0,20)
	v.add(spn,17,0,1)
	spn.get_value()
	pro=ProgressBar(win,0,100,200,1)
	v.add(pro,18,0,1)
#	pro.get_value()

	but=button(win,'OKAY')
	v.add(but,20,0,1)
	but.bind(exit,None)
	mainloop()

if __name__=='__main__':
	main()


