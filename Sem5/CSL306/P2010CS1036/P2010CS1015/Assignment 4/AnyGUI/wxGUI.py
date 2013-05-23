# wxGUI.py
# version 1.1

import wx

''' WX_Main_Window : On it widget can be add_widgeted '''
class Main_Window(wx.Frame):
    parent = None
    Type = "Main_Window"
    def __init__(self, id, title,width,height):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, id, title, wx.DefaultPosition, wx.Size(width, height))
        self.panel = wx.Panel(self, -1)


    def show(self):
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return


    def add_widget(self,widget):
        widget_type = type(widget)

        if(widget_type==TextBox or isinstance(widget,TextBox)):
            widget.instance = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_MULTILINE)
            
        elif(widget_type==Button or isinstance(widget,Button)):
            widget.instance = wx.Button(self.panel, -1, widget.title,  widget.position, widget.size)
            if(widget.callbackMethod != None ):
                widget.instance.Bind(wx.EVT_BUTTON, widget.callbackMethod)

        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.instance = wx.CheckBox(self.panel, -1, widget.title,  widget.position,widget.size)
            widget.instance.SetValue(widget.value)

        elif(widget_type==RadioButtons or isinstance(widget,RadioButtons)):
            widget.instance = []
            radio_instance = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            widget.instance.append(radio_instance)
            for i in range(1,len(widget.labels)):
                radio_instance = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                widget.instance.append(radio_instance)
        
            if(widget.selected_index != None):
                widget.instance[widget.selected_index].SetValue(True)

        elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.instance = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)

        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.instance = wx.StaticText(self.panel, -1,widget.text,widget.position,widget.size)



class Widget:
    pass



''' WIDGETS: TextBox '''
class TextBox(wx.TextCtrl):
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setText(self,text):
        if(self.instance == None):
            self.text = text
        else:
            self.instance.SetValue(text)
        return True

    def getText(self):
        if(self.instance == None):
            return self.text
        else:
            return self.instance.GetValue()

    def clear(self):
        self.instance.Clear()
        return True



''' WIDGETS: Button '''
class Button(wx.Button):
    instance = None
    callbackMethod = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def on_click(self,method):
        if(self.instance == None):
            self.callbackMethod = method
        else:
            self.instance.Bind(wx.EVT_BUTTON, method)
        return True

''' WIDGETS: CheckBox '''
class CheckBox(wx.CheckBox):
    instance = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def set_state(self,value):
        if(self.instance == None):
            self.value = value
        else:
            self.instance.SetValue(value)

    def get_state(self):
        if(self.instance == None):
            return self.value
        else:
            return self.instance.IsChecked()

''' WIDGETS: RadioButtons '''
class RadioButtons(wx.RadioButton):
    instance = None
    selected_index = None
    def __init__(self,width,height):
        self.labels = []
        self.positions = []
        self.size = wx.Size(width, height)

    def add_radiobutton(self,label,X,Y):
        self.labels.append(label)
        self.positions.append((X,Y))
        return True

    def get_state(self):
        for i in range(len(self.instance)):
            if(self.instance[i].GetValue()):
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
