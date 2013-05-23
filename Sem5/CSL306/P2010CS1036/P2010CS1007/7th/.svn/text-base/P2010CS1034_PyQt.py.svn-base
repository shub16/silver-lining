#!/usr/bin/env python
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sys

class App(QtGui.QApplication):													#App:- start and loop an application
	def __init__(self):
		super(App,self).__init__(sys.argv)
			
	def loop(self):
		return sys.exit(self.exec_())

class Windows(QtGui.QWidget):														#class for making a window:- x & y=position; width & height=window size 
	def __init__(self,title,x,y,width,height):						# constructor
		super(Windows, self).__init__(parent=None)
		self.setWindowTitle(title)
		self.setGeometry(x,y,width,height)
		
	def show_window(self,box):														#setlayout and show window
		self.setLayout(box)
		self.show()
	
	def change_title(self,title):
		self.setWindowTitle(title)		

	def move_to_centre(self):															# for centring a window on screen
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
		
	def close_window(self):																# for closing window
		self.close()
	
	def change_color(self,color):													# change color of window
		self.setStyleSheet("QWidget {background-color: %s; }"%color)
	
	def reset_color(self):
		self.setStyleSheet("QWidget {background-color: %s; }"%None)

class Statictext(QtGui.QLabel):													#Statictext:- text=to make label ,frm=parent window
	def __init__(self,frm,text):													#constructor
		super(Statictext, self).__init__(text)
		
	def set_text(self,text):
		self.setText(text)

class button(QtGui.QPushButton):												#button:- name=name of the button; frm=parent window; text=name of button
	def __init__(self,frm,text):													#method= function to call on clicking; *args=arguments of function
		super(button, self).__init__(text)
		self.setFocusPolicy(QtCore.Qt.NoFocus)
			
	def bind(self,method,*args):													#bind:- binding button to function
		if (method!=None and not args) or (method!=None and args[0]==None):
			self.clicked.connect(method)
		elif (method!=None and args!=None):
			self.connect(self,QtCore.SIGNAL('clicked()'),(lambda x = args : method(*x)))

class CheckBox(QtGui.QCheckBox):												#CheckBox:- text=checkbox label; frm=parent window; (value=true or false for activating or deactivating initially)
	def __init__(self,frm,text):													#constructor
		super(CheckBox, self).__init__(text)
		self.setFocusPolicy(QtCore.Qt.NoFocus)

	def get_state(self):																	#state(check/uncheck) of checkbox
		return self.checkState()
	
	def bind(self,method,*args):													#binding to some function
		if (method!=None and not args) or (method!=None and args[0]==None):
			self.clicked.connect(method)
		elif (method!=None and args!=None):
			self.connect(self,QtCore.SIGNAL('clicked()'),(lambda x = args : method(x)))

class ComboBox(QtGui.QComboBox):												#ComboBox:- name=name of combobox;frm=parent window; group=items to add in combobox
	def __init__(self,frm,name,group):										#constructor
		super(ComboBox, self).__init__()
		self.setFocusPolicy(QtCore.Qt.NoFocus)
		self.setStyleSheet("QComboBox { combobox-popup: 0; }")
		if(name!=None):
			self.addItem(name)
		for i in group:
			self.addItem(str(i))
	
	def get_value(self):																	#get selected text
		return self.currentText()

class MultiTextBox(QtGui.QTextEdit):										#MultiTextBox:-multi-line text box; frm=parent window
	def __init__(self,frm):																#constructor
		super(MultiTextBox,self).__init__()
	
	def set_text(self,text):
		self.setText(text)
	
	def get_text(self):
		return self.toPlainText()

class SingleTextBox(QtGui.QLineEdit):										#SingleTextBox:-single-line text box; frm=parent window; visibility= 0/1 for password_protected/normal mode
	def __init__(self,frm,visibility):										#constructor
		super(SingleTextBox,self).__init__()
		if visibility==0:
			self.setEchoMode(self.Password)
		else:
			pass

	def set_text(self,text):
		self.setText(text)
	
	def get_text(self):
		return self.text()

class RadioButtonList(QtGui.QButtonGroup):							#radiobuttonlist:- group=radio button labels
	def __init__(self,frm,group,ch1,ch2,st,grid,start):		#frm=parent window; ch1=0/1 for info/question; ch2=true answer's no.; st=label; i=row of starting radiobuttons
		super(RadioButtonList,self).__init__()
		self.rb={}
		self.group=group
		self.i=len(group)
		self.x=ch1
		self.y=ch2-1
		self.text=st
		for i in range(0,len(group)):
			self.rb[i]=QtGui.QRadioButton(group[i])
			self.rb[i].setFocusPolicy(QtCore.Qt.NoFocus)
			self.rb[i].connect(self.rb[i],QtCore.SIGNAL('clicked()'),self.onclick)
			self.addButton(self.rb[i],i)
			grid.add(self.rb[i],start+i,0,1)

	def onclick(self):
		self.check=self.checkedId()
		if self.x==1:
			if self.check==self.y:
				self.text.set_text("True")
			else:
				self.text.set_text("False")
		elif self.x==0:
			self.text.set_text( " Selected : " + self.group[self.checkedId()] )

class Halignment(QtGui.QHBoxLayout):										#horizontal box:-alignment= left/right/center alignment of widgets;
	def __init__(self,*alignment):												#	 list=list of widget/layout; i=row of starting radiobuttons
		super(Halignment,self).__init__()
		if alignment and alignment[0]=="right":
			self.setAlignment(QtCore.Qt.AlignRight)
		elif alignment and alignment[0]=="left":
			self.setAlignment(QtCore.Qt.AlignLeft)
		else:
			self.setAlignment(QtCore.Qt.AlignHCenter)
	
	def add(self,item,i):
		if(item.isWidgetType()==True):
				self.addWidget(item)
		elif(item.isWidgetType()==False):
				self.addLayout(item)

class Valignment(QtGui.QVBoxLayout):										#vertical box:- list=items to add in vbox; i=row of starting radiobuttons
		def __init__(self):
			super(Valignment,self).__init__()

		def add(self,item,i):
			if(item.isWidgetType()==True):
				self.addWidget(item)
			elif(item.isWidgetType()==False):
				self.addLayout(item)

class Alignment(QtGui.QGridLayout):											#alignment:- making grid; widget=to add to grid; row=row number; column=column number; cspan=colunm span
	def __init__(self,parent):
		super(Alignment,self).__init__()
		
	def add(self,widget,row,column,cspan):
			if(widget.isWidgetType()==True):
				self.addWidget(widget,row,column,1,cspan)
			elif(widget.isWidgetType()==False):
				self.addLayout(widget,row,column,1,cspan)







				
class SpinCtrl(QtGui.QSpinBox):												#SpinCtrl: frame=parent; value=initial value; minv=minimum value; maxv=maximum value
	def __init__(self,frame,value,minv,maxv):
		super(SpinCtrl,self).__init__()
		self.setFocusPolicy(QtCore.Qt.NoFocus)
		self.setMinimum(minv)
		self.setMaximum(maxv)
		self.setValue(value)
		#self.setFixedSize(60,25)
	
	def get_value(self):																# get value in the box
		return self.value()


class Slider(QtGui.QSlider):													#Slider: frame=parent; value=initial value; minv=minimum value; maxv=maximum value
	def __init__(self,frame,value,minv,maxv):
		super(Slider,self).__init__(QtCore.Qt.Horizontal)
		self.setFocusPolicy(QtCore.Qt.NoFocus)
		self.setMinimum(minv)
		self.setMaximum(maxv)
		self.setValue(value)
		self.setToolTip("Slider")
		self.setFixedSize(200,25)		
		
	def get_value(self):																# get value of the slider
		return self.value()
	
	
class ProgressBar(QtGui.QProgressBar):								#Progress Bar: frame=parent; value=initial value; rang=maximum value; width=widget's width; height=widget's height
	def __init__(self,frame,value,rang,width,height):
		super(ProgressBar,self).__init__()
		self.setFocusPolicy(QtCore.Qt.NoFocus) 
		self.setRange(0,rang)
		self.setValue(value)
		self.resize(width,height)
		self.setFixedSize(width,height)
		self.startTimer(100)
		
	def get_value(self):																# get value of the position of progressbar
		return self.value()
		
	def set_value(self,value):													# set value of progressbar
		self.setValue(value)
		
class image(QtGui.QLabel):														#image:- frm=parent window; path=path of the image
	def __init__(self,frm):
		super(image,self).__init__()
		
	def set_image(self,path):
		image=QtGui.QPixmap(path)
		size=QtCore.QSize(10,30)
		#print size
		#print image.height()
		#image.scaled(size,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation)
		self.setPixmap(image)

class FileDialog(QtGui.QFileDialog):									#FileDialog:- frame=parent window; text=title of dialog box
	def __init__(self,frame,text):
		super(FileDialog,self).__init__()
		self.frame=frame
	
	def get_value(self):
		path = QtGui.QFileDialog.getOpenFileName(self.frame, 'Choose a file','/home/ramanjit/Desktop/4/Assign7/')
		return path
		
		
	


