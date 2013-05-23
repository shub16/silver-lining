#import sip
#sip.setapi('QVariant', 2)

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    parent = None
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__() 
     #   print self
        self.id = id
        self.text = title
        self.width = width
        self.height = height
    
    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())

class Main_Window(object):
    window = None
    def __init__(self, id, title,width,height):
        self.window = Window(id, title,width,height)
	 


    def show(self):                                      # Finalizing the Grid for Display
        #print self.window.parent
        self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)                        # setting the geometry for the window
        self.window.center()                                               # Aligning to the center
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())




    def add_widget(self,widget):
        widget_type = type(widget)
     
        if(widget_type==TextBox or isinstance(widget,TextBox)):
            widget.instance = QtGui.QTextEdit(widget.text,self.window)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)
        
        elif(widget_type==Button or isinstance(widget,Button)):
            widget.instance = QtGui.QPushButton(widget.text,self.window)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)
            if(widget.callbackMethod is not None):
                widget.instance.clicked.connect(widget.callbackMethod)


        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.instance = QtGui.QCheckBox(widget.title, self.window)
            widget.instance.setChecked(widget.value)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)
            
        elif(widget_type==RadioButtons or isinstance(widget,RadioButtons)):
            widget.groupBox = QtGui.QGroupBox("", self.window)
            widget.instance = []
            radio_instance = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.positions_X[0], widget.positions_Y[0])
            radio_instance.setChecked(True)
            radio_instance.resize(widget.width, widget.height)
            radio_instance.move(0, 0)
            widget.instance.append(radio_instance)
            for i in range(1,len(widget.labels)):
                radio_instance = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_instance.resize(widget.width, widget.height)
                radio_instance.move(widget.positions_X[i]-widget.positions_X[0], widget.positions_Y[i]-widget.positions_Y[0])
                widget.instance.append(radio_instance)
            if(widget.selected_pos != None):
                widget.instance[widget.selected_pos].setChecked(True)

	elif(widget_type==TextField or isinstance(widget,TextField)):
            widget.instance = QtGui.QLineEdit(self.window)
            #widget.instance.value(widget.text)
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)
            #widget.instance.value(widget.text)

	elif(widget_type==TextFieldPass or isinstance(widget,TextFieldPass)):
            widget.instance = QtGui.QLineEdit(self.window)
            #widget.instance.value(widget.text)
            widget.instance.resize(widget.width, widget.height)    
	    widget.instance.setEchoMode(2)
            widget.instance.move(widget.position_X, widget.position_Y)
            #widget.instance.value(widget.text)



        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.instance = QtGui.QLabel(widget.title,self.window)
            widget.instance.resize(widget.width, widget.height)    
          #  print widget.title
            widget.instance.move(widget.position_X, widget.position_Y)
            #self.setGeometry(300, 300, 250, 180)

	elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.instance = QtGui.QComboBox(self.window)
            widget.instance.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.instance.addItem(widget.choices[i])
            widget.instance.resize(widget.width, widget.height)    
            widget.instance.move(widget.position_X, widget.position_Y)
        
	elif(widget_type==Slider or isinstance(widget,Slider)):
	        widget.instance = QtGui.QSlider(QtCore.Qt.Horizontal,self.window)
		widget.instance.resize(widget.width, widget.height)
		widget.instance.move(widget.position_X, widget.position_Y)
		

	elif(widget_type==SpinBox or isinstance(widget,SpinBox)):
	        widget.instance = QtGui.QSpinBox(self.window)	
		widget.instance.resize(widget.width, widget.height)
		widget.instance.move(widget.position_X, widget.position_Y)
		widget.instance.setMaximum(widget.end)
		


class TextBox(object):
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
         

    def clear(self):
        self.instance.setText("")
        return True


class ValueList(object):
        instance = None
        def __init__(self,choices,X,Y,width,height,value=""):
            self.choices = choices
            self.position_X = X
            self.position_Y = Y
            self.width = width
            self.height = height
            self.value = value

        def getValue(self):
            if(self.instance == None):
                return self.value
            else:
                return self.choices[self.instance.currentIndex() - 1]




class Button(object):
    instance = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def on_click(self,event):
        if(self.instance == None):
            self.callbackMethod = event
        else:
            self.instance.clicked.connect(event)
        return True


class CheckBox(object):
        instance = None
        value = False
        def __init__(self,title,X,Y,width,height):
                self.title = title
                self.position_X = X
                self.position_Y = Y
                self.width = width
                self.height = height

        def set_state(self,value):
                if(self.instance == None):
                    self.value = value
                else:
                    self.instance.setChecked(value)

        def get_state(self):
                if(self.instance == None):
                    return self.value
                else:
                    return self.instance.isChecked()

class RadioButtons(object):
        instance = None
        selected_pos = None

        def __init__(self,width,height):
            self.labels = []
            self.positions_X = []
            self.positions_Y = []
            self.width = width
            self.height = height

        def add_radiobutton(self,label,X,Y):
            self.labels.append(label)
            self.positions_X.append(X)
            self.positions_Y.append(Y)
            return True

        def get_state(self):
                for i in range(len(self.instance)):
                    if(self.instance[i].isChecked()):
                        return self.labels[i]
                return None



''' WIDGETS: LabelText '''
class LabelText(object):
    instance = None		
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

''' WIDGETS: TextField '''
class TextField(object):
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


class TextFieldPass(object):
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










if __name__ == '__main__':

    #Functions bind to button events
    def SubmitButtonClick(event=None):
        if(checkbox1.get_state()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"
    
        if(checkbox2.get_state()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"
    
        report = report + " you are "+rb1.get_state()+"\n"
        report = report + " you need "+rb2.get_state()+"\n"
    
        textarea.appendText("_______________________\n"+report+"\n\n")
        return True 
    
    def AboutButtonClick(event=None):
        textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
        return True
    
    
    
    #Constructor canvas
    canvas = Main_Window(1, 'wxGUI -v1.0 | ArinkVerma' ,510,300)
    
    
    #Dropdown valuelist
    
    #checkboxs
    checkbox1 = CheckBox("I have read the code.",10,45,215,15)
    checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
    checkbox1.set_state(True)
    canvas.add_widget(checkbox1)
    canvas.add_widget(checkbox2)
    
    #radioGroup1
    rb1 = RadioButtons(60,50)
    rb1.add_radiobutton("Nice",10,110)
    rb1.add_radiobutton("Good",70,110)
    rb1.add_radiobutton("Great",140,110)
    canvas.add_widget(rb1)
    
    #radioGroup2
    rb2 = RadioButtons(100,50)
    rb2.add_radiobutton("Option #1",10,160)
    rb2.add_radiobutton("Option #2",110,160)
    canvas.add_widget(rb2)
    
    #TextBox
    textarea = TextBox("\n Click submit button to see output here!!",250,10,250,200)
    canvas.add_widget(textarea)
    
    #Creating Buttons
    submitBtn = Button("Submit",130,230,120,30)
    aboutBtn = Button("About",260,230,120,30)
    
    #Callback methods on buttons click
    submitBtn.on_click(SubmitButtonClick)
    aboutBtn.on_click(AboutButtonClick)
    
    #Adding buttons to canvas
    canvas.add_widget(aboutBtn)
    canvas.add_widget(submitBtn)
    
    canvas.show()



