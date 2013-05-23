#!/usr/bin/python 
#Python program for implementing a GUI for changing passwords

from Tkinter import *
import sys, string, calendar
import Tkinter as tk
import time

#Callback function to be called when the button is clicked
def profileInfo(userName,password,calendar,radiobuttons,scale,text,lst,spinbox,checkbox):
	user = userName.getValue()
	passwd = password.getValue()
	dob = calendar.getValue()
	gender = radiobuttons.getValue()
	height = scale.getValue()
	about = text.getValue()
	lang = lst.getValue()
	ans = spinbox.getValue()
	notify = checkbox.getValue()
	if(user==""):
		user = "Anonymous"
	if(passwd==""):
		print "Please enter the password"
		return
	else:
		if(len(about)==1):
			about = "I am a ...(Default text)"
		if(ans!="20"):
			print "Please enter the correct answer"
			return
		else:
			print "-------------------------------------------------------------------"
			print "Welcome "+user
			print "Your password is "+passwd
			print "Your date of birth is:"
			print dob
			print "Your approx height (in fts) is:"
			print height
			print "About yourself:\n"+about
			print "Your preferred computer language is "+lang
			if(notify=="Yes"):
				print "We will be happy to notify you about our endeavours"
			print "Congratulations! Your information has been successfully submitted"
			print "-------------------------------------------------------------------"
 
#Creating the widgets using the API functions
def createWidgets(obj):
	widgets = []

	#Creating a label
	obj.headLabel = LabelWidget(obj,"Password and answer to the verifying question are necessary")
	widgets.append(obj.headLabel.getWidget())

	#Creating label and entry field for username
	obj.userNameLabel = LabelWidget(obj,"Name:")
	widgets.append(obj.userNameLabel.getWidget())	
	obj.userName = TextLineWidget(obj)
	widgets.append(obj.userName.getWidget())

	#Creating label and entry field for new password
	obj.passwordLabel = LabelWidget(obj,"Password*:")
	widgets.append(obj.passwordLabel.getWidget())	
	obj.password = PasswordWidget(obj)
	widgets.append(obj.password.getWidget())
	
	#Creating label and calendar
	obj.bdayLabel = LabelWidget(obj,"Birth Date:")
	widgets.append(obj.bdayLabel.getWidget())
	obj.cd = CalendarWidget(obj)
	lst = obj.cd.getWidget()
	for item in lst:
		widgets.append(item)
	
	#Creating label and radiobuttons
	obj.genderLabel = LabelWidget(obj,"Gender:")
	widgets.append(obj.genderLabel.getWidget())
	obj.radiobuttons = RadioButtonsWidget(obj,["Male","Female"])
	radioList = obj.radiobuttons.getWidget()
	for item in radioList:
		widgets.append(item)

	#Creating label and slider for height
	obj.sliderLabel = LabelWidget(obj,"Height(in fts):")
	widgets.append(obj.sliderLabel.getWidget())
	obj.slider = SliderWidget(obj,1,7)
	widgets.append(obj.slider.getWidget())	

	#Creating label and textbox
	obj.textLabel = LabelWidget(obj,"About yourself:")
	widgets.append(obj.textLabel.getWidget())
	obj.text = TextBoxWidget(obj)
	widgets.append(obj.text.getWidget())
	
	#Creating label and list
	obj.listLabel = LabelWidget(obj,"Your preferred computer language:")
	widgets.append(obj.listLabel.getWidget())
	obj.lst = ListWidget(obj,["Java","C","C++","Python","Pascal","Fortran","Ada","JavaScript","PHP","HTML","CSS"])
	widgets.append(obj.lst.getWidget())

	#Creating label and spinbox
	obj.spinLabel = LabelWidget(obj,"Solve - 10*2, Your Answer*:")
	widgets.append(obj.spinLabel.getWidget())
	obj.spinbox = SpinBoxWidget(obj,1,100)
	widgets.append(obj.spinbox.getWidget())
	
	#Creating a check-box
	obj.checkbox = CheckBoxWidget(obj,"Do you want us to send you notifications?")
	widgets.append(obj.checkbox.getWidget())

	#Creating a "Submit" button
	obj.button = ButtonWidget(obj,"Submit",profileInfo,obj.userName,obj.password,obj.cd,obj.radiobuttons,obj.slider,obj.text,obj.lst,obj.spinbox,obj.checkbox)
	widgets.append(obj.button.getWidget())

	#Return the list of widgets
	return widgets

#Class for creating text-line widget
class TextLineWidget:
	def __init__(self,parent):
		self.entry = Entry(parent.frame)
	
	def getValue(self):
		value = self.entry.get()
		return value

	def getWidget(self):
		return self.entry 

#Class for creating button widget
class ButtonWidget:
	def __init__(self,parent,name,function,*args):
		self.button = Button(parent.frame, text=name,command=lambda event=self:function(*args))

	def getWidget(self):
		return self.button

#Class for creating checkbox widget
class CheckBoxWidget:
	def __init__(self,parent,name):
		self.checkVar = StringVar()
		self.checkbox = Checkbutton(parent.frame, text=name, variable=self.checkVar,onvalue="Yes",offvalue="No")

	def getValue(self):
		return self.checkVar.get()

	def getWidget(self):
		return self.checkbox

#Class for creating radio-buttons widget
class RadioButtonsWidget:
	def __init__(self,parent,labels):
		self.radioVar = StringVar()
		self.radiobuttons = []
		for radio_label in labels:
			radiobutton = Radiobutton(parent.frame, text=radio_label, variable=self.radioVar, value=radio_label)
			self.radiobuttons.append(radiobutton)		

	def getValue(self):
		return self.radioVar

	def getWidget(self):
		return self.radiobuttons

#Class for creating list widget
class ListWidget:
	def __init__(self,parent,values):			#Function for creating list of values using Listbox widget
		self.listbox = Listbox(parent.frame)
		for item in values:
			self.listbox.insert(END, item)

	def getValue(self):
		items = self.listbox.curselection()
		if(len(items)!=0):				#Getting the number of items selected (It could be 0 or 1)
			data = self.listbox.get(items)
		else:
			data = "Java"
		return data

	def getWidget(self):
		return self.listbox

#Class for creating label widget
class LabelWidget:
	def __init__(self,parent,title):
		self.label = Label(parent.frame,text = title) 		
		
	def getWidget(self):
		return self.label

#Class for creating password widget
class PasswordWidget:
	def __init__(self,parent):
		self.passwd = Entry(parent.frame,show="*")
	
	def getValue(self):
		value = self.passwd.get()
		return value
	
	def getWidget(self):
		return self.passwd
	
#Class for creating Spinbox widget
class SpinBoxWidget:
	def __init__(self,parent,fromValue,toValue):
		self.spin = Spinbox(parent.frame, from_ = fromValue, to = toValue)
	
	def getValue(self):
		value = self.spin.get()
		return value

	def getWidget(self):
		return self.spin

#Class for creating text widget
class TextBoxWidget:
	def __init__(self,parent):
		self.text = Text(parent.frame)
	
	def getValue(self):
		value = self.text.get(1.0,END)
		return value

	def getWidget(self):
		return self.text

#Class for creating slider widget
class SliderWidget:
	def __init__(self,parent,fromValue,toValue):
		self.slider = Scale(parent.frame,from_=fromValue,to=toValue,orient=HORIZONTAL,resolution=0.1)

	def getValue(self):
		return self.slider.get()

	def getWidget(self):
		return self.slider	

#Class for creating calendar widget
class CalendarWidget():
	def __init__(self,parent):
		self.year = time.localtime()[0]
		self.month = time.localtime()[1]
		self.day =time.localtime()[2]
		self.strdate = (str(self.year) +  "/" + str(self.month) + "/" + str(self.day))
		self.parent = parent		
		self.mainFrame()

	def mainFrame(self):
		self.date_var = tk.StringVar()		
		self.date_var.set(self.strdate) 
		self.label = tk.Label(self.parent.frame, textvariable= self.date_var, bg = "white")
		self.testBtn = tk.Button(self.parent.frame, text = 'getdate',command = self.fnCalendar)
	
	def getWidget(self):
		self.lst = []
		self.lst.append(self.label)
		self.lst.append(self.testBtn)
		return self.lst

	def getValue(self):
		return self.date_var.get()

	def fnCalendar(self):
		tkCalendar(self.parent.frame, self.year, self.month, self.day, self.date_var )

#Class for creating pop-up calendar using canvas
class tkCalendar:
  def __init__ (self, master, arg_year, arg_month, arg_day, 
	    arg_parent_updatable_var): 
    self.fnta = ("Times", 12)
    self.fnt = ("Times", 14)
    self.fntc = ("Times", 18, 'bold')

    self.lang="engl"
 
    self.strtitle = "Calendar"
    self.strdays = "Su  Mo  Tu  We  Th  Fr  Sa"
    self.dictmonths = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May',
	'6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov',
	'12':'Dec'}
    self.update_var = arg_parent_updatable_var
    top = self.top = tk.Toplevel(master)
    try : self.intmonth = int(arg_month)
    except: self.intmonth = int(1)
    self.canvas =tk.Canvas (top, width =200, height =220,
      relief =tk.RIDGE, background ="white", borderwidth =1)
    self.canvas.create_rectangle(0,0,303,30, fill="#a4cae8",width=0 )
    self.canvas.create_text(100,17, text=self.strtitle,  font=self.fntc, fill="#2024d6")
    stryear = str(arg_year)

    self.year_var=tk.StringVar()
    self.year_var.set(stryear)
    self.lblYear = tk.Label(top, textvariable = self.year_var, 
	    font = self.fnta, background="white")
    self.lblYear.place(x=85, y = 30)

    self.month_var=tk.StringVar()
    strnummonth = str(self.intmonth)
    strmonth = self.dictmonths[strnummonth]
    self.month_var.set(strmonth)

    self.lblYear = tk.Label(top, textvariable = self.month_var, 
	    font = self.fnta, background="white")
    self.lblYear.place(x=85, y = 50)
    #Variable muy usada
    tagBaseButton = "Arrow"
    self.tagBaseNumber = "DayButton"
    #draw year arrows
    x,y = 40, 43
    tagThisButton = "leftyear"  
    tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
    self.fnCreateLeftArrow(self.canvas, x,y, tagFinalThisButton)
    x,y = 150, 43
    tagThisButton = "rightyear"  
    tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
    self.fnCreateRightArrow(self.canvas, x,y, tagFinalThisButton)
    #draw month arrows
    x,y = 40, 63
    tagThisButton = "leftmonth"  
    tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
    self.fnCreateLeftArrow(self.canvas, x,y, tagFinalThisButton)
    x,y = 150, 63
    tagThisButton = "rightmonth"  
    tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
    self.fnCreateRightArrow(self.canvas, x,y, tagFinalThisButton)
    #Print days 
    self.canvas.create_text(100,90, text=self.strdays, font=self.fnta)
    self.canvas.pack (expand =1, fill =tk.BOTH)
    self.canvas.tag_bind ("Arrow", "<ButtonRelease-1>", self.fnClick)
    self.canvas.tag_bind ("Arrow", "<Enter>", self.fnOnMouseOver)
    self.canvas.tag_bind ("Arrow", "<Leave>", self.fnOnMouseOut)   
    self.fnFillCalendar()

  def fnCreateRightArrow(self, canv, x, y, strtagname):
    canv.create_polygon(x,y, [[x+0,y-5], [x+10, y-5] , [x+10,y-10] , 
		[x+20,y+0], [x+10,y+10] , [x+10,y+5] , [x+0,y+5]],
		tags = strtagname , fill="blue", width=0)

  def fnCreateLeftArrow(self, canv, x, y, strtagname):
    canv.create_polygon(x,y, [[x+10,y-10], [x+10, y-5] , [x+20,y-5] , 
		[x+20,y+5], [x+10,y+5] , [x+10,y+10] ],
		tags = strtagname , fill="blue", width=0)

  def fnClick(self,event):
    owntags =self.canvas.gettags(tk.CURRENT)
    if "rightyear" in owntags:
	intyear = int(self.year_var.get())
	intyear +=1
	stryear = str(intyear)
	self.year_var.set(stryear)
    if "leftyear" in owntags:
	intyear = int(self.year_var.get())
	intyear -=1
	stryear = str(intyear)
	self.year_var.set(stryear)
    if "rightmonth" in owntags:
	if self.intmonth < 12 :
	    self.intmonth += 1 
	    strnummonth = str(self.intmonth)
	    strmonth = self.dictmonths[strnummonth]
	    self.month_var.set(strmonth)
	else :
	    self.intmonth = 1 
	    strnummonth = str(self.intmonth)
	    strmonth = self.dictmonths[strnummonth]
	    self.month_var.set(strmonth)
	    intyear = int(self.year_var.get())
	    intyear +=1
	    stryear = str(intyear)
	    self.year_var.set(stryear)
    if "leftmonth" in owntags:
	if self.intmonth > 1 :
	    self.intmonth -= 1 
	    strnummonth = str(self.intmonth)
	    strmonth = self.dictmonths[strnummonth]
	    self.month_var.set(strmonth)
	else :
	    self.intmonth = 12
	    strnummonth = str(self.intmonth)
	    strmonth = self.dictmonths[strnummonth]
	    self.month_var.set(strmonth)
	    intyear = int(self.year_var.get())
	    intyear -=1
	    stryear = str(intyear)
	    self.year_var.set(stryear)
    self.fnFillCalendar()	    
    
  def fnFillCalendar(self):
    init_x_pos = 20
    arr_y_pos = [110,130,150,170,190,210]
    intposarr = 0
    self.canvas.delete("DayButton")
    self.canvas.update()
    intyear = int(self.year_var.get())
    monthcal = calendar.monthcalendar(intyear, self.intmonth)    
    for row in monthcal:
	xpos = init_x_pos 
	ypos = arr_y_pos[intposarr]
	for item in row:	
	    stritem = str(item)
	    if stritem == "0":
		xpos += 27
	    else :
		tagNumber = tuple((self.tagBaseNumber,stritem))
		self.canvas.create_text(xpos, ypos , text=stritem, 
		    font=self.fnta,tags=tagNumber)	
    		xpos += 27
	intposarr += 1
    self.canvas.tag_bind ("DayButton", "<ButtonRelease-1>", self.fnClickNumber)
    self.canvas.tag_bind ("DayButton", "<Enter>", self.fnOnMouseOver)
    self.canvas.tag_bind ("DayButton", "<Leave>", self.fnOnMouseOut)   

  def fnClickNumber(self,event):
    owntags =self.canvas.gettags(tk.CURRENT)
    for x in owntags:
	if (x == "current") or (x == "DayButton"): pass
	else : 
	    strdate = (str(self.year_var.get()) + "/" + 
		    str(self.intmonth) + "/" +  
		    str(x)) 
	    self.update_var.set(strdate)
	    self.top.withdraw()
  def fnOnMouseOver(self,event):
    self.canvas.move(tk.CURRENT, 1, 1)
    self.canvas.update()

  def fnOnMouseOut(self,event):
    self.canvas.move(tk.CURRENT, -1, -1)
    self.canvas.update()

#Class for creating the layout by taking the list of widgets
class WindowLayout:
	def __init__(self,parent,height,width):		#Initializing function for creating all widgets within a parent frame
		self.frame = parent
	 
	def createLayout(self,lstWidgets):		#Creating the layout by placing the widgets according to the options given by the user
		rowValue = 0				#Initial row
		columnValue = 0				#Initial column
		length = len(lstWidgets)		#Number of widgets to be placed
		places = [2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,2]	#List of placement of widgets
		if(length == 0):			#If there is no widget created yet
			print "You haven't created any widgets"
		else:
			lstWidgets[0].grid(row=rowValue,column=columnValue)
			for i in range(1,length,1):
				widget = lstWidgets[i]
				#place = raw_input("Enter 1 for putting widget in same line and 2 for next line:\n")
				#place = int(place)
				place = places[i-1]
				if(place == 1):		#Placing the widget in same line
					columnValue = columnValue+1
				elif(place == 2):	#Placing the widget in next line
					rowValue = rowValue+1
					columnValue = 0
				widget.grid(row=rowValue,column=columnValue)	

def main():
	root = Tk()
	root.title('My Profile')
	height = 400 
	width = 300
	obj = WindowLayout(root,height,width)
	lstWidgets = createWidgets(obj)
	obj.createLayout(lstWidgets)
	root.mainloop()	

if __name__ =="__main__":
	main()
