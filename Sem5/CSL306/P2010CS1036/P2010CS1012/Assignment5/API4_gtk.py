import gtk

class WindowFrame:
    def __init__(self, id, title,width,height): # Constructor for WindowFrame class
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL) #assigning a window to WindowFrame
        self.window.connect("destroy", gtk.main_quit) #adding a destroy event to close button
        self.window.set_title(title) #setting title 
        self.window.set_size_request(width,height) #setting size for window
        # Create a Fixed Container
        self.fixed = gtk.Fixed() #making a fixed container
        self.window.add(self.fixed) #adding container to class
        self.fixed.show() 


    def show(self):
        self.window.show() 
        gtk.main()
        return

    def add(self,widget):
        WidgetName = type(widget)  #finding type of widget being added
        #print WidgetName     
        if(WidgetName==Button): #if added widget is button
            widget.controller = gtk.Button(widget.text) #setting name for button
            widget.controller.set_size_request(widget.width,widget.height) #setting the size of button
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)   #setting location for button         
            widget.controller.show() #showing the button
            if(widget.callbackMethod != None ): #setting callback method for button
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(WidgetName==TextArea):#if added widget is TextArea
            widget.controller = gtk.TextView(widget.buffer) #setting buffer for the TextArea
            widget.controller.set_size_request(widget.width,widget.height) #setting the size of TextArea
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)   #  setting location for TextArea       
            widget.controller.show() #showing the TextArea
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod) #adding callback method to Textarea
        elif(WidgetName==TextLine): #if widget added is TextLine
	    widget.controller = gtk.Entry() #setting a widget for TextLine
            widget.controller.set_size_request(widget.width,widget.height)#setting the size of TextLine
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y) #  setting location for TextLine
	    widget.controller.show()#showing the TextLine

        elif(WidgetName==CheckBox): #if widget added is CheckBox
            widget.controller = gtk.CheckButton(widget.title)#setting name for CheckBox
            widget.controller.set_size_request(widget.width,widget.height) #setting the size of CheckBox
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y) #setting location for CheckBox             
            widget.controller.show() #showing the CheckBox
            widget.controller.set_active(widget.value)#activating the CheckBox
	####
	elif(WidgetName==Password):#if widget added is Password
	    widget.controller = gtk.Entry() #adding a TextLine for Password
	    widget.controller.set_visibility(0)#making the characters invisible
            widget.controller.set_size_request(widget.width,widget.height)#setting the size of PassWord
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)#setting the position of PassWord
	    widget.controller.show()

            
	elif(WidgetName==Label):#if widget added is Label
	    widget.controller = gtk.Label(widget.text)#getting a Label with widget.text
	    widget.controller.set_size_request(widget.width,widget.height)#setting the size of Label
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)#setting the position of Label
	    widget.controller.show()
	
	###
            
        elif(WidgetName==RadioGroup):#if widget added is RadioGroup
            widget.controller = []#
            radio_controller = gtk.RadioButton(None, widget.labels[0])#getting RadioButtons for the group
            radio_controller.set_size_request(widget.width,widget.height)#setting the size of RadioGroup
            self.fixed.put(radio_controller,widget.position_X[0], widget.position_Y[0])#setting the position of RadioGroup
            radio_controller.show()#showing the RadioButton
            widget.controller.append(radio_controller)#appending RadioButton to RadioController
            for i in range(1,len(widget.labels)):#for adding the remaining RadioButtons we have used the same procedure
                radio_controller = gtk.RadioButton(widget.controller[0], widget.labels[i])
                radio_controller.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_controller,widget.position_X[i], widget.position_Y[i])
                radio_controller.show()
                widget.controller.append(radio_controller)
            
            if(widget.selected_pos != None):#setting the position of the selected RadioButton if it is not NULL
                widget.controller[widget.selected_pos].set_active(True)
            
        elif(WidgetName==DropDownList):#if widget added is DropDownList
            widget.controller = gtk.OptionMenu()#gettin an Option Menu for DropDownList
            widget.controller.set_size_request(widget.width,widget.height)#setting the size of DropDownList
            menu = gtk.Menu()
            for name in widget.choices:#adding  menus in the menubar
                item = gtk.MenuItem(name)#
                item.show()#showing the items added
                menu.append(item)#appending item to the menu
            widget.controller.set_menu(menu)
            widget.controller.show()#showing the OptionMenu
            self.fixed.put(widget.controller,widget.position_X, widget.position_Y)#setting the position of DropDownList


###   These are the abstract classes made to store the values of Xposition ,Yposition ,width,height and other relevant attributes of the widgets which will be used while adding the widgets to the WindowFrame

### These widgets have many functions associated to each of them like constructors, setting text ,getting a value
        

# Button class has a button with style attributes and a fnction clickListener which has a functio is triggered on click
class Button(gtk.Button):
    controller = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):#storing the style attributes
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def clickListener(self,method):
        if(self.controller == None):
            self.callbackMethod = method #storing the callbackmethod to be triggered on click
        else:
            self.controller.connect("clicked", method)
        return True
# Text Area has style attributes and the fnctions for clearing, getting text, appendding text , placing text before a particular string
    
class TextArea(gtk.TextView):
    controller = None
    callbackMethod = None
    buffer = gtk.TextBuffer()
    def __init__(self,title,X,Y,width,height):#storing the style attributes
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
	self.buffer.set_text(title)

    def setText(self,text): #function for setting the text of TextArea
        self.buffer.set_text(text)
        return True
    def getText(self):#fnction to get all the Text of TextArea
	print "hello"
	start=self.buffer.get_start_iter() #getting the pointer to start of buffer of Text Area
	end=self.buffer.get_end_iter()#getting the pointer to end of buffer of Text Area
	text=self.buffer.get_text(start,end,True)#getting the text between the two pointers above calculated
	return text#return the text to callee

    def appendText(self,text):#function for appending text at the end
        self.buffer.insert(self.buffer.get_end_iter(),text)#appending the text to end by getting a pointer to end of buffer
        return True              

    def clear(self):#function for clearing the buffer
        self.buffer.set_text("")#setting the test to empty
        return True
    def AppendBefore(self,text1,text2):# function to append string text2 before text1
	start=self.buffer.get_start_iter()# a pointer to start of buffer
	tuple1=start.forward_search(text1,  gtk.TEXT_SEARCH_VISIBLE_ONLY, limit=None)# searching for a particular text1 and returns pointer to start and end of text word
	#print type(tuple1)
	self.buffer.insert(tuple1[0],text2)# inserting text 2 before the start of text1
####
# Password class is same as TextLine except that Text is not visible here

class Password(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):#storing the style attributes of Password Class
	
        #self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def getText(self):#returns the password entered 
		
        if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get_text()

    def setText(self,text):#function to set the password 
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.set_text(text)
	
        return True
    

#Label is class for a Label which shows on Window
class Label(object):

    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):#storing the style attributes
	

	self.text=text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

# One line Textbox for fields like username etc.
class TextLine(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):#storing the style attributes
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getText(self):#returns the text in TextLine

	if(self.controller == None):
            return ''
	else:
	    return self.controller.get_text()

    def setText(self,text):#sets the text to a default value
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.set_text(text)
	
        return True
    	
    def clear(self):#clears the text in TextLine
	
        self.controller.set_text("")
	
        return True
	
    

####
# Checkbox class has function to setvalue of checkbox and get the value of checkbox
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

    def getValue(self): #returns whether chcked or unchecked
        if(self.controller == None):
            return self.value
        else:
            return self.controller.get_active()

# radiogroup class has radiobuttons one of them will be turned on
class RadioGroup(gtk.RadioButton):
    GroupController = None
    controller = None
    selected_pos = None
    def __init__(self,width,height): #storing the style attributes of radiogroup
        self.labels = []
        self.position_X = []
        self.position_Y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def addRadioButton(self,label,X,Y): #adds a radiobutton to the RadioGroup
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def getValue(self): #returns which radiobutton is checked 
        for i in range(len(self.controller)):
            if(self.controller[i].get_active()):
                return self.labels[i]
        return "None"

    def setButtonTrue(self,pos):#selects a radiobutton
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.set_active(True)
# DropDownList is a dropdown list which displays the options on clicking 
#has options to get the value of currently selected option

class DropDownList(gtk.OptionMenu):
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


