#import sip
#sip.setapi('QVariant', 2)

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    parent = None
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__() 
        print self
        self.id = id
        self.text = title
        self.width = width
        self.height = height
    
    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())

class Canvas(object):
    window = None
    def __init__(self, id, title,width,height):
        self.window = Window(id, title,width,height)


    def show(self):                                      # Finalizing the Grid for Display
        print self.window.parent
        self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)                        # setting the geometry for the window
        self.window.center()                                               # Aligning to the center
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())




    def add(self,widget):
        widget_type = type(widget)
        print widget_type
        if(widget_type==TextArea or isinstance(widget,TextArea)):
            widget.controller = QtGui.QTextEdit(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
        
        elif(widget_type==Button or isinstance(widget,Button)):
            widget.controller = QtGui.QPushButton(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            if(widget.callbackMethod is not None):
                widget.controller.clicked.connect(widget.callbackMethod)


        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = QtGui.QCheckBox(widget.title, self.window)
            widget.controller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            
        elif(widget_type==RadioGroup or isinstance(widget,RadioGroup)):
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
                
        elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.controller = QtGui.QComboBox(self.window)
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)

        elif(widget_type==TextField or isinstance(widget,TextField)):
            widget.controller = QtGui.QLineEdit(self.window)
            #widget.controller.value(widget.text)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            #widget.controller.value(widget.text)

        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.controller = QtGui.QLabel(widget.title,self.window)
            widget.controller.resize(widget.width, widget.height)
            if(widget.fontsize is not None):
                jksfjch = str(widget.fontsize)
                style = "padding: 0px; margin: 0px;  font-weight: bold;font-size: "+jksfjch+";"
                print style
                widget.controller.setStyleSheet( style )
            print widget.title
            widget.controller.move(widget.position_X, widget.position_Y)
            #self.setGeometry(300, 300, 250, 180)
            
        elif(widget_type==Slider or isinstance(widget,Slider)):
            widget.controller = QtGui.QSlider(QtCore.Qt.Horizontal, self.window)
            widget.controller = QtGui.QSlider(QtCore.Qt.Horizontal)            
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            widget.controller.setTickPosition(1)
            widget.controller.setRange(widget.from_,widget.to_)
            print widget.to_
            #widget.controller.connect(widget.controller.connect, None, widget.value_changed)
            #widget.controller.valueChanged.connect(widget.handleSlider)
	    
            #QAbstractSlider.value (self)
            #widget.controller.TicksAbove	
            #widget.controller.resize(widget.width, widget.height)    
            #print widget.title
            #widget.controller.move(widget.position_X, widget.position_Y)
            #self.setGeometry(300, 300, 250, 180)
        #elif(widget_type==Dialog or isinstance(widget,Dialog)):
           # widget.controller=QtGui.QDialog(None)
            #widget.controller.setVisible(True)
            

class Dialog(object):
    controller = None
    def __init__(self,title,text):
        self.text = text
        
    
    def show(self,width,height,title,text):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text);
        msgBox.exec_();
       
        

''' WIDGETS: Slider '''
class Slider(object):
    controller = None
    callbackMethod = None
    Type = None
    Slider_var = 0
    def __init__(self,title,X,Y,width,height,from_,to_):
        self.Type = "Slider"
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.from_ = from_
        self.to_ = to_

    def value_changed(self,value):
        print "ok"

    def getValue(self):
        print self.Slider_var
        return self.controller.value()
    #def handleSlider(self, val):
	#newVal = fit(val,self.slider.minimum(),self.slider.maximum(),self._new_slider_min,self._new_slider_max)

	#print "Slider: %0.2f => %0.2f" % (val, newVal)

        

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


''' WIDGETS: LabelText '''
class LabelText(object):
    controller = None
    def __init__(self,title,X,Y,width,height,size=None):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.fontsize = size
        

''' WIDGETS: TextField '''
class TextField(object):
    controller = None
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
            self.controller.SetValue(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.text()


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


if __name__ == '__main__':

    #Functions bind to button events
    def SubmitButtonClick(event=None):
        report = " Your city is "+valuelist.getValue()+"\n"
        if(checkbox1.getValue()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"
    
        if(checkbox2.getValue()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"
    
        report = report + " you are "+rb1.getValue()+"\n"
        report = report + " you need "+rb2.getValue()+"\n"

        #age = int(slider.getValue())
        #textarea.appendText("_______________________\n"+report+"\n\n"+age)
        Msg.show(100,200,"Hello","This is test Dialog!")
  
        return True 
    
    def AboutButtonClick(event=None):
        textarea.setText("Created by qtGUI Author : Prateek Mukati\n")
        return True
    
    
    
    #Constructor canvas
    canvas = Canvas(1, 'qtGUI | Prateek Mukati' ,510,300)
    
    
    #Dropdown valuelist
    cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
    valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
    canvas.add(valuelist)
    
    #checkboxs
    checkbox1 = CheckBox("I have read the code.",10,45,215,15)
    checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
    checkbox1.setValue(True)
    canvas.add(checkbox1)
    canvas.add(checkbox2)
    
    #radioGroup1
    rb1 = RadioGroup(60,50)
    rb1.addRadioButton("Nice",10,110)
    rb1.addRadioButton("Good",70,110)
    rb1.addRadioButton("Great",140,110)
    rb1.setButtonTrue(2)
    canvas.add(rb1)
    
    #radioGroup2
    rb2 = RadioGroup(100,50)
    rb2.addRadioButton("Option #1",10,160)
    rb2.addRadioButton("Option #2",110,160)
    rb2.setButtonTrue(0)
    canvas.add(rb2)
    
    #TextArea
    textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
    canvas.add(textarea)
    
    #Creating Buttons
    submitBtn = Button("Submit",130,230,120,30)
    aboutBtn = Button("About",260,230,120,30)

    #Slider
    slider = Slider("Select your Age :",10,200,100,60,18,24)
    canvas.add(slider)

    Msg = Dialog()
    canvas.add(Msg)

    lab = LabelText("sdaf",10,200,100,10)
    #canvas.add(lab)

    #img = QImage("/tmp/example.png")
    
    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    
    #Adding buttons to canvas
    canvas.add(aboutBtn)
    canvas.add(submitBtn)
    
    canvas.show()

