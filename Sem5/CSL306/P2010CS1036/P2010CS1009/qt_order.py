import sys
from PyQt4 import QtGui
class window(QtGui.QWidget):
    def __init__(self):
        super(window,self).__init__()
        self.initUI()
    def initUI(self):
            text = QtGui.QTextEdit(self)
            text.resize(240,260)
            text.move(5,5)
            btn = QtGui.QPushButton('BUTTON',self)
            btn.move(90,270)
            self.setGeometry(500,300,250,310)
            self.setWindowTitle('ABHISHEK KATIYAR')
            self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()
