import os
import sys
import re	
from PyQt4 import QtGui, QtCore	
from functools import partial

class SurveyWindow(QtGui.QWidget):	
    parent = None	
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(SurveyWindow, self).__init__() 
        self.id = id
        self.text = title
        self.width = width
        self.height = height
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
	######   setting the geometry for the window
	self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)
        self.window.center()                                               # Aligning to the center
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())
    def add(self,widget):
        widgetName = type(widget)
        
	if(widgetName==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = QtGui.QCheckBox(widget.title, self.window)
            widget.controller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
        elif(widgetName==Button or isinstance(widget,Button)):
            widget.controller = QtGui.QPushButton(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            if(widget.callbackMethod is not None):
                widget.controller.clicked.connect(widget.callbackMethod)
	###
	elif(widgetName==Password or isinstance(widget,Password)):
	    widget.controller = QtGui.QLineEdit(self.window)
	    widget.controller.setEchoMode(2)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)

	elif(widgetName==Slider or isinstance(widget,Slider)):
	    widget.controller = QtGui.QSlider(QtCore.Qt.Horizontal,self.window)
	    widget.controller.setFocusPolicy(QtCore.Qt.NoFocus)
	    widget.controller.setMinimum(widget.start)
	    widget.controller.setMaximum(widget.end)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(widgetName==SpinBox or isinstance(widget,SpinBox)):
	    widget.controller = QtGui.QSpinBox(self.window)
	    widget.controller.setMinimum(widget.start)
	    widget.controller.setMaximum(widget.end)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(widgetName==Label or isinstance(widget,Label)):
	    widget.controller = QtGui.QLabel(widget.text,self.window)
	    widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(widgetName==TextLine or isinstance(widget,TextLine)):
	    widget.controller = QtGui.QLineEdit(self.window)
	    #widget.controller.setEchoMode(2)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	###
	elif(widgetName==TextArea or isinstance(widget,TextArea)):
            widget.controller = QtGui.QTextEdit(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)

        elif(widgetName==RadioGroup or isinstance(widget,RadioGroup)):	
            widget.groupBox = QtGui.QGroupBox("", self.window)
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
	
        elif(widgetName==ValueList or isinstance(widget,ValueList)):
            widget.controller = QtGui.QComboBox(self.window)
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	

####

class Password(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):
	
        #self.text = text
	
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
    

class Slider(object):

    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):
	
        #self.text = text
	self.start=start
	self.end=end
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getValue(self):
	
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.value()
   
class SpinBox(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):
	
        #self.text = text
	self.start=start
	self.end=end
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
    
    def getValue(self):
	
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
    	
    def clear(self):
	
        self.controller.setText("")
	
        return True
	
    

####
class TextArea(object):
	
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
	
	
    def appendText(self,text):
	
        if(self.controller == None):
	
            self.text = self.text+text
	
        else:
	
            self.text = self.controller.toPlainText() + text
	
            self.controller.setText(self.text)
	
        return True              
	
	
    def clear(self):
	
        self.controller.setText("")
	
        return True
	
	
	
	
class Button(object):
	
    controller = None
	
    callbackMethod = None
	
    def __init__(self,text,X,Y,width,height):
	
        self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def clickListener(self,method):
	
        if(self.controller == None):
	
            self.callbackMethod = method
	
        else:
	
            self.controller.clicked.connect(method)
	
        return True
	
    #### shubham
    

    ###### end
	
class CheckBox(object):
	
        controller = None
	
        value = False
	
        def __init__(self,title,X,Y,width,height):
	
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
	
	
        def setButtonTrue(self,pos):
	
            if(self.controller == None):
	
                self.selected_pos = pos
	
            else:
	
                button_controller = self.controller[pos]
	
                button_controller.setChecked(True)
	
	
''' WIDGETS: ValueList '''
	
	
class ValueList(object):
	
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
	

########3333
## for ass5


def isAlphaNumeric(string):
    strMatchAlnum = re.findall('[a-zA-Z0-9]', string)
    strMatchNum = re.findall('[0-9]',string)
    strMatchAlpha = re.findall('[a-zA-z]',string)
    if len(string) == len(strMatchAlnum) and len(strMatchNum) > 0 and len(strMatchAlpha) > 0:
        return True
    else:
        return False

class changePassword:

    def __init__(self, username, oldPasswd, newPasswd, confirmPasswd):
        self.username = username
        self.oldPasswd = oldPasswd
        self.newPasswd = newPasswd
        self.confirmPasswd = confirmPasswd
        #print self.newPasswd
        #print self.confirmPasswd

    def checkPasswordValidity(self):

        if len(self.newPasswd) <= 6:
            print("Password must have more than 6 characters.")
            return False
        elif not(isAlphaNumeric(self.newPasswd)):
            print "Password must have atleast 1 alphabet and 1 digit."
            return False
        elif self.newPasswd != self.confirmPasswd:
            print "Passwords did not match."
            return False

        return True

def submitData(List):
    uname = List[0]
    oldPwd = List[1]
    newPwd = List[2]
    confirmPwd = List[3]

    #print oldPwd
    #print newPwd
    #print confirmPwd
    cp = changePassword(uname, oldPwd, newPwd, confirmPwd)
    if cp.checkPasswordValidity():
        print "Password changed successfully."
        sys.exit()
        return True
    else:
	List[0]=''
        List[1]=''
        List[2]=''
        List[3]=''
        return False





    

###############
	


if __name__ == '__main__':

### main for ass5
	global List
	List=[]
	
	def test(event=None):
		List = [text.getText(), pass1.getText(),pass2.getText() , pass3.getText()]

		
		text.setText('')
		pass1.setText('')
		pass2.setText('')
		pass3.setText('')

		submitData(List)

	Frame = WindowFrame(1, 'login' ,510,300)
	username=Label('Username', 10, 10,150,30)
	oldpass=Label('Old Password', 10, 50,150,30)
	newpass=Label('New Password', 10, 90,150,30)
	confirmpass=Label('Confirm Password', 10, 130,150,30)
	
	text=TextLine(200,10,150,30)
	pass1=Password(200,50,150,30)		
	pass2=Password(200,90,150,30)		
	pass3=Password(200,130,150,30)		
	
	button=Button('submit',170,170,60,30)
	Frame.add(username)
	Frame.add(oldpass)
	Frame.add(newpass)
	Frame.add(confirmpass)
	Frame.add(text)
	Frame.add(pass1)
	Frame.add(pass2)
	Frame.add(pass3)
	Frame.add(button)

        List = [text.getText(), pass1.getText(),pass2.getText() , pass3.getText()]
        button.clickListener(test)
    

	Frame.show()

#
	


