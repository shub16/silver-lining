'''using PyQt environment This file has been edited please see diff file'''


#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

class Dialog_box(QtGui.QWidget):
    
    def __init__(self,parent,title,width,height):
        super(Dialog_box, self).__init__(parent)
        self.app = QtGui.QApplication(sys.argv)
        self.setWindowTitle(title)    
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.resize(width, height)

    def addButton(self,title):
        btn = QtGui.QPushButton(title, self)
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(btn, 0)
        self.mainLayout.addLayout(buttonLayout)
        return btn

    def addTextArea(self,title):
        nameLabel = QtGui.QLabel(title)
        self.nameLine = QtGui.QTextEdit()
        self.mainLayout.addWidget(nameLabel, 0 )
        self.mainLayout.addWidget(self.nameLine, 0 )
        return nameLabel

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Input_box = Dialog_box(None,"Input",220,400)
    Input_box.addTextArea("Name and Address:")
    Input_box.addButton("okay")
    Input_box.show()
    app.exec_()
