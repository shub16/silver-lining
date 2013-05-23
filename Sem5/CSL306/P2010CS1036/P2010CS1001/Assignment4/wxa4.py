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



''' ---SAMPLE--- '''

if __name__ == '__main__':

        def call_method(event):
            print ("\n Your Entered Data \n");
            print ("****************************\n")
            print ("Your Name :  "+ tb.getText());
         #   print ("Your Favourite Tool-Kit is :  "+rbgrp.getValue())
            if(ck1.getCheckState()==True):
			   print ("You Love Animals")
            if(ck2.getCheckState()==True):
               print("You Love Birds")
            print("Your Favourite Animal is : "+ listBox.Selected());
			
			
        def exit_method(event):
            print 'wxPython window made by Abhisaar Sharma'
            return
        
        
        WindowPanel = myWindow('wxPython Window By Abhisaar Sharma' ,50,50,450,400)
        
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
        
        rb1.setChecked(True)
        
        #Textbox
        tb=TextBox("  ",100,15,150,30,WindowPanel)
        
        #Listbox
        listBox=ListBox("Choose Animal",250,80,180,190,WindowPanel)
        myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightingale"]
        listBox.addItems(myList)
        
        
        Exit_btn= Button("Info",260,320,150,50,WindowPanel)
        Exit_btn.buttonListener(exit_method)
        WindowPanel.show()
