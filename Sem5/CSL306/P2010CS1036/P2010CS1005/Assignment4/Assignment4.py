
import tkMessageBox
import sys,os
import Tkinter as root
import Tkinter as tk
import time
import calendar

try:
    import Tkinter
    import tkFont
except ImportError: # py3k
    import tkinter as Tkinter
    import tkinter.font as tkFont

import ttk




class myWindow(object):
    window = None
    def __init__(self,title,X,Y,width,height):
        self.window = root.Tk()
        self.window.title(title)
        self.window.geometry('%dx%d+%d+%d' % (width, height, X, Y))
        
        
    def show(self):
        self.window.mainloop()
        return

        
''' WIDGETS: Button '''
class Button(object):
    controller = None
    callbackMethod = None
    Type = None
    def __init__(self,title,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Button(frame, text=title,command= self.callbackMethod)
        self.controller.pack(fill=root.BOTH, expand=1)

    def buttonListener(self,method):
        self.controller.config(command=method)
        

''' WIDGETS: TextArea '''
class TextBox(object):
    controller = None
    callback = None
    Type = None
    def __init__(self,text,X,Y,width,height,cntrl):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Text(frame)
        self.controller.pack(fill=root.BOTH, expand=1)
        self.controller.insert(root.INSERT,text)

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def setText(self,text):
        self.controller.delete(1.0, root.END)
        self.controller.insert(root.INSERT,text)


    def clear(self):
        self.controller.delete(1.0, root.END)
        return True


''' WIDGETS: Label '''
class Label(object):
    controller = None
    Type = None
    v=''
    label_var = 0
    def __init__(self,text,X,Y,width,height,cntrl):
        self.v=text
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Label(frame, text=self.v)
        self.controller.pack(fill=root.BOTH, expand=1)

    def setLabel(self,text):
        self.controller.config(text=text)






''' WIDGETS: CheckBox '''
class CheckBox(object):
    controller = None
    value = False
    Type = None
    def __init__(self,title,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.value=root.IntVar()
        self.controller = root.Checkbutton(frame, text=title,variable=self.value)
        #widget.controller.pack(fill=root.BOTH, expand=1)
        self.controller.grid(sticky=root.W)

    def setCheckState(self,value):
        if(value):
            self.controller.select()
        else:
            self.controller.deselect()

    def getCheckState(self):
        if(self.value.get()== 1):
            return True
        else:
            return False

 
''' WIDGETS: RadioGroup '''
class ButtonGroup(object):
    controller = []
    cntrl = None
    selected_index = None
    
    def __init__(self,cntrl):
         self.cntrl = cntrl
           
    def addButtons(self,radiolist):
         for i in range(1,len(radiolist)):
               self.controller.append(radiolist[i])


    def setButtonTrue(self,index):
        button_controller = self.controller[index]
        button_controller.select()
globalvar=0

class RadioButton(object):
    controller = None
    labels=""
    def __init__(self,title,X,Y,width,height,cntrl):
	V=root.IntVar()
        V=0
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        global globalvar
        self.controller= root.Radiobutton(frame, text=title,variable=V,value=globalvar)
	globalvar=globalvar+1
        self.controller.pack(fill=root.BOTH, expand=1)
        self.controller.grid(sticky=root.W)
        self.labels=title



    def isChecked(self):
        for i in range(len(self.controller)):
            if(self.value.get()==i):
                return self.labels[i]
        return None

    def setChecked(self,index):
        button_controller = self.controller[index]
        button_controller.select()




''' WIDGETS: ListBox '''
class ListBox(object):
    controller = None
    Type = None
    list_var = 0
    list_var = 1

    def __init__(self,title,value,X,Y,width,height,cntrl):
        array = ['']
        self.list_var = root.StringVar()
        self.list_var.set(value)
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.list_var1 = root.StringVar()
        array[0]=title
        array=array+value
        self.list_var1.set(array[0])

        self.controller = apply(root.OptionMenu, (frame, self.list_var1) + tuple(array))
        self.controller.pack(fill=root.BOTH, expand=1)


    def addItems(self,choices):
         self.controller.SetItems(choices)

    def Selected(self):
         return self.list_var1.get()







if __name__ == '__main__':

        def call_method():
            print ("\n Your Entered Data \n");
            print ("****************************\n")
            print ("Your Name :  "+ tb.getText());
         #   print ("Your Favourite Tool-Kit is :  "+rbgrp.getValue())
            if(ck1.getCheckState()==True):
			   print ("You Love Animals")
            if(ck2.getCheckState()==True):
               print("You Love Birds")
            print("Your Favourite Animal is : "+ listBox.Selected());
			
			
        def exit_method():
            print 'tkPython window made by Aditya Gujral'
            return
        
        
        WindowPanel = myWindow('wxPython Window By Aditya Gujral' ,50,50,450,400)
        
        #Labels
        nameLbl=Label("Your Name :",20,15,80,30,WindowPanel)
        toollbl=Label("Your Favourite Tool-Kit",15,100,140,40,WindowPanel)
        Listlbl=Label("Your Favourite Animal",280,30,160,60,WindowPanel)
        
        #Buttons
        btn= Button("Print On Console",30,320,150,50,WindowPanel)
        btn.buttonListener(call_method)
        
        #Checkboxes
        ck1=CheckBox("I Love Animals ",20,45,150,50,WindowPanel)
        ck1.setCheckState(0)
        ck2=CheckBox("I Love Birds ",150,45,150,50,WindowPanel)
        ck2.setCheckState(2)
        
        
        
        #Radios
        rbgrp=ButtonGroup(WindowPanel)
        
        rb1=RadioButton("PyQT4",10,140,100,20,WindowPanel)
        rb2=RadioButton("Wx-Python",10,160,100,20,WindowPanel)
        rb3=RadioButton("PyGTK",10,180,100,20,WindowPanel)
        rb4=RadioButton("Tkinter",10,200,100,20,WindowPanel)
        
        rlist=[rb1,rb2,rb3,rb4]
        rbgrp.addButtons(rlist)
        #Textbox
        tb=TextBox("",100,15,150,30,WindowPanel)
        
        #Listbox
        myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightingale"]
        listBox=ListBox("Choose Animal",myList,250,80,180,190,WindowPanel)
        
        
        Exit_btn= Button("Info",260,320,150,50,WindowPanel)
        Exit_btn.buttonListener(exit_method)
        WindowPanel.show()
