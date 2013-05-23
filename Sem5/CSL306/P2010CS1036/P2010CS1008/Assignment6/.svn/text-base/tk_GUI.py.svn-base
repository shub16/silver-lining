import tkMessageBox
import Tkinter as root
storePass = "oldpassword"
secure = True

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
        widget_type = type(widget)
        if(widget_type == "Button" or isinstance(widget,Button) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Button(frame, text=widget.title, command=widget.callbackMethod)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "TextArea" or isinstance(widget,TextArea) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Text(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT,widget.text)

	elif(widget_type == "ShowText"or isinstance(widget,ShowText) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Label(frame, text=widget.text)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "TextBuffer" or isinstance(widget,TextBuffer) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Text(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT,widget.text)


        elif(widget_type == "CheckBox" or isinstance(widget,CheckBox) ):
            frame = self.abs_frame(widget)
            var = widget.value 
            widget.value = root.IntVar()
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.controller = root.Checkbutton(frame, text=widget.title, variable=widget.value)
            widget.controller.grid(sticky=root.W)
	
	elif(isinstance(widget,ShowText) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Label(frame, text=widget.text)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "RadioButton" or isinstance(widget,RadioButton) ):
            frame = self.abs_frame_radio(widget.width,widget.height,widget.positions_X[0],widget.positions_Y[0])
            widget.controller = []
            radio_var = widget.value
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_controller = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_controller.pack(fill=root.BOTH, expand=1)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                frame = self.abs_frame_radio(widget.width,widget.height,widget.positions_X[i],widget.positions_Y[i])
                radio_controller = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)
                radio_controller.pack(fill=root.BOTH, expand=1)
                widget.controller.append(radio_controller)

	elif(isinstance(widget,TextArea)):
            frame = self.abs_frame(widget)
            widget.controller = root.Entry(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "PasswordField" or isinstance(widget,PasswordField) ):
	    frame = self.abs_frame(widget)
	    widget.controller = root.Entry(frame, show="*")
	    widget.controller.pack(fill=root.BOTH, expand=1)

	elif(isinstance(widget,List) ):
            array = ['']
            array[0] = widget.value
            array = array + widget.choices
            widget.list_var = root.StringVar()
            
            widget.list_var.set(array[0])

            frame = self.abs_frame(widget)
            widget.controller = apply(root.OptionMenu, (frame, widget.list_var) + tuple(array))
            widget.controller.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "Slider" or isinstance(widget,Slider) ):
	    frame = self.abs_frame(widget)
	    widget.controller = root.Scale(frame, from_=widget.start, to=widget.end , orient=root.HORIZONTAL)
	    widget.controller.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "SpinBox" or isinstance(widget,SpinBox) ):
	    frame = self.abs_frame(widget)
	    widget.controller = root.Spinbox(frame, from_=widget.start, to=widget.end ,increment=0.1 )
	    widget.controller.pack(fill=root.BOTH, expand=1)

	elif(widget_type == "TextBox" or isinstance(widget,TextBox) ):
            frame = self.abs_frame(widget)
            widget.controller = root.Text(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT,widget.text)

    def abs_frame(self,widget):
        frame = root.Frame(self.window, width=widget.width,height=widget.height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=widget.position_X,y=widget.position_Y)
        return frame

    def abs_frame_radio(self,W,H,X,Y):
        frame = root.Frame(self.window, width=W,height=H)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        return frame

class SpinBox(object):
    controller = None
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
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get()
        
''' WIDGETS: Button '''
class Button(object):
    controller = None
    callbackMethod = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def clickTrigger(self,event):
        if(self.controller == None):
            self.callbackMethod = event
        else:
            self.controller.callback(event)
        return True

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
''' WIDGETS: TextBox '''
class TextBox(object):
    controller = None
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
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def appendText(self,text):
        if(self.controller == None):
            self.text = self.text + text
            print self.text
        else:
            self.controller.insert(root.INSERT, text)
        return True              

    def clear(self):
        self.controller.delete(1.0, root.END)
        return True

''' WIDGETS: TextBuffer '''
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

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

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


''' WIDGETS: TextArea '''
class TextArea(object):
    controller = None
    callbackMethod = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "TextArea"
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def clear(self):
        self.controller.delete(1.0, root.END)
        return True

class ShowText(object):
    controller = None
    Type = None
    label_var = 0
    def __init__(self,text,X,Y,width,height):
        self.Type = "ShowText"
        label_var = text
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.label_var.set(text)
        return True

    def clear(self):
        self.controller.Clear()
        return True


''' WIDGETS: CheckBox '''
class CheckBox(object):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
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
    def select_value(self):
	if self.value==True:
		self.controller.select()
    def getBox(self):
        if(self.controller == None):
            return self.value
        else:
            if(self.value.get() == 1):
                return True
            else:
                return False
''' WIDGETS: Label '''

class Slider(object):
    controller = None
    callback = None
    Type = "Slider"
    def __init__(self,start,end,X,Y,width,height):
	self.start=start
	self.end=end
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    def getbox(self):
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get()

 
''' WIDGETS: RadioButton '''
class RadioButton(object):
    controller=None
    controller = None
    selected_index = None
    value = 0
    def __init__(self,width,height):
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
