import sys,os
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from functools import partial

# myWindow Class to Create a WindowPanel which is the main Window,the parent of other widgets.
class myWindow(QtGui.QWidget):
        def __init__(self,title,x_pos,y_pos,width,height):
            #app = QtGui.QApplication(sys.argv)            
            super(myWindow,self).__init__()
            self.setGeometry(x_pos,y_pos,width,height)
            self.setWindowTitle(title)       

#Close Method to close Window
        def Close(self):
            self.close()
         
#Show Method to Show the Window
        def Show(self):
            self.show()
            #sys.exit(self.app.exec_())


#Label Class to Create a Label Widget
class Label(QtGui.QLabel):
        def __init__(self,label,x_pos,y_pos,width,height,parent):
            super(Label,self).__init__(label,parent)
            self.setGeometry(x_pos,y_pos,width,height);

        def setLabel(self,text):			
            self.setText(text)

#Button Class to Create a PushButton Widget
class Button(QtGui.QPushButton):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(Button,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height);
            self.setText(title)
			
#Button Listener for PushButton
        def buttonListener(self,call_method,*args):
            self.clicked.connect(partial(call_method, *args))    # On clicking Button it calls the on_click method.
       

#CheckBox Class to Create the CheckBox Widget
class CheckBox(QtGui.QCheckBox):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(CheckBox,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height)
            self.setText(title)
            self.setCheckState(0)

#method to set the initial Check-State of the CheckBox
        def setCheckState(self,state):
            super(CheckBox,self).setCheckState(state)
			
#Method returns the current check state of the CheckBox
        def getCheckState(self):
            if self.checkState()==0:
                return False
            else :
                return True

#Class ButtonGroup to Create a  Widget Which will contaim a group of Buttons
class ButtonGroup(QtGui.QButtonGroup):
        def __init__(self,parent):
            super(ButtonGroup,self).__init__(parent)
            			
#returns the Id of the Button Checked in the Button Group
     	def getChecked(self):
		    return self.checkedId()

# returns the Text of the Button Checked in the Button Group
        def getValue(self):
            return (self.checkedButton()).text();
				
# Adds the Button to this Group
        def addButtons(self,BtnList):
            for i in range(len(BtnList)):
                self.addButton(BtnList[i],i)
	    
        
# Class RadioButton to create a RadioButton Widget
class RadioButton(QtGui.QRadioButton):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(RadioButton,self).__init__(parent)
            self.setText(title)
            self.setGeometry(x_pos,y_pos,width,height)
            
#TextBox Class to create a TextBox Widget
class TextBox(QtGui.QLineEdit):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(TextBox,self).__init__(title,parent)
            self.setGeometry(x_pos,y_pos,width,height)
            self.setText(title)

# returns the Text entered in the TextBox
        def getText(self):
            return self.text()

# ListBox Class to Create a ListBox Widget.
class ListBox(QtGui.QListWidget):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(ListBox,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height)

# Adding Items to the ListBox
        def addItems(self,myList):
            m= self.count()
            if(m==0):
               for i in range(len(myList)):
                    self.addItem(myList[i])		
            
# Get the Selected Item from the ListBox
        def Selected(self):
            if(len(self.selectedItems())>0):
                return self.selectedItems()[0].text()
            else :
                return ""			
		
#Password Class to Create a Password Box Widget
class PasswordBox(QtGui.QLineEdit):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(PasswordBox,self).__init__(title,parent)
            self.setGeometry(x_pos,y_pos,width,height)
            self.setText(title)
            self.setEchoMode(2)

# Get the text entered in the password Box
        def getText(self):
            return self.text()

# class for the calendar widget
class Calendar(QtGui.QCalendarWidget):

    # create the calendar
        def __init__(self,x_pos,y_pos,width,height,parent):
            super(Calendar,self).__init__(parent)
            self.setGridVisible(True)
            self.setGeometry(x_pos,y_pos,width,height)

    # function to extract the value of the widget
        def getValue(self):
            return self.selectedDate().toString()
	
# class for the slider widget
class Slider(QtGui.QSlider):

        def __init__(self,x_pos,y_pos,width,height,parent):
            super(Slider,self).__init__(QtCore.Qt.Horizontal,parent)
            self.setFocusPolicy(QtCore.Qt.NoFocus)
            self.setGeometry(x_pos,y_pos,width,height)

# method to set the maximum and minimum Value of the slider
        def setRange(self,fromValue,toValue):
            self.setMinimum(fromValue)
            self.setMaximum(toValue)

        def getValue(self):
            return self.value()


#ComboBox Class to Create a ComboBox Widget

class ComboBox(QtGui.QComboBox):
        combo_string=""
        def __init__(self,title,myList,x_pos,y_pos,width,height,parent):
            super(ComboBox,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height)
            self.connect(self, QtCore.SIGNAL('activated(QString)'), self.combo_chosen) 
            self.addItems(myList)

# It will set combo_string to the text of the selected item in the combobox
        def combo_chosen(self, text):
            self.combo_string =text
  
#  Selected method will return the Selected items in the ComboBox widget.
        def Selected(self):
            return self.combo_string

# MenuBar Class to Create a MenuBar
class MenuBar(QtGui.QMenuBar):

        def __init__(self,x_pos,y_pos,width,height,parent):
            super(MenuBar,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height)
            

# addItems method to add Menu Items and its Action.
        def addItems(self,menu_list,*args):
            menu=[]
            Action=[]
            for i in range(len(menu_list)):
                Action.append(QtGui.QAction(menu_list[i][1], self) )
                Action[i].triggered.connect(menu_list[i][2])        		
                menu.append(self.addMenu(menu_list[i][0]))
                menu[i].addAction(Action[i])
            
