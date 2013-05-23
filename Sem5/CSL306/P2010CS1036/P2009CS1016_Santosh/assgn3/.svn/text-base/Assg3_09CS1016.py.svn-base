#  Created By Santosh Kumar P2009CS1016

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
class TextBtn(QtGui.QWidget):
    
    def __init__(self):
        super(TextBtn, self).__init__()     # calling constructor of parent class by super command
        
        self.init_GUI()
		
		
		# method to create the Listbox 
    def init_list(self):
          # animal_list is the list of animals to be displayed in the list box 
		  
        animal_list = ["Tiger","Lion","Leopard","Giraffe","Fox","Elephant","Dog","Crocodile","Hippo"]
        self.btn_load = QtGui.QPushButton("Load List",self)                       # A Button to Load the animal list in the listbox
        self.btn_load.move(300, 270)                                              # Adjusting the position of the Button
        self.animal_list=animal_list 
        self.connect(self.btn_load, QtCore.SIGNAL("clicked()"), self.on_click)    # On clicking Button it calls the on_click method.
        self.listbox = QtGui.QListWidget(self)                                    # creating a List Widget
        self.listbox.move(30,190)                                                 # Adjusting the position of the ListWidget
        self.connect(self.listbox, QtCore.SIGNAL("itemSelectionChanged()"), self.on_select)      #On Selecting an item in the listbox,it calls the on_select method
    
	# method called on clicking the "Load List" Button
	
    def on_click(self):
           #   Getting the number of items in the ListWidget, and adding the list of animals in the ListWidget only if the ListWidget is empty.
        m= (self.listbox.count())
        if(m==0):
            self.listbox.addItems(self.animal_list)

# method called on selecting the items in the ListWidget
# On clicking/Selecting any item in the ListWidget, that item will be displayed in the textbox.
    def on_select(self):
    	
    	selected_animal = self.listbox.selectedItems()[0].text()
    	self.myTextBox.setText(selected_animal)

	# method to create the RadioButton and initialize its features.
    def init_radio(self):      

        self.rb = QtGui.QRadioButton('Radio Button', self)
        self.rb.move(260, 100)                                              # Adjusting the position of the RadioButton in the main Window
        self.rb.toggle()                                                    # Toggle operation for the radio button
        self.rb.toggled.connect(self.RBTxt)                             # If the state of the RadioButton is changed,it will call RBTxt() method.
                       
    # method called on clicking the RadioButton
	
    def RBTxt(self):      
        if self.rb.isChecked():
           self.myTextBox.setText("Radio Box Checked")
        else:
           self.myTextBox.setText("Radio Box UnChecked")
    
    # method to create the CheckBox button and to initialize its different features	
    def init_check(self):      

        cb = QtGui.QCheckBox('Check Box', self) 
        cb.move(30, 100)                                             # Adjusting the position of the checkBox in the main Window
        cb.toggle()                                                  # Toggle Operation for the CheckBox
        cb.stateChanged.connect(self.ChkBoxTxt)                    # On changed state,it will call the ChkBoxTxt() method.
                
	# method called on clicking the checkbox.
    def ChkBoxTxt(self, state):
      
        if state == QtCore.Qt.Checked:
            self.myTextBox.setText("Check Box Checked")
        else:
            self.myTextBox.setText("Check Box Unchecked")

# Creating the main Window 
# This function is same as the very first program , with textbox and button, the only added lines are 
#      1.      self.init_check()          to add a checkBox
#      2.      self.init_radio()          to add a radioButton 
#      3.      self.init_list()           to add a listWidget


    def init_GUI(self):     
        self.myButton = QtGui.QPushButton('Print On Console', self)         # creating an object of Push Button
        self.myButton.move(290, 25)
        self.myButton.clicked.connect(self.button_click)        
        self.myTextBox = QtGui.QLineEdit(self)             #  creating an object of TextBox
        self.myTextBox.resize(250,40)       
        self.myTextBox.setText("Enter Something")          # Setting the initial text in the textbox
        self.myTextBox.move(20,20)
        self.init_check()
        self.init_radio()
        self.init_list()
        self.setGeometry(300, 300, 400, 400)               # Setting the window location on desktop and size of the window
        self.setWindowTitle('PyQT TextBox with Button,CheckBox,RadioButton and ListBox')    # Setting the title of the window
        self.show()
        
    def button_click(self):                                # Button Click Listener 
        txtMsg = self.myTextBox.text()                     # Get Text from TextBox.
        print (txtMsg)                                     #Prints Text on Console.        
        
def TxtBtnApp():										   # Creating object for our application
    app = QtGui.QApplication(sys.argv)
    myObject= TextBtn()
    sys.exit(app.exec_())


if __name__ == '__main__':
    TxtBtnApp()