import sys
from PyQt4 import QtGui, QtCore

# Object Oriented Programming instead of Procedural Programming option  available.

class Form(QtGui.QWidget):
    
    def __init__(self, parent=None): # Constructor of class Form
        super(Form, self).__init__(parent)
        self.initUI() # calls initUI method to initialize all GUI objects in Window
        
    def initUI(self):
        self.setGeometry(300, 300, 400, 400)      
        self.Textbox() 
        self.Button()
        self.Checkbox()
        self.Radiobox()
        self.List()
        self.ListButton()
        layout = QtGui.QFormLayout() # Creates Layout Object
        layout.addWidget(self.tBox) # Adds TextBox to Window
        layout.addWidget(self.butn) # Adds Button to Window
        layout.addWidget(self.cBox) # Adds CheckBox to Window
        layout.addWidget(self.rBox) # Adds RadioButton to Window
        layout.addWidget(self.listBox) #Adds ListWidget to Window
        layout.addWidget(self.list_btn) #Adds Button to Load List
        self.setLayout(layout) # Sets Layout
        
        #Assigning Signals to cBox, butn, rBox GUI Objects
        self.butn.clicked.connect(self.button_click) # Assigning Button Click Event to Button.
        self.cBox.stateChanged.connect(self.changeTitle) #Toggles title of the window
        self.rBox.toggled.connect(self.Rbox_toggle) #Displays whether Radio Box is checked or not
        self.list_btn.clicked.connect(self.LoadList)    # Assigning LoadList Event to list_btn 
        self.listBox.itemSelectionChanged.connect(self.onSelect)  #Assign onSelect Event on selecting a list element    
        self.show()
       
    def Textbox(self):            
        self.tBox = QtGui.QLineEdit() #creates object for Single Line Text Box. Note: In pyQT there are no multiline Text Box.
        self.tBox.setObjectName("TextBox") # Setting Object name
        self.tBox.setText("Type Your Name Here") # Setting Text in Text Box

    def Button(self):
        self.butn = QtGui.QPushButton() #creates object for Button
        self.butn.setObjectName("Print") #setting Object name for button
        self.butn.setText("Print") #Setting button text.

    def button_click(self): #Button Click Event[On Button Click this code is executed]
        Cprint = self.tBox.text() #Accesses text from TextBox.
        print Cprint #Prints on Command Line.


    def Checkbox(self):
        self.cBox = QtGui.QCheckBox('Show/Hide title', self)
        self.cBox.toggle()
        self.setWindowTitle('QtGui.QCheckBox')

    def changeTitle(self, state): #called on toggle of checkBox selection
      
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('Check Box is Checked')
        else:
            self.setWindowTitle('Check Box is Unchecked')
        
 
    def Radiobox(self):      
        self.rBox = QtGui.QRadioButton('Radio Button', self)
        self.rBox.toggle()                                                    

    def Rbox_toggle(self): #called on toggle of Radiobox selection
        if self.rBox.isChecked():
            self.tBox.setText("Radio Box is Checked")
        else:
            self.tBox.setText("Radio Box is UnChecked")           

    def ListButton(self):
        self.list_btn = QtGui.QPushButton("Load List",self)     #To Load planet list in ListWidget

    def List(self):
        planetList = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        self.planetList=planetList 
        self.listBox = QtGui.QListWidget(self)                                    # creating a List Widget
        
    def LoadList(self): #This method is called on clicking list_btn
        listCount= (self.listBox.count())   #Only adds to list if the list is empty
        if(listCount==0):
            self.listBox.addItems(self.planetList)

    def onSelect(self): #This method is called on selecting a list element
        planet = self.listBox.selectedItems()[0].text() # Picks the selected Planet
        self.tBox.setText(planet) #Prints the selected planet in Textbox

def main():
    app = QtGui.QApplication(sys.argv) 
    form = Form()
    form.show() #Shows the form
    app.exec_() #Exits the application Safely.
    
if __name__ == '__main__':  
    main() #calling main method
    
