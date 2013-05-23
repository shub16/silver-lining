import tkMessageBox
import Tkinter as root


        
#button field defined here
class Button(object):
    handle = None
    callbackMethod = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "Button"
        self.title = title
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height
        
    def clickListener(self,method):
        if(self.handle == None):
            self.callbackMethod = method
        else:
            self.handle.callback(method)
        return True   

#text field defined here
class TextView(object):
    handle = None
    callback = None
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "TextView"
        self.text = title
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.handle == None):
            self.text = text
        else:
            self.handle.delete(1.0, root.END)
            self.handle.insert(root.INSERT,text)
        return True
    
    def getText(self):
        if(self.handle == None):
            return self.text
        else:
            return self.handle.get(1.0, root.END)
    def clear(self):
        self.handle.delete(1.0, root.END)
        return True

 
#radio buttons defined here
class Radio(object):
    handle = None
    selected_index = None
    Type = None
    value = 0
    def __init__(self,width,height):
        self.Type = "Radio"
        self.labels = []
        self.cords_x = []
        self.cords_y = []
        self.width = width
        self.height = height
#another name change here
    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.cords_x.append(X)
        self.cords_y.append(Y)
        return True

    def setButtonTrue(self,index):
        if(self.handle == None):
            self.value=index
        else:
            button_handle = self.handle[index]
            button_handle.select()


#list box defined here
class DropDownList(object):
    handle = None
    Type = None
    list_var = 0
    def __init__(self,choices,X,Y,width,height,value=""):
        self.Type = "DropDownList"
        self.choices = choices
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height
        self.value = value
 
#check boxes defined here
class CheckBox(object):
    handle = None
    value = False
    Type = None
    def __init__(self,title,X,Y,width,height):
        self.Type = "CheckBox"
        self.title = title
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def setValue(self,value):
        if(self.handle == None):
            self.value = value
        else:
            if(value):
                self.handle.select()
            else:
                self.handle.deselect()


#################################################################

class Xwindow(object):
    window = None
    def __init__(self, id, title,width,height):
        self.window = root.Tk()
        self.window.title(title)
        
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()

        x = (ws/2) - (width/2)    
        y = (hs/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    def show(self):
        self.window.mainloop()
        return

    def add(self,widget):
        widget_type = widget.Type
        if(widget_type == "Button" ):
            frame = self.abs_frame(widget)
            widget.handle = root.Button(frame, text=widget.title, command=widget.callbackMethod)
            widget.handle.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "TextView"  ):
            frame = self.abs_frame(widget)
            widget.handle = root.Text(frame)
            widget.handle.pack(fill=root.BOTH, expand=1)
            widget.handle.insert(root.INSERT,widget.text)

        elif(widget_type == "CheckBox"  ):
            frame = self.abs_frame(widget)
            var = widget.value 
            widget.value = root.IntVar()
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.handle = root.Checkbutton(frame, text=widget.title, variable=widget.value, onvalue=1, offvalue=0)
            #widget.handle.pack(fill=root.BOTH, expand=1)
            widget.handle.grid(sticky=root.W)
            if(widget.value):
                widget.handle.select()
            else:
                widget.handle.deselect()

        elif(widget_type == "Radio"):
            frame = self.abs_frame1(widget.width,widget.height,widget.cords_x[0],widget.cords_y[0])
            widget.handle = []
            radio_var = widget.value
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_handle = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_handle.pack(fill=root.BOTH, expand=1)
            widget.handle.append(radio_handle)
            for i in range(1,len(widget.labels)):
                frame = self.abs_frame1(widget.width,widget.height,widget.cords_x[i],widget.cords_y[i])
                radio_handle = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)
                radio_handle.pack(fill=root.BOTH, expand=1)
                widget.handle.append(radio_handle)

        elif(widget_type=="DropDownList" ):
            array = ['']
            array[0] = widget.value
            array = array + widget.choices
            widget.list_var = root.StringVar()
            
            widget.list_var.set(array[0])

            frame = self.abs_frame(widget)
            widget.handle = apply(root.OptionMenu, (frame, widget.list_var) + tuple(array))
            widget.handle.pack(fill=root.BOTH, expand=1)
            

    def abs_frame(self,widget):
        frame = root.Frame(self.window, width=widget.width,height=widget.height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=widget.cord_x,y=widget.cord_y)
        return frame

    def abs_frame1(self,W,H,X,Y):
        frame = root.Frame(self.window, width=W,height=H)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        return frame




