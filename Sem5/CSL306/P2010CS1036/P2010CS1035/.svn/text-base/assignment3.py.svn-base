
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

class Example(QtGui.QWidget):
    
    def __init__(self):
		super(Example, self).__init__()

		cb = QtGui.QCheckBox('PyQt', self)
		cb1 = QtGui.QCheckBox('WxPy', self)
		cb.move(10, 20)
		cb1.move(10, 40)
		cb.stateChanged.connect(self.case_1)
		cb1.stateChanged.connect(self.case_2)
		button = QtGui.QPushButton('Quit', self)
		btn1 = QtGui.QPushButton('PyQt', self)
		btn2 = QtGui.QPushButton('WxPy', self)
		button.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn1.clicked.connect(self.case_1)
		btn2.clicked.connect(self.case_2)
		button.move(80, 110) 
		btn1.move(150,20)
		btn2.move(150,50)
        
		combo = QtGui.QComboBox(self)
		listt=["Ubuntu","Fedora","Mandriva","Red hat","Gentoo"]
		combo.addItems(listt)

		combo.move(150, 80)
        
		self.setGeometry(299,299, 279, 169)
		self.setWindowTitle('The Collection!!!')
        
		rbtn=QtGui.QRadioButton('RB1',self)
		rbtn.move(90,20)
		rbtn2=QtGui.QRadioButton('RB2',self)
		rbtn2.move(90,40)
		self.setGeometry(300, 300, 250, 150)
        
		self.show()
        
    def case_1(self):
		w=Other()
		w.__init__()

    def case_2(self):
		import wx_file
	
		
	
  
	
		
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
def main():
    
    app = QtGui.QApplication(sys.argv)
#    w=MyWindow()
    
    ex = Example()
	
	
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
