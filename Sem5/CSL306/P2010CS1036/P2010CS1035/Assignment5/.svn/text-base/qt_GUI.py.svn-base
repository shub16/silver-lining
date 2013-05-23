#import sip
#sip.setapi('QVariant', 2)

import sys
from PyQt4 import QtGui, QtCore
class Window(QtGui.QWidget):
    parent = None
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__() 
#        print self
        self.id = id
        self.text = title
        self.width = width
        self.height = height
    
    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())


class Vista(object):
    wndow = None
    def __init__(self, id, title,width,height):
        self.wndow = Window(id, title,width,height)
	
	def end(self):
#		self.app.exec_()   
		QtCore.QCoreApplication.instance().quit

    def show(self):                                      # Finalizing the Grid for Display
 #       print self.wndow.parent
        self.wndow.setGeometry(self.wndow.width, self.wndow.height, self.wndow.width, self.wndow.height)                        # setting the geometry for the wndow
        self.wndow.center()                                               # Aligning to the center
        self.wndow.setWindowTitle(self.wndow.text)
        self.wndow.show()
        sys.exit(self.wndow.app.exec_())

    def addWidget(self,widget):
        widget_type = type(widget)
#        print widget_type

        
        if(widget_type==Button or isinstance(widget,Button)):
            widget.controller = QtGui.QPushButton(widget.text,self.wndow)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            if(widget.callbackMethod is not None):
                widget.controller.clicked.connect(widget.callbackMethod)

        elif(widget_type==TextBuffer or isinstance(widget,TextBuffer)):
            widget.controller = QtGui.QTextEdit(widget.text,self.wndow)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
        
        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = QtGui.QCheckBox(widget.title, self.wndow)
            widget.controller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            
        elif(widget_type==RadioButton or isinstance(widget,RadioButton)):
            widget.groupBox = QtGui.QGroupBox("", self.wndow)
            widget.controller = []
            radio_controller = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.positions_X[0], widget.positions_Y[0])
            
            radio_controller.resize(widget.width, widget.height)
            radio_controller.move(0, 0)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_controller.resize(widget.width, widget.height)
                radio_controller.move(widget.positions_X[i]-widget.positions_X[0], widget.positions_Y[i]-widget.positions_Y[0])
                widget.controller.append(radio_controller)
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].setChecked(True)
                
        elif(widget_type==List or isinstance(widget,List)):
            widget.controller = QtGui.QComboBox(self.wndow)
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)

        elif(widget_type==TextArea or isinstance(widget,TextArea)):
            widget.instance = QtGui.QLineEdit(self.wndow)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)

        elif(widget_type==ShowText or isinstance(widget,ShowText)):
            widget.instance = QtGui.QLabel(widget.title,self.wndow)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)

        elif(widget_type==Slider or isinstance(widget,Slider)):
			widget.instance = QtGui.QSlider(QtCore.Qt.Horizontal,self.wndow)
			widget.instance.resize(widget.width,widget.height)
			widget.instance.move(widget.position_X, widget.position_Y)
		
        elif(widget_type==SpinBox or isinstance(widget,SpinBox)):
			widget.instance = QtGui.QSpinBox(self.wndow)	
			widget.instance.resize(widget.width, widget.height)
			widget.instance.move(widget.position_X, widget.position_Y)
			widget.instance.setMaximum(widget.end)

        elif(widget_type==PasswordField or isinstance(widget,PasswordField)):
            widget.instance = QtGui.QLineEdit(self.wndow)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.setEchoMode(2)
            widget.instance.move(widget.position_X, widget.position_Y)





class Button(object):
    controller = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def clickTrigger(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.clicked.connect(method)
        return True
        
class TextBuffer(object):
    controller = None
    callback = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.setText(text)
        return True

    def concatText(self,text):
        if(self.controller == None):
            self.text = self.text+text
        else:
            self.text = self.controller.toPlainText() + text
            self.controller.setText(self.text)
        return True              

    def clearBuffer(self):
        self.controller.setText("")
        return True



class CheckBox(object):
        controller = None
        value = False
        def __init__(self,title,X,Y,width,height):
                self.title = title
                self.position_X = X
                self.position_Y = Y
                self.width = width
                self.height = height

        def setBox(self,value):
                if(self.controller == None):
                    self.value = value
                else:
                    self.controller.setChecked(value)

        def getBox(self):
                if(self.controller == None):
                    return self.value
                else:
                    return self.controller.isChecked()

''' WIDGETS: List '''

class List(object):
        controller = None
        def __init__(self,choices,X,Y,width,height,value=""):
            self.choices = choices
            self.position_X = X
            self.position_Y = Y
            self.width = width
            self.height = height
            self.value = value

        def getValue(self):
            if(self.controller == None):
                return self.value
            else:
                return self.choices[self.controller.currentIndex() - 1]

class TextArea(object):
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.setText(text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.text()



''' WIDGETS: LabelText '''
class ShowText(object):
    instance = None		
  #  print "Hello"
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

class Slider(object):
    instance = None
    def __init__(self,start,end,X,Y,width,height):
	self.start=start
        self.end=end
        self.position_X = X
        self.position_Y = Y
        self.width = width
	self.height = height

    def getValue(self):
	    if(self.instance == None):
		return ''
	    else:   
		return str(self.instance.value())

class SpinBox(object):
    instance = None

    def __init__(self,start,end,X,Y,width,height):
        self.start=start
        self.end=end
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def getValue(self):
	if(self.instance == None):
	    return ''
	else:   
            return str(self.instance.value())


class PasswordField(object):
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.setText(text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.text()


class RadioButton(object):
        controller = None
        selected_pos = None

        def __init__(self,width,height):
            self.labels = []
            self.positions_X = []
            self.positions_Y = []
            self.width = width
            self.height = height

        def addButton(self,label,X,Y):
            self.labels.append(label)
            self.positions_X.append(X)
            self.positions_Y.append(Y)
            return True

        def getButton(self):
                for i in range(len(self.controller)):
                    if(self.controller[i].isChecked()):
                        return self.labels[i]
                return None

        def setButton(self,pos):
            if(self.controller == None):
                self.selected_pos = pos
            else:
                button_controller = self.controller[pos]
                button_controller.setChecked(True)
