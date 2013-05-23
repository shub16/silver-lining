import wx
import wx.calendar

class WindowLayout(wx.Frame):
    def __init__(self,parent,title,width,height):
        wx.Frame.__init__(self, None, -1, title, size=(width,height))    #creating a wx.Frame widget which is parent for all other widgets. Its parent is none.
        self.panel=wx.Panel(self)                                   #creating a panel as an attribute of this frame

    def createLayout(self,widgets):                 #to display the window after all widgets are set
        vbox = wx.BoxSizer(wx.VERTICAL)             #vertical boxSizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)           #horizontal boxSizer
        i=0
        n='1'
        for widget in widgets:
            if i==0:
                hbox.Add(widget)                    #Adds the first widget
            else:
                if n=='1':                          #if in same line add to same horizontal boxSizer
                    hbox.Add(widget)
                    n='2'
                else:                              #if to add in new line then create a new horizontal boxSize
                    vbox.Add(hbox)
                    vbox.Add((-1,10))
                    hbox=wx.BoxSizer(wx.HORIZONTAL)
                    hbox.Add(widget)
                    n='1'
            i=i+1
        vbox.Add(hbox)
        self.panel.SetSizer(vbox)                    #set the main vertical boxSizer as the sizer for the main window's panel
        self.Show()     

class ButtonWidget:                                       #class to create a button widget in its constructor as an attribute
    def __init__(self,parent,name,function,*args):
        self.widget=wx.Button(parent.panel,label=name)
        self.widget.Bind(wx.EVT_BUTTON, lambda event: function(event, *args))

    def getWidget(self):                            #to return the widget
        return self.widget

class TextLineWidget:                                  #class to create a textctrl widget in its constructor as an attribute
    def __init__(self,parent):
        self.widget=wx.TextCtrl(parent.panel,-1)
        self.widget.SetInsertionPoint(0)

    def getWidget(self):                        #to return the widget
        return self.widget

    def getValue(self):                         #to get the value of the widget
        return self.widget.GetValue()

class TextBoxWidget:                                  #class to create a textctrl widget in its constructor as an attribute
    def __init__(self,parent):
        self.widget=wx.TextCtrl(parent.panel,-1,style=wx.TE_MULTILINE)
        self.widget.SetInsertionPoint(0)

    def getWidget(self):                        #to return the widget
        return self.widget

    def getValue(self):                         #to get the value of the widget
        return self.widget.GetValue()
    
class RadioButtonWidget:                              #class to create a group of radiobuttons in its constructor as an attribute
    def __init__(self,parent,labels,varName):
        radiobuttons=[]
        for l in labels:                    #labels contains the list of labels for the radiobuttons                
            rb= wx.RadioButton(parent.panel, label=l, name=varName) 
            radiobuttons.append(rb)
        self.widget=radiobuttons

    def getWidget(self):                    #to return list of radiobuttons
        return self.widget

    def getValue(self):                     #to get the label of the active radiobutton from the group
        for rb in self.widget:
            if(rb.GetValue()):
                break
        return rb.GetLabel()
        
class ListWidget:                                 #class to create a list(combobox) widget in its constructor as an attribute
    def __init__(self,parent,values):
        self.widget=wx.ComboBox(parent.panel,choices=values,style=wx.CB_READONLY)

    def getWidget(self):                    #to return the widget
        return self.widget

    def getValue(self):                     #to get the selected value from the list widget
        return self.widget.GetValue()

class PasswordFieldWidget:                        #class to create a password textctrl widget in its constructor as an attribute
    def __init__(self,parent):
        self.widget=wx.TextCtrl(parent.panel,style=wx.TE_PASSWORD)
        self.widget.SetInsertionPoint(0)

    def getWidget(self):                    #to return the widget
        return self.widget

    def getValue(self):                     #to get the value of the widget
        return self.widget.GetValue()       

class LabelWidget:                                #class to create a StaticText widget in its constructor as an attribute
    def __init__(self,parent,name):
        self.widget=wx.StaticText(parent.panel,label=name)

    def getWidget(self):                    #to return the widget
        return self.widget
        

class CheckBoxWidget:                             #class to create a checkbox widget in its constructor as an attribute
    def __init__(self,parent,name,varName):
        self.widget=wx.CheckBox(parent.panel,label=name)

    def getWidget(self):                    #to return the widget
        return self.widget

    def getValue(self):                     #to get the value of the checkbox whether True or False
        return self.widget.GetValue()

class SpinBoxWidget:                            #class to create a spinbox widget in its constructor as an attribute
    def __init__(self,parent,fromvalue,tovalue):
        self.widget=wx.SpinCtrl(parent.panel,value='')
        self.widget.SetRange(fromvalue,tovalue)

    def getWidget(self):                        #to return the widget
        return self.widget

    def getValue(self):                         #to get the value of the spinbox
        return self.widget.GetValue()

class CalendarWidget:
    def __init__(self,parent):                  #class to create a calendar widget in its constructor as an attribute
        self.widget=wx.calendar.CalendarCtrl(parent.panel)

    def getWidget(self):                        #to return the widget
        l=[]
        l.append(self.widget)
        return l

    def getValue(self):                         #to get the selected date from the calendar
        return self.widget.GetDate()

class SliderWidget:                             #class to create a slider widget in its constructor as an attribute
    def __init__(self,parent,fromvalue,tovalue):
        self.widget=wx.Slider(parent.panel,minValue=fromvalue,maxValue=tovalue,style=wx.SL_HORIZONTAL)

    def getWidget(self):                         #to return the widget
        return self.widget

    def getValue(self):                         #to get the value of the slider                         
        return self.widget.GetValue()

    
        
def print_button(e,obj):
    if(validate(obj.pwd2.getValue(),obj.pwd3.getValue())):
        wx.MessageBox("Thanks for using this application. Your new password is valid and will be set", 'Info',wx.OK | wx.ICON_INFORMATION)               #displaying the string in the dialog box
        obj.Close(True)     #predefined function in wx.Frame that closes the application
    else:
        wx.MessageBox("The new password entered is invalid. It should match,have more than 6 chars and contain both alpha and numeric fields", 'Info',wx.OK | wx.ICON_INFORMATION)               #displaying the string in the dialog box
        
def close(e,obj):
    obj.Close(True)     #predefined function in wx.Frame that closes the application
       

def createWidgets(obj):
    widgets=[]                          #list of widgets to be added
    obj.l1=LabelWidget(obj,"Username")        #call to the Label class that adds a staticText widget with panel as the parent
    widgets.append(obj.l1.getWidget())  #returns the widget to append to the list of widgets
    obj.textbox=TextLineWidget(obj)            #call to the TextBox class that adds a single line textctrl widget with panel as the parent
    widgets.append(obj.textbox.getWidget())

    obj.l2=LabelWidget(obj,"Old Password")
    widgets.append(obj.l2.getWidget())
    obj.pwd1=PasswordFieldWidget(obj)         #call to the PasswordField class that adds a single line textctrl widget of password style with panel as the parent
    widgets.append(obj.pwd1.getWidget())

    obj.l3=LabelWidget(obj,"New Password")
    widgets.append(obj.l3.getWidget())
    obj.pwd2=PasswordFieldWidget(obj)         #call to the PasswordField class that adds a single line textctrl widget of password style with panel as the parent
    widgets.append(obj.pwd2.getWidget())

    obj.l4=LabelWidget(obj,"New Password(repeat)")
    widgets.append(obj.l4.getWidget())
    obj.pwd3=PasswordFieldWidget(obj)         #call to the PasswordField class that adds a single line textctrl widget of password style with panel as the parent
    widgets.append(obj.pwd3.getWidget())

    obj.l5=LabelWidget(obj,"Age")
    widgets.append(obj.l5.getWidget())
    obj.spinbox=SpinBoxWidget(obj,18,70)         #call to the SpinBox class that adds spinctrl widget with panel as the parent
    widgets.append(obj.spinbox.getWidget())

    obj.l6=LabelWidget(obj,"Date of Birth")
    widgets.append(obj.l6.getWidget())
    obj.cal=CalendarWidget(obj)                 #call to the Calendar widget class that adds a calendar widget with panel as the parent
    l=obj.cal.getWidget()
    for cal_widg in l:
        widgets.append(cal_widg)

    labels=["Male","Female"]
    stringname="gender"
    obj.rb=RadioButtonWidget(obj,labels,stringname)               #call to the RadioButton widget class that adds list of radiobuttons with panel as the parent
    radiobuttons=obj.rb.getWidget()
    for rb in radiobuttons:
        widgets.append(rb)

    obj.l8=LabelWidget(obj,"Nationality")
    widgets.append(obj.l8.getWidget())
    values=["Indian","British","Chinese","American","Others"]
    obj.list=ListWidget(obj,values)               #call to the List widget class that adds a combobox with list of options with panel as the parent
    widgets.append(obj.list.getWidget())

    obj.l9=LabelWidget(obj,"Rating for this application")
    widgets.append(obj.l9.getWidget())
    obj.sl=SliderWidget(obj,0,10)               #call to the Slider widget class that adds Slider ctrl widget with panel as the parent
    widgets.append(obj.sl.getWidget())
    

    obj.button=ButtonWidget(obj,"Submit",print_button,obj)  #call to the Button class that adds a button widget with panel as the parent
    widgets.append(obj.button.getWidget())                  #returns the widget to append to the list of widgets

    obj.button2=ButtonWidget(obj,"Close",close,obj)  #call to the Button class that adds a button widget with panel as the parent
    widgets.append(obj.button2.getWidget())
    return widgets

def validate(str1,str2):            #function to validate two strings if they match, are greater than 6 in length and contain both alpha and numeric fields
    
    if(cmp(str1,str2)!=0):          #to compare two strings(returns 0 if equal)   
        return False

    if(len(str1)<=6):               #to check the length of the string
        return False    

    if(str1.isalnum()):             #checks if string only alpha or numeric fiels
        if(str1.isalpha()|str1.isdigit()):          #But invalidates if only alpha or only numeric fields as should contain both
            return False        
        return True
    else:
        return False


if __name__ == '__main__':

    print "Creating a wxPython application"
    app = wx.App()
    obj = WindowLayout(app,'WxPython Application',300,500)     #creates an instance of TextFrame class which creates an instance of wx.Frame  
    widgets=createWidgets(obj)                              #function call to construct the widgets in the application
    obj.createLayout(widgets)                               #To layout the widgets in the window
    app.MainLoop()

    #Following is the part to give a choice for a GUI which will be used when integrated
    
    #print "Choose your preferred Gui toolkit by entering a number"
    #print "1 wxPython"
    #print "2 pyGTK"
    #print "3 Tkinter"
    
    #num=raw_input()

    #if(num=='1'):
        #print "Creating a wxPython application"
        #app = wx.App()
        #obj = TextFrame(app,'WxPython Application',250,250)     #creates an instance of TextFrame class which creates an instance of wx.Frame  
        #widgets=createWidgets(obj)                              #function call to construct the widgets in the application
        #obj.createLayout(widgets)                               #To layout the widgets in the window
        #app.MainLoop()

    #elif(num=='2'):
        #print "Creating a pyGTK application"
        #import assignment_1
    
    #elif(num=='3'):
        #print "Creating a Tkinter application"
        #import Assignment1_tkinter

    #else:
        #print "Invalid selection Should enter 1, 2 or 3"
