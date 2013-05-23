import sys
from PyQt4 import QtGui,QtCore
from Tkinter import *
import assign2

def tkinter_window():
        root = Tk()
	app = assign2.App(root)
	root.mainloop()
class GridLayout2(QtGui.QWidget):
     def __init__(self, parent=None):
         QtGui.QWidget.__init__(self, parent)
         name = QtGui.QLabel('Name')
         email = QtGui.QLabel('Email')
         branch= QtGui.QLabel('Sex:')
         city= QtGui.QLabel('CITY:')
         tkinter= QtGui.QLabel('Tkinter Gui')
         btn1 = QtGui.QPushButton('Tkinter', self);
    	 btn1.clicked.connect(self.buttonClicked)
         nameEdit = QtGui.QLineEdit()
         emailEdit = QtGui.QLineEdit()
         rb1 = QtGui.QRadioButton('Male', self)
         rb2 = QtGui.QRadioButton('Female', self)
         qualification=QtGui.QLabel('Qualification:')
         self.cb1 = QtGui.QCheckBox('X', self)
         self.cb2 = QtGui.QCheckBox('XII', self)
         self.cb3 = QtGui.QCheckBox('Graduation', self)
         self.cb4 = QtGui.QCheckBox('PostGraduation', self)
         btn2 = QtGui.QPushButton('SUBMIT', self)
         btn3 = QtGui.QPushButton('EXIT', self)
         btn3.clicked.connect(self.close)
         self.lv = QtGui.QListWidget(self)
         self.lv.addItem("NEW DELHI")
         self.lv.addItem("CHANDIGARH")
         self.lv.addItem("MUMBAI")
         self.lv.addItem("ALIGARH")
         self.lv.addItem("BANGLORE")
         self.lv.addItem("CHENNAI")
         self.lv.addItem("KOLKATA")
         self.lv.addItem("JAIPUR")
         grid = QtGui.QGridLayout()
         grid.setSpacing(15)
         grid.addWidget(name, 1, 0)
         grid.addWidget(nameEdit, 1, 1,1,3)
         grid.addWidget(email, 2, 0)
         grid.addWidget(emailEdit, 2, 1,1,3)
         grid.addWidget(branch, 3, 0)
         grid.addWidget(rb1, 3, 1)
         grid.addWidget(rb2, 3, 2)
         grid.addWidget(qualification, 4, 0)
         grid.addWidget(self.cb1, 4, 1)
         grid.addWidget(self.cb2, 4, 2)
         grid.addWidget(self.cb3, 5, 1)
         grid.addWidget(self.cb4, 5, 2)
         grid.addWidget(city, 5, 3)
         grid.addWidget(self.lv,5,4,3,4)
         grid.addWidget(tkinter, 6, 0)
         grid.addWidget(btn1, 6, 1)
         grid.addWidget(btn2, 7, 1)
         grid.addWidget(btn3, 7, 2)
         self.setLayout(grid)
         self.resize(450, 400)
     def buttonClicked(self):       
         sender = self.sender()
         tkinter_window()
         
def main():
    app = QtGui.QApplication(sys.argv)
    ex = GridLayout2()
    ex.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        
