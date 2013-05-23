#This Program displays the input given in the QLineEdit TextBox in the command Line on clicking the Button..

import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout

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

def TxtBtnApp():
    app = QApplication(sys.argv) 
    form = Form()
    form.show() #Shows the form
    app.exec_() #Exits the application Safely.

if __name__ == '__main__':
    TxtBtnApp()
