#xGUI.py
#Wrapper Class for All GUI module
#author : Arinkverma
import xGUIBase as base

class xGUI:
    def __init__(self, Environment = "wx"): 
        if(Environment == "wx"):
            #By ArinkVerma p2009cs1017
            temp = __import__('AnyGUI', globals(), locals(), ['wxGUI'], -1)
            LoadedModule = temp.wxGUI
        elif(Environment == "fltk"):
            #By KamalDeep p2009cs1011
            temp = __import__('AnyGUI', globals(), locals(), ['fltkGUI'], -1)
            LoadedModule = temp.fltkGUI
        elif(Environment == "tk"):
            #By Pravesh p2009cs1001
            temp = __import__('AnyGUI', globals(), locals(), ['tkGUI'], -1)
            LoadedModule = temp.tkGUI
        elif(Environment == "gtk"):
            #By Gaurav p2009cs1019
            temp = __import__('AnyGUI', globals(), locals(), ['gtkGUI'], -1)
            LoadedModule = temp.gtkGUI
        elif(Environment == "qt"):
            #By Prateek p2009cs1002
            temp = __import__('AnyGUI', globals(), locals(), ['qtGUI'], -1)
            LoadedModule = temp.qtGUI
            
        try:
            Canvas.__bases__ = (getattr(LoadedModule, 'Canvas'),)     
            ValueList.__bases__ = (getattr(LoadedModule, 'ValueList'),)
            CheckBox.__bases__ = (getattr(LoadedModule, 'CheckBox'),)
            RadioGroup.__bases__ = (getattr(LoadedModule, 'RadioGroup'),)
            TextArea.__bases__ = (getattr(LoadedModule, 'TextArea'),)
            Button.__bases__ = (getattr(LoadedModule, 'Button'),)
            TextField.__bases__ = (getattr(LoadedModule, 'TextField'),)
            LabelText.__bases__ = (getattr(LoadedModule, 'LabelText'),)
            Slider.__bases__ = (getattr(LoadedModule, 'Slider'),)
            Dialog.__bases__ = (getattr(LoadedModule, 'Dialog'),)
        except AttributeError:
            print "Error"

class Canvas(base.Canvas):pass

class ValueList(base.ValueList):pass

class CheckBox(base.CheckBox):pass

class RadioGroup(base.RadioGroup):pass

class TextArea(base.TextArea):pass

class Button(base.Button):pass

class TextField(base.TextField):pass

class LabelText(base.LabelText):pass

class Dialog(base.Dialog):pass

class Slider(base.Slider):pass
