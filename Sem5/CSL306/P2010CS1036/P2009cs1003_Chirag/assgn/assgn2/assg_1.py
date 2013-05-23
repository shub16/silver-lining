import sip
sip.setapi('QVariant', 2)

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()                             # calling constructor of super class

        self.initUI()

    def initUI(self):

        title = QtGui.QLabel('Title')                               # Create a label
       
        titleEdit = QtGui.QTextEdit()                               # Create a Text Line
        
        submitButton = QtGui.QPushButton("Submit")                  # Create a Push Button
        submitButton.resize(submitButton.sizeHint())

        grid = QtGui.QGridLayout()                                  # Setting up Grid Layout for attaching widgets
        grid.setSpacing(10)

     #   grid.addWidget(title, 1, 0)                                # Adding widget Title to the Grid
        grid.addWidget(titleEdit, 0, 0, 3, 3)                       # Adding Text Widget to the Grid

        grid.addWidget(submitButton, 4, 1)                          # Adding Submit Button to the Grid

        self.setLayout(grid)                                        # Finalizing the Grid for Display

        self.setGeometry(400, 400, 400, 400)                        # setting the geometry for the window
        self.center()                                               # Aligning to the center
        self.setWindowTitle('Review')
        self.setWindowIcon(QtGui.QIcon('Web.png'))
        self.show()                                                 # display 
    
    # Used for centring the box that is displayed

    def center(self):

        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())

    def closeEvent(self,event):

        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, key):

        if key.key() ==QtCore.Qt.Key_Escape:
            self.close()

def PyQt():                                 # Function to call PyQT GUI
    app = QtGui.QApplication(sys.argv)                              
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()