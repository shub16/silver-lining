import tkMessageBox
import Tkinter as root

class Main_Window(object):
    window = None
    def __init__(self, id, title,width,height):
        self.window = root.Tk()
        self.window.title(title)
        
        # get screen width and height
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (width/2)    
        y = (hs/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))
            
    def show(self):
        self.window.mainloop()
        return

    def add_widget(self,widget):
        widget_type = type(widget)
        if(widget_type == "Button" or isinstance(widget,Button) ):
            frame = self.placing(widget)
            widget.instance = root.Button(frame, text=widget.title, command=widget.callbackMethod)
            widget.instance.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "TextBox" or isinstance(widget,TextBox) ):
            frame = self.placing(widget)
            widget.instance = root.Text(frame)
            widget.instance.pack(fill=root.BOTH, expand=1)
            widget.instance.insert(root.INSERT,widget.text)

        elif(widget_type == "CheckBox" or isinstance(widget,CheckBox) ):
            frame = self.placing(widget)
            var = widget.value 
            widget.value = root.IntVar()
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.instance = root.Checkbutton(frame, text=widget.title, variable=widget.value)
            widget.instance.grid(sticky=root.W)
	
	elif(widget_type == "LabelText" or isinstance(widget,LabelText) ):
            frame = self.placing(widget)
            widget.instance = root.Label(frame, text=widget.text)
            widget.instance.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "RadioButtons" or isinstance(widget,RadioButtons) ):
            frame = self.placing_radio(widget.width,widget.height,widget.positions_X[0],widget.positions_Y[0])
            widget.instance = []
            radio_var = widget.value
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_instance = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_instance.pack(fill=root.BOTH, expand=1)
            widget.instance.append(radio_instance)
            for i in range(1,len(widget.labels)):
                frame = self.placing_radio(widget.width,widget.height,widget.positions_X[i],widget.positions_Y[i])
                radio_instance = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)
                radio_instance.pack(fill=root.BOTH, expand=1)
                widget.instance.append(radio_instance)

	elif(widget_type == "TextField" or isinstance(widget,TextField)):
            frame = self.placing(widget)
            widget.instance = root.Entry(frame)
            widget.instance.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "TextFieldPass" or isinstance(widget,TextFieldPass) ):
	    frame = self.placing(widget)
	    widget.instance = root.Entry(frame, show="*")
	    widget.instance.pack(fill=root.BOTH, expand=1)

	elif(isinstance(widget,ValueList) ):
            array = ['']
            array[0] = widget.value
            array = array + widget.choices
            widget.list_var = root.StringVar()
            
            widget.list_var.set(array[0])

            frame = self.placing(widget)
            widget.instance = apply(root.OptionMenu, (frame, widget.list_var) + tuple(array))
            widget.instance.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "Slider" or isinstance(widget,Slider) ):
	    frame = self.placing(widget)
	    widget.instance = root.Scale(frame, from_=widget.start, to=widget.end , orient=root.HORIZONTAL)
	    widget.instance.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "SpinBox" or isinstance(widget,SpinBox) ):
	    frame = self.placing(widget)
	    widget.instance = root.Spinbox(frame, from_=widget.start, to=widget.end ,increment=0.1 )
	    widget.instance.pack(fill=root.BOTH, expand=1)

    def placing(self,widget):
        frame = root.Frame(self.window, width=widget.width,height=widget.height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=widget.position_X,y=widget.position_Y)
        return frame

    def placing_radio(self,W,H,X,Y):
        frame = root.Frame(self.window, width=W,height=H)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        return frame

class SpinBox(object):
    instance = None
    callback = None
    Type = None
    def __init__(self,start,end,X,Y,width,height):
        self.type = "SpinBox"
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
	    return self.instance.get()
        
class Button(object):
    instance = None
    callbackMethod = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def on_click(self,event):
        if(self.instance == None):
            self.callbackMethod = event
        else:
            self.instance.callback(event)
        return True

class TextFieldPass(object):
    instance = None
    callback = None
    Type= "TextFieldPass"
    def __init__(self,title,X,Y,width,height):
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    def getText(self):
        if(self.instance == None):
	    return ''
	else:	
	    return self.instance.get()
    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.delete(root.END)
            self.instance.insert(root.INSERT,text)
        return True
 
       

class TextBox(object):
    instance = None
    callback = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "TextArea"
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.delete(1.0, root.END)
            self.instance.insert(root.INSERT,text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.get(1.0, root.END)

    def appendText(self,text):
        if(self.instance == None):
            self.text = self.text + text
            print self.text
        else:
            self.instance.insert(root.INSERT, text)
        return True              

    def clear(self):
        self.instance.delete(1.0, root.END)
        return True

class ValueList(object):
    instance = None
    Type = None
    list_var = 0
    def __init__(self,choices,X,Y,width,height,value=""):
        self.Type = "ValueList"
        self.choices = choices
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.value = value

    def getValue(self):
            if(self.instance == None):
                return self.title
            else:
                return self.list_var.get()



class TextField(object):
    instance = None
    callbackMethod = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "TextField"
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.delete(root.END)
            self.instance.insert(root.INSERT,text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.get()
    def clear(self):
        self.instance.delete(1.0, root.END)
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
            if(value):
                self.instance.select()
            else:
                self.instance.deselect()
    def select_value(self):
	if self.value==True:
		self.instance.select()
    def get_state(self):
        if(self.instance == None):
            return self.value
        else:
            if(self.value.get() == 1):
                return True
            else:
                return False

class LabelText(object):
    instance = None
    Type = None
    label_var = 0
    def __init__(self,text,X,Y,width,height):
        self.Type = "LabelText"
        label_var = text
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.label_var.set(text)
        return True

    def clear(self):
        self.instance.Clear()
        return True

class Slider(object):
    instance = None
    callback = None
    Type = "Slider"
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
	    return self.instance.get()

 

class RadioButtons(object):
    instance = None
    selected_index = None
    value = 0
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
            if(self.value.get()==i):
                return self.labels[i]
        return None

def Submit():
    newps1 = NewPstb.getText();
    newps2 = ReNewPstb.getText();
    if(IsValidPswd(newps1,newps2)):
        print (" TextFieldPass Successfully Changed ! ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
    else:
        print (" Retry by Entering new TextFieldPass!  ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
 


def IsValidPswd(newps1, newps2):
    if newps1 != newps2:
       print(" TextFieldPass Error !  TextFieldPasss donot match! ")
       return False
    
    if(len(newps1)<=6):               # Check the length of the TextFieldPass
       print(" TextFieldPass Error ! TextFieldPass Length should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):             #checks if TextFieldPass conatins only alpha or numeric fiels
        
        if(str(newps1).isalpha()):          # invalidates if  TextFieldPass contains only alphabets not a combination.
            print(" TextFieldPass Error ! TextFieldPass cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(newps1).isdigit()):	    #Invalidates if TextFieldPass contains only digits not a combination.
            print(" TextFieldPass Error ! TextFieldPass cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            #print ("TextFieldPass Successfully Changed. !");
            return True
    else:                                            # Invalidates if TextFieldPass have non-alphanumeric characters.
       print (" TextFieldPass Error ! TextFieldPass should contain only alphabets and digits.");
       return False

      
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

