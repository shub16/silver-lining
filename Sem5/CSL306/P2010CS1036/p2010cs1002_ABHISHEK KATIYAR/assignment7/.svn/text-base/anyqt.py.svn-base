#Assignment no. 4
import sys
from PyQt4 import QtGui, QtCore

now_position=[180,10]
def default_position(w):						#setting default positions for widgets
	now_position[1]=now_position[1]+10+w
	return now_position
	
class Window(QtGui.QWidget):						#adjusting window
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
        qr = self.frameGeometry()					# get current window frame of desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()	# get center point of Desktop window
        qr.moveCenter(cp)						# moving the center of the window to the cp
        self.move(qr.topLeft())

class frame(object):							#creating frame
    window = None
    id = -1
    title = "frame"
    size = (600,750)
    def __init__(self, id=-1, title="frame",width=600,height=750):
        self.window = Window(id, title,width,height)


    def show(self):                                      # to display frame
        print self.window.parent
        self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)	#setting geometry for the window
        self.window.center()                                               #aligning to center
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())



    def append(self,widget):						#adding widgets to frame
        widget_type = type(widget)
        print widget_type
        if(widget_type==text_area or isinstance(widget,text_area)):	#adding text area
            widget.aps = QtGui.QTextEdit(widget.label,self.window)
            widget.aps.resize(widget.size[0], widget.size[1])    
            widget.aps.move(widget.pos[0], widget.pos[1])
        
        elif(widget_type==button or isinstance(widget,button)):		#adding button
            widget.aps = QtGui.QPushButton(widget.label,self.window)
            widget.aps.resize(widget.size[0], widget.size[1])    
            widget.aps.move(widget.pos[0], widget.pos[1])
            if(widget.callbackMethod is not None):
                widget.aps.clicked.connect(widget.callbackMethod)
                
      	elif(widget_type==text_field or isinstance(widget,text_field)):	#adding text field
		widget.aps = QtGui.QLineEdit(widget.txt,self.window)
        	widget.aps.resize(widget.size[0], widget.size[1])    
            	widget.aps.move(widget.pos[0], widget.pos[1])
            	
        elif(widget_type==text_field2 or isinstance(widget,text_field2)):	#adding protected text field
		widget.aps = QtGui.QLineEdit(widget.text,self.window)
        	widget.aps.resize(widget.size[0], widget.size[1])    
            	widget.aps.move(widget.pos[0], widget.pos[1])
            	widget.aps.setEchoMode(2)
            				 
	elif(widget_type==static_text or isinstance(widget,static_text)):#adding static text
        	widget.aps = QtGui.QLabel(widget.label,self.window)
        	widget.aps.resize(widget.size[0], widget.size[1])    
            	widget.aps.move(widget.pos[0], widget.pos[1])

        elif(widget_type==check_box or isinstance(widget,check_box)):	#adding check box
            widget.aps = QtGui.QCheckBox(widget.label, self.window)
            widget.aps.setChecked(widget.value)
            widget.aps.resize(widget.size[0], widget.size[1])    
            widget.aps.move(widget.pos[0], widget.pos[1])
            
        elif(widget_type==radio_buttons or isinstance(widget,radio_buttons)):#adding radio buttons
            widget.groupBox = QtGui.QGroupBox("", self.window)
            widget.aps = []
            radio_aps = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.positions_X[0], widget.positions_Y[0])
            radio_aps.resize(widget.size[0], widget.size[1])
            radio_aps.move(0, 0)
            widget.aps.append(radio_aps)
            for i in range(1,len(widget.labels)):
                radio_aps = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_aps.resize(widget.size[0], widget.size[1])
                radio_aps.move(widget.positions_X[i]-widget.positions_X[0], widget.positions_Y[i]-widget.positions_Y[0])
                widget.aps.append(radio_aps)
            if(widget.selected_pos != None):
                widget.aps[widget.selected_pos].setChecked(True)
                
        elif(widget_type==Slider or isinstance(widget,Slider)):					#adding slider
	        widget.instance = QtGui.QSlider(QtCore.Qt.Horizontal,self.window,value=3)
		widget.instance.resize(widget.width, widget.height)
		widget.instance.move(widget.position_X, widget.position_Y)
                
        elif(widget_type==combo_box or isinstance(widget,combo_box)):	#adding combo box
            widget.aps = QtGui.QComboBox(self.window)
            widget.aps.addItem(widget.default)
            for i in range(0,len(widget.labels)):
                widget.aps.addItem(widget.labels[i])
            widget.aps.resize(widget.size[0], widget.size[1])    
            widget.aps.move(widget.pos[0], widget.pos[1])
            
        elif(widget_type==SpinBox or isinstance(widget,SpinBox)):	#adding spinbox
	        widget.instance = QtGui.QSpinBox(self.window)	
		widget.instance.resize(widget.width, widget.height)
		widget.instance.move(widget.position_X, widget.position_Y)
		widget.instance.setMaximum(widget.end)

class text_area(object):		#creating class for text area
    aps = None
    apps = None
    id = -1
    p= default_position(0)
    pos=(p[0],p[1])
    size = (185,35)
    default_position(35)
    label="textarea"
    def __init__(self):
        self.text = self.label
        self.position_X = self.pos[0]
        self.position_Y = self.pos[1]
        self.width = self.size[0]
        self.height = self.size[1]

    def set_text(self,text):				#setting values of text
        if(self.aps == None):
            self.text = text
        else:
            self.aps.setText(text)
        return True

    def append_text(self,text):				#adding text
        if(self.aps == None):
            self.text = self.text+text
        else:
            self.text = self.aps.toPlainText() + text
            self.aps.setText(self.text)
        return True              

    def clear(self):					#clearing text
        self.aps.set_text("")
        return True

class button(object):					#class for button
    aps = None
    callbackMethod = None
    id = -1
    p= default_position(0)
    pos=(300,300)
    size = (185,35)
    default_position(35)
    label="button"
    def __init__(self):
        temp=5


    def onclick(self,method):				#function for click on button
        if(self.aps == None):
            self.callbackMethod = method
        else:
            self.aps.clicked.connect(method)
        return True
        
class Slider(object):					#class for slider
    
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
		
class SpinBox(object):					#class for spin box
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

class check_box(object):				#class for checkbox
        aps = None
        parent = None
        label="check box"
        p=default_position(0)
        pos=(p[0],p[1])
        size=(20,20)
        value = False
        def __init__(self):
        	temp=5

        def setValue(self,value):			#setting values for checkbox
                if(self.aps == None):
                    self.value = value
                else:
                    self.aps.setChecked(value)

        def get_value(self):				#getting values for checkbox
                if(self.aps == None):
                    return self.value
                else:
                    return self.aps.isChecked()

class radio_buttons(object):				#class for radio buttons
        aps = None
        selected_pos = None
	size = (30,40)
	pos=(300,330)
	labels=[]
        def __init__(self):
            self.labels = []
            self.positions_X = []
            self.positions_Y = []

        def add_rb(self,label,X,Y):			#adding radio button
            self.labels.append(label)
            self.positions_X.append(X)
            self.positions_Y.append(Y)
            return True

        def get_value(self):				#taking values
                for i in range(len(self.aps)):
                    if(self.aps[i].isChecked()):
                        return self.labels[i]
                return None

        def set_true(self,pos):
            if(self.aps == None):
                self.selected_pos = pos
            else:
                button_aps = self.aps[pos]
                button_aps.setChecked(True)
                
class static_text(object):				#class for static text
	aps=None
	value=False
	pos=(200,300)
	size=(100,50)
	label="static text"
	def __init__(self):
	         temp=5
                 
        def Set_value(self,value):
		if(self.aps==None):
			self.value=value

class combo_box(object):				#class for combo box
        aps = None
        labels=[]
        pos=(250,200)
        size=(30,40)
        default="combo obx"
        def __init__(self):
           temp=5
        def get_value(self):
            if(self.aps == None):
                return self.value
            else:
                return self.labels[self.aps.currentIndex() - 1]

class text_field(object): 				#class for text field
    aps = None
    callback = None
    p=(300,200)
    pos=(p[0],p[1])
    size=(500,200)
    txt=""
    def __init__(self):
       i=1
       
    def set_text(self,text):				#setting value for text
        if(self.aps == None):
            self.text = text
        else:
            self.aps.setText(text)
        return True

    def get_text(self):					#taking value of text
        if(self.aps == None):
            return self.text
        else:
            return self.aps.text()


    def Clear_field(self):				#clearing text field
         if(self.aps == None):
            self.text = text
         else:
            self.aps.set_text(text)
         return True

class text_field2(object): 				#class for text field
    aps = None
    callback = None
    p=(300,200)
    pos=(p[0],p[1])
    size=(500,200)
    text=""
    visibility=True
    def __init__(self):
       i=1
       
    def set_text(self,text):				#setting value for text
        if(self.aps == None):
            self.text = text
        else:
            self.aps.setText(text)
        return True

    def get_text(self):					#taking value of text
        if(self.aps == None):
            return self.text
        else:
            return self.aps.text()  

    def Clear_field(self):				#clearing text field
         if(self.aps == None):
            self.text = text
         else:
            self.aps.set_text(text)
         return True

if __name__ == '__main__':				#main function
	temp=5
	g=Slider(0,10,200,100,50,50)
	frame.append(g)
	
