import sys

import Assignment1_2010cs1001                  # Importing the wxpython module

from PyQt4 import QtGui
class TextBtn(QtGui.QWidget):
    
    def __init__(self):
        super(TextBtn, self).__init__()     # calling constructor of parent class by super command
        
        self.init_GUI()
        
# Initialize the GUI
    def init_GUI(self):     
        self.myButton = QtGui.QPushButton('Print On Console', self)         # creating an object of Push Button
        self.myButton.move(90, 90)
        self.myButton.clicked.connect(self.button_click)        
        self.myTextBox = QtGui.QLineEdit(self)             #  creating an object of TextBox
        self.myTextBox.resize(250,40)       
        self.myTextBox.setText("Enter Something")          # Setting the initial text in the textbox
        self.myTextBox.move(20,20)
        self.setGeometry(300, 300, 290, 170)               # Setting the window location on desktop and size of the window
        self.setWindowTitle('PyQT TextBox with Button')    # Setting the title of the window
        self.show()
        
    def button_click(self):                                # Button Click Listener 
        txtMsg = self.myTextBox.text()                     # Get Text from TextBox.
        print (txtMsg)                                     #Prints Text on Console.        
        
def TxtBtnApp():										   # Creating object for our application
    app = QtGui.QApplication(sys.argv)
    myObject= TextBtn()
    sys.exit(app.exec_())

# The only changes in the code is in the main
# choices are added for PYQT and wxpython 

if __name__ == '__main__':
#    TxtBtnApp()
     print (" Enter Your Choice:  ")
     print (" 1 for GUI in PYQT4 ")
     print (" 2 for GUI in wxpython")
     print (" 3 for Exit ")
     try:
        x = int(raw_input())  # User choice as an integer
     except ValueError:
        print ('Invalid Number')
     if (x==1):
         TxtBtnApp()                      # Invoking PyQT app for choice=1
     elif(x==2):
         app = Assignment1_2010cs1001.MyApp(0)  # Invoking wxpython app for choice=2 
         app.MainLoop()
     else:
         sys.exit(0)
