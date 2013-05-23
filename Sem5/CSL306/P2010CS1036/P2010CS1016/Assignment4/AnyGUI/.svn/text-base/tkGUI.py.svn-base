import tkMessageBox
import Tkinter as root

class Main_Window(object):
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

    def add_widget(self,widget):
        widget_type = type(widget)
        if(widget_type == "Button" or isinstance(widget,Button) ):
            frame = self.placing(widget)
            widget.instance = root.Button(frame, text=widget.title, command=widget.callbackMethod)
            widget.instance.pack(fill=root.BOTH, expand=1)

        elif(widget_type == "TextBox" or isinstance(widget,TextBox) ):
            frame = self.placing(widget)
            widget.instance = root.Text(frame)
            widget.instance.pack(fill=root.BOTH, expand=1)
            widget.instance.insert(root.INSERT,widget.text)

        elif(widget_type == "CheckBox" or isinstance(widget,CheckBox) ):
            frame = self.placing(widget)
            var = widget.value 
            widget.value = root.IntVar()
            if(var):
                widget.value.set(1)
            else:
                widget.value.set(0)
            
            widget.instance = root.Checkbutton(frame, text=widget.title, variable=widget.value)
            widget.instance.grid(sticky=root.W)

        elif(widget_type == "RadioButtons" or isinstance(widget,RadioButtons) ):
            frame = self.placing_radio(widget.width,widget.height,widget.positions_X[0],widget.positions_Y[0])
            widget.instance = []
            radio_var = widget.value
            widget.value = root.IntVar()
            widget.value.set(radio_var)
            radio_instance = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_instance.pack(fill=root.BOTH, expand=1)
            widget.instance.append(radio_instance)
            for i in range(1,len(widget.labels)):
                frame = self.placing_radio(widget.width,widget.height,widget.positions_X[i],widget.positions_Y[i])
                radio_instance = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value,value=i)
                radio_instance.pack(fill=root.BOTH, expand=1)
                widget.instance.append(radio_instance)

    def placing(self,widget):
        frame = root.Frame(self.window, width=widget.width,height=widget.height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=widget.position_X,y=widget.position_Y)
        return frame

    def placing_radio(self,W,H,X,Y):
        frame = root.Frame(self.window, width=W,height=H)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        return frame

class Button(object):
    instance = None
    callbackMethod = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height


    def on_click(self,event):
        if(self.instance == None):
            self.callbackMethod = event
        else:
            self.instance.callback(event)
        return True
        
class TextBox(object):
    instance = None
    def __init__(self,title,X,Y,width,height):
        self.text = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.delete(1.0, root.END)
            self.instance.insert(root.INSERT,text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.get(1.0, root.END)           

    def clear(self):
        self.instance.delete(1.0, root.END)
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

    def set_state(self,value):
        if(self.instance == None):
            self.value = value
        else:
            if(value):
                self.instance.select()
            else:
                self.instance.deselect()
    def select_value(self):
	if self.value==True:
		self.instance.select()
    def get_state(self):
        if(self.instance == None):
            return self.value
        else:
            if(self.value.get() == 1):
                return True
            else:
                return False	
 


class RadioButtons(object):
    instance = None
    selected_index = None
    value = 0
    def __init__(self,width,height):
        self.labels = []
        self.positions_X = []
        self.positions_Y = []
        self.width = width
        self.height = height

    def add_radiobutton(self,label,X,Y):
        self.labels.append(label)
        self.positions_X.append(X)
        self.positions_Y.append(Y)
        return True
    def get_state(self):
        for i in range(len(self.instance)):
            if(self.value.get()==i):
                return self.labels[i]
        return None


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

