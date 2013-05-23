#!/usr/bin/python

import sys
from PyQt4.QtGui import *
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui, QtCore 
import re

def main(): 
    window = CommonAPI("A5", 900, 500)
    T1 = window.CreateTextBox(200,20)
    T2 = window.CreateTextBox(200,70,True)
    T3 = window.CreateTextBox(200,120,True)
    T4 = window.CreateTextBox(200,170,True)
    window.CreateLabel(10,20,"ENTER USERNAME:")
    window.CreateLabel(10,70,"ENTER OLD PASSWORD:")
    window.CreateLabel(10,120,"ENTER NEW PASSWORD:")
    window.CreateLabel(10,170,"RE-ENTER NEW PASSWORD:")
    b1 = window.CreateButton(200,220,"SUBMIT INFO!")
    window.connect(b1, QtCore.SIGNAL("clicked()"), (lambda p = [T1,T2,T3,T4] : window.GetValues(p)))

    window.CreateToggleButton(50, 220, "Toggle Button")
    window.CreateTextArea(50,270)
    window.CreateSlider(400, 350)
    i = CreateImage("h1.gif")
    window.AddImage(400,20,i)
    window.CreateProgressBar(400,420)
    window.CreateClock(700, 20)
    window.CreateSpinBox(600,410)
    window.Show()  
		
class CommonAPI(QWidget):
    global app
    app = QtGui.QApplication(sys.argv)
    def __init__(self, Title, Length, Breadth):
        QtGui.QWidget.__init__(self,None)
        self.setWindowTitle(Title)
        self.setGeometry(50, 50, Length, Breadth)
        palette = QPalette()
	palette.setColor(QPalette.Background,QtCore.Qt.darkGray)
	self.setPalette(palette)
	        
    def CreateButton(self, xPos, yPos, Title):                 #Button
	self.b1 = QPushButton(Title, self)
	self.b1.move(xPos, yPos)
	return self.b1

    def GetValues(self, TextBoxes):
	Values = []
	for item in TextBoxes:
		Values.append(item.text())
	#print Values[0],Values[1],Values[2],Values[3]
	self.Validate(Values)

    def Validate(self, Values):                               #Check for if fields are empty
	for value in Values:                         
		if not value:
			print "Fields Empty!"
			return
		else:
			continue
	self.PwdValidate(Values[2], Values[3])            

    def PwdValidate(self, str1, str2):                        #Passwords constrains check
	if not str1 or not str2:
		print "Fields Empty!"
	elif len(str1) < 6:
	    	print "Password should contain more than 6 characters"
	    	print "Password should contain more than 6 characters"
	elif str1 != str2:                   
		print "New Passwords do not Match"
	elif ((re.search("[A-Za-z]+", str1) is None) or (re.search("[0-9]+", str1) is None)) or not(str(str1).isalnum()):
		print "New Passwords should contain both alpha-numeric characters"
	else:
		print "Password changed successfully! :D"
		QtCore.QCoreApplication.instance().quit()
	 
    def CreateCheckBox(self, xPos, yPos, Title):                        #Check Box
	self.cb = QCheckBox(Title, self)
	self.cb.move(xPos,yPos) 
    
    def CreateRadioButton(self, xPos, yPos, Title):                      #Radio Button
	self.rb = QRadioButton(Title, self)
	self.rb.move(xPos, yPos)     
    
    def CreateTextBox(self, xPos, yPos, passwd=False):                  #Text Box
	global tex
	tex = QLineEdit(self)
	tex.move(xPos, yPos)
	if passwd == False:
		tex.setEchoMode(0)                              #Display characters as they are entered
	else:
		tex.setEchoMode(2)                              #Display asterisks instead of the characters actually entered.
	return tex

    def CreateList(self,xPos, yPos, List):                                  # List
	self.lw = QListWidget(self)
	self.lw.addItems(List)
	self.lw.move(xPos,yPos)

    def CreateLabel(self,xPos,yPos,Title):                                   #Label
	self.lb = QLabel(Title, self)
	self.lb.move(xPos,yPos)
 
    #new widgets
    def CreateToggleButton(self,xPos, yPos, Title):                          #Toggle Button
	self.b2 = QPushButton(Title, self)
	self.b2.move(xPos, yPos)
	self.b2.setCheckable(True)

    def CreateTextArea(self, xPos, yPos):                                  #Text Area
	area = QTextEdit(self)
	area.move(xPos, yPos)

    def CreateSlider(self, xPos, yPos):                                        #Slider
	sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
	sld.move(xPos, yPos)
	sld.resize(200,40)
	lcd = QtGui.QLCDNumber(self)
	sld.valueChanged.connect(lcd.display)
	lcd.move(xPos+120, yPos-20)

    def AddImage(self,xPos,yPos,Path):                                          #Image
	pixmap = QtGui.QPixmap(Path)
	lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
	lbl.move(xPos, yPos)  

    def CreateProgressBar(self, xPos, yPos):                                  #Progress Bar
	self.pbar = QtGui.QProgressBar(self)
	self.pbar.move(xPos, yPos)        
        self.step = 75
	self.pbar.setValue(self.step)  

    def CreateClock(self, xPos, yPos):                                       #Clock
	global x
	global y
	x = xPos
	y = yPos
	timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()

    def showTime(self):
	global x
	global y
	lcd = QtGui.QLCDNumber(self)
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ':' + text[3:]
	lcd.resize(150,60)
        lcd.display(text)
	lcd.move(x, y)
		
    def CreateSpinBox(self,xPos,yPos):                                                  #Spin Box
	spin = QtGui.QSpinBox(self)    
        spin.move(xPos,yPos)
	spin.resize(60,40)

    def CreateDialogBox(self,Text):                                                      #Dialog Box
	reply = QtGui.QMessageBox.warning(self, "" ,Text)
        
    def Show(self):
	self.show()
	app.exec_()

def CreateImage(Path):
	return Path

if __name__ == '__main__':
    main()  
