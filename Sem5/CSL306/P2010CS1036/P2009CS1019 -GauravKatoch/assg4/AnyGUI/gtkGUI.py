'''    The code is not completely object oriented right now, I have some other ideas in which I will divide each
       widget into a class, in this way things would make more sense.
       
       Currently there is only one class with many functions to create different widgets, but consistency and
       understandability is a bit complex
''' 

import gtk

class Canvas(object):
    parent = None
    def __init__(self, id, title,width,height):
        #Initialize the Widget
        

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
        if(widget_type==Button or isinstance(widget,Button)):
            widget.controller = gtk.Button(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextArea or isinstance(widget,TextArea) ):
            widget.controller = gtk.TextView(widget.buffer)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextField or isinstance(widget,TextField)):
            widget.controller = gtk.Entry()
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
            widget.controller.set_text(widget.title)            
            widget.controller.show()

        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = gtk.CheckButton(widget.title)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            widget.controller.set_active(widget.value)
            
        elif(widget_type==RadioGroup or isinstance(widget,RadioGroup)):
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
            
        elif(widget_type==ValueList or isinstance(widget,ValueList)):
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
        
        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.controller = gtk.Label(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)    
            widget.controller.set_markup("<span font_desc='Calibri "+str(widget.size)+"'>"+widget.text+"</span>" )        
            widget.controller.show()
            
        elif(widget_type == Slider or isinstance(widget,Slider)):
            widget.controller = gtk.Adjustment(1.0, widget._from, widget._to, 1.0, 1.0, 0.0)
            widget.scale = gtk.HScale(widget.controller)
            widget.scale.set_digits(0)
            widget.scale.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.scale,widget.position_X,widget.position_Y)
            widget.scale.show()
            
        elif(widget_type == Dialog or isinstance(widget,Dialog)):
            widget.title=widget.title
''' WIDGETS: LabelText '''
class LabelText(object):
    controller = None
   
    def __init__(self,text,X,Y,width,height,size):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.size = size
        
    def setTextSize(self,size):
        self.controller.set_markup("<span font_desc='Tahoma "+str(size/2)+"'>"+self.text+"</span>" )


class Button(object):
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
    
class TextArea(object):
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

''' WIDGETS: TextField '''
class TextField(object):
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


class CheckBox(object):
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


class RadioGroup(object):
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
            if(self.controller[i].get_active()):
                return self.labels[i]
        return "None"

    def setButtonTrue(self,pos):
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.set_active(True)

class ValueList(object):
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

''' WIDGETS: Slider '''
class Slider(object):
    controller = None
    def __init__(self,text,X,Y,width,height,_from,_to):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self._from = _from
        self._to = _to

    def getValue(self):
        return int (self.controller.get_value())

''' WIDGETS: Dialog '''
class Dialog(object):
    controller = None
    def __init__(self,title,text):
       self.title=title
       self.text=text
        
    def show(self,width,height,title,text):
        self.controller = gtk.MessageDialog(None, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, 
            gtk.BUTTONS_OK, self.text)
        self.controller.set_title(self.title)
        self.controller.set_size_request(width,height)
        self.controller.run()
        self.controller.destroy() 
       
        
    

if __name__ == '__main__':

    #Functions bind to button events
    def SubmitButtonClick(event):
        report = " Your city is "+valuelist.getValue()+"\n"
        if(checkbox1.getValue()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"

        if(checkbox2.getValue()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"

        report = report + " you are "+rb1.getValue()+"\n"
        report = report + " you need "+rb2.getValue()+"\n"

        textarea.appendText("_______________________\n"+report+"\n\n")
        return True 

    def AboutButtonClick(event):
        textarea.setText("Created by gtkGUI -v1.0\nAuthor : Gaurav Katoch\n\nhttp://10.1.0.140/trac/wiki/GauravKatoch\n")
        return True



    #Constructor canvas
    canvas = Canvas(1, 'GTK -v1.0 | Gaurav Katoch' ,510,300)

    #Dropdown valuelist
    cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
    valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
    canvas.add(valuelist)

    #checkboxs
    checkbox1 = CheckBox("I have read the code.",10,45,215,15)
    checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
    checkbox1.setValue(True)
    canvas.add(checkbox1)
    canvas.add(checkbox2)

    #radioGroup1
    rb1 = RadioGroup(60,50)
    rb1.addRadioButton("Nice",10,110)
    rb1.addRadioButton("Good",70,110)
    rb1.addRadioButton("Great",140,110)
    rb1.setButtonTrue(2)
    canvas.add(rb1)

    #radioGroup2
    rb2 = RadioGroup(100,50)
    rb2.addRadioButton("Option #1",10,160)
    rb2.addRadioButton("Option #2",110,160)
    rb2.setButtonTrue(0)
    canvas.add(rb2)

    #TextArea
    textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
    canvas.add(textarea)

    #Creating Buttons
    submitBtn = Button("Submit",130,230,120,30)
    aboutBtn = Button("About",260,230,120,30)

    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)

    #Adding buttons to canvas
    canvas.add(aboutBtn)
    canvas.add(submitBtn)

    canvas.show()

    