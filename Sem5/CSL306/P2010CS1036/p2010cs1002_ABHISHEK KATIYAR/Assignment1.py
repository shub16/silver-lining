import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Tkinter import *
import module1
def tkintermodule():
    root = Tk()
    app = module1.Widget(root)
    root.mainloop()

class assign3(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        text = QtGui.QTextEdit(self)
        text.resize(100,100)
        text.move(130,30)

        button = QtGui.QPushButton('NEXT',self)    #buttton to go in tkinter module
        button.move(10,150)
	button.clicked.connect(self.buttonclicked)
        button2 = QtGui.QPushButton('QUIT',self)     #button to quit
        button2.move(150,150)
        button2.clicked.connect(self.close)
        
        self.setGeometry(300, 300, 270, 200)    #setting window parameters
        self.setWindowTitle('assignment3')
        
        self.cbox = QtGui.QCheckBox('Checkbox', self) #constructor for checkbox
        self.cbox.move(10, 10)

        self.button = QtGui.QRadioButton('Radio Button', self) #constructor for radio button
        self.button.move(150, 10)

        self.downlist = QtGui.QLabel(self)  #makiing comboboxes
        box = QtGui.QComboBox(self)
        box.addItem("LINE 1")
        box.addItem("LINE 2")
        box.addItem("LINE 3")
        box.addItem("LINE 4")
        box.addItem("LINE 5")
        box.move(10,50)
        self.downlist.move(30,120)
        box.activated[str].connect(self.onActivated)
        
        
    def onActivated(self, text):
        self.downlist.setText(text)
        self.downlist.adjustSize()
    def buttonclicked(self):
                sender = self.sender()
                tkintermodule()
        
app = QtGui.QApplication(sys.argv)
icon = assign3()
icon.show()
app.exec_()
