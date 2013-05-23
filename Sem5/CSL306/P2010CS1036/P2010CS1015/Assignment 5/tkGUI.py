import tkMessageBox
import Tkinter as root
storePass = "oldpassword"
secure = True

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
	
	elif(isinstance(widget,LabelText) ):
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

	elif(isinstance(widget,TextField)):
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
        
''' WIDGETS: Button '''
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
 
       
''' WIDGETS: TextBox '''
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


''' WIDGETS: TextField '''
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

''' WIDGETS: Label '''

''' WIDGETS: CheckBox '''
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
''' WIDGETS: Label '''
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

 
''' WIDGETS: RadioButtons '''
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
       print(" TextFieldPass Error !  Passwords donot match! ")
       return False
    
    if(len(newps1)<=6):               # Check the length of the password
       print(" TextFieldPass Error ! TextFieldPass Length should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(newps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" TextFieldPass Error ! TextFieldPass cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(newps1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print(" TextFieldPass Error ! TextFieldPass cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            #print ("TextFieldPass Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print (" TextFieldPass Error ! TextFieldPass should contain only alphabets and digits.");
       return False

def ShowButtonClick(event=None):
    global storePass,secure
    if(secure == False):
        secure = True        
        storePass = oldpassText.getText()
    else:
        secure = False
    oldpassText.setText(rentSecure(storePass,secure))
    #oldpassText.setText(storePass)
    return True

def rentSecure(password,isSecure):
    if(isSecure):
        for i in range(len(password)):
           password = password.replace(password[i],"*")
   # print isSecure,password
    return password
      
if __name__ == '__main__':
	
	canvas = Main_Window(1, 'fltkGUI -v1.0 | Kamaldeep Singh' ,560,600)


	userLbl = LabelText("Username: ",20,40,120,30)
	usrtb = TextField("Username: ",150,40,300,25)
	canvas.add_widget(userLbl)
	canvas.add_widget(usrtb)


	OldPswdLbl = LabelText("Current TextFieldPass: ",20,100,120,30)
	OldPstb= TextField(rentSecure(storePass,secure),150,100,300,25)
	canvas.add_widget(OldPswdLbl)
	canvas.add_widget(OldPstb)



	NewPswdLbl = LabelText("New TextFieldPass: ",20,160,120,30)
	NewPstb= TextFieldPass("New TextFieldPass: ",150,160,300,25)
	canvas.add_widget(NewPswdLbl)
	canvas.add_widget(NewPstb)

	label = LabelText("Confirm TextFieldPass: ",20,220,120,30)
	ReNewPstb = TextFieldPass("Confirm TextFieldPass: ",150,220,300,25)
	canvas.add_widget(label)
	canvas.add_widget(ReNewPstb)




	btn= Button("Register",130,400,120,30)

    #Creating Buttons
	#submitBtn = Button("Submit",100,300,120,30)

    #Callback methods on buttons click
	btn.on_click(Submit)

    #Adding buttons to canvas
	canvas.add_widget(btn)

	canvas.show()


