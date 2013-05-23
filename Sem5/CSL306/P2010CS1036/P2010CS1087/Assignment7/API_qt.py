import sip
sip.setapi('QString', 2)
import os
import sys
import re	
from PyQt4 import QtGui, QtCore	
from functools import partial

class SurveyWindow(QtGui.QMainWindow):			#	
    parent = None	
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(SurveyWindow, self).__init__() 
        self.id = id
        self.text = title
        self.width = width
        self.height = height
    #def menu(self):
	
    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())
	
class WindowFrame(object):	
    window = None	
    def __init__(self, id, title,width,height):
        self.window = SurveyWindow(id, title,width,height)
    def show(self):                                      # Finalizing the Grid for Display
	
	self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height) #   setting the geometry for the window
        self.window.center()                                               # Aligning to the center
        self.window.setWindowTitle(self.window.text)       		   # Setting the title of window
        self.window.show()						   # Displaying the window
        sys.exit(self.window.app.exec_())

    def add(self,widget):						   # Adds the widgets to the window
	WidgetName = type(widget)					
        
	if(WidgetName==CheckBox or isinstance(widget,CheckBox)):		# checking for WidgetName as CheckBox		
            widget.controller = QtGui.QCheckBox(widget.title, self.window)	# setting the controller as Checkbox
            widget.controller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)    		# resizing the widget
            widget.controller.move(widget.position_X, widget.position_Y)	# placing the widget at a fixed position
	
        
	elif(WidgetName==Password or isinstance(widget,Password)):		# checking for WidgetName as Password
	    widget.controller = QtGui.QLineEdit(self.window)			# setting the controller as Checkbox
	    widget.controller.setEchoMode(2)					# Encripting the value of the text in the Password
            widget.controller.resize(widget.width, widget.height)    		# resizing the widget
            widget.controller.move(widget.position_X, widget.position_Y)	# placing the widget at a fixed position

	elif(WidgetName==Slider or isinstance(widget,Slider)):			# checking for WidgetName as slider
	    widget.controller = QtGui.QSlider(QtCore.Qt.Horizontal,self.window)
	    widget.controller.setFocusPolicy(QtCore.Qt.NoFocus)
	    widget.controller.setMinimum(widget.start)				# setting the minimum value of the slider
	    widget.controller.setMaximum(widget.end)				# setting the max value of the slider
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(WidgetName==SpinBox or isinstance(widget,SpinBox)):
	    widget.controller = QtGui.QSpinBox(self.window)
	    widget.controller.setMinimum(widget.start)
	    widget.controller.setMaximum(widget.end)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(WidgetName==Label or isinstance(widget,Label)):
	    widget.controller = QtGui.QLabel(widget.text,self.window)		# setting the controller as Label
	    widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(WidgetName==Button or isinstance(widget,Button)):			# checking for WidgetName as Button
            widget.controller = QtGui.QPushButton(widget.text,self.window)	# setting the controller as Button
            widget.controller.resize(widget.width, widget.height)    		# resizing the widget
            widget.controller.move(widget.position_X, widget.position_Y)	# placing the widget at a fixed position
            if(widget.callbackMethod is not None):
                widget.controller.clicked.connect(widget.callbackMethod)


	elif(WidgetName==TextLine or isinstance(widget,TextLine)):
	    widget.controller = QtGui.QLineEdit(self.window)			# setting the controller as TextLine
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(WidgetName==TextArea or isinstance(widget,TextArea)):		# checking for WidgetName as TextArea
            widget.controller = QtGui.QTextEdit(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    		# resizing the widget
            widget.controller.move(widget.position_X, widget.position_Y)

        elif(WidgetName==RadioGroup or isinstance(widget,RadioGroup)):			# checking for WidgetName as RadioGroup
            widget.groupBox = QtGui.QGroupBox("", self.window)
            widget.controller = []
            radio_controller = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.positions_X[0], widget.positions_Y[0])
            radio_controller.resize(widget.width, widget.height)			# resizing the widget
            radio_controller.move(0, 0)				
            widget.controller.append(radio_controller)
	
            for i in range(1,len(widget.labels)):
                radio_controller = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_controller.resize(widget.width, widget.height)						# resizing the widget
                radio_controller.move(widget.positions_X[i]-widget.positions_X[0], widget.positions_Y[i]-widget.positions_Y[0])
                widget.controller.append(radio_controller)
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].setChecked(True)
	
        elif(WidgetName==DropDownList or isinstance(widget,DropDownList)):			# checking for WidgetName as DropDownList
            widget.controller = QtGui.QComboBox(self.window)				# setting the controller as DropDownList
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    			# resizing the widget
            widget.controller.move(widget.position_X, widget.position_Y)		# placing the widget at a fixed position
	
	
        elif(WidgetName==SelectList or isinstance(widget,SelectList)):		# checking for WidgetName as SelectList
            widget.controller = QtGui.QListWidget(self.window)				# setting the controller as SelectList
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    			# resizing the widget
            widget.controller.move(widget.position_X, widget.position_Y)		# placing the widget at a fixed position


class SelectList(object):						# Class of SelectList
	controller = None
	
        def __init__(self,choices,X,Y,width,height,value=""):		# constructor to initialize attributes
	
            self.choices = choices
	
            self.position_X = X
	
            self.position_Y = Y
	
            self.width = width
	
            self.height = height
	
            self.value = value

	def clickListener(self,method):					# Action Listener function
	
	     if(self.controller == None):
		
	         self.callbackMethod = method
		
	     else:
		
	         self.controller.currentTextChanged.connect(method)     # calling function 'method' 
		
	     return True

class Password(object):				# Class of Password	
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):	# constructor to initialize attributes
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def getText(self):				# Extracting the text from the TextLine
		
        if(self.controller == None):
	    return ''
	else:	
	    return self.controller.text()


    def setText(self,text):			# setting predefined text to the TextLine
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.setText(text)
	
        return True
    

class Slider(object):				# Class Slider

    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):		# constructor to initialize attributes
	
	self.start=start
	self.end=end
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getValue(self):						# Extracting the value of the slider
	
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.value()
   
class SpinBox(object):					# Class of SpinBox
	
    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):		# constructor to initialize attributes
	
        #self.text = text
	self.start=start
	self.end=end
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
    
    def getValue(self):						# Extracting the value from SpinBox
	
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.value()


class Label(object):			

    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):
	

	self.text=text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height


class TextLine(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getText(self):

	if(self.controller == None):
            return ''
	else:
	    return self.controller.text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.setText(text)
	
        return True
    	
    def clear(self):					# Clearing all the text from the TextLine
	
        self.controller.setText("")
	
        return True
	
    

####
	
class Button(object):
	
    controller = None
	
    callbackMethod = None
	
    def __init__(self,text,X,Y,width,height):    	
	
        self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def clickListener(self,method):			# adding action listener
	
        if(self.controller == None):
	
            self.callbackMethod = method
	
        else:
	
            self.controller.clicked.connect(method)	# Calling function 'method' after the button is clicked	
	
        return True

class CheckBox(object):
	
        controller = None
	
        value = False
	
        def __init__(self,title,X,Y,width,height):	# Constructor for initializing the attributes
	
                self.title = title
	
                self.position_X = X
	
                self.position_Y = Y
	
                self.width = width
	
                self.height = height
	
	
        def setValue(self,value):
	
                if(self.controller == None):
	
                    self.value = value
	
                else:
	
                    self.controller.setChecked(value)
	
	
        def getValue(self):
	
                if(self.controller == None):
	
                    return self.value
	
                else:
	
                    return self.controller.isChecked()
	
	
class RadioGroup(object):
	
        controller = None
	
        selected_pos = None
	
	
        def __init__(self,width,height):
	
            self.labels = []
	
            self.positions_X = []
	
            self.positions_Y = []
	
            self.width = width
	
            self.height = height
	
	
        def addRadioButton(self,label,X,Y):
	
            self.labels.append(label)
	
            self.positions_X.append(X)
	
            self.positions_Y.append(Y)
	
            return True
	
	
        def getValue(self):
	
                for i in range(len(self.controller)):
	
                    if(self.controller[i].isChecked()):
	
                        return self.labels[i]
	
                return None
	
	
        def setButtonTrue(self,pos):			# initializing a radio button as true
	
            if(self.controller == None):
	
                self.selected_pos = pos
	
            else:
	
                button_controller = self.controller[pos]
	
                button_controller.setChecked(True)
	
	
class DropDownList(object):			# Class of widget DropDownList
	
        controller = None
	
        def __init__(self,choices,X,Y,width,height,value=""):
	
            self.choices = choices
	
            self.position_X = X
	
            self.position_Y = Y
	
            self.width = width
	
            self.height = height
	
            self.value = value
	
	
        def getValue(self):				# function to extract the seleced value from a list	
	
            if(self.controller == None):
	
                return self.value
	
            else:
	
                return self.choices[self.controller.currentIndex() - 1]



class TextArea(object):			# Class TextArea
	
    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):		# constructor to initialize the attributes
	
        self.text = text

        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
	
    def setText(self,text):				# setting text in the TextArea
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.setText(text)
	
        return True
    def getText(self):					# it returns the text which is currently in TextArea

	if(self.controller == None):
            return ''
	else:
	    return self.controller.toPlainText()
	
	
    def appendText(self,text):				# adding text at the end of the TextArea
	
        if(self.controller == None):
	
            self.text = self.text+text
	
        else:
	
            self.text = self.controller.toPlainText() + text
	
            self.controller.setText(self.text)
	
        return True              
	
	
    def clear(self):					# clear all the text from the TextArea
	
        self.controller.setText("")
	
        return True
        
    def AppendBefore(self,str1,str2):			# function to insert text before a particular string
	document = self.controller.document()			
	cursor = document.find(str1)			# finds the position of the string str1 in the TextArea
	if cursor.isNull():
		return
	cursor.beginEditBlock()
	cursor.insertText(str2)				# inserting string str2 before string str1
	cursor.insertText(str1)
	cursor.endEditBlock()
	
