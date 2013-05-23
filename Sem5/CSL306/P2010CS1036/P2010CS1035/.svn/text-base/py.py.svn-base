
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel(self)
        text_box = QtGui.QLineEdit(self)
        
        text_box.move(60, 20)
        self.lbl.move(1600, 40)

        text_box.textChanged[str].connect(self.when_change)
        
        button = QtGui.QPushButton('Quit', self)
#        button.clicked.connect(self.closeEvent)
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.setToolTip('Press to quit ')
        button.resize(button.sizeHint())
        button.move(80, 100) 
        
        self.setGeometry(299,299, 279, 169)
#		self.setGeometry(300,300, 280, 170)
        self.setWindowTitle('Hello!')
        self.show()
	


        
    def when_change(self, text):
        self.lbl.adjustSize()        

        """
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()

        def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()     
        """
        

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
        



if __name__ == '__main__':
    main()
