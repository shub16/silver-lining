'''    The code is not completely object oriented right now, I have some other ideas in which I will divide each
       widget into a class, in this way things would make more sense.
       
       Currently there is only one class with many functions to create different widgets, but consistency and
       understandability is a bit complex
''' 

import gtk
import sys
class Canvas:
    def __init__(self, id, title,width,height):
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

    def add(self,widget):
        widget_type = type(widget)  
        print widget_type     
        if(widget_type==Button):
            widget.controller = gtk.Button(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextArea):
            widget.controller = gtk.TextView(widget.buffer)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
        elif(widget_type==TextLine):
	    widget.controller = gtk.Entry()
            widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()

        elif(widget_type==CheckBox):
            widget.controller = gtk.CheckButton(widget.title)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            widget.controller.set_active(widget.value)
	####
	elif(widget_type==Password):
	    widget.controller = gtk.Entry()
	    widget.controller.set_visibility(0)
            widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()

	elif(widget_type==Slider):
	    widget.controller = gtk.HScale()
	    widget.controller.set_range(widget.start, widget.end)
	    widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()
            
	
	elif(widget_type==SpinBox):
	    widget.controller = gtk.SpinButton()
	    widget.controller.set_range(widget.start,widget.end)
	    widget.controller.set_increments(1, 1)
	    widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()
            
	elif(widget_type==Label):
	    widget.controller = gtk.Label(widget.text)
	    widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()
	
	###
            
        elif(widget_type==RadioGroup):
            widget.controller = []
            radio_controller = gtk.RadioButton(None, widget.labels[0])
            radio_controller.set_size_request(widget.width,widget.height)
            self.fixed.put(radio_controller,widget.position_X[0], widget.position_Y[0])
            radio_controller.show()
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = gtk.RadioButton(widget.controller[0], widget.labels[num])
                radio_controller.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_controller,widget.position_X[num], widget.position_Y[num])
                radio_controller.show()
                widget.controller.append(radio_controller)
            
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].set_active(True)
            
        elif(widget_type==ValueList):
            widget.controller = gtk.OptionMenu()
            widget.controller.set_size_request(widget.width,widget.height)
            menu = gtk.Menu()
            for name in widget.choices:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
                print "gis"
            widget.controller.set_menu(menu)
            widget.controller.show()
            self.fixed.put(widget.controller,widget.position_X, widget.position_Y)
            

class Button(gtk.Button):
    controller = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def clickListener(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.connect("clicked", method)
        return True
    
class TextArea(gtk.TextView):
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

    def appendText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True
####

class Password(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):
	
        #self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def getText(self):
		
        if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get_text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.set_text(text)
	
        return True
    

class Slider(object):

    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):
	
        #self.text = text
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
	    return self.controller.get_value()
   
class SpinBox(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):
	
        #self.text = text
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
	    return self.controller.get_value()


class Label(object):

    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):
	

	self.text=text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height


class TextLine(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getText(self):

	if(self.controller == None):
            return ''
	else:
	    return self.controller.get_text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.set_text(text)
	
        return True
    	
    def clear(self):
	
        self.controller.set_text("")
	
        return True
	
    

####

class CheckBox(gtk.CheckButton):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    
    def setValue(self,value):   #True or False for checked
        if(value != True or value != False):
            return
        if(self.controller == None):
            self.value = value
        else:
            self.controller.set_active(value)

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.get_active()


class RadioGroup(gtk.RadioButton):
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

    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def getValue(self):
        for i in range(len(self.controller)):
            if(self.controller[num].get_active()):
                return self.labels[num]
        return "None"

    def setButtonTrue(self,pos):
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.set_active(True)

class ValueList(gtk.OptionMenu):
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
            temp.append(choices[num])
        self.choices = temp

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            IntValue = self.controller.get_history()
            if(IntValue < 0):
                return None
            return self.choices[IntValue] 
            
            


class API:
    '''
    Initialize the object using following parameters
    API ( title ="" , height=500, width=500)
    
    
    '''
    def __init__(self,title="", height=500, width=500):
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        self.window.show()
       
    def createLabel(self,name="Label"):
        label = gtk.Label(name)
        label.show()
        return label
    
    def createButton(self, name="Button"):
        button = gtk.Button(name)

        button.show()
        return button
    
    def createCheckButton(self, name="CheckButton"):
        checkButton = gtk.CheckButton(name)
        checkButton.show()
        return checkButton
    
    def createRadioButton(self, nameList, widget , func = None):
        ''' 
        Create RadioButton will take as argument a list containing names
        of the radioButton and a widget to which these radio buttons should 
        be attached
        
        createRadioButton( ListOfNames, WidgetToAddButtonsTo, FunctionToCallWhenToggled = None)
        '''
        count = 0
        for a in nameList:
            if(count == 0):
                radioButton = gtk.RadioButton(None, a)
            else:
                radioButton = gtk.RadioButton(radioButton, a)
            widget.add(radioButton)
            radioButton.show()
            count = count + 1
            
    def createBox(self, Vertical = True):
        '''
        When Vertical is set to true, this function will return Vertical Box
        in which widgets are added vertically.
        When set to False, Horizontal Box will be return in which widgets are
        added Horizontally
        '''
        if(Vertical):
            box = gtk.VBox(False,2)
        else:
            box = gtk.HBox(False,2)
        box.show()
        return box
    
    def createTextBox(self, CharLimit = 0):
        textBox = gtk.Entry(CharLimit)
        textBox.show()
        return textBox
        
    def createDropDownList(self, ListNames):
        opt = gtk.OptionMenu()
        menu = gtk.Menu()
        
        for name in ListNames:
            item = gtk.MenuItem(name)
            item.show()
            menu.append(item)
        opt.set_menu(menu)
        opt.show()
        return opt




                         
class assign5:
    def check(self,submitButton,textBox1,textBox2,textBox3,textBox4):   
                entry_text1 = textBox3.get_text()
		entry_text2 = textBox4.get_text()
		entry_text3 = textBox1.get_text()
		entry_text4 = textBox2.get_text()
		san = API("ALERT",100,400)                                 
		Hbox6 = san.createBox(False)
		Hbox7 = san.createBox(False)                                                                     
                Vbox = san.createBox(True)
                if len(entry_text3)==0 :
                      label9 = san.createLabel("The Username must be specified !!!")                                                
		      Hbox6.pack_start(label9)
		if len(entry_text4)==0 :
                      label10 = san.createLabel("We need old password to change your password !!!")                                                
		      Hbox6.pack_start(label10)      
                
		if len(entry_text1)<=6:
		      label6 = san.createLabel("The Password must be atleast 7 characters !!!")                                                
		      Hbox6.pack_start(label6)
		else:
		        
		      if entry_text1 != entry_text2:
		        label6 = san.createLabel("The Passwords does'nt match !!!")                                                
		        Hbox6.pack_start(label6)
		        
		      else:
		        #for i in entry_text1[]
		                
		                
		                for num in range(len(entry_text1)):
		                       if entry_text1[num]=='`' or entry_text1[num]=='~' or entry_text1[num]=='!' or entry_text1[num]=='@' or entry_text1[num]=='#' or entry_text1[num]=='$' or entry_text1[num]=='%' or entry_text1[num]=='^' or entry_text1[num]=='&' or entry_text1[num]=='*' or entry_text1[num]=='(' or entry_text1[num]==')' or entry_text1[num]=='-' or entry_text1[num]=='_' or entry_text1[num]=='=' or entry_text1[num]=='+' or entry_text1[num]=='|' or entry_text1[num]==' ' or entry_text1[num]==',' or entry_text1[num]=='<' or entry_text1[num]=='.' or entry_text1[num]=='>' or entry_text1[num]=='/' or entry_text1[num]=='?' :
		                             
		                             
		                             label7 = san.createLabel("Password should contain only alphabets and digits !!!")                                                
		                             Hbox6.pack_start(label7)   
		                             break
		                             
		                       else:
		                             label8 = san.createLabel("The Passwords match and are strong !!!")                                                
		                             Hbox6.pack_start(label8)        
		                 
		      		
		      
                Vbox.pack_start(Hbox6)
                quitButton = san.createButton("CLOSE ALERT")
                quitButton.connect("clicked", gtk.main_quit)
                Hbox7.pack_start(quitButton)
                Vbox.pack_start(Hbox7)
                san.window.add(Vbox)                       
    def __init__(self):
        san = API("SampleProgram",200,300)                                
        Hbox1 = san.createBox(False) 
        Hbox2 = san.createBox(False)                                                                                                           
        Hbox3 = san.createBox(False)
        Hbox4 = san.createBox(False)
        Hbox5 = san.createBox(False)                                                                     
        Vbox = san.createBox(True)                                                
                                                                                     
        label1 = san.createLabel("USERNAME")                                                
        textBox1 = san.createTextBox(20)
        
        Hbox1.pack_start(label1)  
        Hbox1.pack_start(textBox1)
        Vbox.pack_start(Hbox1)
        
        label2 = san.createLabel("OLD PASSWORD")                                                
        textBox2 = san.createTextBox(20)
        textBox2.set_visibility(False)
        Hbox2.pack_start(label2)  
        Hbox2.pack_start(textBox2)
        Vbox.pack_start(Hbox2)        
        
        label3 = san.createLabel("NEW PASSWORD")                                                
        textBox3 = san.createTextBox(20)
        textBox3.set_visibility(False)
        Hbox3.pack_start(label3)  
        Hbox3.pack_start(textBox3)
        Vbox.pack_start(Hbox3)
        
        label4 = san.createLabel("NEW PASSWORD")                                                
        textBox4 = san.createTextBox(20)
        #pas=Password(130,280,150,30)
        #textBox4 = pas.getText()
        #san.add(pas)
        #Hbox4.pack_start(pas)
        textBox4.set_visibility(False)
        Hbox4.pack_start(label4)  
        Hbox4.pack_start(textBox4)
        Vbox.pack_start(Hbox4)


        submitButton = san.createButton("Submit")
        submitButton.connect("clicked", self.check,textBox1,textBox2,textBox3,textBox4)
        Hbox5.pack_start(submitButton)
        Vbox.pack_start(Hbox5)




                
        san.window.add(Vbox)        
        #san.window.add(Hbox)
        gtk.main()        
                
                
if __name__ == "__main__":
	
	assign5() 

       
    


