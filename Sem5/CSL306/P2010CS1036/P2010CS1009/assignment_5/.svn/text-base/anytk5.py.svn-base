import tkMessageBox	  #importin library to use Message Box in Tkinter
import Tkinter as root	 
 

now_position=[10,10]  #initialising the variable "now_position"

#Function to evaluate positions of widgets intially
def default_position(x,y):  	  
        now_position[0]=now_position[0]+x
        now_position[1]=now_position[1]+y
        return now_position
        

class frame(object):
    window = None    
    id =--1
    title = "frame"
    size  =  (600 , 750)
    
    def __init__(self , id=-1, title ="frame" , width =  750 ,height = 500):
        self.window = root.Tk()
        self.window.title(title)
        
        # get screen width ( size[0])and height ( size[1])
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        
        # calculate position x, y
        x = (ws/2) - (width/2)    
        y = (hs/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
#shows the main window with all the added widgets        
    def show(self):
        self.window.mainloop()
        return

#fuction for adding widgets like Button , checkbox , textarea , radiobuttons,  which depends on passing argument
    def append(self,widget):
        widget_type = widget.Type
        if(widget_type == "button" or isinstance(widget,button) ):
            frame = self.abs_frame(widget)	#Setting the widget into a frame
            widget.controller = root.Button(frame, text=widget.label, command=widget.callbackMethod)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "text_area" or isinstance(widget,text_area) ):
            frame = self.abs_frame(widget)	#Setting the widget into a frame
            widget.controller = root.Text(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT,widget.text)

        elif(widget_type == "static_text"  or isinstance(widget,static_text) ):
            temp = widget.label
            widget.label = root.StringVar()
            widget.label.set(temp)
            frame = self.abs_frame(widget)	#Setting the widget into a frame
            widget.controller = root.Label(frame, textvariable=widget.label)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "check_box" or isinstance(widget,check_box) ):
            frame = self.abs_frame(widget)	#Setting the widget into a frame
            var = widget.value   # Widget.value contain whether the widget need to be marked or not
            widget.value = root.IntVar()
          
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.controller = root.Checkbutton(frame, text=widget.title, variable=widget.value, onvalue=1, offvalue=0)     
            widget.controller.grid(sticky=root.W)
            
            if(widget.value):
                widget.controller.select()
            else:
                widget.controller.deselect()

        elif(widget_type == "radio_buttons" or isinstance(widget,radio_buttons) ):
            frame = self.abs_frame1(widget.size[0],widget.size[1],widget.positions_X[0],widget.positions_Y[0])	#Setting the widget into a frame
            widget.controller = []
            radio_var = widget.value 		# Widget.value contain whether the widget need to be marked
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_controller = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_controller.pack(fill=root.BOTH, expand=1)
            widget.controller.append(radio_controller)
           
            for i in range(1,len(widget.labels)):
                frame = self.abs_frame1(widget.size[0],widget.size[1],widget.positions_X[i],widget.positions_Y[i])
                radio_controller = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)
                radio_controller.pack(fill=root.BOTH, expand=1)
                widget.controller.append(radio_controller)

        elif(widget_type=="combo_box" or isinstance(widget,combo_box) ):
            array = ['']
            array[0] = widget.default
            array = array + widget.labels
            widget.list_var = root.StringVar()            
            widget.list_var.set(array[0])
            frame = self.abs_frame(widget)
            widget.controller = apply(root.OptionMenu, (frame, widget.list_var) + tuple(array))
            widget.controller.pack(fill=root.BOTH, expand=1)
            
	elif(widget_type=="textbox" or isinstance(widget, text_field)):
	    frame = self.abs_frame(widget)
	    widget.controller = root.Entry(frame)
	    widget.controller.pack()
	    
	elif(widget_type=="textbox2" or isinstance(widget, text_field2)):
	    frame = self.abs_frame(widget)
	    widget.controller = root.Entry(frame , show = "*")
	    widget.controller.pack()	    

	elif(widget_type=="spin" or isinstance (widget , Spin)):
	    frame = self.abs_frame(widget)
	    widget.controller=root.Spinbox(frame,from_=widget.min,to=widget.max)
	    widget.controller.pack()	    
	
    def abs_frame(self,widget):   # Creating frame for widgets , thus setting width and height of widget
        frame = root.Frame(self.window, width=widget.size[0],height=widget.size[1])
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=widget.pos[0],y=widget.pos[1])  #positoin of widget within frame
        return frame

    def abs_frame1(self,W,H,X,Y):   #Creating Frame for radiobuttons
        frame = root.Frame(self.window, width=W,height=H)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        return frame

#**********<<<SpinBox Widget>>>**********
class Spin:
    pos = (180, 200)
    size = (40  ,50)
    def __init__(self,posX,posY,From,To,length=80,breadth=50):
	self.Type="spin"
	self.position_X = posX
	self.position_Y = posY
	self.width=length
	self.height=breadth
	self.min = From
	self.max = To  

#**********<<<Button Widget>>>**********
class button(object):
    controller = None
    callbackMethod = None
    id = -1
    p =  default_position(200 , 130)
    pos =  (p[0] , p[1])
    size = (100 , 35)
    label = "button"
    
    Type = None
    def __init__(self):
        self.Type = "button"


    def onclick(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.callback(method)
        return True
        

#**********<<<TextArea Widget>>>**********'''
class text_area(object):
    controller = None
    callback = None
    Type = None
    
    parent=None
    id= -1  
    p=(300 , 10)
    pos=(p[0],p[1])
    text = ""
    size = (100 , 100)
    
    
    def __init__(self):
        self.Type = "text_area"
        self.text = self.text

    def set_text(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def get_text(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def append_text(self,text):
        if(self.controller == None):
            self.text = self.text + text
            print self.text
        else:
            self.controller.insert(root.INSERT, text)
        return True              

    def clear(self):
        self.controller.delete(1.0, root.END)
        return True

#**********<<<TextField Widget>>>**********
class text_field:
    pos  =(230, 200)
    size = (100 , 100)
    def __init__(self):
	self.Type="textbox"

    def set_text(self, text1):
    	self.widget.set(text1)
    	return
    	
    def get_text(self):
    	self.string =  self.controller.get()
    	return self.string
    

    def Clear_field(self):
        self.controller.delete(0,root.END)
        return True	
       
class text_field2:
    pos  =(230, 200)
    size = (100 , 100)
    def __init__(self):
	self.Type="textbox2"

    def set_text(self, text1):
    	self.widget.set(text1)
    	return
    	
    def get_text(self):
    	self.string =  self.controller.get()
    	return self.string
    

    def Clear_field(self):
        self.controller.delete(0,root.END)
        return True	        


#**********<<<Label>>>**********
class static_text(object):
    controller = None
    Type = None
    label = 0   
   
    parent=None
    id= -1  
    pos = (200 , 100)
    size  =  (150  , 50)
    label =  "default"
 
    def __init__(self):
        self.Type = "static_text"
	  

    def set_text(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.label.set(text)
        return True

    def clear(self):
        self.controller.Clear()
        return True


#**********<<<CheckBox Widget>>>**********
class check_box(object):
    controller = None
    value = False
    Type = None
    parent = None
    label =  "check box"
    p = default_position(150 ,  150)
    pos =  (p[0] , p[1])
    size = (150 , 20)
    
    def __init__(self):
        self.Type = "check_box"
        self.title = self.label
        self.position_X = self.p[0]
        self.position_Y = self.p[1]
        self.width = self.size[0]
        self.height = self.size[1]

    def setValue(self,value):    #setting the value of checkbox(is it marked or unmarked)
        if(self.controller == None):
            self.value = value
        else:
            if(value):
                self.controller.select()
            else:
                self.controller.deselect()

    def get_value(self):    #Returning the value of checkbox(is it marked or unmarked)
        if(self.controller == None):
            return self.value
        else:
            if(self.value.get() == 1):
                return True
            else:
                return False

 
#**********<<<Widget For Randobuttons>>>**********
class radio_buttons(object):
    controller = None
    selected_index = None
    Type = None
    value = 0
    size = (100, 20)
    
    def __init__(self):
        self.Type = "radio_buttons"
        self.labels = []
        self.positions_X = []   #creating empty list for positions for  radiobuttons 
        self.positions_Y = []
  
    def add_rb(self,label,X,Y):   #Adding the label and position for a particular radiobutton
        self.labels.append(label)
        self.positions_X.append(X)  #Appending the position in the position LIST
        self.positions_Y.append(Y)
        return True

    def get_value(self):      #Returning the value for radiobutton(marked or unmarked)
        for i in range(len(self.controller)):
            if(self.value.get()==i):
                return self.labels[i]
        return None

    def set_true(self,index):    #Setting the value for radiobutton(marked or unmarked)
        if(self.controller == None):
            self.value=index
        else:
            button_controller = self.controller[index]
            button_controller.select()

#**********<<<ComboBox Widget>>>**********
class combo_box(object):
    controller = None
    Type = None
    list_var = 0
    
    
    
    labels =  []
    pos = (10 , 20)
    size = (150  , 30)
    default  =  "<default>"
    Type = "combo_box"
    def __init__(self):
      	i=1

    def get_value(self):
            if(self.controller == None):
                return self.title
            else:
                return self.list_var.get()


   


