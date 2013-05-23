import gtk

class Main_Window(object):
    parent = None
    def __init__(self, id, title,width,height):
        #Initialize the Widget
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        # Create a Fixed Container
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()


    def show(self):
        self.window.show()
        gtk.main()
        return

    def add_widget(self,widget):
    
        widget_type = type(widget) 
         
       # print widget_type     
        if(widget_type == Button or isinstance(widget,Button)):
            widget.instance = gtk.Button(widget.text)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
            if(widget.callbackMethod != None ):
                widget.instance.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextBox or isinstance(widget,TextBox) ):
            widget.instance = gtk.TextView(widget.buffer)
          
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
        
     
        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.instance = gtk.CheckButton(widget.title)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
            widget.instance.set_active(widget.value)
            
        elif(widget_type==RadioButtons or isinstance(widget,RadioButtons)):
            widget.instance = []
            radio_instance = gtk.RadioButton(None, widget.labels[0])
            radio_instance.set_size_request(widget.width,widget.height)
            self.fixed.put(radio_instance,widget.position_X[0], widget.position_Y[0])
            radio_instance.show()
            widget.instance.append(radio_instance)
            for i in range(1,len(widget.labels)):
                radio_instance = gtk.RadioButton(widget.instance[0], widget.labels[i])
                radio_instance.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_instance,widget.position_X[i], widget.position_Y[i])
                radio_instance.show()
                widget.instance.append(radio_instance)
            
            if(widget.selected_pos != None):
                widget.instance[widget.selected_pos].set_active(True)
       
        
        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.instance = gtk.Label(widget.text)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
            
        elif(widget_type==TextField or isinstance(widget,TextField)):
            widget.instance = gtk.Entry()
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)
            widget.instance.set_text(widget.title)            
            widget.instance.show()
        elif(widget_type==TextFieldPass or isinstance(widget,TextField)):
            widget.instance = gtk.Entry()
            widget.instance.set_visibility(False)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)
            widget.instance.set_text(widget.title)            
            widget.instance.show()
            
        elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.instance = gtk.OptionMenu()
            widget.instance.set_size_request(widget.width,widget.height)
            menu = gtk.Menu()
            for name in widget.choices:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
                #print "gis"
            widget.instance.set_menu(menu)
            widget.instance.show()
            self.fixed.put(widget.instance,widget.position_X, widget.position_Y)
        elif(widget_type == "Slider" or isinstance(widget,Slider) ):
        	'''
            	frame = self.abs_frame(widget)
        	widget.instance = gtk.HScale(frame, from_=widget.start, to=widget.end , orient=root.HORIZONTAL)
       	 	widget.instance.pack(fill=root.BOTH, expand=1)
        	'''	
		adj1 = gtk.Adjustment(0.0, widget.start, widget.end, 0.1, 1.0, 1.0)
		widget.instance = gtk.HScale(adj1)
   	        widget.instance.set_size_request(widget.width,widget.height)
   	        self.fixed.put(widget.instance, widget.position_X, widget.position_Y)
            	widget.instance.show()
            	
	elif(widget_type == "SpinBox" or isinstance(widget,SpinBox) ):
		'''
       	 	frame = self.abs_frame(widget)
        	widget.instance = root.Spinbox(frame, from_=widget.start, to=widget.end )
        	widget.instance.pack(fill=root.BOTH, expand=1)
        	'''
        	
        	#adj = gtk.Adjustment(0, widget.start, widget.end, 1.0, 1.0, 0.0)
        	adj = gtk.Adjustment(0.0, widget.start, widget.end, 0.1,0.1, 0.0)
        	widget.instance = gtk.SpinButton(adj , 0.1 , 1)
        	widget.instance.set_size_request(widget.width,widget.height)
   	        self.fixed.put(widget.instance, widget.position_X, widget.position_Y)
            	widget.instance.show()    
            
''' LabelText '''
class LabelText(object):
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


        
        
''' ValueList '''
class ValueList(object):
    instance = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.title = ""
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.value = value
        temp = [value]
        for i in range(len(choices)):
            temp.append(choices[i])
        self.choices = temp

    def getValue(self):
        if(self.instance == None):
            return self.value
        else:
            IntValue = self.instance.get_history()
            if(IntValue < 0):
                return None
            return self.choices[IntValue]

''' TEXT FIELD '''
class TextField(object):
    instance = None
    text = ""
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.set_text(text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.get_text()

''' TextFieldPass '''
class TextFieldPass(object):
    instance = None
    text = ""
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.set_text(text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.get_text()




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
            self.instance.connect("clicked", event)
        return True
    
class TextBox(object):
    instance = None
    buffer = gtk.TextBuffer()
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        self.buffer.set_text(text)
        return True

    def appendText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True

''' WIDGETS: TextField '''


class CheckBox(object):
    instance = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    
    def set_state(self,value):   #True or False for checked
        if(value != True or value != False):
            return
        if(self.instance == None):
            self.value = value
        else:
            self.instance.set_active(value)

    def get_state(self):
        if(self.instance == None):
            return self.value
        else:
            return self.instance.get_active()


class RadioButtons(object):
    GroupController = None
    instance = None
    selected_pos = None
    def __init__(self,width,height):
        self.labels = []
        self.position_X = []
        self.position_Y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def add_radiobutton(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def get_state(self):
        for i in range(len(self.instance)):
            if(self.instance[i].get_active()):
                return self.labels[i]
        return "None"

class TextArea(object):
    instance = None
    callbackMethod = None
    buffer = gtk.TextBuffer()
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        self.buffer.set_text(text)
        return True

    def appendText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True

class Slider(object):
    instance = None
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
    	    return str(self.instance.get_value())
    	    
    	    
    	    
class SpinBox(object):
    instance = None
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
        	return str(self.instance.get_value())
            

#Functions bind to button events
def Submit(self):
    newps1 = NewPstb.getText();
    print "Hello",newps1
    newps2 = ReNewPstb.getText();
    if(IsValidPswd(newps1,newps2)):
        print (" Password Successfully Changed ! ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
    else:
        print (" Retry by Entering new Password!  ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
 


storePass = "oldpassword"
secure = True


def rentSecure(password,isSecure):
    if(isSecure):
        for i in range(len(password)):
           password = password.replace(password[i],"*")
   #  isSecure,password
    return password
    
def ShowButtonClick(event=None):
    global storePass,secure
    if(secure == False):
        secure = True        
        storePass = oldpassText.getText()
    else:
        secure = False
    oldpassText.setText(rentSecure(storePass,secure))
    return True

def IsValidPswd(newps1, newps2):
    if newps1 != newps2:
       print(" Password Error !  Passwords donot match! ")
       return False
    
    if(len(newps1)<=6):               # Check the length of the password
       print(" Password Error ! Password Length should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(newps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" Password Error ! Password cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(newps1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print(" Password Error ! Password cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            print ("Password Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print (" Password Error ! Password should contain only alphabets and digits.");
       return False





#Constructor canvas
'''
canvas = Main_Window(1, 'Change Password' ,560,600)
userLbl = LabelText("Username: ",20,40,120,30)
usrtb = TextField("",150,40,300,25)
canvas.add_widget(userLbl)
canvas.add_widget(usrtb)
OldPswdLbl = LabelText("Current Password: ",20,100,120,30)
OldPstb= TextFieldPass("",150,100,300,25)
canvas.add_widget(OldPswdLbl)
canvas.add_widget(OldPstb)
NewPswdLbl = LabelText("New Password: ",20,160,120,30)
NewPstb= TextFieldPass("",150,160,300,25)
canvas.add_widget(NewPswdLbl)
canvas.add_widget(NewPstb)
label = LabelText("Confirm Password: ",20,220,120,30)
ReNewPstb = TextFieldPass("",150,220,300,25)
canvas.add_widget(label)
canvas.add_widget(ReNewPstb)
btn= Button("Register",130,400,120,30)
btn.on_click(Submit)
canvas.add_widget(btn)
cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
canvas.add_widget(valuelist)
'''
      
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

	
