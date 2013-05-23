import sys
from PyQt4 import QtGui,QtCore
class lab1(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('grid layout')
        tkinter= QtGui.QLabel('Tkinter Gui')
        name = QtGui.QLabel('Name')
        college = QtGui.QLabel('College')
        btn1 = QtGui.QPushButton('Tkinter', self);
        btn1.clicked.connect(self.gui)
        nameEdit = QtGui.QLineEdit()
        collegeEdit = QtGui.QLineEdit()
        branch=QtGui.QLabel('Branch :')
        self.lv = QtGui.QListWidget(self)
        rb1 = QtGui.QRadioButton('CS', self)
        rb2 = QtGui.QRadioButton('EE', self)
        rb3 = QtGui.QRadioButton('ME', self)
        subjects = QtGui.QLabel('Courses :')
        self.cb1 = QtGui.QCheckBox('English', self)
        self.cb2 = QtGui.QCheckBox('Chemistry', self)
        self.cb3 = QtGui.QCheckBox('Physics', self)
        self.cb4 = QtGui.QCheckBox('Maths', self)
        self.cb5 = QtGui.QCheckBox('History', self)
        self.cb6 = QtGui.QCheckBox('Economics', self)
        
        self.connect(self.cb1, QtCore.SIGNAL('stateChanged(int)'),self.list1)
        self.connect(self.cb2, QtCore.SIGNAL('stateChanged(int)'),self.list1)
        self.connect(self.cb3, QtCore.SIGNAL('stateChanged(int)'),self.list1)
        self.connect(self.cb4, QtCore.SIGNAL('stateChanged(int)'),self.list1)
        self.connect(self.cb5, QtCore.SIGNAL('stateChanged(int)'),self.list1)
        self.connect(self.cb6, QtCore.SIGNAL('stateChanged(int)'),self.list1)
        
        btn2 = QtGui.QPushButton('Submit', self)
        self.connect(btn2,QtCore.SIGNAL('clicked()'), self.sb)
        btn3 = QtGui.QPushButton('Close', self)
        btn3.clicked.connect(self.close)        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(tkinter, 1, 0,)
        grid.addWidget(btn1, 1, 1)
        grid.addWidget(name, 2, 0)
        grid.addWidget(nameEdit, 2, 1,1,3)
        grid.addWidget(college, 3, 0)
        grid.addWidget(collegeEdit, 3, 1,1,3)
        grid.addWidget(branch, 4, 0)
        grid.addWidget(rb1, 5, 1)
        grid.addWidget(rb2, 6, 1)
        grid.addWidget(rb3, 7, 1)
        grid.addWidget(subjects, 8, 0)
        grid.addWidget(self.cb1, 9, 1)
        grid.addWidget(self.cb2, 10, 1)
        grid.addWidget(self.cb3, 11, 1)
        grid.addWidget(self.cb4, 9, 2)
        grid.addWidget(self.cb5, 10, 2)
        grid.addWidget(self.cb6, 11, 2)
        grid.addWidget(btn2, 12, 0)
        grid.addWidget(btn3, 12, 1)
        grid.addWidget(self.lv,9,3,3,1)
        self.setLayout(grid)
        self.resize(400, 300)
    message=" Your profile is submitted"
    def gui(self):
	import vikas
        #execfile("abhishek.py")
    def sb(self):
        QtGui.QMessageBox.information(self,"Message", lab1.message)
    def list1(self):
        self.lv.clear()
        if self.cb1.isChecked():
            self.lv.addItem("English")
        if self.cb2.isChecked():
            self.lv.addItem("Chemistry")
        if self.cb3.isChecked():
            self.lv.addItem("Physics")
        if self.cb4.isChecked():
            self.lv.addItem("Maths")
        if self.cb5.isChecked():
            self.lv.addItem("History")
        if self.cb6.isChecked():
            self.lv.addItem("Economics")
        else:
            self.setWindowTitle('grid layout')
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = lab1()
    ex.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
