import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
        # create objects
        self.le = QTextEdit()   # text box
        self.bu = QPushButton('Button', self)   # push button

        # layout of the window
        layout = QVBoxLayout(self)
        layout.addWidget(self.le)
        layout.addWidget(self.bu)
        self.setLayout(layout)
