import gtk

class Vista(object):
    parent = None
    def __init__(self, id, title,width,height):
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()
	#def end(self):
		#gtk.main_quit()
    def show(self):
        self.window.show()
        gtk.main()
        return

    def addWidget(self,widget):
        widget_type = type(widget)  
        if(widget_type==Button or isinstance(widget,Button)):
            widget.controller = gtk.Button(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextBuffer or isinstance(widget,TextBuffer) ):
            widget.controller = gtk.TextView(widget.buffer)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)

        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = gtk.CheckButton(widget.title)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            widget.controller.set_active(widget.value)
            
        elif(widget_type==RadioButton or isinstance(widget,RadioButton)):
            widget.controller = []
            radio_controller = gtk.RadioButton(None, widget.labels[0])
            radio_controller.set_size_request(widget.width,widget.height)
            self.fixed.put(radio_controller,widget.position_X[0], widget.position_Y[0])
            radio_controller.show()
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = gtk.RadioButton(widget.controller[0], widget.labels[i])
                radio_controller.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_controller,widget.position_X[i], widget.position_Y[i])
                radio_controller.show()
                widget.controller.append(radio_controller)
            
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].set_active(True)
            
        elif(widget_type==List or isinstance(widget,List)):
            widget.controller = gtk.OptionMenu()
            widget.controller.set_size_request(widget.width,widget.height)
            menu = gtk.Menu()
            for name in widget.choices:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
            widget.controller.set_menu(menu)
            widget.controller.show()
            self.fixed.put(widget.controller,widget.position_X, widget.position_Y)
                
        elif(widget_type==TextArea or isinstance(widget,TextArea)):
            widget.controller = gtk.Entry()
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
            widget.controller.set_text(widget.title)            
            widget.controller.show()
                
        elif(widget_type==PasswordField or isinstance(widget,PasswordField)):
            widget.controller = gtk.Entry()
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
            widget.controller.set_text(widget.title)
            widget.controller.set_visibility(gtk.FALSE)            
            widget.controller.show()
                
        elif(widget_type==ShowText or isinstance(widget,ShowText)):
            widget.controller = gtk.Label(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()

        elif(widget_type == "Slider" or isinstance(widget,Slider) ):
			adj1 = gtk.Adjustment(0.0, widget.start, widget.end, 0.1, 1.0, 1.0)
			widget.instance = gtk.HScale(adj1)
			widget.instance.set_size_request(widget.width,widget.height)
			self.fixed.put(widget.instance, widget.position_X, widget.position_Y)
			widget.instance.show()
            	
	elif(widget_type == "SpinBox" or isinstance(widget,SpinBox) ):
			adj = gtk.Adjustment(0.0, widget.start, widget.end, 0.1,0.1, 0.0)
			widget.instance = gtk.SpinButton(adj , 0.1 , 1)
			widget.instance.set_size_request(widget.width,widget.height)
			self.fixed.put(widget.instance, widget.position_X, widget.position_Y)
			widget.instance.show()    
                        	
class Button(object):
    controller = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def clickTrigger(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.connect("clicked", method)
        return True 


class TextBuffer(object):
    controller = None
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

    def concatText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clearBuffer(self):
        self.buffer.set_text("")
        return True


class CheckBox(object):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    
    def setBox(self,value):   #True or False for checked
        if(value != True or value != False):
            return
        if(self.controller == None):
            self.value = value
        else:
            self.controller.set_active(value)

    def getBox(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.get_active()


class RadioButton(object):
    GroupController = None
    controller = None
    selected_pos = None
    def __init__(self,width,height):
        self.labels = []
        self.position_X = []
        self.position_Y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def addButton(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def getButton(self):
        for i in range(len(self.controller)):
            if(self.controller[i].get_active()):
                return self.labels[i]
        return "None"

    def setButton(self,pos):
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.set_active(True)


class List(object):
    controller = None
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
        if(self.controller == None):
            return self.value
        else:
            IntValue = self.controller.get_history()
            if(IntValue < 0):
                return None
            return self.choices[IntValue]


class TextArea(object):
    controller = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.set_text(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get_text()

class PasswordField(object):
    controller = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.set_text(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get_text()

class ShowText(object):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

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
    	    return self.instance.get()
    	    
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

