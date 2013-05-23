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
        
	elif(widget_type==TextField or isinstance(widget,TextField)):
            widget.instance = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size)

	elif(widget_type==TextFieldPass or isinstance(widget,TextFieldPass)):
            widget.instance = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style = wx.TE_PASSWORD)
    
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

        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.instance = wx.StaticText(self.panel, -1,widget.text,widget.position,widget.size)

        elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.instance = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)

        elif(widget_type==Slider or isinstance(widget,Slider)):
            widget.instance = wx.Slider(self.panel, -1,minValue=widget._from, maxValue=widget._to, pos=widget.position, size=widget.size,  style=wx.SL_HORIZONTAL) 

	elif(widget_type==SpinBox or isinstance(widget,SpinBox)):
	    widget.instance = wx.SpinCtrl(self.panel,-1,size = widget.size,pos = widget.position, style=wx.SP_HORIZONTAL)
	    widget.instance.SetRange(widget.start, widget.end)


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

class LabelText(wx.StaticText):						# Labeltext
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)

class TextFieldPass(wx.TextCtrl):
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, -1)

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

class TextField(wx.TextCtrl):						# TextField
    instance = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, -1)

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

storePass = "oldpassword"						# Rent Secure
secure = True

def rentSecure(password,isSecure):
    if(isSecure):
        for i in range(len(password)):
           password = password.replace(password[i],"*")
    print isSecure,password
    return password

def Submit(self):							# Submit
    newps1 = NewPstb.getText();
    newps2 = ReNewPstb.getText();
    if(IsValidPswd(newps1,newps2)):
        print (" Password Successfully Changed ! ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
    else:
        print (" Retry by Entering new Password!  ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");

def IsValidPswd(newps1, newps2):						# Is valid Password
    if newps1 != newps2:
       print(" Password Error !  Passwords donot match! ")
       return False
    
    if(len(newps1)<=6):               # Check the length of the password
       print(" Password Error ! Password Length should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(newps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" Password Error ! Password cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(newps1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print(" Password Error ! Password cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            print ("Password Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print (" Password Error ! Password should contain only alphabets and digits.");
       return False



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

class ValueList(wx.ComboBox):
    instance = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.choices = choices
        self.position = (X,Y)
        self.size = (width,-1)
        self.value = value

    def getValue(self):
            if(self.instance == None):
                return self.value
            else:
                return self.instance.GetValue()


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

''' WIDGETS: Slider '''
class Slider(wx.Slider):
    instance = None
    def __init__(self,_from,_to,X,Y,width,height):
        self.position = (X,Y)
        self.size = wx.Size(width, height)
        self._from = _from
        self._to = _to

    def getValue(self):
        return self.instance.GetValue()

class SpinBox(wx.SpinCtrl):
    instance = None

    def __init__(self,_from,_to,X,Y,width,height):
	self.position = (X,Y)
	self.size = wx.Size(width,height)
	self._from = _from
	self._to = _to

    def getValue(self):
	return self.instance.GetValue()

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
    
    canvas = Main_Window(1, 'wxPython | Jag Ustit Singh' ,560,600)


    userLbl = LabelText("Username: ",20,40,120,30)
    usrtb = TextField("",150,40,300,25)
    canvas.add_widget(userLbl)
    canvas.add_widget(usrtb)


    OldPswdLbl = LabelText("Current Password: ",20,100,120,30)
    OldPstb= TextFieldPass("",150,100,300,25)
    canvas.add_widget(OldPswdLbl)
    canvas.add_widget(OldPstb)



    NewPswdLbl = LabelText("New Password: ",20,160,120,30)
    NewPstb= TextFieldPass("",150,160,300,25)
    canvas.add_widget(NewPswdLbl)
    canvas.add_widget(NewPstb)

    label = LabelText("Confirm Password: ",20,220,120,30)
    ReNewPstb = TextFieldPass("",150,220,300,25)
    canvas.add_widget(label)
    canvas.add_widget(ReNewPstb)




    btn= Button("Register",130,400,120,30)

    #Callback methods on buttons click
    btn.on_click(Submit)

    #Adding buttons to canvas
    canvas.add_widget(btn)

    canvas.show()

