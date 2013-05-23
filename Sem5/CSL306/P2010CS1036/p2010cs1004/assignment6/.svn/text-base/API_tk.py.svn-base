import tkMessageBox
import Tkinter as root		# import python Tkinter Library

#Main GUI window class
class WindowFrame(object):
    window = None
    def __init__(self, id, title,width,height): 	# Constructor to create a main window with given sizes
        self.window = root.Tk()				# To create a Main Tkinter window
        self.window.title(title)			# Set Title
        ws = self.window.winfo_screenwidth()		
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (width/2)    			# X displacement
        y = (hs/2) - (height/2)				# Y displacement
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))	# Set Geometry of Main window
        
    def show(self):
        self.window.mainloop()				# Enter into event loop.It will show the main window.
        return

    def add(self,widget):				# Function to add Widgets to Main window
        WidgetName = widget.Type
        if(WidgetName == "Button" or isinstance(widget,Button) ):   # It will add a Button widget to main window
            frame = self.abs_frame(widget)
            widget.controller = root.Button(frame, text=widget.title, command=widget.callbackMethod)		# Create a Button widget
            widget.controller.pack(fill=root.BOTH, expand=1)
	
        elif(WidgetName == "TextArea" or isinstance(widget,TextArea) ):	# It will add a TextArea widget to main window
            frame = self.abs_frame(widget)					# Create a Frame,widget will be packed in this frame
            widget.controller = root.Text(frame,wrap=root.WORD)				# Create a Text widget
            scrollbar = root.Scrollbar(frame, orient=root.VERTICAL)
	    widget.controller.config(yscrollcommand=scrollbar.set)
	    scrollbar.config(command=widget.controller.yview)
	    scrollbar.pack(side = root.RIGHT, fill=root.Y)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT,widget.text)

        elif(WidgetName == "Label"  or isinstance(widget,Label) ):	# It will add a Label widget to main window
            temp = widget.label_var
            widget.label_var = root.StringVar()
            widget.label_var.set(temp)
            frame = self.abs_frame(widget)						# Create a Frame,widget will be packed in this frame
            widget.controller = root.Label(frame, textvariable=widget.label_var)	# Create a Label widget
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif(WidgetName == "CheckBox" or isinstance(widget,CheckBox) ):	# It will add a CheckBox widget to main window
            frame = self.abs_frame(widget)
            var = widget.value 
            widget.value = root.IntVar()	
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            widget.controller = root.Checkbutton(frame, text=widget.title, variable=widget.value, onvalue=1, offvalue=0)	# Create a CheckBox widget
            widget.controller.grid(sticky=root.W)
            if(widget.value):
                widget.controller.select()
            else:
                widget.controller.deselect()

        elif(WidgetName == "RadioGroup" or isinstance(widget,RadioGroup) ):	# It will add a RadioGroup widget to main window
            frame = self.abs_frame1(widget.width,widget.height,widget.positions_X[0],widget.positions_Y[0])	# Create a Frame,widget will be packed in this frame
            widget.controller = []
            radio_var = widget.value
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_controller = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)	# Create a RadioGroup widget
            radio_controller.pack(fill=root.BOTH, expand=1)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                frame = self.abs_frame1(widget.width,widget.height,widget.positions_X[i],widget.positions_Y[i])		
                radio_controller = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)	# Create individual Radio Buttons
                radio_controller.pack(fill=root.BOTH, expand=1)
                widget.controller.append(radio_controller)

        elif(WidgetName=="DropDownList" or isinstance(widget,DropDownList) ):	# It will add a DropDownList widget to main window
            array = ['']
            array[0] = widget.value
            array = array + widget.choices
            widget.list_var = root.StringVar()
            widget.list_var.set(array[0])
            frame = self.abs_frame(widget)								# Create a Frame,widget will be packed in this frame
            widget.controller = apply(root.OptionMenu, (frame, widget.list_var) + tuple(array))		# Create a DropDownList widget
            widget.controller.pack(fill=root.BOTH, expand=1)
            
	elif(WidgetName == "SpinBox" or isinstance(widget,SpinBox) ):		# It will add a SpinBox widget to main window
	    frame = self.abs_frame(widget)							# Create a Frame,widget will be packed in this frame
	    widget.controller = root.Spinbox(frame, from_=widget.start, to=widget.end )		# Create a SpinBox widget
	    widget.controller.pack(fill=root.BOTH, expand=1)

	elif(WidgetName == "Slider" or isinstance(widget,Slider) ):
	    frame = self.abs_frame(widget)					# Create a Frame,widget will be packed in this frame
	    widget.controller = root.Scale(frame, from_=widget.start, to=widget.end , orient=root.HORIZONTAL)
	    widget.controller.pack(fill=root.BOTH, expand=1)

	elif(WidgetName == "Password" or isinstance(widget,Password) ):	# It will add a Password widget to main window
	    frame = self.abs_frame(widget)					# Create a Frame,widget will be packed in this frame
	    widget.controller = root.Entry(frame,textvariable=widget.mytext, show="*")			# Create a Password widget
	    widget.controller.pack(fill=root.BOTH, expand=1)

	elif(WidgetName == "TextLine" or isinstance(widget,TextLine) ):	# It will add a TextLine widget to main window
	    frame = self.abs_frame(widget)					# Create a Frame,widget will be packed in this frame
	    widget.controller = root.Entry(frame)				# Create a TextLine widget
	    widget.controller.pack(fill=root.BOTH, expand=1)

		
        elif(WidgetName == "SelectList" or isinstance(widget,SelectList)):		 # It will add a SelectList widget to main window
	    frame = self.abs_frame(widget)						 # Create a Frame,widget will be packed in this frame
	    widget.controller = root.Listbox(frame)
	    scrollbar = root.Scrollbar(frame, orient=root.HORIZONTAL , width=10)
	    widget.controller.config(xscrollcommand=scrollbar.set)
	    scrollbar.config(command=widget.controller.xview)
	    widget.controller.bind('<<ListboxSelect>>', widget.forward_request )
	    widget.controller.insert(0,widget.choices[0])				
            for i in range(1,len(widget.choices)):
                widget.controller.insert(i,widget.choices[i])				# Add values to SelectList
	    scrollbar.pack(side = root.BOTTOM,fill=root.X)
	    widget.controller.pack(fill=root.BOTH, expand=1)
	    	    
	    
    def abs_frame(self,widget):			# To Set the dimensions of a frame, widgets will be placed inside these frames 
        frame = root.Frame(self.window, width=widget.width,height=widget.height)  # Set the height and width of frame 
        frame.pack_propagate(0) # don't shrink
        frame.pack()		# Place the frame in Maine Window
        frame.place(x=widget.position_X,y=widget.position_Y)			  # Set the X and Y positions of frame
        return frame

    def abs_frame1(self,W,H,X,Y):					# To Set the dimensions of a frame, widgets will be placed inside these frames
        frame = root.Frame(self.window, width=W,height=H)		# Place the frame in Maine Window
        frame.pack_propagate(0) # don't shrink
        frame.pack()							# Place the frame in Maine Window
        frame.place(x=X,y=Y)						# Set the X and Y positions of frame
        return frame

# Class to create a SelectList object and set its attributes.
# Later this will be used to create an actual widget using WindowFrame.add(widget).
class SelectList(object):	 
	controller = None
	Type = "SelectList"
	callbackmethod= None
        def __init__(self,choices,X,Y,width,height,value=""):		# Constructor to set attributes
            self.choices = choices
            self.position_X = X
            self.position_Y = Y
            self.width = width
            self.height = height
            self.value = value

	def clickListener(self,method):					# To associate a function to SelectList
	     if(self.controller == None):
	         self.callbackmethod = method				# Set the value of callbackmethod
	     else:
		 self.callbackmethod = method
	     return True
        
        def forward_request(self,evt):					# Function to bypass triggere action on SelectList
             w = evt.widget						
	     index = int(w.curselection()[0])
             value = w.get(index)
	     if self.callbackmethod != None:				
	     	self.callbackmethod(value)		      		# Call the respective function

''' WIDGETS: Button '''
# Class to create a Button object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class Button(object):
    controller = None
    callbackMethod = None					
    Type = None
    def __init__(self,title,X,Y,width,height):				# Constructor to set attributes
        self.Type = "Button"
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def clickListener(self,method):					# Set a function to happen when user clicked this button
        if(self.controller == None):
            self.callbackMethod = method				# Set the value of callbackmethod
        else:
            self.controller.config(command=method)			# Set the value of callbackmethod
        return True



''' WIDGETS: TextArea '''
# Class to create a TextArea object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class TextArea(object):
    controller = None
    callback = None
    Type = None
    def __init__(self,title,X,Y,width,height):				# Constructor to set attributes
        self.Type = "TextArea"
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):						# Function to set the text in the Textarea
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        return True

    def getText(self):							# Function to get the text inside Textarea
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def appendText(self,text):						# Append text to the end of Textarea
        if(self.controller == None):
            self.text = self.text + text
        else:
            self.controller.insert(root.INSERT, text)
        return True              

    def clear(self):							# Clear the existing text in the Textarea
        self.controller.delete(1.0, root.END)
        return True

    def AppendBefore(self,text1,text2):					# Append string text2 before text1
	x=self.controller.search(text1,1.0)	
	self.controller.insert(x, text2)

''' WIDGETS: Password '''
# Class to create a Password Entry object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class Password(object):
    controller = None
    callback = None
    Type= "Password"
    def __init__(self,X,Y,width,height):				# Constructor to set attributes
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.mytext = root.StringVar()
    def getText(self):							# Function to get the entered value of Password
        if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get()        
    def setText(self,text):
	    self.mytext.set(text) 

''' WIDGETS: Slider '''
# Class to create a Slider object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class Slider(object):
    controller = None
    callback = None
    Type = "Slider"
    def __init__(self,start,end,X,Y,width,height):			# Constructor to set attributes
	self.start=start
	self.end=end
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    def getValue(self):							# Function to get the selected value of Slider
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get()




''' WIDGETS: Spinbox '''
# Class to create a Spinbox object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class SpinBox(object):				
    controller = None
    callback = None
    Type = None
    def __init__(self,start,end,X,Y,width,height):			# Constructor to set attributes
        self.type = "SpinBox"
	self.start=start
	self.end=end
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def getValue(self):							# Function to select the value in the Spinbox widget
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.get()



''' WIDGETS: Label '''
# Class to create a Label object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class Label(object):
    controller = None
    Type = None
    label_var = 0
    def __init__(self,text,X,Y,width,height):				# Constructor to set attributes
        self.Type = "Label"
        self.label_var = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):						# Function to set text to Label
        if(self.controller == None):
            self.text = text
        else:
            self.label_var.set(text)
        return True

    def clear(self):							# Function to erase the text of Label
        self.controller.Clear()
        return True



''' WIDGETS: Textline'''
# Class to create a TextLine object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class TextLine(object):
    controller = None
    callback = None
    Type= "TextLine"	
    def __init__(self,X,Y,width,height):				# Constructor to set attributes
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def getText(self):							# Function to get the content of TextLine
	if(self.controller == None):
            return ''
	else:
	    return self.controller.get()

    def setText(self,text):						# Function to set the content of TextLine to string text
        if(self.controller == None):
            self.text = text
        else:
	    self.controller.delete(0, root.END)
            self.controller.insert(0, text)
        return True
    
    def clear(self):							# Function to clear the content of TextLine
	if(self.controller == None):
            self.text = ""
	else:
	    self.controller.delete(0, root.END)	
        return True



''' WIDGETS: CheckBox '''
# Class to create a CheckBox object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class CheckBox(object):
    controller = None
    value = False
    Type = None
    def __init__(self,title,X,Y,width,height):				# Constructor to set attributes
        self.Type = "CheckBox"
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setValue(self,value):						# Function To select a CheckButton
        if(self.controller == None):
            self.value = value
        else:
            if(value):
                self.controller.select()
            else:
                self.controller.deselect()

    def getValue(self):							# Function to check whether a CheckBox is selected
        if(self.controller == None):
            return self.value
        else:
            if(self.value.get() == 1):
                return True
            else:
                return False




''' WIDGETS: RadioGroup '''
# Class to create a RadioGroup object and attributes of individual Radiobuttons will be added to this.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class RadioGroup(object):
    controller = None
    selected_index = None
    Type = None
    value = 0
    def __init__(self,width,height):					# Constructor to set attributes
        self.Type = "RadioGroup"
        self.labels = []
        self.positions_X = []
        self.positions_Y = []
        self.width = width
        self.height = height

    def addRadioButton(self,label,X,Y):					# Add individual buttons to a RadioGroup
        self.labels.append(label)
        self.positions_X.append(X)
        self.positions_Y.append(Y)
        return True

    def getValue(self):							# To get the value of selected RadioButtons
        for i in range(len(self.controller)):
            if(self.value.get()==i):
                return self.labels[i]
        return None

    def setButtonTrue(self,index):					# Function to select the CheckBox to True
        if(self.controller == None):
            self.value=index
        else:
            button_controller = self.controller[index]			
            button_controller.select()



''' WIDGETS: DropDownList '''
# Class to create a DropDownList object and set its attributes.
# Later this will be used to create an actual widget using "WindowFrame.add(widget)" function.
class DropDownList(object):
    controller = None
    Type = None
    list_var = 0
    def __init__(self,choices,X,Y,width,height,value=""):		 # Constructor to set attributes
        self.Type = "DropDownList"
        self.choices = choices
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.value = value

    def getValue(self):						# Get the Value of selected DropDownList option 
            if(self.controller == None):
                return self.title
            else:
                return self.list_var.get()
