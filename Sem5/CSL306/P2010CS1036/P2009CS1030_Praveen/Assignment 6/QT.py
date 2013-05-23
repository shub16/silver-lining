import sys
from PyQt4 import QtGui, QtCore

class Xwindow(object):
    window = None
    def __init__(self, id, title,width,height):
        self.window = Window(id, title, width, height)

	#Shows window
    def show(self):                                      
        self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)                        # setting the geometry for the window
        self.window.center()   # Displaying App in the center
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())
	#Adds a widget to window
    def add(self,widget):
        widget_type = type(widget)
        if(widget_type==TextView):
            widget.controller = QtGui.QTextEdit(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.cord_x, widget.cord_y)
        
        elif(widget_type==Button):
            widget.controller = QtGui.QPushButton(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.cord_x, widget.cord_y)
            if(widget.callbackMethod is not None):
                widget.controller.clicked.connect(widget.callbackMethod)
                
        elif(widget_type== TextLine):
            widget.controller = QtGui.QLineEdit(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.cord_x, widget.cord_y)
        
        elif(widget_type==LabelText):
            widget.controller = QtGui.QLabel(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.cord_x, widget.cord_y)
            
        elif(widget_type==CheckBox):
            widget.controller = QtGui.QCheckBox(widget.title, self.window)
            widget.controller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.cord_x, widget.cord_y)
            
        elif(widget_type==Radio):
            widget.groupBox = QtGui.QGroupBox("", self.window)
            widget.controller = []
            radio_controller = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.cords_x[0], widget.cords_y[0])
            
            radio_controller.resize(widget.width, widget.height)
            radio_controller.move(0, 0)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_controller.resize(widget.width, widget.height)
                radio_controller.move(widget.cords_x[i]-widget.cords_x[0], widget.cords_y[i]-widget.cords_y[0])
                widget.controller.append(radio_controller)
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].setChecked(True)
       
        elif(widget_type==DropDownList):
            widget.controller = QtGui.QComboBox(self.window)
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.cord_x, widget.cord_y)     
                
class Window(QtGui.QWidget):
    def __init__(self,id,title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__() 
        self.text = title
        self.width = width
        self.height = height
    
    #This function centers the application no matter what is the size and resolution of the monitor on which this application is ruiing.
    def center(self):
        qr = self.frameGeometry()                                   
        cp = QtGui.QDesktopWidget().availableGeometry().center()    
        qr.moveCenter(cp)                                           
        self.move(qr.topLeft())

#Button Widget		
class Button(object):
    controller = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height
    def clickListener(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.clicked.connect(method)
        return True

#TextLine Widget		
class TextLine(QtGui.QWidget):
    controller = None
    callback = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def setText(self, text):
        self.lineEdit.setText(text)

#Label Widget		
class LabelText(object):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

#TextView Widget    
class TextView(object):
    controller = None
    callback = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def getText(self):
        return self.text;
    
    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.setText(text)
        return True
    
    def appendText(self,text):
        if(self.controller == None):
            self.text = self.text+text
        else:
            self.text = self.controller.toPlainText() + text
            self.controller.setText(self.text)
        return True              

    def clearText(self):
        self.controller.setText("")
        return True
        
#CheckBox widget
class CheckBox(object):
        controller = None
        value = False
        def __init__(self,title,X,Y,width,height):
                self.title = title
                self.cord_x = X
                self.cord_y = Y
                self.width = width
                self.height = height

        def setValue(self,value):
                if(self.controller == None):
                    self.value = value
                else:
                    self.controller.setChecked(value)

#Radio Button Widget					
class Radio(object):
        controller = None
        selected_pos = None

        def __init__(self,width,height):
            self.labels = []
            self.cords_x = []
            self.cords_y = []
            self.width = width
            self.height = height

        def addRadioButton(self,label,X,Y):
            self.labels.append(label)
            self.cords_x.append(X)
            self.cords_y.append(Y)
            return True

        def setButtonTrue(self,pos):
            if(self.controller == None):
                self.selected_pos = pos
            else:
                button_controller = self.controller[pos]
                button_controller.setChecked(True)
                
#DropDown Widget
class DropDownList(object):
        controller = None
        def __init__(self,choices,X,Y,width,height,value=""):
            self.choices = choices
            self.cord_x = X
            self.cord_y = Y
            self.width = width
            self.height = height
            self.value = value

        def getValue(self):
            if(self.controller == None):
                return self.value
            else:
                return self.choices[self.controller.currentIndex() - 1]                
