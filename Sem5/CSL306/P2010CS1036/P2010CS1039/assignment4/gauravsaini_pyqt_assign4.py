import sys	
from PyQt4 import QtGui, QtCore	

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
	
class Canvas(object):	
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
            
class Label(object):

    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):
	

	self.text=text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
            
	
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
	
        report = " You are giving your review of the following dishes of "+ relist.getValue() +' in ' +valuelist.getValue()+".\n"
	
        if(checkbox1.getValue()):
	
            report = report + " Pizza\n"
	

    
	
        if(checkbox2.getValue()):
	
            report = report + " Cheese tomato\n"

        if(checkbox3.getValue()):
	
            report = report + " Chicken Tikka Butter Masala\n"
		
        if(checkbox4.getValue()):
	
            report = report + " Chana Masala\n"
	    
	
        report = report + " You felt food was---> "+rb1.getValue()+".\n"
        
        if(rb2.getValue()=='Not for me!'):
            report =report + "You would not revisit the Restaurant. \n"
        else:
            report =report + "You would love to have a visit again. \n"
	
    
	
        textarea.appendText("_______________________\n"+report+"\n\n")
	
        return True 
	
    
	
    def AboutButtonClick(event=None):
	
        textarea.setText("Created by qtGUI Author : Gaurav Saini\n")
	
        return True
	
    
	
    
	
    
	
    #Constructor Frame
	
    Frame = Canvas(1, 'qtGUI | Gaurav Saini' ,800,500)
	
    
	
    
	
    #Dropdown valuelist
	
    cities = ['New Delhi', 'London', 'Ropar', 'Ludhiana', 'Chandigrah', 'Rome', 'Jaipur' ]
    restaurants = ['Mc Donalds','Pind Baluchi', 'KFC' , 'CCD']
	
    valuelist = ValueList(cities,10,10,110,20,"<Select city>")
    relist = ValueList(restaurants,140,10,150,20,"<Select restaurant>")
	
    Frame.add(valuelist)
    Frame.add(relist)
	
    
	
    #checkboxs
	
    checkbox1 = CheckBox("Pizza",10,45,215,15)
	
    checkbox2 = CheckBox("cheese tomato",10,65,235,15)
    checkbox3 = CheckBox("Chicken Tikka Butter Masala",10,85,235,15)
    checkbox4 = CheckBox("Chana Masala",10,105,235,15)
	
    checkbox1.setValue(True)
    #dishes  = Label('Dishes you like:',10,20,210,15)
    #Frame.add(dishes)
    Frame.add(checkbox1)
	
    Frame.add(checkbox2)
    Frame.add(checkbox3)
    Frame.add(checkbox4)
	
    
	
    #radioGroup1
	
    rb1 = RadioGroup(80,50)
	
    rb1.addRadioButton("Nice",10,130)
	
    rb1.addRadioButton("Good",70,130)
	
    rb1.addRadioButton("Great",140,130)
	
    rb1.setButtonTrue(2)
	
    Frame.add(rb1)
    #radioGroup2
    rb2 = RadioGroup(100,50)
    rb2.addRadioButton("Like to visit again!",10,170)
    rb2.addRadioButton("Not for me!",110,170)
    rb2.setButtonTrue(0)
    Frame.add(rb2)
    #TextArea
    textarea = TextArea("\n Click submit button to see output here!!",500,10,250,400)
    Frame.add(textarea)
    #Creating Buttons
    submitBtn = Button("Submit",130,460,120,30)
    aboutBtn = Button("About",260,460,120,30)
    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    #Adding buttons to Frame
    Frame.add(aboutBtn)
    Frame.add(submitBtn)
    Frame.show()
