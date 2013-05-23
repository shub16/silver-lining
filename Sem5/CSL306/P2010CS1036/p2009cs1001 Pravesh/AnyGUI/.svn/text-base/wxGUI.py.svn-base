# wxGUI.py
# version 1.1
# ArinkVerma 
import wx

''' WX_Canvas : On it widget can be added '''
class Canvas(wx.Frame):
    parent = None
    Type = "Canvas"
    def __init__(self, id, title,width,height):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, id, title, wx.DefaultPosition, wx.Size(width, height))
        self.panel = wx.Panel(self, -1)


    def show(self):
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return


    def add(self,widget):
        widget_type = type(widget)
        print widget_type
        if(widget_type==TextArea or isinstance(widget,TextArea)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_MULTILINE)

        elif(widget_type==TextField or isinstance(widget,TextField)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size)
            
        elif(widget_type==Button or isinstance(widget,Button)):
            widget.controller = wx.Button(self.panel, -1, widget.title,  widget.position, widget.size)
            #(self, parent, id, label, pos, size, style, validator, name)
            if(widget.callback != None ):
                widget.controller.Bind(wx.EVT_BUTTON, widget.callback)

        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = wx.CheckBox(self.panel, -1, widget.title,  widget.position,widget.size)
            widget.controller.SetValue(widget.value)

        elif(widget_type==RadioGroup or isinstance(widget,RadioGroup)):
            widget.controller = []
            radio_controller = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                widget.controller.append(radio_controller)
        
            if(widget.selected_index != None):
                widget.controller[widget.selected_index].SetValue(True)

        elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.controller = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)

        elif(widget_type==LabelText or isinstance(widget,LabelText)):
            widget.controller = wx.StaticText(self.panel, -1,widget.text,widget.position,widget.size)

        elif(widget_type==Slider or isinstance(widget,Slider)):
            widget.controller = wx.Slider(self.panel, -1,minValue=widget._from, maxValue=widget._to, pos=widget.position, size=widget.size, style=wx.SL_HORIZONTAL) 

        elif(widget_type==Dialog or isinstance(widget,Dialog)):
            widget.controller = wx.MessageDialog(self.panel, widget.text, widget.title, wx.OK | wx.ICON_INFORMATION) 



class Widget:
    pass



''' WIDGETS: Dialog '''
class Dialog(wx.MessageDialog):
    controller = None
    def __init__(self,title,text):
        self.title = title
        self.text = text

    def show(self):
        self.controller = wx.MessageDialog(None, self.text, self.title, wx.OK | wx.ICON_INFORMATION) 
        self.controller.ShowModal()
       

''' WIDGETS: Slider '''
class Slider(wx.Slider):
    controller = None
    def __init__(self,text,X,Y,width,height,_from,_to):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, -1)
        self._from = _from
        self._to = _to

    def getValue(self):
        return self.controller.GetValue()


''' WIDGETS: TextField '''
class TextField(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, -1)

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.SetValue(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.GetValue()

''' WIDGETS: TextArea '''
class LabelText(wx.StaticText):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)


''' WIDGETS: TextArea '''
class TextArea(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.SetValue(text)
        return True

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.GetValue()


    def appendText(self,text):
        if(self.controller == None):
            self.text = self.controller.GetValue() + text
        else:
            self.controller.AppendText(text)
        return True              

    def clear(self):
        self.controller.Clear()
        return True






''' WIDGETS: Button '''
class Button(wx.Button):
    controller = None
    callback = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def clickListener(self,method):
        if(self.controller == None):
            self.callback = method
        else:
            self.controller.Bind(wx.EVT_BUTTON, method)
        return True

''' WIDGETS: CheckBox '''
class CheckBox(wx.CheckBox):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position = (X,Y)
        self.size = wx.Size(width, height)

    def setValue(self,value):
        if(self.controller == None):
            self.value = value
        else:
            self.controller.SetValue(value)

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.IsChecked()

''' WIDGETS: RadioGroup '''
class RadioGroup(wx.RadioButton):
    controller = None
    selected_index = None
    def __init__(self,width,height):
        self.labels = []
        self.positions = []
        self.size = wx.Size(width, height)

    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.positions.append((X,Y))
        return True

    def getValue(self):
        for i in range(len(self.controller)):
            if(self.controller[i].GetValue()):
                return self.labels[i]
        return None

    def setButtonTrue(self,index):
        if(self.controller == None):
            self.selected_index = index
        else:
            button_controller = self.controller[index]
            button_controller.SetValue(True)

''' WIDGETS: ValueList '''
class ValueList(wx.ComboBox):
    controller = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.choices = choices
        self.position = (X,Y)
        self.size = (width,-1)
        self.value = value

    def getValue(self):
            if(self.controller == None):
                return self.value
            else:
                return self.controller.GetValue()



''' ----------------------------------------------------------------
        This is just demo! 
        IT IS NOT THE PART OF LIB '''

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
        label.setText("Label Text changed!")
        return True 

    def AboutButtonClick(event):
        textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
        print textarea.getText()
        return True



    #Constructor canvas
    canvas = Canvas(1, 'wxGUI -v1.0 | ArinkVerma' ,510,300)

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


    label = LabelText("This is demo Label Text!",10,95,215,30)
    canvas.add(label)

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