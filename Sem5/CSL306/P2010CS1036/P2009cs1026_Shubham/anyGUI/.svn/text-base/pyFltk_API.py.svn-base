#########################################################
####    Standard PyFltk API for different widgets    ####
#########################################################

import fltk

def quit_action(widget):     
    import sys
    sys.exit(0)

def submit_action(win, text):
    fltk.fl_message(text)

# starts the main loop    
def run_app():
    return fltk.Fl.run()

def print_console(widg, data):
    print data

# returns a dialog echoing passed text
def py_dialog(text):
    return fltk.fl_message(text)
          
# returns a window with specified size
class Py_Window(fltk.Fl_Window):
    def __init__(self, width = 100, height = 100, label = "pyFltk Window") :
        super(Py_Window, self).__init__(width, height, label)
    def add_Py_Widgets(self, *widgets):
        for wid in widgets :
            self.add(wid.widget)
    def remove_Py_Widgets(self, *widgets):
        for wid in widgets :
            self.remove(wid.widget)
        self.redraw()
    def help_cb(self, widget, data):								# show the help dialog
        if (self.help_dialog_ == None) :
            self.help_dialog_ = fltk.Fl_Help_Dialog()
            self.help_dialog_.value(data)
        else :
            self.help_dialog_.value(data)      
        self.help_dialog_.show()
    def finish(self):                               				# Finishes creation of window                              
        self.show()

# return a specific Input-box .
class Py_Input() :
    
    def __init__( self, pos_X, pos_Y, width, height, label = "", type = "normal") :
        if type == "normal" or type == "N" :
            self.widget = fltk.Fl_Input(pos_X, pos_Y, width, height, label)
        elif type == "int" or type == "I" :
            self.widget = fltk.Fl_Int_Input(pos_X, pos_Y, width, height, label)
        elif type == "float" or type == "F" :
            self.widget = fltk.Fl_Float_Input(pos_X, pos_Y, width, height, label)
        elif type == "secret" or type == "S" :
            self.widget = fltk.Fl_Secret_Input(pos_X, pos_Y, width, height, label)
        elif type == "multiline" or type == "M" :
            self.widget = fltk.Fl_Multiline_Input(pos_X, pos_Y, width, height, label)
        else :
            return None
    def set_Text(self, text) :
        self.widget.insert(text)
    def getValue(self):
        return self.widget.value()    
    def action_listener(self, *args):
        self.widget.callback(*args)
           
class Py_Button():
    def action_listener(self, *args):
        self.widget.callback(*args)
    def customize(self):
        self.widget.box(fltk.FL_PLASTIC_UP_BOX)
        self.widget.color(fltk.FL_GREEN)
    def __init__(self, x, y, w, h, label = "button") :
        self.widget = fltk.Fl_Button(x, y, w, h, label)
        self.customize()
        
class Py_CheckBox():

    def __init__(self, x, y, w, h, label = "check") :
        self.widget = fltk.Fl_Check_Button(x, y, w, h, label)
        self.widget.down_box(fltk.FL_DOWN_BOX)
    def getValue(self):
        return self.widget.value()
    def action_listener(self, *args):
        self.widget.callback(*args)

class Py_RadioButton() :
    
    def __init__(self, x, y, w, h, label = "choose") :
        self.widget = fltk.Fl_Round_Button(x, y, w, h, label)
        self.widget.type(102)
    def getValue(self):
        return self.widget.value()
    def action_listener(self, *args):
        self.widget.callback(*args)
        
class Py_list_Values() :
    
    def __init__(self, x, y, w, h, choices, label):
        self.choices = choices
        self.widget = fltk.Fl_Choice(x, y, w, h, label)
        self.widget.copy(choices)
    def action_listener(self, *args):
        self.widget.callback(*args)

class Py_Menu_bar():
    def __init__(self, x, y, width, height, table):
        self.widget = fltk.Fl_Menu_Bar(x, y, width, height)
        self.widget.copy(table)
    def action_listener(self, *args):
        self.widget.callback(*args)
    
class Py_Slider():
    def __init__(self, x, y, width, height, type = "slide" ):
        if type == "slide" :
            self.widget = fltk.Fl_Scrollbar(x, y, width, height)
        elif type == "nice" :
            self.widget = fltk.Fl_Nice_Slider(x, y, width, height)
        elif type == "fill" :
            self.widget = fltk.Fl_Fill_Slider(x, y, width, height)
        elif type == "h_fill" :
            self.widget = fltk.Fl_Hor_Fill_Slider(x, y, width, height)
        else :
            self.widget = None
    def action_listener(self, *args):
        self.widget.callback(*args)

def main():
    xpos, ypos = 20, 20
    
    # create main window
    win = Py_Window( 500, 500, " Registration Form ")

    # input boxes        
    name = Py_Input( xpos + 60, ypos + 20, 250, 30, " Name : " )
    name.set_Text( "e.g. SHUBHAM KUMAR" )
    college = Py_Input( xpos + 60, ypos + 60 , 250, 30, "College :" )
    college.set_Text("e.g. IIT ROPAR")
    win.add_Py_Widgets(name, college)

    # radio buttons 
    g1 = Py_RadioButton( xpos + 100 , ypos + 120, 100, 20, " Male ")
    g2 = Py_RadioButton( xpos + 220 , ypos + 120, 100, 20, " Female ")
    win.add_Py_Widgets(g1, g2)

    # check boxes
    cbox1 = Py_CheckBox(xpos + 60, ypos + 275, 80, 15, " Research ")
    cbox2 = Py_CheckBox(xpos + 60, ypos + 305, 80, 15, " Job ")
    cbox3 = Py_CheckBox(xpos + 60, ypos + 335, 70, 15, " others:")
    win.add_Py_Widgets(cbox1, cbox2)

    # Buttons
    submit = Py_Button(xpos + 60, ypos + 400, 80, 40, "Submit")
    quit = Py_Button(xpos + 220, ypos + 400, 80, 40, "Quit")
    quit.action_listener(quit_action)
    win.add_Py_Widgets(submit, quit)

    # list of choices
    choices = ( ("select", ), ("CSE",), ("EE",), ("Others",), (None,) )
    choice_list = Py_list_Values(xpos + 150, ypos + 200, 150, 25, choices, "Branch  ")
    win.add_Py_Widgets(choice_list)
       
	# finishes creation of window
    win.finish()
    run_app()

if __name__=='__main__' :
     main()                                                   # run Fltk event loop
    