
import gtk

class myWindow(object):
    parent = None
    def __init__(self, title,X,Y,width,height):
        id = None
        #Initialize the Widget
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        # Create a Fixed Container
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()


    def show(self):
        self.window.show()
        gtk.main()
        return

    def close(self):pass




class TextBox(object):
    instance = None
    buffer = gtk.TextBuffer()
    def __init__(self,title,X,Y,width,height,cntrl):
        self.instance = gtk.TextView(self.buffer)
        self.instance.set_size_request(width,height) 
        cntrl.fixed.put(self.instance, X, Y)            
        self.instance.show()

    def setText(self,text):
        self.buffer.set_text(text)
        return True

    def appendText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True

class Button(object):
    
    def __init__(self,title,X,Y,width,height,cntrl):
        self.instance = gtk.Button(title)
        self.instance.set_size_request(width,height)
        cntrl.fixed.put(self.instance,X,Y)            
        self.instance.show()
        
	def buttonListener(self,method):   
		self.instance.connect("clicked",method)
		return True
                
                ''' WIDGETS: LabelText '''
class Label(object):
    def __init__(self,text,X,Y,width,height,cntrl):
        self.instance = gtk.Label(text)
        cntrl.fixed.put(self.instance, X, Y)   
        self.instance.set_size_request(width,height)         
        self.instance.show()


''' WIDGETS: MyRadioGroup '''
class ButtonGroup(object):
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
class RadioButton(object):
    controller = None
    def __init__(self,title,X,Y,width,height,cntrl):
        self.controller = gtk.RadioButton(None, title)
        self.controller.set_size_request(width,height)
        self.controller.set_active(False)
        cntrl.fixed.put(self.controller,X,Y)
        self.controller.show()

    def setChecked(self,value):
        self.controller.set_active(value)

    def isChecked(self):
        return self.controller.GetValue()
        
class CheckBox(object):
	controller = None
	value=False
	def __init__(self,title,X,Y,width,height,cntrl):
		self.controller = gtk.CheckButton(title)
		self.controller.set_size_request(width,height)
		cntrl.fixed.put(self.controller, X,Y)
		self.controller.show()
		self.controller.set_active(self.value)
	
	
	def setCheckState(self,value):   #True or False for checked
		self.controller.set_active(value)
            
	def get_state(self):
		self.controller.get_active()	
		    
'''
class ListBox(object):
	controller=None
	instance=None
	def __init__(self,title,X,Y,width,height,cntrl):
		self.controller = gtk.OptionMenu()
            self.controller.set_size_request(width,height)
			menu = gtk.Menu()
			for name in widget.choices:
				item = gtk.MenuItem(name)
				item.show()
				menu.append(item)
				#print "gis"
			widget.controller.set_menu(menu)
			widget.controller.show()
			self.fixed.put(widget.controller,widget.position_X, widget.position_Y)

	def on_changed(self,value):
		self.controller.set_label(self.get_active_text()) 

'''
#class Slider(object):
	#controller=None
	#def __init__(self,X,Y,width,height,cntrl):
		#self.controller = gtk.HScale()
        #self.controller.set_range(0, 100)
        #self.controller.set_increments(1, 10)
        #self.controller.set_digits(0)
        #self.controller.set_size_request(width, height)
        #self.controller.connect("value-changed", self.on_changed)
        #cntrl.fixed.put(sacle.controller, X, Y)
        
        #self.controller.show()
		
	#def setRange(self,start,end):
		#self.controller.set_range(start,end)
	
		
	#def getValue(self):
		#self.controller.get()
		
class Calendar(object):
	controller=None
	widget=None
	def __init__(self,X,Y,width,height,cntrl):
		   self.controller=gtk.Calendar()
		   cntrl.fixed.put(self.controller, X, Y)
		   print "fu"
		   self.controller.connect("day_selected", self.on_day_selected)
		   #cntrl.fix.put(self.label, 40, 230)
		   self.controller.show()
		   
	def on_day_selected(self, widget):
		(year, month, day) = widget.get_date()
		self.label.set_label(str(month) + "/" + str(day) + "/" + str(year))
		   



        
    
WindowPanel = myWindow('wxWindow by Abhisaar Sharma' ,50,50,350,250)
      
userLbl=Label("Name :",20,15,80,30,WindowPanel)
OldPswdLbl=Label("Old Password",20,50,140,30,WindowPanel)
NewPswdLbl=Label("New Password",20,85,160,30,WindowPanel)
ReNwPsLbl=Label("Repeat Password",20,120,160,30,WindowPanel)
usrtb=TextBox("",150,15,150,30,WindowPanel)
#OldPstb=PasswordBox("",150,50,150,30,WindowPanel)
#NewPstb=PasswordBox("",150,85,150,30,WindowPanel)
#ReNewPstb=PasswordBox("",150,120,150,30,WindowPanel)
    
btn= Button("Submit",30,180,100,35,WindowPanel)    
#btn.buttonListener(Submit)
      
#sld1=Slider(300,350,180,20,WindowPanel)
#sld1.setRange(0,10)

cal1=Calendar(240,140,240,140,WindowPanel) 
if __name__ == '__main__':
    WindowPanel.show()

'''
    #Functions bind to button events
    def SubmitButtonClick(event):
        report = " Your city is "+ valuelist.get_state()+"\n"
        if(checkbox1.get_state()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"

        if(checkbox2.get_state()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"

        report = report + " you are "+rb1.get_state()+"\n"
        report = report + " you need "+rb2.get_state()+"\n"

        textarea.appendText("_______________________\n"+report+"\n\n")
        return True 

    def AboutButtonClick(event):
        textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
        return True


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
       
    #Textbox
    tb=TextBox(" dfsf ",100,15,150,30,WindowPanel)
    Listlbl=Label("Your Favourite Animal",280,30,160,60,WindowPanel)
    #Buttons
    btn= Button("Print On Console",30,320,150,150,WindowPanel)
    #btn.buttonListener(call_method)
    
    
    
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
    
    rb4.setChecked(False)
    
    
    #sld1=Slider(300,350,180,20,WindowPanel)
    #sld1.setRange(0,10)
    myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightingale"]
    #listBox=ListBox("fuck off",250,80,180,190,WindowPanel)
    
    #listBox.addItems(myList)
    cal1=Calendar(240,140,240,140,WindowPanel)
    WindowPanel.show()
    
'''
