import gtk											# importing the module gtk
now_position=[10,10]										# defining a global variable now_position 
def default_position(x,y):									# writing a method to assign default positions to widgets
        now_position[0]=now_position[0]+x
        now_position[1]=now_position[1]+y
        return now_position

class frame(object):										# creating  frame class to create a frame in which widgets will be embeded
    parent = None 
    id=-1
    title="default title"							
    size=(600,750)
   	
    
    def __init__(self, id, title="frame",width=750, height=500):				# creating a constructor. The frame object will take 4 inoput values: id, title, width, height
        
        

        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)						# creating a frame/window
        self.window.connect("destroy", gtk.main_quit)						# connecting the destroy signal to quit method
        self.window.set_title(title)			
        											# setting frame title
        self.window.set_size_request(width,height)						# setting the size of the frame
       
        self.fixed = gtk.Fixed()								# creating a container to embed the widgets 
        self.window.add(self.fixed)
        self.fixed.show()


    def show(self):										# defining the show method which displays the window
        self.window.show()
        gtk.main()										# initialising the gtk event handling loop by calling gtk.main()
        return

    def append(self,widget):									# creating a method to append widgets to an instance of the frame. The append method takes widget as input and
        widget_type = type(widget)  								# executes the code corresponding to that widget in the following if conditions
          	
        if(isinstance(widget,button)):								# if widget type is button this if condition creates a button 
            widget.ctr = gtk.Button(widget.label)
            widget.ctr.set_size_request(widget.size[0],widget.size[1])
            self.fixed.put(widget.ctr, widget.pos[0], widget.pos[1])            
            widget.ctr.show()
            if(widget.callbackMethod != None ):
                widget.ctr.connect('clicked',widget.callbackMethod)
                
        elif(isinstance(widget,text_area) ):							# if widget type is text_area this if condition creates a text_area 
            widget.ctr = gtk.TextView(widget.buffer)	
            widget.ctr.set_size_request(widget.size[0],widget.size[1])
            self.fixed.put(widget.ctr, widget.pos[0], widget.pos[1])            
            widget.ctr.show()
            if(widget.callbackMethod != None ):
                widget.ctr.connect('clicked',widget.callbackMethod)
                
        elif(isinstance(widget,text_field)):							# if widget type is text_field this elseif condition creates a text_field 
            widget.ctr = gtk.Entry()
            widget.ctr.set_size_request(widget.size[0],widget.size[1])
            widget.ctr.set_visibility(widget.visibility)
            self.fixed.put(widget.ctr, widget.pos[0], widget.pos[1])
            widget.ctr.set_text(widget.label)            
            widget.ctr.show()

        elif(isinstance(widget,check_box)):							# if widget type is check_box this elseif condition creates a check_box
            widget.ctr = gtk.CheckButton(widget.label)
            widget.ctr.set_size_request(widget.size[0],widget.size[1])
            self.fixed.put(widget.ctr, widget.pos[0], widget.pos[1])            
            widget.ctr.show()
            widget.ctr.set_active(widget.value)
            
        elif(isinstance(widget,radio_buttons)):							# if widget type is radio_buttons this elseif condition creates a radiobuttons
            widget.ctr = []
            radio_ctr = gtk.RadioButton(None, widget.labels[0])
            radio_ctr.set_size_request(widget.size[0],widget.size[1])
            self.fixed.put(radio_ctr,widget.position_X[0], widget.position_Y[0])
            radio_ctr.show()
           
            widget.ctr.append(radio_ctr)
            for i in range(1,len(widget.labels)):
                radio_ctr = gtk.RadioButton(widget.ctr[0], widget.labels[i])
                radio_ctr.set_size_request(widget.size[0],widget.size[1])
                self.fixed.put(radio_ctr,widget.position_X[i], widget.position_Y[i])
                radio_ctr.show()
                widget.ctr.append(radio_ctr)
            
            if(widget.selected_pos != None):
                widget.ctr[widget.selected_pos].set_active(True)
            
        elif(isinstance(widget,combo_box)):							# if widget type is combo_box this elseif condition creates a combo_box
            widget.ctr = gtk.OptionMenu()
            widget.ctr.set_size_request(widget.size[0],widget.size[1])
            menu = gtk.Menu()
           
            
            widget.labels.insert(0,widget.default)
            											
            for name in widget.labels:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
               
            widget.ctr.set_menu(menu)
            widget.ctr.show()
            self.fixed.put(widget.ctr,widget.pos[0], widget.pos[1])
        
        elif(isinstance(widget,static_text)):							# if widget type is static_text this elseif condition creates a static_text
            widget.ctr = gtk.Label(widget.label)
            widget.ctr.set_size_request(widget.size[0],widget.size[1])
            self.fixed.put(widget.ctr, widget.pos[0], widget.pos[1])            
            widget.ctr.show()
            
class static_text(object):									# creating a class for static_field widget
    ctr = None
    id=-1
    pos=(200,100)
    size=(150,50)
    label="default"
    def __init__(self):
        temp=1
class button(object):										# creating a class for a button
    ctr = None
    callbackMethod = None
    id=-1
    p=default_position(100,150)
    pos=(p[0],p[1])
    size=(185,35)
    label="button"
    
    def __init__(self):
        temp=1

    def onclick(self,method):									
        if(self.ctr == None):
            self.callbackMethod = method
        else:
            self.ctr.connect("clicked", method)
        return True
    
class text_area(object):									# creating a class for text_area
    ctr = None
    callbackMethod = None
    text="this is the text area"
    p=(100,20)
    pos=(p[0],p[1])
    size=(100,100)
    buffer = gtk.TextBuffer()
    def __init__(self):
        i=1

    def set_text(self,text):
        self.buffer.set_text(text1)
        return True

    def append_text(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True


class text_field(object):
												# creating a class for text_field
    ctr = None
    label="default title"
    pos=(230,200)
    size=(100,100)
    visibility= True
    
    
    def __init__(self):
        i=1
       

    def set_text(self,text1):
	self.ctr.set_text(text1)
	return
    def get_text(self):
	self.string=self.ctr.get_text()
	return self.string
	
class text_field2(object):
												# creating a class for text_field
    ctr = None
    label="default title"
    pos=(230,200)
    size=(100,100)
    visibility= False
    
    
    def __init__(self):
        i=1
       

    def set_text(self,text1):
	self.ctr.set_text(text1)
	return
    def get_text(self):
	self.string=self.ctr.get_text()
	return self.string

class check_box(object):									# creating a class for check_box 
    ctr = None
    value = False
    parent=None
    label="checkbox"
    p=default_position(150,150)
    pos=(p[0],p[1])
    size=(150,20)
    
    def __init__(self):
    	varr=1    
    
    def set_value(self,value):   								# method to set the value in the text field
        if(value != True or value != False):
            return
        if(self.ctr == None):
            self.value = value
        else:
            self.ctr.set_active(value)

    def get_value(self):									# method to get value from the text fiels
        if(self.ctr == None):
            return self.value
        else:
            return self.ctr.get_active()


class radio_buttons(object):									# creating a class for radio_buttons
    GroupController = None
    ctr = None
    selected_pos = None
    total=1
    name=[]               
    label=[]
    parent=None
    pos=[]    
    size=(100,20)   
    def __init__(self):
        self.labels = []
        self.position_X = []
        self.position_Y = []
        
        self.GroupController = None

    def add_rb(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def get_value(self):
        for i in range(len(self.ctr)):
            if(self.ctr[i].get_active()):
                return self.labels[i]
        return "None"

    def set_true(self,pos):
        if(self.ctr == None):
            self.selected_pos = pos
        else:
            button_ctr = self.ctr[pos]
            button_ctr.set_active(True)
            
            


class combo_box(object):									# creating a class for combo_box
    ctr = None
    default="default"
    labels=[]
    pos=(100,200)
    size=(100,20)
    
    
    def __init__(self):
        i=0
        

    def get_value(self):
        if(self.ctr == None):
            return self.value
        else:
            IntValue = self.ctr.get_history()
            if(IntValue < 0):
                return None
            return self.labels[IntValue]


    
