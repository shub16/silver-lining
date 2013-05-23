import sys
from PyQt4 import QtGui

class Example (QtGui.QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI() 
	
    def initUI(self):
        
        area=QtGui.QTextEdit(self)
        area.resize(300,200)
        area.move(2,2)
        button=QtGui.QPushButton('button',self)
        button.move(100,210)
        self.setGeometry(300,300,250,250)
        self.setWindowTitle('Naveen Kumar')
        self.show()


def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
#if __name__ == '__main__':
#   main()
