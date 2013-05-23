#!/usr/bin/python

import sys
from PyQt4.QtGui import *
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui, QtCore 

def main(): 
    app = QtGui.QApplication(sys.argv)
    window = CommonAPI("A4", 600, 300)
    window.CreateButton(150,20,"Button")
    window.CreateCheckBox(10,50,"Red")
    window.CreateCheckBox(10,70,"Black")
    window.CreateCheckBox(10,90,"White")
    window.CreateRadioButton(150,50,"Blue")
    window.CreateRadioButton(150,70,"Green")
    window.CreateRadioButton(150,90,"Purple")
    window.CreateTextBox(10,20)
    item = ["Hibiscus", "Dianthus", "Rose Emblem", "Tulip", "Daffodil", "Calla Lily White", "Lotus", "Primrose", "Myrtle", "Sunflower", "Jasmine"]
    window.CreateList(300,20,item)
    window.Show()
    app.exec_()
		
class CommonAPI(QWidget):
    def __init__(self, Title, Length, Breadth):
        QtGui.QWidget.__init__(self,None)
        self.setWindowTitle(Title)
        self.setGeometry(50, 50, Length, Breadth)
        palette = QPalette()
	palette.setColor(QPalette.Background,QtCore.Qt.cyan)
	self.setPalette(palette)
	        
    def CreateButton(self, xPos, yPos, Title):
	self.b1 = QPushButton(Title, self)
	self.b1.move(xPos, yPos)
	 
    def CreateCheckBox(self, xPos, yPos, Title):
	self.cb = QCheckBox(Title, self)
	self.cb.move(xPos,yPos) 
    
    def CreateRadioButton(self, xPos, yPos, Title):
	self.rb = QRadioButton(Title, self)
	self.rb.move(xPos, yPos)     
    
    def CreateTextBox(self, xPos, yPos):
	tex = QLineEdit(self)
	tex.move(xPos, yPos)

    def CreateList(self,xPos, yPos, List):
	self.lw = QListWidget(self)
	self.lw.addItems(List)
	self.lw.move(xPos,yPos)

    def Show(self):
	self.show()

if __name__ == '__main__':
    main()  
