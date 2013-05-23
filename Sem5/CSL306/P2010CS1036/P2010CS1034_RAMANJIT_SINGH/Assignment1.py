#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sys

class Dialog_box(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(Dialog_box, self).__init__(parent)

        self.setWindowTitle("Choose a Toolkit")
        nameLabel = QtGui.QLabel("Choose one of these:")
        self.btn = QtGui.QPushButton('PyQT', self)
        self.btn.clicked.connect(self.pyqtbox)
        self.btn2 = QtGui.QPushButton('Tkinter', self)
        self.btn2.clicked.connect(self.tkbox)
        self.btn3 = QtGui.QPushButton('Close', self)
        self.btn3.clicked.connect(self.close)
        
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.btn, 0)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.btn2, 0)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.btn3, 0)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(nameLabel, 0 )
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        self.setGeometry(400,350,340, 100)
        self.setFixedSize(340, 100)

    def pyqtbox(new):

        new=QtGui.QDialog()
        new.setWindowTitle("PyQT")    																#Title of the box
        new.btn3 = QtGui.QPushButton('OK',new)												#Creating buttons and their actions
        new.btn4 = QtGui.QPushButton('Cancel',new)
        new.btn3.clicked.connect(new.close)
        new.btn4.clicked.connect(new.close)

        nameLabel2 = QtGui.QLabel("Name and Address :")								#Adding labels
        nameLabel3 = QtGui.QLabel("I am :")
        nameLabel4 = QtGui.QLabel("Date of Birth :")

        new.nameLine2 = QtGui.QTextEdit()															#Creating text box.

        new.chb1=QtGui.QCheckBox('I am a student.',new)								#Creating checkboxes.
        new.chb2=QtGui.QCheckBox('I am an employee.',new)
        new.chb3=QtGui.QCheckBox('I like reading novels.',new)
        new.chb4=QtGui.QCheckBox('I am addicted to the internet.',new)

        new.rb1=QtGui.QRadioButton('Male',new)												#Creating radio buttons.
        new.rb2=QtGui.QRadioButton('Female',new)

        new.cmb1=QtGui.QComboBox(new)																	#Creating Combo boxes.
        new.cmb2=QtGui.QComboBox(new)
        new.cmb3=QtGui.QComboBox(new)
        list=("January" , "February", "March", "April", "May", "June" , "July", "August", "September", "October", "November", "December")

        new.cmb1.addItem("Day")																				#Adding items to combo boxes.
        for i in range(1,32):
          new.cmb1.addItem(str(i))
        new.cmb2.addItem("Month")
        new.cmb2.addItems(list)
        new.cmb3.addItem("Year")
        for i in range(1940,2013):
          new.cmb3.addItem(str(i))

        new.cmb1.setStyleSheet("QComboBox { combobox-popup: 0; }")		#Combobox drop down
        new.cmb2.setStyleSheet("QComboBox { combobox-popup: 0; }")
        new.cmb3.setStyleSheet("QComboBox { combobox-popup: 0; }")

        buttonLayout2 = QtGui.QHBoxLayout()							  						#Layout of the "OK" and "Cancel" buttons.
        buttonLayout2.addStretch(1)
        buttonLayout2.addWidget(new.btn3, 0)
        buttonLayout2.addWidget(new.btn4, 0)
        new.btn3.setFocusPolicy(QtCore.Qt.NoFocus)
        new.btn4.setFocusPolicy(QtCore.Qt.NoFocus)

        radioLayout=QtGui.QHBoxLayout()                   						#Layout of the radio buttons.
        radioLayout.addWidget(new.rb1)
        radioLayout.addWidget(new.rb2)
        new.rb1.setFocusPolicy(QtCore.Qt.NoFocus)
        new.rb2.setFocusPolicy(QtCore.Qt.NoFocus)

        comboLayout=QtGui.QHBoxLayout()                   						#Layout of the combo buttons.
        comboLayout.addStretch(1)
        comboLayout.addWidget(new.cmb1,1)
        comboLayout.addWidget(new.cmb2,1)
        comboLayout.addWidget(new.cmb3,1)
        new.cmb1.setFocusPolicy(QtCore.Qt.NoFocus)
        new.cmb2.setFocusPolicy(QtCore.Qt.NoFocus)
        new.cmb3.setFocusPolicy(QtCore.Qt.NoFocus)

        checkLayout=QtGui.QVBoxLayout()                   						#Layout of the check boxes.
        checkLayout.addWidget(new.chb1)
        checkLayout.addWidget(new.chb2)
        checkLayout.addWidget(new.chb3)
        checkLayout.addWidget(new.chb4)
        new.chb1.setFocusPolicy(QtCore.Qt.NoFocus)
        new.chb2.setFocusPolicy(QtCore.Qt.NoFocus)
        new.chb3.setFocusPolicy(QtCore.Qt.NoFocus)
        new.chb4.setFocusPolicy(QtCore.Qt.NoFocus)

        mainLayout2 = QtGui.QVBoxLayout()															#Main layout
        mainLayout2.addWidget(nameLabel2, 0 )
        mainLayout2.addWidget(new.nameLine2, 0 )
        mainLayout2.addWidget(nameLabel3, 0 )
        mainLayout2.addLayout(radioLayout)
        mainLayout2.addWidget(nameLabel4, 0 )
        mainLayout2.addLayout(comboLayout)
        mainLayout2.addLayout(checkLayout)
        mainLayout2.addLayout(buttonLayout2)
        
        new.setLayout(mainLayout2)

        new.resize(400, 380)																					# new.setFixedSize(400, 380)
        new.show()
        QDialog.exec_(new)
               
        
    def tkbox(self):
        import P2010CS1007_tkinter


def main():
    app = QtGui.QApplication(sys.argv)
    Input_box = Dialog_box()
    Input_box.show()
    sys.exit(app.exec_())
    
            
if __name__ == '__main__':
    main()
