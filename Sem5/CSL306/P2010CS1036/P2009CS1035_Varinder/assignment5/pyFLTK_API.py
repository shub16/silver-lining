from fltk import *
import sys

class Button(Fl_Button):
    controller = None
    callbackMethod = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def clickListener(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.callback(method)
        return True

class TextView(Fl_Multiline_Input):
    controller = None
    callback = None
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.value(text)
        return True
    
    def getText(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.value()

    def appendText(self,text):
        if(self.controller == None):
            self.text = self.text+text
        else:
            self.text = self.controller.value() + text
            self.controller.value(text)
        return True              

    def clear(self):
        self.controller.Clear()
        return True


class CheckBox(Fl_Check_Button):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.cord_x = X
        self.cord_y = Y
        self.width = width
        self.height = height

    def setValue(self,value):
        if(self.controller == None):
            self.value = value
        else:
            self.controller.value(value)
        

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.value()


class Radio(Fl_Round_Button):
    GroupController = None
    controller = None
    selected_pos = None
    def __init__(self,width,height):
        self.labels = []
        self.cord_x = []
        self.cord_y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.cord_x.append(X)
        self.cord_y.append(Y)
        return True

    def getValue(self):
        for i in range(len(self.controller)):
            if(self.controller[i].value()):
                return self.labels[i]
        return "None"

    def setButtonTrue(self,pos):
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.value(True)

class Xwindow(Fl_Widget):
    parent = None
    def __init__(self, id, title,width,height):
        self.window = Fl_Window(0,0,width,height,title)
        self.window.position((Fl.w() - self.window.w())/2, (Fl.h() - self.window.h())/2);

    def show(self):
        self.window.end()
        self.window.show(sys.argv)
        Fl.run()
        return

    def add(self,widget):
        widget_type = type(widget)
        if(widget_type==TextView or isinstance(widget,TextView)):
            widget.controller = Fl_Multiline_Input(widget.cord_x, widget.cord_y, widget.width, widget.height)
            widget.controller.value(widget.title)
        elif(widget_type==Button or isinstance(widget,Button)):
            widget.controller = Fl_Button(widget.cord_x, widget.cord_y, widget.width, widget.height, widget.title)
            if(widget.callbackMethod != None ):
                widget.controller.callback(widget.callbackMethod)

        elif(widget_type==Radio or isinstance(widget,Radio)):
            widget.GroupController = Fl_Group(widget.cord_x[0], widget.cord_y[0], len(widget.labels)*widget.width, 2*widget.height, "")
            widget.controller = []
            radio_controller = Fl_Round_Button(widget.cord_x[0], widget.cord_y[0], widget.width, widget.height, widget.labels[0]);
            radio_controller.type(FL_RADIO_BUTTON);
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = Fl_Round_Button(widget.cord_x[i], widget.cord_y[i], widget.width, widget.height, widget.labels[i]);
                radio_controller.type(FL_RADIO_BUTTON);
                widget.GroupController.add(radio_controller)
                widget.controller.append(radio_controller)
            widget.GroupController.end()
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].value(True)

        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = Fl_Check_Button(widget.cord_x, widget.cord_y, widget.width, widget.height, widget.title)
            widget.controller.type(FL_TOGGLE_BUTTON)
            widget.controller.value(widget.value)

    
