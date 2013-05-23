import tkMessageBox
import sys
import Tkinter as root


class Dashboard(root.Tk):
    def __init__(self,title,length,breadth):
        self.window = root.Tk()
        self.window.title(title)
        
        # get screen width and height
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (length/2)    
        y = (hs/2) - (breadth/2)
        self.window.geometry('%dx%d+%d+%d' % (length, breadth, x, y))
        
        # To show the main window with checkbox , buttons etc.
    def Display(self, choice = True):
        self.window.mainloop()
        return

#Adding Button , checkbox , textarea , radiobutton as a widget which depends on passing argument
    def Add(self,widget):
        name = widget.name
        if(name == "button"):
            fram = self.fram(widget)  #Setting the widget into a fram
            widget.controller = root.Button(fram, text=widget.title, command=widget.call)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(name == "textarea"):
            fram = self.fram(widget)  #Setting the widget into a fram
            widget.controller = root.Text(fram)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(name == "checkbox"):
            fram = self.fram(widget)  # Setting the widget into a fram
            var = widget.value         # Widget.value contain whether the widget need to be marked
            widget.value = root.IntVar()
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.controller = root.Checkbutton(fram, text=widget.title, variable=widget.value, onvalue=1, offvalue=0)  # Creating the widget checkbutton
            widget.controller.grid(sticky=root.W)
            
        elif(name == "radiobox"):
            fram = self.fram1(widget.width,widget.height,widget.positions_X[0],widget.positions_Y[0])
            widget.controller = [] #creating the list for widgets
            radio_var = widget.value # Widget.value contain whether the widget need to be marked
            widget.value = root.IntVar()
            radio_controller = root.Radiobutton(fram, text=widget.labels[0], variable=widget.value, value=0)
            radio_controller.pack(fill=root.BOTH, expand=1)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)): #for each radiobutton , creating radiobutton acc, to pos.
                fram = self.fram1(widget.width,widget.height,widget.positions_X[i],widget.positions_Y[i])
                radio_controller = root.Radiobutton(fram, text=widget.labels[i], variable=widget.value,value=i)
                radio_controller.pack(fill=root.BOTH, expand=1) #packing the radiobuttons
                widget.controller.append(radio_controller)
	elif(name=="textbox"):
	    fram = self.fram(widget)
	    widget.controller = root.Entry(fram)
	    widget.controller.pack()
	elif(name=="Password"):
	    fram = self.fram(widget)
	    widget.controller = root.Entry(fram,show="*")
	    widget.controller.pack()
	elif(name=="ValueList"):
            array = ['']
            array[0] = widget.value
            array = array + widget.choices
            widget.list_var = root.StringVar()
            
            widget.list_var.set(array[0])

            fram = self.fram(widget)
            widget.controller = apply(root.OptionMenu, (fram, widget.list_var) + tuple(array))
            widget.controller.pack(fill=root.BOTH, expand=1)
	elif(name=="spin"):
	    fram = self.fram(widget)
	    widget.controller=root.Spinbox(fram,from_=widget.min,to=widget.max)
	    widget.controller.pack()


	elif(name == "LabelText"):
	   
            temp = widget.label_var
            widget.label_var = root.StringVar()
            widget.label_var.set(temp)
            fram = self.fram(widget)
            widget.controller = root.Label(fram, textvariable=widget.label_var)
            widget.controller.pack(fill=root.BOTH, expand=1)

    def fram(self,widget): # Creating fram for widgets , thus setting width and height of widget
	fram = root.Frame(self.window, width=widget.width,height=widget.height)
        fram.pack_propagate(0) # don't shrink
        fram.pack()
        fram.place(x=widget.position_X,y=widget.position_Y) #positoin of widget within fram
        return fram

    def fram1(self,W,H,X,Y):   #Creating fram for radiobuttons
        fram = root.Frame(self.window, width=W,height=H)
        fram.pack_propagate(0) # don't shrink
        fram.pack()
        fram.place(x=X,y=Y)
        return fram

# FOR Button Widget ........................

class Create_button:
    controller = None
    call = None
    Type = None
    def __init__(self,posX,posY,title="MyButton",length=100,breadth=30): #constructor setting pos_x,pos_y, width and height 
        self.name = "button"
        self.title = title
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Click_listener(self,method): #method for handling click Events
        if(self.controller == None):
            self.call = method
        else:
            self.controller.callback(method)
        return True
        
# FOR TextArea Widget ........................

class Text_area:
    controller = None
    def __init__(self,posX,posY,length=300,breadth=200,text=""): #constructor setting pos_x,pos_y , width and height
        self.name = "textarea"
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_text(self,text): #Setting text for textarea
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def Get_text(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def Append_text(self,text):
	print "narender"	
        if(self.controller == None):
	    self.text = self.text + text
        else:
            self.controller.insert(root.INSERT, text)
        return True                    

    def Clear_area(self):
        self.controller.delete(1.0, root.END)
        return True
#For TextBox Widget .........................

class Text_field:
    def __init__(self,posX,posY,text="",length=250,breadth=25):
	self.name="textbox"
	self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_text(self,text): #Setting text for textarea
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def Get_text(self):          #Returning text which textarea is holding
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get()

    def Clear_field(self):
        self.controller.delete(0,root.END)
        return True	

#######################################################################

class Password_field:
    def __init__(self,posX,posY,text="",length=250,breadth=25):
	self.name="Password"
	self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_text(self,text): #Setting text for textarea
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def Get_text(self):          #Returning text which textarea is holding
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get()

    def Clear_field(self):
        self.controller.delete(0,root.END)
        return True	

#######################################################################

class Static_text:
    controller = None
    label_var = ""
    def __init__(self,posX,posY,length=150,breadth=30,text=""):
        
	self.label_var=text
        self.name= "LabelText"
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_value(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.label_var.set(text)
        return True


########################################################################



# FOR CheckBox Widget ........................

class Check_box:
    controller = None
    value = True

    def __init__(self,posX,posY,title,length,breadth): #constructor setting pos_x,pos_y , width and height
        self.name = "checkbox"
        self.title=title
        self.position_X = posX
        self.position_Y = posY
	self.width = length
        self.height = breadth
       
    def Set_checked(self,value=True): #setting marked or unmarked for checkbox
        if(self.controller == None):
            self.value = value
        else:
	    if(value):
                self.controller.select()
            else:
                self.controller.deselect()

    def Is_checked(self): #Returning the value of checkbox(is it marked or unmarked)
        if(self.controller == None):
            return self.value
        else:
            if(self.value.get() == 1):  
                return True
            else:
                return False
		

 
# FOR RadioButton Widget ........................
 
class Radio_button:
    controller = None
    selected_index = None
    Type = None
    value = 0
   
    def __init__(self,label1,posX,posY):#Returning the value of checkbox(is it marked or unmarked)
	self.positions_X = [] #creating empty list for positions for  radiobuttons 
    	self.positions_Y = []
	self.labels = []
        self.name = "radiobox"
	self.width=100
	self.height=50
	self.Add_radio_button(label1,posX,posY)       
                                                            
    def Add_radio_button(self,label,posX,posY):  #Adding the label and position for a particular radiobutton
        self.labels.append(label)
        self.positions_X.append(posX) #Appending the position in the position LIST
        self.positions_Y.append(posY)
        return True

    def Get_selected(self):  #Returning the value for radiobutton(marked or unmarked)
        for i in range(len(self.controller)):
            if(self.value.get()==i):
                return self.labels[i]
        return None


    #def setButtonTrue(self,index): #Setting the value for radiobutton(marked or unmarked)
     #   if(self.controller == None):
      #      self.value=index
       # else:
        #    button_controller = self.controller[index]
         #   button_controller.select()
##############################################################################

class Drop_list:
    controller = None
    Type = None
    list_var = 0
    name=None
    def __init__(self,posX,posY,name1,values,length=100,breadth=27):
        self.name = "ValueList"
        self.choices = values
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth
        self.value = name1

    def Get_value(self):
            if(self.controller == None):
                return self.title
            else:
                return self.list_var.get()


#Spin Here and There

class Spin_list:
    def __init__(self,posX,posY,length=100,breadth=25,minimum=0,maximum=100):
	self.name="spin"
	self.position_X = posX
        self.position_Y = posY
	self.width=length
	self.height=breadth
	self.min = minimum
        self.max = maximum

    def Get_value(self):	
	return 6


#########################################################################
#Here Comes Main Part , DEMO Part........................................

def Check(self):					#Checks if the password is set satisfactorily
    password1 = NewPassEntry.Get_text();
    password2 = ReNewPassEntry.Get_text();
    if(Is_valid_pass(password1,password2)):		#calls Is_valid_pass
        print ("Password Successfully Changed ! ");
        OldPassEntry.Clear_field();
        NewPassEntry.Clear_field();
        ReNewPassEntry.Clear_field();
    else:
        print ("Retry by Entering new Password!  ");
        OldPassEntry.Clear_field();
        NewPassEntry.Clear_field();
        ReNewPassEntry.Clear_field();
 

def Is_valid_pass(pass1, pass2):		#Checks if the passwords satisfy all the criteria
    if pass1 != pass2:
       print("Error in Password! --> Passwords do not match! ")
       return False
    
    if(len(pass1)<=6):               # Check the length of the password
       print("Error in Password! --> Password Length should be more than 6. ")
       return False    
    
    if(str(pass1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(pass1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print("Error in Password!--> Password cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(pass1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print("Error in Password!--> Password cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            print ("Password Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print ("Error in Password!--> Password should contain only alphabets and digits.");
       return False


#----------------Unit Test Window------------------------------------------------------------------
#------------------Creates a Login Window-------------------------------------------------------
OuterPanel = Dashboard("Unit Test",400, 300)
NameLabel = Static_text( 15, 30, 80, 30,  "Name :")
OuterPanel.Add(NameLabel)
OldPassLabel = Static_text( 10, 75,140, 30, "Old Password :",)
OuterPanel.Add(OldPassLabel)
NewPassLabel = Static_text( 4, 120,160, 30, "New Password :",)
OuterPanel.Add(NewPassLabel)
ReTypeLabel = Static_text( 14, 170, 160, 30, "Re-Type Password :")
OuterPanel.Add(ReTypeLabel)
NameEntry = Text_field(180, 30, "", 150, 30)
OuterPanel.Add(NameEntry)
OldPassEntry = Password_field(180, 75, "", 150, 30)
OuterPanel.Add(OldPassEntry)
NewPassEntry = Password_field(180, 120, "", 150, 30)
OuterPanel.Add(NewPassEntry)
ReNewPassEntry = Password_field(180, 170, "", 150, 30)
OuterPanel.Add(ReNewPassEntry)
SubmitButton = Create_button(150, 230, "Log In", 100, 35)
SubmitButton.Click_listener(Check)
OuterPanel.Add(SubmitButton)
 
if __name__ == '__main__':
    OuterPanel.Display()
