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

	def SubmitButtonClick(event=None):

	    hobbies_temp = "Your hobbies are the following:"
	    hobbies = ""
	    h_list = []
	    h_count = 0

	    if(checkbox11.get_state()):
		hobbies = hobbies + "You like Swimming\n"
		h_list = h_list + ["Swimming"]
		h_count = h_count + 1

	    if(checkbox12.get_state()):
		hobbies = hobbies + "You like Football\n"
		h_list = h_list + ["Football"]
		h_count = h_count + 1

	    if(checkbox13.get_state()):
		hobbies = hobbies + "You like Cycling\n"
		h_list = h_list + ["Cycling"]
		h_count = h_count + 1

	    if(checkbox14.get_state()):
		hobbies = hobbies + "You like Coding :P\n"
		h_list = h_list + ["Coding"]
		h_count = h_count + 1

	    if(checkbox15.get_state()):
		hobbies = hobbies + "You like Jogging\n"
		h_list = h_list + ["Jogging"]
		h_count = h_count + 1

	    if(checkbox16.get_state()):
		hobbies = hobbies + "You like Chatting :)\n"
		h_list = h_list + ["Chatting"]
		h_count = h_count + 1



	    skills_temp = "You are comfortable with the following languages:"
	    skills = ""
	    skill_list = []
	    skill_count = 0;

	    if(checkbox1.get_state()):
		skills = skills + "You like Java\n"
		skill_list = skill_list + ["Java"]    
	    	skill_count = skill_count + 1;
	    
	    if(checkbox2.get_state()):
		skills = skills + "You like C\n"
		skill_list = skill_list + ["C"]    
	    	skill_count = skill_count + 1;

	    if(checkbox3.get_state()):
		skills = skills + "You like C++\n"
		skill_list = skill_list + ["C++"]    
	    	skill_count = skill_count + 1;

	    if(checkbox4.get_state()):
		skills = skills + "You like Python\n"
		skill_list = skill_list + ["Python"]    
	    	skill_count = skill_count + 1;

	    if(checkbox5.get_state()):
		skills = skills + "You like Objective C\n"
		skill_list = skill_list + ["Obejective C"]    
	    	skill_count = skill_count + 1;

	    if(checkbox6.get_state()):
		skills = skills + "You like Ruby :)\n"
		skill_list = skill_list + ["Ruby"]    
	    	skill_count = skill_count + 1;

	
	    Student_Name = name.getText()
	    Student_Rollno = rollno.getText()

	 
	    Gender = rb1.get_state()
	    Department = rb2.get_state()

	    Year = valuelist.getValue()
	    CG = str(CGPA.getValue())
	    per = str(marks.getValue())

	    textarea.setText("Name : " +Student_Name+"\n"+"Entry No :"+Student_Rollno+"\n"+"Year : "+Year+"\n"+"Gender :"+Gender+"\n"+ "Programming Skills :"+"\n"+skills+"\n"+"Hobbies :"+"\n"+hobbies+"\n"+"Department : "+Department+"\n"+"CGPA :"+CG+"\n"+"Marks : "+per)

	    if(Year == "First Year"):
		cv_yr = "1st"
		sem = "1"
	    elif(Year == "Second Year"):
		cv_yr = "2nd"
		sem = "3"
	    elif(Year == "Third Year"):
		sem = "5"
		cv_yr = "3rd"
	    elif(Year == "Fourth Year"):
		sem = "7"
		cv_yr = "4th"

	    skill_str = ""
	    hobby_str = ""

	    for i in range(0,skill_count):
		skill_str = skill_str + "\t* "+skill_list[i]+"\n"

	    for i in range(0,h_count):
		hobby_str = hobby_str + "\t* "+h_list[i]+"\n"

	    cv = Student_Name+"\t\t\t\t"+"Entry No.: "+Student_Rollno+"\n"+Gender+", "+cv_yr+" "+Department+"\t\t"+per+"% in 12th Standard"+ "\n-----------------------------------------------------------------\n"+"\nSecured a CGPA of "+CG+"/10 in "+sem+" semesters\n"+"\n\nProgramming Skills:"+"\n"+skill_str+"\n"+"Co-curriculars:"+"\n"+hobby_str

	    filename = "Resume-"+Student_Name+".txt"
	    cv_file = open('../'+filename,'w')
	    cv_file.write(cv)
	    cv_file.close()
	    return True

	#Constructor canvas
	canvas = Main_Window(1, 'Common API' ,510,670)




	label_name = LabelText("Name:",30,40,60,40)
	name = TextField("",100,40,120,40)
	canvas.add_widget(label_name)
	canvas.add_widget(name)

	label_rollno = LabelText("Entry No:",270,40,80,40)
	rollno = TextField("",360,40,120,40)
	canvas.add_widget(label_rollno)
	canvas.add_widget(rollno)


	year = ['First Year', 'Second Year', 'Third Year', 'Fourth Year']
	valuelist = ValueList(year,20,100,200,20,"Select your year")
	canvas.add_widget(valuelist)


	rb1 = RadioButtons(90,20)
	rb1.add_radiobutton("Male",350,100)
	rb1.add_radiobutton("Female",350,120)
	canvas.add_widget(rb1)




	label_skills = LabelText("PROGRAMMING SKILLS :",20,150,190,40)
	canvas.add_widget(label_skills)


	checkbox1 = CheckBox("Java",20,190,215,20)
	checkbox2 = CheckBox("C",20,215,215,20)
	checkbox3 = CheckBox("C++",20,240,215,20)
	checkbox4 = CheckBox("Python",20,265,215,20)
	checkbox5 = CheckBox("Objective C",20,290,215,20)
	checkbox6 = CheckBox("Ruby",20,315,215,20)


	canvas.add_widget(checkbox1)
	canvas.add_widget(checkbox2)
	canvas.add_widget(checkbox3)
	canvas.add_widget(checkbox4)
	canvas.add_widget(checkbox5)
	canvas.add_widget(checkbox6)


	label_hobbies = LabelText("HOBBIES :",280,150,190,40)
	canvas.add_widget(label_hobbies)

	checkbox11 = CheckBox("Swimming",280,190,215,20)
	checkbox12 = CheckBox("Football",280,215,215,20)
	checkbox13 = CheckBox("Cycling",280,240,215,20)
	checkbox14 = CheckBox("Coding :P",280,265,215,20)
	checkbox15 = CheckBox("Jogging",280,290,215,20)
	checkbox16 = CheckBox("Chatting :)",280,315,215,20)


	canvas.add_widget(checkbox11)
	canvas.add_widget(checkbox12)
	canvas.add_widget(checkbox13)
	canvas.add_widget(checkbox14)
	canvas.add_widget(checkbox15)
	canvas.add_widget(checkbox16)

	label_CGPA = LabelText("CGPA ",20,380,60,50)
	CGPA =  SpinBox(0.0,10.0,70,380,80,30)
	canvas.add_widget(label_CGPA)
	canvas.add_widget(CGPA)

	label_marks = LabelText("12th Marks:",20,485,90,50)
	marks=Slider(0,100,120,470,200,50)
	canvas.add_widget(label_marks)
	canvas.add_widget(marks)


	label_department = LabelText("DEPARTMENT :",280,370,190,40)
	canvas.add_widget(label_department)


	rb2 = RadioButtons(150,20)
	rb2.add_radiobutton("Mechanical",280,410)
	rb2.add_radiobutton("Electrical",280,430)
	rb2.add_radiobutton("Computer Science",280,450)
	canvas.add_widget(rb2)


	label_name = LabelText("GENDER :",280,90,70,40)
	canvas.add_widget(label_name)


	textarea = TextBox("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,520,220,130)
	canvas.add_widget(textarea)

	submitBtn = Button("Evaluate",360,620,120,30)
	submitBtn.on_click(SubmitButtonClick)

	canvas.add_widget(submitBtn)

	canvas.show()

