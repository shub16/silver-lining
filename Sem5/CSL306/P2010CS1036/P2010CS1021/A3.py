#!/usr/bin/python

import sys
from PyQt4.QtGui import *
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui, QtCore 

def main(): 
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    app.exec_()
		
class MyWindow(QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
       
	self.b1 = QPushButton('PyQt', self)
	self.b1.move(20, 50)
	self.A1=Asg1()
	self.b1.clicked.connect(self.A1.mycode)

	self.b2 = QPushButton('Tkinter', self)
	self.b2.move(150, 50)
	self.b2.clicked.connect(self.othercode)

	self.b3 = QPushButton('Fltk', self)
	self.b3.move(20, 90)
	self.b3.clicked.connect(self.othercode1)

	self.b4 = QPushButton('Exit', self)
	self.b4.move(150, 90)
	self.b4.clicked.connect(QtCore.QCoreApplication.instance().quit)

	palette = QPalette()
	palette.setColor(QPalette.Background,QtCore.Qt.darkRed)
	self.setPalette(palette)
	self.setGeometry(200, 200, 250, 200)
        self.setWindowTitle('Assignment 3')    
        self.show()

    def othercode(self):
	import asg1

    def othercode1(self):
	from lab1 import ex1
	q=ex1()
  
class Asg1(QWidget):
    def mycode(self):
        QtGui.QWidget.__init__(self)

	text = QLineEdit(self)
	text.move(20,50)

	self.button = QPushButton('Hello', self)
        self.button.move(150, 50)

	self.cb = QCheckBox('Red', self)
	self.cb.move(20,90)

	self.rb = QRadioButton('Blue', self)
	self.rb.move(20,130)

	self.lw = QListWidget(self)
	item = ["Hibiscus", "Dianthus", "Rose Emblem", "Tulip", "Daffodil", "Calla lily white"]
	self.lw.addItems(item)
	self.lw.move(150,90)
	
	palette = QPalette()
	palette.setColor(QPalette.Background,QtCore.Qt.cyan)
	self.setPalette(palette)
	self.setGeometry(200, 200, 450, 300)
        self.setWindowTitle('Hello!')  
	self.show()

if __name__ == '__main__':
    main()
