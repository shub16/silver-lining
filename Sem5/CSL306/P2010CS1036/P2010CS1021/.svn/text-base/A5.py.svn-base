#!/usr/bin/python

import sys
from PyQt4.QtGui import *
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui, QtCore 
import re

def main(): 
    window = CommonAPI("A5", 400, 300)
    T1 = window.CreateTextBox(200,20)
    T2 = window.CreateTextBox(200,70,True)
    T3 = window.CreateTextBox(200,120,True)
    T4 = window.CreateTextBox(200,170,True)
    window.CreateLabel(10,20,"ENTER USERNAME:")
    window.CreateLabel(10,70,"ENTER OLD PASSWORD:")
    window.CreateLabel(10,120,"ENTER NEW PASSWORD:")
    window.CreateLabel(10,170,"RE-ENTER NEW PASSWORD:")
    b1 = window.CreateButton(200,220,"SUBMIT!")
    window.connect(b1, QtCore.SIGNAL("clicked()"), (lambda p = [T1,T2,T3,T4] : window.GetValues(p)))
    window.Show()    
		
class CommonAPI(QWidget):
    global app
    app = QtGui.QApplication(sys.argv)
    def __init__(self, Title, Length, Breadth):
        QtGui.QWidget.__init__(self,None)
        self.setWindowTitle(Title)
        self.setGeometry(50, 50, Length, Breadth)
        palette = QPalette()
	palette.setColor(QPalette.Background,QtCore.Qt.gray)
	self.setPalette(palette)
	        
    def CreateButton(self, xPos, yPos, Title):
	self.b1 = QPushButton(Title, self)
	self.b1.move(xPos, yPos)
	return self.b1

    def GetValues(self, TextBoxes):
	Values = []
	for item in TextBoxes:
		Values.append(item.text())
	#print Values[0],Values[1],Values[2],Values[3]
	self.Validate(Values)

    def Validate(self, Values):                                     #Check for if fields are empty
	for value in Values:                         
		if not value:
			print "Fields Empty!"
			return
		else:
			continue
	self.PwdValidate(Values[2], Values[3])

    def PwdValidate(self, str1, str2):                                #Passwords constrains check
	if not str1 or not str2:
		print "Fields Empty!"
	elif len(str1) < 6:
	    	print "Password should contain more than 6 characters"
	elif str1 != str2:                   
		print "New Passwords do not Match"
	elif ((re.search("[A-Za-z]+", str1) is None) or (re.search("[0-9]+", str1) is None)) or not(str(str1).isalnum()):
		print "New Passwords should contain both alpha-numeric characters"
	else:
		print "Password changed successfully! :D"
		QtCore.QCoreApplication.instance().quit()
	 
    def CreateCheckBox(self, xPos, yPos, Title):
	self.cb = QCheckBox(Title, self)
	self.cb.move(xPos,yPos) 
    
    def CreateRadioButton(self, xPos, yPos, Title):
	self.rb = QRadioButton(Title, self)
	self.rb.move(xPos, yPos)     
    
    def CreateTextBox(self, xPos, yPos, passwd=False):
	global tex
	tex = QLineEdit(self)
	tex.move(xPos, yPos)
	if passwd == False:
		tex.setEchoMode(0)                             #Display characters as they are entered
	else:
		tex.setEchoMode(2)                             #Display asterisks instead of the characters actually entered.
	return tex

    def CreateList(self,xPos, yPos, List):
	self.lw = QListWidget(self)
	self.lw.addItems(List)
	self.lw.move(xPos,yPos)

    def CreateLabel(self,xPos,yPos,Title):
	self.lb = QLabel(Title, self)
	self.lb.move(xPos,yPos)
    
    def Show(self):
	self.show()
	app.exec_()

if __name__ == '__main__':
    main()  
