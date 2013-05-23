
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
  
        button = QtGui.QPushButton('Quit', self)
        btn1 = QtGui.QPushButton('PyQt', self)
        btn2 = QtGui.QPushButton('WxPy', self)
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn1.clicked.connect(self.case_1)
        btn2.clicked.connect(self.case_2)
        button.move(90, 100) 
        btn1.move(40,40)
        btn2.move(140,40)
        self.setGeometry(299,299, 279, 169)
        self.setWindowTitle('Hello! Select Any one')
        self.show()        
        
    def case_1(self,widget):
		w=Other()
		w.__init__()

    def case_2(self):
		import wx_file
   
        
    def when_change(self, text):
        self.lbl.adjustSize()        

class Other(QtGui.QWidget):
    
    def __init__(self):
        super(Other, self).__init__()
        self.initUI()
    def initUI(self):      

        self.lbl = QtGui.QLabel(self)
        text_box = QtGui.QLineEdit(self)
        
        text_box.move(60, 20)
        self.lbl.move(1600, 40)
        button = QtGui.QPushButton('Quit', self)
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.setToolTip('Press to quit ')
        button.resize(button.sizeHint())
        button.move(80, 100) 
        self.setGeometry(299,299, 279, 169)
        self.setWindowTitle('Hello!')
        self.show()
        
        
        


    
app = QtGui.QApplication(sys.argv)
x = Example()
app.exec_()
        
        



