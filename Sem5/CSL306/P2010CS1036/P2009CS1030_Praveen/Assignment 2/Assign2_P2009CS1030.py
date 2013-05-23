#This Program displays GUI Interface developed through either pyQT4 or wxpython based on user choice read from shell.
# Abhisaar Sharma Code is modular made me to import and invoke his GUI very easily

import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout

import Assignment1_2010cs1001  # Importing wxpython module of other student.

# Object Oriented Programming instead of Procedural Programming option  available.

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.tBox = QLineEdit() #creates object for Single Line Text Box. Note: In pyQT there are no multiline Text Box.
        self.tBox.setObjectName("TextBox") # Setting Object name
        self.tBox.setText("Type Your Name Here") # Setting Text in Text Box


        self.butn = QPushButton() #creates object for Button
        self.butn.setObjectName("Print") #setting Object name for button
        self.butn.setText("Print") #Setting button text.

        layout = QFormLayout() # Creates Layout Object
        layout.addWidget(self.tBox) # Adds TextBox to Window
        layout.addWidget(self.butn) # Adds Button to Window

        self.setLayout(layout) # Sets Layout
        self.connect(self.butn, SIGNAL("clicked()"),self.button_click) # Assigning Button Click Event to Button.
        self.setWindowTitle("Learning") #Sets window Title to learning

    def button_click(self): #Button Click Event[On Button Click this code is executed]
        # shost is a QString object
        Cprint = self.tBox.text() #Accesses text from TextBox.
        print Cprint #Prints on Command Line.

def pyQTApp():
	app = QApplication(sys.argv) 
	form = Form()
	form.show() #Shows the form
	app.exec_() #Exits the application Safely.


if __name__ == '__main__': #main from where execution starts.

     print " Enter Your Choice of GUI Framwork to Run:  " # Asking user for choice of GUI to Run.
     print " 1 for PYQT Application to Run"
     print " 2 for wxpython Application to Run"
     print " Other than 1 and 2 to Exit "
     try:
        x = int(raw_input()) # Parsing User String Input to int
     except ValueError: # To Catch Exception
        print 'Invalid Input Value Entered'
     if (x==1):
		pyQTApp() # Invoking PyQT Module Written by me for input 1.
     elif(x==2):        
		app = Assignment1_2010cs1001.MyApp(0)  # Invoking wxpython Module for input 2.
		app.MainLoop()
     else:
		sys.exit(0) # If input is other than 1 or 2 exit Application smoothly.
