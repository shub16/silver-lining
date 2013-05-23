import wx

class myWindow(wx.Frame):
    parent = None
    def __init__(self,title,X,Y,width,height):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, 1, title, (X,Y),wx.Size(width, height))
        self.panel = wx.Panel(self, -1)

    def show(self):
        self.Show(True)
        self.Centre()
        self.app.MainLoop()
        return
    
    def close(self):
        self.Close()
            
''' WIDGETS: TextBox '''
class TextBox(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height,cntrl):
        self.controller=wx.TextCtrl(cntrl.panel, -1, text,  (X,Y), wx.Size(width, height) , style=wx.TE_MULTILINE)
    
    
    def setText(self,text):
        self.controller.SetValue(text)
        return True
    
    def getText(self):
        return self.controller.GetValue()
        
''' WIDGETS: PasswordBox '''
class PasswordBox(wx.TextCtrl):
    controller = None
    def __init__(self,text,X,Y,width,height,cntrl):
        self.controller=wx.TextCtrl(cntrl.panel, -1, text,  (X,Y), wx.Size(width, height) , style=wx.TE_PASSWORD)
    
    def setText(self,text):
        self.controller.SetValue(text)
        return True
    
    def getText(self):
        return self.controller.GetValue()

''' WIDGETS: LABEL '''
class Label(wx.StaticText):
    def __init__(self,text,X,Y,width,height,cntrl):
        wx.StaticText(cntrl.panel, -1,text,(X,Y),wx.Size(width,height))
  

''' WIDGETS: Button '''
class Button(wx.Button):
    controller = None
    def __init__(self,title,X,Y,width,height,cntrl):
        self.controller=wx.Button(cntrl.panel, -1, title, (X,Y), wx.Size(width,height) )
            
    def buttonListener(self,method):
        self.controller.Bind(wx.EVT_BUTTON, method)
        
''' WIDGETS: CheckBox '''
class CheckBox(wx.CheckBox):
    controller = None
    def __init__(self,title,X,Y,width,height,cntrl):
        self.controller=wx.CheckBox(cntrl.panel, -1, title, (X,Y),wx.Size(width, height))
    
    def setCheckState(self,value):
        self.controller.SetValue(value)
           
    def getCheckState(self):
        return self.controller.IsChecked()


''' WIDGETS: MyRadioGroup '''
class ButtonGroup(wx.RadioButton):
    controller = []
    cntrl = None
    selected_index = None
    
    def __init__(self,cntrl):
         self.cntrl = cntrl
           
    def addButtons(self,radiolist):
         for i in range(1,len(radiolist)):
               self.controller.append(radiolist[i])
        

    def getValue(self):
        for i in range(len(self.controller)):
            if(self.controller[i].GetValue()):
                return self.controller[i].label
        return None

''' WIDGETS: RadioButton '''
class RadioButton(wx.RadioButton):
    controller = None
    def __init__(self,title,X,Y,width,height,cntrl):
        self.controller=wx.RadioButton(cntrl.panel, -1, title, (X,Y),wx.Size(width, height))

    def setChecked(self,value):
        self.controller.SetValue(value)

    def isChecked(self):
        return self.controller.GetValue()

''' WIDGETS: ListBox '''
class ListBox(wx.ListBox):
     controller=None
     def __init__(self,value,X,Y,width,height,cntrl):
         self.controller=wx.ComboBox(cntrl.panel, -1,value,(X,Y),wx.Size(width,height),style=wx.CB_READONLY)
         
     def addItems(self,choices):
         self.controller.SetItems(choices)
         
     def Selected(self):
         return self.controller.GetValue()

       
def Submit(self):
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


        
        
        
        
WindowPanel = myWindow('wxWindow by Abhisaar Sharma' ,50,50,350,250)
      
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
