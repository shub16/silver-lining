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
"""
if __name__ == '__main__':

    #Functions bind to button events
    def SubmitButtonClick(event):
        report = " Your city is "+valuelist.getValue()+"\n"
        if(checkbox1.getBox()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"

        if(checkbox2.getBox()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"

        report = report + " you are "+rb1.getButton()+"\n"
        report = report + " you need "+rb2.getButton()+"\n"

        textarea.concatText("_______________________\n"+report+"\n\n")
        return True 

    def AboutButtonClick(event):
        textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
        return True


'''

    #Constructor Vista
    Vista = Vista(1, 'GTK -v1.0 | Gaurav Katoch' ,510,300)

    #Dropdown valuelist
    cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
    valuelist = List(cities,10,10,200,20,"<Select your city>")
    Vista.addWidget(valuelist)

    #checkboxs
    checkbox1 = CheckBox("I have read the code.",10,45,215,15)
    checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
    checkbox1.setBox(True)
    Vista.addWidget(checkbox1)
    Vista.addWidget(checkbox2)

    #radioGroup1
    rb1 = RadioButton(60,50)
    rb1.addButton("Nice",10,110)
    rb1.addButton("Good",70,110)
    rb1.addButton("Great",140,110)
    rb1.setButton(2)
    Vista.addWidget(rb1)

    #radioGroup2
    rb2 = RadioButton(100,50)
    rb2.addButton("Option #1",10,160)
    rb2.addButton("Option #2",110,160)
    rb2.setButton(0)
    Vista.addWidget(rb2)

    #TextArea
    textarea = TextBuffer("\n Click submit button to see output here!!",250,10,250,200)
    Vista.addWidget(textarea)

    #Creating Buttons
    submitBtn = Button("Submit",130,230,120,30)
    aboutBtn = Button("About",260,230,120,30)

    #Callback methods on buttons click
    submitBtn.clickTrigger(SubmitButtonClick)
    aboutBtn.clickTrigger(AboutButtonClick)

    #Adding buttons to Vista
    Vista.addWidget(aboutBtn)
    Vista.addWidget(submitBtn)

    Vista.show()

'''    
#Constructor canvas
canvas = Vista(1, 'Common API' ,510,500)


#Dropdown valuelist
cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
valuelist = List(cities,130,180,200,20,"<Select your city>")
canvas.addWidget(valuelist)

#checkboxs
checkbox1 = CheckBox("Swimming",370,20,215,20)
checkbox2 = CheckBox("Reading Books",370,45,215,20)
checkbox3 = CheckBox("Music",370,70,215,20)
checkbox4 = CheckBox("Cycling",370,95,215,20)
checkbox5 = CheckBox("Poetry",370,120,215,20)
checkbox6 = CheckBox("Dancing",370,145,215,20)
'''checkbox1.set_state(True)
checkbox2.set_state(True)
checkbox3.set_state(True)
checkbox4.set_state(True)
checkbox5.set_state(True)
checkbox6.set_state(True)'''

canvas.addWidget(checkbox1)
canvas.addWidget(checkbox2)
canvas.addWidget(checkbox3)
canvas.addWidget(checkbox4)
canvas.addWidget(checkbox5)
canvas.addWidget(checkbox6)


#radioGroup1
rb1 = RadioButton(90,30)
rb1.addButton("Male",10,20)
rb1.addButton("Female",10,45)
canvas.addWidget(rb1)


#TextBox
textarea = TextArea("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,20,220,150)
canvas.addWidget(textarea)

#Creating Buttons
submitBtn = Button("Evaluate",170,310,120,30)

#Callback methods on buttons click
submitBtn.clickTrigger(SubmitButtonClick)

#Slider
vol = ShowText("Volume ",55,205,60,50)
volume=Slider(0,101,130,220,200,50)
canvas.addWidget(volume)
canvas.addWidget(vol)

#Spin Box
vol = ShowText("CGPA ",70,410,60,50)
Spin =  SpinBox(0.0,10.0,130,420,200,30)
canvas.addWidget(Spin)
canvas.addWidget(vol)
#Adding buttons to canvas

canvas.addWidget(submitBtn)

canvas.show()
"""
