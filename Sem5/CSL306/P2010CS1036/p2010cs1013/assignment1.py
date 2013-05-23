import sys
from PyQt4 import QtGui,QtCore
from Tkinter import *


def Tkinter_window():
   # app = wx.App()
    #app.MainLoop()
	import p2010cs1039

class bbox (QtGui.QWidget):
    def __init__(self):
        super(bbox,self).__init__()
        self.initUI()
        
    def initUI(self,parent = None):
	 QtGui.QWidget.__init__(self, parent)
         name = QtGui.QLabel('Name')
         about = QtGui.QLabel('About Yourself')
         branch= QtGui.QLabel('Sex')
         tool= QtGui.QLabel('ToolKit you prefer')
         btn1 = QtGui.QPushButton('Tkinter GUI', self);
         btn1.clicked.connect(self.buttonClicked)
         namearea = QtGui.QLineEdit()
         aboutarea = QtGui.QTextEdit(self)
	 aboutarea.resize(250,80)
         rb1 = QtGui.QRadioButton('Male', self)
         rb2 = QtGui.QRadioButton('Female', self)
         os=QtGui.QLabel('OS you work on')
         self.cb1 = QtGui.QCheckBox('Windows', self)
         self.cb2 = QtGui.QCheckBox('Linux-Ubuntu', self)
         self.cb3 = QtGui.QCheckBox('Linux-Fedora', self)
         self.cb4 = QtGui.QCheckBox('Mac', self)
         btn2 = QtGui.QPushButton('SUBMIT', self)
         btn3 = QtGui.QPushButton('CLOSE', self)
         btn3.clicked.connect(self.close)
         self.lv = QtGui.QListWidget(self)
         self.lv.addItem("Tkinter")
         self.lv.addItem("pyGTK")
         self.lv.addItem("wxPython")
         self.lv.addItem("PyQt")
         self.lv.addItem("pyFltk")
         self.lv.addItem("Pygame")
         self.lv.addItem("pyjs")
         self.lv.addItem("easyGUI")
         grid = QtGui.QGridLayout()
         grid.setSpacing(15)
         grid.addWidget(name, 1, 0)
         grid.addWidget(namearea, 1,1,1,3)
         grid.addWidget(about, 2, 0)
         grid.addWidget(aboutarea, 2, 1,1,3)
         grid.addWidget(branch, 3, 0)
         grid.addWidget(rb1, 3, 1)
         grid.addWidget(rb2, 3, 2)
         grid.addWidget(os, 4, 0)
         grid.addWidget(self.cb1, 4, 1)
         grid.addWidget(self.cb2, 4, 2)
         grid.addWidget(self.cb3, 5, 1)
         grid.addWidget(self.cb4, 5, 2)
         grid.addWidget(tool, 3, 3)
         grid.addWidget(self.lv,4,3,3,4)
         grid.addWidget(btn1, 7, 1)
         grid.addWidget(btn2, 7, 2)
         grid.addWidget(btn3, 7, 5)
         self.setLayout(grid)
         self.resize(450, 400)
	 self.setWindowTitle('UI with PyQt')
	 self.show()
	

        
    def buttonClicked(self):
        sender = self.sender()
        Tkinter_window()
        

def main():
    app = QtGui.QApplication(sys.argv)
    var = bbox()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
