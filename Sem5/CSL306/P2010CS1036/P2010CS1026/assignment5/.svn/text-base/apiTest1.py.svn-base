import sys
from PyQt4 import QtGui, QtCore

class Frame(QtGui.QWidget):
		par= None
		def __init__(self, title,length,breadth):
			 self.app = QtGui.QApplication(sys.argv)
			 super(Frame,self).__init__()
			 self.text=title
			 self.width=length
			 self.height=breadth
			 
			 
class Dashboard(object):
		frame=None
		def __init__(self,title,length,breadth):
			self.frame=Frame(title,length,breadth)
		
		def Display(self, choice = True):
			self.frame.setGeometry(self.frame.width, self.frame.height, self.frame.width, self.frame.height)   #setting the window geometry
			self.frame.setWindowTitle(self.frame.text)
			if( choice):
				self.frame.show()
			else:
				self.frame.close()
			sys.exit(self.frame.app.exec_())
		
		def Add(self,widget):					#for adding a widget on a window 
			WidType = type(widget)	
			if(WidType==Check_box or isinstance(widget,Check_box)):
           			 widget.control = QtGui.QCheckBox(widget.title, self.frame)
           			 widget.control.setChecked(widget.value)
            			 widget.control.resize(widget.width, widget.height)    
            			 widget.control.move(widget.position_X, widget.position_Y)
            			 		
		    	elif(WidType==Create_button or isinstance(widget,Create_button)):
				widget.control = QtGui.QPushButton(widget.text,self.frame)
				widget.control.resize(widget.width, widget.height)    
                    	        widget.control.move(widget.position_X, widget.position_Y)
				if(widget.callBackMethod is not None):
               			  widget.control.clicked.connect(widget.callBackMethod)
               			  
                        elif(WidType==Drop_list or isinstance(widget,Drop_list)):
         			   widget.control = QtGui.QComboBox(self.frame)
           			   widget.control.addItem(widget.value)
            			   for i in range(0,len(widget.choices)):
             				   widget.control.addItem(widget.choices[i])
            			   widget.control.resize(widget.width, widget.height)    
            			   widget.control.move(widget.position_X, widget.position_Y)
            			   
            		elif(WidType==Radio_button or isinstance(widget,Radio_button)):
         			   widget.groupBox = QtGui.QGroupBox("", self.frame)
            			   widget.control = []
            			   radio_control = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
          			   widget.groupBox.move(widget.position_X[0], widget.position_Y[0])
            
                                   radio_control.resize(widget.width, widget.height)
            			   radio_control.move(0, 0)
            			   widget.control.append(radio_control)
          			   for i in range(1,len(widget.labels)):
                			radio_control = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                			radio_control.resize(widget.width, widget.height)
                			radio_control.move(widget.position_X[i]-widget.position_X[0], widget.position_Y[i]-widget.position_Y[0])
                			widget.control.append(radio_control)
            			   if(widget.selectPosition != None):
                                         widget.control[widget.selectPosition].setChecked(True)
                                         
                        elif(WidType==Text_area or isinstance(widget,Text_area)):
           				 widget.control = QtGui.QTextEdit(widget.text,self.frame)
        			         widget.control.resize(widget.width, widget.height)    
            				 widget.control.move(widget.position_X, widget.position_Y)
            				
            		elif(WidType==Text_field or isinstance(widget,Text_field)):
           				 widget.control = QtGui.QLineEdit(widget.text,self.frame)
        			         widget.control.resize(widget.width, widget.height)    
            				 widget.control.move(widget.position_X, widget.position_Y)
            				 
            		elif(WidType==Password_field or isinstance(widget,Password_field)):
           				 widget.control = QtGui.QLineEdit(widget.text,self.frame)
        			         widget.control.resize(widget.width, widget.height)    
            				 widget.control.move(widget.position_X, widget.position_Y)		 
            				 widget.control.setEchoMode(QtGui.QLineEdit.Password)
            				 
            		elif(WidType==Static_text or isinstance(widget,Static_text)):
           				 widget.control = QtGui.QLabel(widget.text,self.frame)
        			         widget.control.resize(widget.width, widget.height)    
            				 widget.control.move(widget.position_X, widget.position_Y)
            				 
            		elif(WidType==Spin_list or isinstance(widget,Spin_list)):
           				 widget.control = QtGui.QSpinBox(self.frame)  
           				 widget.control.setMinimum(widget.min)
           				 widget.control.setMaximum(widget.max)
           				 widget.control.resize(widget.width, widget.height) 
            				 widget.control.move(widget.position_X, widget.position_Y)		 
               		
    				
     
#class creating Button 			
class Create_button(object):
	control = None
	callBackMethod = None
	def __init__(self,posX,posY,title="MyButton",length=100,breadth=30):
	        self.text = title
	        self.position_X = posX
	        self.position_Y = posY
	        self.width = length
	        self.height = breadth


	def Click_listener(self,method):			#function for clicked Button Event
		if(self.control == None):
			self.callBackMethod = method
		else:
        	      self.control.clicked.connect(method)
        	return True
        	
#class creating CheckBox
class Check_box(object):
	control=None
	callBackMethod = None
	value=True
        def __init__(self,posX,posY,title,length,breadth):
       	 self.title = title
       	 self.position_X = posX
       	 self.position_Y = posY
       	 self.width = length
       	 self.height = breadth
       	 
	def Set_checked(self,value=True):
		if(self.control==None):
			self.value=value
		else:
			 self.control.setChecked(value)		
		
	def Is_checked(self):
		if(self.control == None):
                    return self.value
                else:
                    return self.control.isChecked()		
 
#class for creating List		
class Drop_list(object):
		control=None
		def __init__(self,posX,posY,name1,values,length="100",breadth="27"):
                    self.position_X = posX
                    self.position_Y = posY
                    self.width = length
                    self.height = breadth
                    self.choices=values
                    self.value=name1
       	
           	def Get_value(self):
           	      if(self.control == None):
                     	return self.value
    	              else:
                     	return self.choices[self.control.currentIndex() - 1]
                    	
#class for creating radioButton
class Radio_button(object):
		control =None
		selectPosition=None
		def __init__(self,label1,posX,posY):
			self.position_X=[]
			self.position_Y=[]
			self.labels = []
			self.width = 100
			self.height = 30
			self.Add_radio_button(label1,posX,posY)
			
		def Add_radio_button(self,label,posX,posY):
		            self.labels.append(label)
		            self.position_X.append(posX)
		            self.position_Y.append(posY)
		            return True
		
		def Get_selected(self):
	                for i in range(len(self.control)):
	                    if(self.control[i].isChecked()):
	                        return self.labels[i]
	                return None			
	               
                		
 #class for creating TextArea               		
class Text_area(object):
    control = None
    callback = None
    def __init__(self,posX,posY,length=300,breadth=200,text=""):
        self.text = text
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_text(self,text):
        if(self.control == None):
            self.text = text
        else:
            self.control.setText(text)
        return True
	
    def Get_text(self):
    	if(self.control == None):
            return ' '
        else:
        	return   self.control.toPlainText()
        
    def Append_text(self,text):
        if(self.control == None):
            self.text = self.text+text
        else:
            self.text = self.control.toPlainText() + text
            self.control.setText(self.text)
        return True              

    def Clear_area(self):
        if(self.control == None):
            self.text = ""
        else:
            self.control.setText("")
        return True
	 		        	
 #class for TextField       		        	
class Text_field(object): 
    control = None
    callback = None
    def __init__(self,posX,posY,text="",length=250,breadth=25):
        self.text = text
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_text(self,text):
        if(self.control == None):
            self.text = text
        else:
            self.control.setText(text)
        return True
      
    def Get_text(self):
        if(self.control == None):
            return ' '
        else:
        	return   self.control.text()           


    def Clear_field(self):
         if(self.control == None):
            self.text = ""
         else:
            self.control.setText("")
         return True
	     		        	
#creating class for Label 
class Static_text(object):
	control=None
	value=False
	def __init__(self,posX,posY,length=150,breadth=30,text=""):
	         self.text=text
                 self.position_X = posX
                 self.position_Y = posY
                 self.width = length
                 self.height = breadth
                 
        def Set_value(self,text):
		if(self.control==None):
			self.value=text
		
#class of password field                
class Password_field(object): 
    control = None
    callback = None
    def __init__(self,posX,posY,text="",length=200,breadth=25):
        self.text = text
        self.position_X = posX
        self.position_Y = posY
        self.width = length
        self.height = breadth

    def Set_text(self,text):
        if(self.control == None):
            self.text = text
        else:
            self.control.setText(text)
        return True
      
    def Get_text(self):
        if(self.control == None):
            return ' '
        else:
        	return   self.control.text()            

    def Clear_field(self):
         if(self.control == None):
            self.text = ""
         else:
            self.control.setText("")
         return True
	     		         	       		        	
#class for spinlist
class Spin_list:
	control = None
	def __init__(self,positionX,positionY,length=100,breadth=25,minimum=0,maximum=100):
              self.position_X = positionX
              self.position_Y = positionY
              self.min=minimum
              self.max=maximum
              self.width = length
              self.height = breadth
        def Get_value(self):
      		if(self.control ==None):
      			return ' '
		else :
			return self.control.value()       	
       	       
         #def  Get_value()    #get value
       	      		        									

		
			

#--------------------------------------------------UNIT Test Demonstration--------------------------------#

def Check(self):					#Checks if the password is set satisfactorily
    password1 = NewPassEntry.Get_text();
    password2 = ReNewPassEntry.Get_text();
    if(Is_valid_pass(password1,password2)):		#calls Is_valid_pass
        print ("Password Successfully Changed ! ");
        OldPassEntry.Clear_field();
        NewPassEntry.Clear_field();
        ReNewPassEntry.Clear_field();
    else:
        print ("Retry by Entering new Password!  ");
        OldPassEntry.Clear_field();
        NewPassEntry.Clear_field();
        ReNewPassEntry.Clear_field();
 

def Is_valid_pass(pass1, pass2):		#Checks if the passwords satisfy all the criteria
    if pass1 != pass2:
       print("Error in Password! --> Passwords do not match! ")
       return False
    
    if(len(pass1)<=6):               # Check the length of the password
       print("Error in Password! --> Password Length should be more than 6. ")
       return False    
    
    if(str(pass1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(pass1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print("Error in Password!--> Password cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(pass1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print("Error in Password!--> Password cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            print ("Password Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print ("Error in Password!--> Password should contain only alphabets and digits.");
       return False


#----------------Unit Test Window------------------------------------------------------------------
#------------------Creates a Login Window-------------------------------------------------------
OuterPanel = Dashboard("Unit Test",400, 300)
NameLabel = Static_text( 15, 30, 80, 30,  "Name :")
OuterPanel.Add(NameLabel)
OldPassLabel = Static_text( 10, 75,140, 30, "Old Password :",)
OuterPanel.Add(OldPassLabel)
NewPassLabel = Static_text( 4, 120,160, 30, "New Password :",)
OuterPanel.Add(NewPassLabel)
ReTypeLabel = Static_text( 14, 170, 160, 30, "Re-Type Password :")
OuterPanel.Add(ReTypeLabel)
NameEntry = Text_field(180, 30, "", 150, 30)
OuterPanel.Add(NameEntry)
OldPassEntry = Password_field(180, 75, "", 150, 30)
OuterPanel.Add(OldPassEntry)
NewPassEntry = Password_field(180, 120, "", 150, 30)
OuterPanel.Add(NewPassEntry)
ReNewPassEntry = Password_field(180, 170, "", 150, 30)
OuterPanel.Add(ReNewPassEntry)
SubmitButton = Create_button(150, 230, "Log In", 100, 35)
OuterPanel.Add(SubmitButton)
SubmitButton.Click_listener(Check) 
if __name__ == '__main__':
    OuterPanel.Display()
