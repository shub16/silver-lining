import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from functools import partial 
import re

#  Main Window Class to Contain All the Widgets

class myWindow(QtGui.QWidget):
        def __init__(self,title,x_pos,y_pos,width,height):
            super(myWindow,self).__init__()
            self.setGeometry(x_pos,y_pos,width,height)
            self.setWindowTitle(title)       

#Label Class to create a label

class Label(QtGui.QLabel):
        def __init__(self,label,x_pos,y_pos,width,height,parent):
            super(Label,self).__init__(label,parent)
            self.setGeometry(x_pos,y_pos,width,height);

#Button Class to Create a PushButton
			
class Button(QtGui.QPushButton):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(Button,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height);
            self.setText(title)
	    
        def buttonListener(self,call_method,*args):
            self.clicked.connect(partial(call_method, *args))    # On clicking Button it calls the on_click method.
       
#CheckBox Class to Create a CheckBox Widget
			
class CheckBox(QtGui.QCheckBox):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(CheckBox,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height)
            self.setText(title)
            self.setCheckState(0)
			
        def setCheckState(self,state):
            super(CheckBox,self).setCheckState(state)
			
        def getCheckState(self):
            if self.checkState()==0:
                return False
            else :
                return True

#ButtonGroup Class to Contain the CheckBoxes or Group Of RadioButtons

class ButtonGroup(QtGui.QButtonGroup):
        def __init__(self,parent):
            super(ButtonGroup,self).__init__(parent)
            			
     	def getChecked(self):
		    return self.checkedId()

        def getValue(self):
            return (self.checkedButton()).text();
				
        def addButtons(self,BtnList):
            for i in range(len(BtnList)):
                self.addButton(BtnList[i],i)
	    
#RadioButton Class to create a RadioButton Widget
        
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

#  getText method to return the text in the TextBox 

        def getText(self):
            return self.text()


#ListBox Class to Create a ListBox Widget

class ListBox(QtGui.QListWidget):
        def __init__(self,title,x_pos,y_pos,width,height,parent):
            super(ListBox,self).__init__(parent)
            self.setGeometry(x_pos,y_pos,width,height)

#addItems method to add items in the ListBox Widget
        def addItems(self,myList):
            m= self.count()
            if(m==0):
               for i in range(len(myList)):
                    self.addItem(myList[i])		
            
   
#  Selected method will return the Selected items in the ListBox widgets.
        def Selected(self):
            if(len(self.selectedItems())>0):
                return self.selectedItems()[0].text()
            else :
                return ""			
		
