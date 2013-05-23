import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
 

class Example(QtGui.QWidget):
    def myold(self):

        QtGui.QWidget.__init__(self)
        self.button1 = QtGui.QPushButton('Button', self)
        self.button1.move(20, 30)       

	self.button3 = QtGui.QPushButton('Close',self)
	self.button3.move(120,30)
	self.button3.clicked.connect(QtCore.QCoreApplication.instance().quit)

	self.qle = QtGui.QLineEdit(self)
	self.qle.move(40,70)        

        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Assignment 2')  
	self.show()
    
class New(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.button1 = QtGui.QPushButton('Other', self)
	self.button1.move(10, 30)
        self.button1.clicked.connect(self.otherCode)

	self.button2 = QtGui.QPushButton('MY ', self)
	self.button2.move(110, 30)   
	self.myobj = Example()
	self.button2.clicked.connect(self.myobj.myold) 	

	self.button3 = QtGui.QPushButton('Close',self)
	self.button3.move(210,30)
	self.button3.clicked.connect(QtCore.QCoreApplication.instance().quit)

	self.checkBox1 = QtGui.QCheckBox('Cycling', self)
	self.checkBox2 = QtGui.QCheckBox('Swimming', self)
	self.checkBox3 = QtGui.QCheckBox('Jogging', self)
	
	self.checkBox1.move(110 , 80)
	self.checkBox2.move(110 , 100)
	self.checkBox3.move(110 , 120)

	self.radioButton1 = QtGui.QRadioButton('Male' , self)
	self.radioButton1.move(10 , 80)

	self.radioButton2 = QtGui.QRadioButton('Female' , self)
	self.radioButton2.move(10 , 100)

	self.lv=QtGui.QListWidget(self)
	self.lv.addItem("Dan Brown")
	self.lv.addItem("Lee Child")
	self.lv.addItem("Agatha Christie")
	self.lv.addItem("Erle Stanley Gardner")
	self.lv.addItem("Sydney Sheldon")
	self.lv.addItem("Lee Child")
	self.lv.addItem("Agatha Christie")
	self.lv.addItem("Erle Stanley Gardner")
	self.lv.addItem("Sydney Sheldon")
	self.lv.move(220 , 80)
	self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Choose your GUI')  

    def otherCode(self):
        import Gurpreet_Tkinter

def main():
    app = QtGui.QApplication(sys.argv)
    tb = New()
    tb.show()
    app.exec_()

if __name__=='__main__':
    main()
