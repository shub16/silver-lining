import sys
from PyQt4 import QtGui
class lab1(QtGui.QWidget): 
    def __init__(self):
        super(lab1, self).__init__()
        self.initUI()
    def initUI(self):
        text = QtGui.QTextEdit(self)
        text.resize(200,200)
        text.move(10,10)
        btn = QtGui.QPushButton('Button', self)
        btn.move(80,215)
        self.setGeometry(300, 300, 220, 250)
        self.setWindowTitle('SHUBHAM')    
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = lab1()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
