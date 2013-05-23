
import gtk

class Main_Window(object):
    parent = None
    def __init__(self, id, title,width,height):
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()


    def show(self):
        self.window.show()
        gtk.main()
        return

    def add_widget(self,widget):
    
        widget_type = type(widget) 
         
        if(widget_type == Button or isinstance(widget,Button)):
            widget.instance = gtk.Button(widget.text)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
            if(widget.callbackMethod != None ):
                widget.instance.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextBox or isinstance(widget,TextBox) ):
            widget.instance = gtk.TextView(widget.buffer)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
        
     
        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.instance = gtk.CheckButton(widget.title)
            widget.instance.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.instance, widget.position_X, widget.position_Y)            
            widget.instance.show()
            widget.instance.set_active(widget.value)
            
        elif(widget_type==RadioButtons or isinstance(widget,RadioButtons)):
            widget.instance = []
            radio_instance = gtk.RadioButton(None, widget.labels[0])
            radio_instance.set_size_request(widget.width,widget.height)
            self.fixed.put(radio_instance,widget.position_X[0], widget.position_Y[0])
            radio_instance.show()
            widget.instance.append(radio_instance)
            for i in range(1,len(widget.labels)):
                radio_instance = gtk.RadioButton(widget.instance[0], widget.labels[i])
                radio_instance.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_instance,widget.position_X[i], widget.position_Y[i])
                radio_instance.show()
                widget.instance.append(radio_instance)
            
            if(widget.selected_pos != None):
                widget.instance[widget.selected_pos].set_active(True)
            
    
            



class Button(object):
    instance = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def on_click(self,event):
        if(self.instance == None):
            self.callbackMethod = event
        else:
            self.instance.connect("clicked", event)
        return True
    
class TextBox(object):
    instance = None
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



class CheckBox(object):
    instance = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    
    def set_state(self,value):   #True or False for checked
        if(value != True or value != False):
            return
        if(self.instance == None):
            self.value = value
        else:
            self.instance.set_active(value)

    def get_state(self):
        if(self.instance == None):
            return self.value
        else:
            return self.instance.get_active()


class RadioButtons(object):
    GroupController = None
    instance = None
    selected_pos = None
    def __init__(self,width,height):
        self.labels = []
        self.position_X = []
        self.position_Y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def add_radiobutton(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def get_state(self):
        for i in range(len(self.instance)):
            if(self.instance[i].get_active()):
                return self.labels[i]
        return "None"



if __name__ == '__main__':

	def Evaluate(event=None):
		    display = "" 
		    textarea.clear()
		    temp = "Your hobbies are the following:"
	
		   	
		    if(checkbox1.get_state()):
			display = display + "You like Swimming\n"
		    
		    if(checkbox2.get_state()):
			display = display + "You like reading novels\n"

		    if(checkbox3.get_state()):
			display = display + "You like listening to music\n"

		    if(checkbox4.get_state()):
			display = display + "You like cycling\n"

		    if(checkbox5.get_state()):
			display = display + "You like to write poems\n"

		    if(checkbox6.get_state()):
			display = display + "You like dancing\n"

		    if(not(checkbox1.get_state()) and not(checkbox2.get_state()) and not(checkbox3.get_state()) and not(checkbox4.get_state()) and not(checkbox5.get_state()) and not(checkbox6.get_state())):
			display = display + "No hobbies? Get a Life :P \n"   


		    
		    textarea.setText("You are "+rb1.get_state()+"\n\n"+temp+"\n\n"+display+"\n\n")
		    return True 


		#Constructor canvas
	canvas = Main_Window(1, 'Common API' ,510,300)

		#Creating checkboxes for displaying hobbies
	checkbox1 = CheckBox("Swimming",370,20,215,20)
	checkbox2 = CheckBox("Reading Books",370,45,215,20)
	checkbox3 = CheckBox("Music",370,70,215,20)
	checkbox4 = CheckBox("Cycling",370,95,215,20)
	checkbox5 = CheckBox("Poetry",370,120,215,20)
	checkbox6 = CheckBox("Dancing",370,145,215,20)
		#Adding checkboxes 
	canvas.add_widget(checkbox1)
	canvas.add_widget(checkbox2)
	canvas.add_widget(checkbox3)
	canvas.add_widget(checkbox4)
	canvas.add_widget(checkbox5)
	canvas.add_widget(checkbox6)

	#Radio buttons for gender
	rb1 = RadioButtons(90,30)
	rb1.add_radiobutton("Male",10,20)
	rb1.add_radiobutton("Female",10,45)
	canvas.add_widget(rb1)
	#Adding the text area
	textarea = TextBox("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,20,230,150)
	canvas.add_widget(textarea)
	#Creating Buttons
	submitBtn = Button("Evaluate",170,210,120,30)
	#Callback methods on button click
	submitBtn.on_click(Evaluate)
	#Adding button to canvas
	canvas.add_widget(submitBtn)
	canvas.show()

