import tkMessageBox
from Tkinter import *
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
    def Display(self):
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

    def Get_text(self):          #Returning text which textarea is holding
        if(self.controller == None):
            return self.text
        

    def Append_text(self,text):
        if(self.controller == None):
            self.text = self.text + text
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


if __name__ == '__main__':

    def SubmitButtonClick(): #Joining the values from various selected widgets
	string = " Your Character is "+valuelist.Get_value()+"\n\n"
#Checking the marked checkbox and then updating the string to be displayed on clicking Button

        if(checkbox1.Is_checked()):
            string = string + " You selected Physics\n\n"
        else:
            string = string + " You dropped Physics\n\n"

        if(checkbox2.Is_checked()):
            string = string + " You selected Chemistry\n\n"
        else:
            string = string + " You dropped Chemistry\n\n"
	
	if(checkbox3.Is_checked()):
            string = string + " You selected Maths\n\n"
        else:
            string = string + " You dropped Maths\n\n"

#Getting the value from Radiogroup rb1 and rb2 and hence updatin the string
        string = string + " God is "+rb1.Get_selected()+"\n\n"
        string = string + " You Got "+rb2.Get_selected()+"\n\n"
        textarea.Set_text(string+"\n\n")
        t1.Clear_field()
	t2.Clear_field()
        return True

#Action on clicking the ME Button
    def AboutButtonClick():
        textarea.Set_text("Tkinter GUI\n\nAssignment 4 API\n\nWith : Narender Yadav\n       P2010CS1025")
        #print textarea.getText()
	return True

    #Tkinter Constructor with Title and dimension for screen
    Dashboard = Dashboard('Tkinter with Narender yadav' ,900,600)
    character = ['Batman', 'Superman', 'Spiderman', 'Hulk', 'Ironman']
   

    #Creatin the objects for checkboxes
    checkbox1 = Check_box(25,140,"Physics",215,15)
    checkbox2 = Check_box(25,165,"Chemistry",215,15)
    checkbox3 = Check_box(25,190,"Maths",215,15)
    checkbox1.Set_checked(True)
#Adding the CheckBox Objects
    Dashboard.Add(checkbox1)
    Dashboard.Add(checkbox2)
    Dashboard.Add(checkbox3)


#Adding Lable Text

    label = Static_text(20,40,70,30,"Username")
    Dashboard.Add(label)
    t1=Text_field(110,40,"",215,25)
    Dashboard.Add(t1)

    label = Static_text(20,80,70,30,"Password")
    Dashboard.Add(label)

    t2=Password_field(110,80,"",215,25)
    Dashboard.Add(t2)


###################################################################33

 #Creatin the objects for Text-Field
    
    t1=Text_field(110,40,"",215,25)
    Dashboard.Add(t1)


    #Creating the RadioGroup and thus Adding the radiobuttons and setting the second button true
  
    rb1 = Radio_button("Great",0,225)
    rb1.Add_radio_button("Powerful",80,225)
    rb1.Add_radio_button("Omnicent",170,225)
    rb1.Add_radio_button("Everywhere",270,225)
#Adding the RadioGroup rb1
    Dashboard.Add(rb1)


    #Creating the textarea
    textarea = Text_area(570,90,300,200,"\n Click submit button to see output here!!")
    Dashboard.Add(textarea)
###########################################################
 
#Creating The Buttons "See" and "ME"
    submitBtn = Create_button(450,370,"See",120,30)
    aboutBtn = Create_button(610,370,"ME",120,30)

#Calling Corresponding Methods on Clicking the Buttons "See" and "ME" 
    submitBtn.Click_listener(SubmitButtonClick)
    aboutBtn.Click_listener(AboutButtonClick)
    
    #Adding Buttons "See" and "ME"
    Dashboard.Add(aboutBtn)
    Dashboard.Add(submitBtn)
    
#Finally Showing the Main window with various widgets Added
    Dashboard.Display()

    
    
#Q. What basically self.controller==None means


