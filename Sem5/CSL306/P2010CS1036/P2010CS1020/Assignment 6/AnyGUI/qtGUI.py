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
            report = "" 
	    textarea.clear()
	    temp = "Your hobbies are the following:"

	   
	    temp2 = "Your city is "+valuelist.getValue()+"\n"

	    if(checkbox1.get_state()):
		report = report + "You like Swimming\n"
	    
	    if(checkbox2.get_state()):
		report = report + "You like reading novels\n"

	    if(checkbox3.get_state()):
		report = report + "You like listening to music\n"

	    if(checkbox4.get_state()):
		report = report + "You like cycling\n"

	    if(checkbox5.get_state()):
		report = report + "You like to write poems\n"

	    if(checkbox6.get_state()):
		report = report + "You like dancing\n"

	    if(not(checkbox1.get_state()) and not(checkbox2.get_state()) and not(checkbox3.get_state()) and not(checkbox4.get_state()) and not(checkbox5.get_state()) and not(checkbox6.get_state())):
		report = report + "No hobbies? Get a Life :P \n"   

	    marks =str( performance.getValue())
	    cg = str(Spin.getValue())
	    
	    textarea.setText("You are "+rb1.get_state()+"\n\n"+temp2+"\n"+temp+"\n\n"+report+"\n\n"+"Marks :"+marks+"\n\n"+"CGPA :"+cg)
	    return True 





	#Constructor canvas
    canvas = Main_Window(1, 'Common API | Kshitij_Qt' ,510,400)

	#Spin Box
    label_marks = LabelText("CGPA ",55,270,60,50)
    Spin =  SpinBox(0.0,10.0,130,275,100,30)
    canvas.add_widget(Spin)
    canvas.add_widget(label_marks)

	#Dropdown valuelist
    cities = ['Amritsar', 'Mumbai', 'Ropar', 'Bhatinda', 'Chandigrah' ]
    valuelist = ValueList(cities,130,200,220,20,"<Select your city>")
    canvas.add_widget(valuelist)

	#checkboxs
    checkbox1 = CheckBox("Swimming",370,20,215,20)
    checkbox2 = CheckBox("Reading Books",370,45,215,20)
    checkbox3 = CheckBox("Music",370,70,215,20)
    checkbox4 = CheckBox("Cycling",370,95,215,20)
    checkbox5 = CheckBox("Poetry",370,120,215,20)
    checkbox6 = CheckBox("Dancing",370,145,215,20)


    canvas.add_widget(checkbox1)
    canvas.add_widget(checkbox2)
    canvas.add_widget(checkbox3)
    canvas.add_widget(checkbox4)
    canvas.add_widget(checkbox5)
    canvas.add_widget(checkbox6)


	#radioGroup1
    rb1 = RadioButtons(90,30)
    rb1.add_radiobutton("Male",10,20)
    rb1.add_radiobutton("Female",10,45)
    canvas.add_widget(rb1)


	#TextBox
    textarea = TextBox("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,20,230,150)
    canvas.add_widget(textarea)

#Creating Buttons
    submitBtn = Button("Evaluate",170,350,120,30)

	#Callback methods on buttons click
    submitBtn.on_click(SubmitButtonClick)

	#Slider
    label_marks = LabelText("Marks ",55,225,60,50)
    performance=Slider(0,100,130,220,200,50)
    canvas.add_widget(performance)
    canvas.add_widget(label_marks)
	#Adding buttons to canvas

    canvas.add_widget(submitBtn)
    canvas.show()
