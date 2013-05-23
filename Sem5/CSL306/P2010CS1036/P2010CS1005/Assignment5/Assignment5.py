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


''' WIDGETS: RadioButton '''
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




''' WIDGETS: ComboBox '''
class ComboBox(object):
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


''' WIDGETS: Password Box '''
class PasswordBox:
    controller = None
    callback = None
    Type= "Password"
    def __init__(self,text,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Entry(frame, show="*")
        self.controller.pack(fill=root.BOTH, expand=1)
        self.controller.insert(root.INSERT,text)

    def getText(self):
        return self.controller.get()

    def setText(self):
        self.controller.delete(1.0, root.END)
        return True
    

def Submit():
    newps1 = NewPstb.getText();
    newps2 = ReNewPstb.getText();
    if(IsValidPswd(newps1,newps2)):
        print (" Password Successfully Changed ! ");
    else:
        print (" Retry by Entering new Password!  ");
 





def IsValidPswd(newps1, newps2):
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










WindowPanel = myWindow('tkWindow by Aditya Gujral' ,50,50,350,250)
      
userLbl=Label("Name :",20,15,80,30,WindowPanel)
OldPswdLbl=Label("Old Password",20,50,140,30,WindowPanel)
NewPswdLbl=Label("New Password",20,85,160,30,WindowPanel)
ReNwPsLbl=Label("Repeat Password",20,120,160,30,WindowPanel)
usrtb=TextBox("",150,15,150,30,WindowPanel)
OldPstb=PasswordBox("",150,50,150,30,WindowPanel)
NewPstb=PasswordBox("",150,85,150,30,WindowPanel)
ReNewPstb=PasswordBox("",150,120,150,30,WindowPanel)
    
btn= Button("Submit",30,180,100,35,WindowPanel)    
btn.buttonListener(Submit)
      
if __name__ == '__main__':
    WindowPanel.show()
