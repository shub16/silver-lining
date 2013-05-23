import sys
from PyQt4 import QtGui, QtCore

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
        
        if(widget_type==LabelText):
            widget.handle = QtGui.QLabel(widget.text,self.window)
            widget.handle.resize(widget.width, widget.height)    
            widget.handle.move(widget.cord_x, widget.cord_y)
            
        elif(widget_type==TextView):
            widget.handle = QtGui.QTextEdit(widget.text,self.window)
            widget.handle.resize(widget.width, widget.height)    
            widget.handle.move(widget.cord_x, widget.cord_y)
        
        elif(widget_type==Button):
            widget.handle = QtGui.QPushButton(widget.text,self.window)
            widget.handle.resize(widget.width, widget.height)    
            widget.handle.move(widget.cord_x, widget.cord_y)
            if(widget.callbackMethod is not None):
                widget.handle.clicked.connect(widget.callbackMethod)
                
        elif(widget_type== TextLine):
            widget.handle = QtGui.QLineEdit(widget.text,self.window)
            widget.handle.resize(widget.width, widget.height)    
            widget.handle.move(widget.cord_x, widget.cord_y)
            
        elif(widget_type==CheckBox):
            widget.handle = QtGui.QCheckBox(widget.title, self.window)
            widget.handle.setChecked(widget.value)
            widget.handle.resize(widget.width, widget.height)    
            widget.handle.move(widget.cord_x, widget.cord_y)
            
        elif(widget_type==Radio):
            widget.groupBox = QtGui.QGroupBox("", self.window)
            widget.handle = []
            radio_handle = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.cords_x[0], widget.cords_y[0])
            
            radio_handle.resize(widget.width, widget.height)
            radio_handle.move(0, 0)
            widget.handle.append(radio_handle)
            for i in range(1,len(widget.labels)):
                radio_handle = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_handle.resize(widget.width, widget.height)
                radio_handle.move(widget.cords_x[i]-widget.cords_x[0], widget.cords_y[i]-widget.cords_y[0])
                widget.handle.append(radio_handle)
            if(widget.selected_pos != None):
                widget.handle[widget.selected_pos].setChecked(True)
                
# Label Widget
class LabelText(object):
    handle = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

#Button Widget
class Button(object):
    handle = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height
        
#TextLine Widget
class TextLine(QtGui.QWidget):
    handle = None
    callback = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def setText(self, text):
        self.lineEdit.setText(text)

#TextArea Widget
class TextView(object):
    handle = None
    callback = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

#CheckBox Widget
class CheckBox(object):
        handle = None
        value = False
        def __init__(self,title,X,Y,width,height):
                self.title = title
                self.cord_x = X
                self.cord_y = Y
                self.width = width
                self.height = height

        def setValue(self,value):
                if(self.handle == None):
                    self.value = value
                else:
                    self.handle.setChecked(value)

#Radio Button Widget
class Radio(object):
        handle = None
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
            if(self.handle == None):
                self.selected_pos = pos
            else:
                button_handle = self.handle[pos]
                button_handle.setChecked(True)
