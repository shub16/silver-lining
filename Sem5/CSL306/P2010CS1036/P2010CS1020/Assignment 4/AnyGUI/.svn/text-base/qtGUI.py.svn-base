

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    parent = None
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__() 
        self.id = id
        self.text = title
        self.width = width
        self.height = height
    
    def center(self):
        qr = self.frameGeometry()                                   
        cp = QtGui.QDesktopWidget().availableGeometry().center()    
        qr.moveCenter(cp)                                           
        self.move(qr.topLeft())

class Main_Window(object):
    window = None
    def __init__(self, id, title,width,height):
        self.window = Window(id, title,width,height)
	 


    def show(self):                                      
        self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)                        
        self.window.center()                                               
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
	    radio_instance.setChecked(True)
            widget.groupBox.move(widget.positions_X[0], widget.positions_Y[0])
            
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



if __name__ == '__main__':

	def Evaluate(event=None):
	    display = "" 
	    textarea.clear()
	    temp = "Your hobbies are the following:"
	
	   	
	    if(checkbox1.get_state()):
		display = display + "You like Swimming\n"
	    
	    if(checkbox2.get_state()):
		display = display + "You like reading novels\n"

	    if(checkbox3.get_state()):
		display = display + "You like listening to music\n"

	    if(checkbox4.get_state()):
		display = display + "You like cycling\n"

	    if(checkbox5.get_state()):
		display = display + "You like to write poems\n"

	    if(checkbox6.get_state()):
		display = display + "You like dancing\n"

	    if(not(checkbox1.get_state()) and not(checkbox2.get_state()) and not(checkbox3.get_state()) and not(checkbox4.get_state()) and not(checkbox5.get_state()) and not(checkbox6.get_state())):
		display = display + "No hobbies? Get a Life :P \n"   


	    
	    textarea.setText("You are "+rb1.get_state()+"\n\n"+temp+"\n\n"+display+"\n\n")
	    return True 


	#Constructor canvas
	canvas = Main_Window(1, 'Common API | Kshitij_PyQt' ,510,300)

	#Creating checkboxes for displaying hobbies
	checkbox1 = CheckBox("Swimming",370,20,215,20)
	checkbox2 = CheckBox("Reading Books",370,45,215,20)
	checkbox3 = CheckBox("Music",370,70,215,20)
	checkbox4 = CheckBox("Cycling",370,95,215,20)
	checkbox5 = CheckBox("Poetry",370,120,215,20)
	checkbox6 = CheckBox("Dancing",370,145,215,20)

	#Adding checkboxes 
	canvas.add_widget(checkbox1)
	canvas.add_widget(checkbox2)
	canvas.add_widget(checkbox3)
	canvas.add_widget(checkbox4)
	canvas.add_widget(checkbox5)
	canvas.add_widget(checkbox6)


	#Radio buttons for gender
	rb1 = RadioButtons(90,30)
	rb1.add_radiobutton("Male",10,20)
	rb1.add_radiobutton("Female",10,45)
	canvas.add_widget(rb1)


	#Adding the text area
	textarea = TextBox("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,20,230,150)
	canvas.add_widget(textarea)

	#Creating Buttons
	submitBtn = Button("Evaluate",170,210,120,30)

	#Callback methods on button click
	submitBtn.on_click(Evaluate)


	#Adding button to canvas
	canvas.add_widget(submitBtn)

	canvas.show()
