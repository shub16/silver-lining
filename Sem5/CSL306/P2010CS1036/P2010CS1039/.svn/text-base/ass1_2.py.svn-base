import sys
from PyQt4 import QtGui

class bbox (QtGui.QWidget):
    def __init__(self):
        super(bbox,self).__init__()
        self.initUI()
        
    def initUI(self):
        area = QtGui.QTextEdit(self)
        area.resize(250,140)
        area.move(20,20)
        button=QtGui.QPushButton('Submit',self)
        button.move(110,200)
        self.setGeometry(800,400,290,310)
        self.setWindowTitle('UI with PyQt')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    var = bbox()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

