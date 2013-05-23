import tkMessageBox
import Tkinter as root

class PasswordField(object):
    controller = None
    callback = None
    Type= "PasswordField"
    def __init__(self,title,X,Y,width,height):
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    def getText(self):
        if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get()
    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(root.END)
            self.controller.insert(root.INSERT,text)
        return True
 

class Vista(object):                                             
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

    def addWidget(self,widget):                                                  
        widget_type = widget.Type
        if(widget_type == "Button" or isinstance(widget,Button) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Button(frame, text=widget.title, command=widget.callbackMethod)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "TextBuffer" or isinstance(widget,TextBuffer) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Text(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT,widget.text)

        elif(widget_type == "ShowText"  or isinstance(widget,ShowText) ):
            temp = widget.label_var
            widget.label_var = root.StringVar()
            widget.label_var.set(temp)
            frame = self.abs_frame(widget)
            widget.controller = root.Label(frame, textvariable=widget.label_var)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "CheckBox" or isinstance(widget,CheckBox) ):
            frame = self.abs_frame(widget)
            var = widget.value 
            widget.value = root.IntVar()
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.controller = root.Checkbutton(frame, text=widget.title, variable=widget.value, onvalue=1, offvalue=0)
            #widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.grid(sticky=root.W)
            if(widget.value):
                widget.controller.select()
            else:
                widget.controller.deselect()

        elif(widget_type == "RadioButton" or isinstance(widget,RadioButton) ):
            frame = self.abs_frame1(widget.width,widget.height,widget.positions_X[0],widget.positions_Y[0])
            widget.controller = []
            radio_var = widget.value
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_controller = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_controller.pack(fill=root.BOTH, expand=1)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                frame = self.abs_frame1(widget.width,widget.height,widget.positions_X[i],widget.positions_Y[i])
                radio_controller = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)
                radio_controller.pack(fill=root.BOTH, expand=1)
                widget.controller.append(radio_controller)

        elif(widget_type=="List" or isinstance(widget,List) ):
            array = ['']
            array[0] = widget.value
            array = array + widget.choices
            widget.list_var = root.StringVar()
            
            widget.list_var.set(array[0])

            frame = self.abs_frame(widget)
            widget.controller = apply(root.OptionMenu, (frame, widget.list_var) + tuple(array))
            widget.controller.pack(fill=root.BOTH, expand=1)
            

    def abs_frame(self,widget):
        frame = root.Frame(self.window, width=widget.width,height=widget.height)
        frame.pack_propagate(0) 
        frame.pack()
        frame.place(x=widget.position_X,y=widget.position_Y)
        return frame

    def abs_frame1(self,W,H,X,Y):
        frame = root.Frame(self.window, width=W,height=H)
        frame.pack_propagate(0) 
        frame.pack()
        frame.place(x=X,y=Y)
        return frame

class Button(object):
    controller = None
    callbackMethod = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "Button"
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def clickTrigger(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.callback(method)
        return True
        
        

class TextBuffer(object):                                             
    controller = None
    callback = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "TextBuffer"
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True


    def concatText(self,text):
        if(self.controller == None):
            self.text = self.text + text
            print self.text
        else:
            self.controller.insert(root.INSERT, text)
        return True              

    def clearBuffer(self):                                                   
        self.controller.delete(1.0, root.END)
        return True

class TextArea(object):
    controller = None
    Type = None
    label_var = 0
    def __init__(self,text,X,Y,width,height):
        self.Type = "ShowText"
        label_var = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.label_var.set(text)
        return True

class ShowText(object):
    controller = None
    Type = None
    label_var = 0
    def __init__(self,text,X,Y,width,height):
        self.Type = "ShowText"
        label_var = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    def clearBuffer(self):
        self.controller.clearBuffer()
        return True


class CheckBox(object):
    controller = None
    value = False
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "CheckBox"
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setBox(self,value):                  
        if(self.controller == None):
            self.value = value
        else:
            if(value):
                self.controller.select()
            else:
                self.controller.deselect()

    def getBox(self):                                   
        if(self.controller == None):
            return self.value
        else:
            if(self.value.get() == 1):
                return True
            else:
                return False
 
''' WIDGETS: RadioButton '''
class RadioButton(object):                    
    controller = None
    selected_index = None
    Type = None
    value = 0
    def __init__(self,width,height):
        self.Type = "RadioButton"
        self.labels = []
        self.positions_X = []
        self.positions_Y = []
        self.width = width
        self.height = height

    def addButton(self,label,X,Y):      
        self.labels.append(label)
        self.positions_X.append(X)
        self.positions_Y.append(Y)
        return True

    def getButton(self):                        
        for i in range(len(self.controller)):
            if(self.value.get()==i):
                return self.labels[i]
        return None

    def setButton(self,index):             
        if(self.controller == None):
            self.value=index
        else:
            button_controller = self.controller[index]
            button_controller.select()


class List(object):                   
    controller = None
    Type = None
    list_var = 0
    def __init__(self,choices,X,Y,width,height,value=""):
        self.Type = "List"
        self.choices = choices
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.value = value

    def getValue(self):                                                         
            if(self.controller == None):
                return self.title
            else:
                return self.list_var.get()

''' ----------------------------------------------------------------
        This is just demo! 
        IT IS NOT THE PART OF LIB '''
'''
if __name__ == '__main__':

    #Functions bind to button events
    def SubmitButtonClick():
        report = " Your city is "+List.getValue()+"\n"
        print checkbox1.getBox()
        if(checkbox1.getBox()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"

        if(checkbox2.getBox()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"

        report = report + " you are "+rb1.getButton()+"\n"
        report = report + " you need "+rb2.getButton()+"\n"

        TextBuffer.setText("_______________________\n"+report+"\n\n")
       # label.setText("Label Text changed!")
        return True

    def AboutButtonClick():
        TextBuffer.setText("Created in Tkinter GUI -v1.0\nAuthor : Pravesh Jain")
        print TextBuffer.getText()
        return True



    #Constructor Vista
    Vista = Vista(1, 'TkGUI -v1.0 | Pravesh Jain' ,510,300)

    #Dropdown List
    cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
    List = List(cities,10,10,200,20,"<Select your city>")
    Vista.addWidget(List)

    #checkboxs
    checkbox1 = CheckBox("I have read the code.",10,45,215,15)
    checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
    checkbox1.setBox(True)
    Vista.addWidget(checkbox1)
    Vista.addWidget(checkbox2)


    label = ShowText("This is demo Label Text!",10,95,215,30)
    Vista.addWidget(label)

    #RadioButton1
    rb1 = RadioButton(60,50)
    rb1.addButton("Nice",10,120)
    rb1.addButton("Good",70,120)
    rb1.addButton("Great",140,120)
    rb1.setButton(2)
    Vista.addWidget(rb1)

    #RadioButton2
    rb2 = RadioButton(100,50)
    rb2.addButton("Option #1",10,160)
    rb2.addButton("Option #2",110,160)
    rb2.setButton(0)
    Vista.addWidget(rb2)

    #TextBuffer
    TextBuffer = TextBuffer("\n Click submit button to see output here!!",250,10,250,200)
    Vista.addWidget(TextBuffer)

    #Creating Buttons
    submitBtn = Button("Submit",130,230,120,30)
    aboutBtn = Button("About",260,230,120,30)

    #Callback methods on buttons click
    submitBtn.clickTrigger(SubmitButtonClick)
    aboutBtn.clickTrigger(AboutButtonClick)

    #Adding buttons to Vista
    Vista.addWidget(aboutBtn)
    Vista.addWidget(submitBtn)
    Vista.show()
'''
