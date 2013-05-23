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
		
		def Display(self):
			self.frame.setGeometry(self.frame.width, self.frame.height, self.frame.width, self.frame.height)   #setting the window geometry
			self.frame.setWindowTitle(self.frame.text)
			self.frame.show()
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
               			  
                      
            			   
            		elif(WidType==RadioButton or isinstance(widget,RadioButton)):
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
        	      self.control.clicked.connect()
        	return True
        	
#class creating CheckBox
class Check_box(object):
	control=None
	callBackMethod = None
	value=False
        def __init__(self,posX,posY,title,length,breadth):
       	 self.title = title
       	 self.position_X = posX
       	 self.position_Y = posY
       	 self.width = length
       	 self.height = breadth
       	 
	def Set_value(self,value):
		if(self.control==None):
			self.value=value
		else:
			 self.control.setChecked(value)		
		
	def Get_value(self):
		if(self.control == None):
                    return self.value
                else:
                    return self.control.isChecked()		

                    	
#class for creating radioButton
class RadioButton(object):
		control =None
		selectPosition=None
		def __init__(self,length,breadth):
			self.position_X=[]
			self.position_Y=[]
			self.labels = []
			self.width = length
			self.height = breadth
			
		def addRadioButton(self,label,X,Y):
		            self.labels.append(label)
		            self.position_X.append(X)
		            self.position_Y.append(Y)
		            return True
		
		def Get_value(self):
	                for i in range(len(self.control)):
	                    if(self.control[i].isChecked()):
	                        return self.labels[i]
	                return None			
	                
		def setButtonTrue(self,pos):
           		 if(self.control == None):
                		self.selectPosition = pos
            		 else:
                		button_controller = self.control[pos]
                		button_controller.setChecked(True)	
                		
 #class for creating TextArea               		
class Text_area(object):
    control = None
    callback = None
    def __init__(self,posX,posY,length,breadth,text):
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
	
    def Get_text(self,text):
        return self.text  
        
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
    def __init__(self,positionX,positionY,text="",length=250,breadth=25):
        self.text = text
        self.position_X = positionX
        self.position_Y = positionY
        self.width = length
        self.height = breadth

    def Set_text(self,text):
        if(self.control == None):
            self.text = text
        else:
            self.control.setText(text)
        return True
      
    def Get_text(self,text):
    	print text
        return self.text              


    def Clear_field(self):
         if(self.control == None):
            self.text = text
         else:
            self.control.setText(text)
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
                 
        def Set_value(self,value):
		if(self.control==None):
			self.value=value
		
#class of password field                
class Password_field(object): 
    control = None
    callback = None
    def __init__(self,positionX,positionY,text="",length=200,breadth=25):
        self.text = text
        self.position_X = positionX
        self.position_Y = positionY
        self.width = length
        self.height = breadth

    def Set_text(self,text):
        if(self.control == None):
            self.text = text
        else:
            self.control.setText(text)
        return True
      
    def Get_text(self,text):
    	print text
        return self.text              


    def Clear_field(self):
         if(self.control == None):
            self.text = text
         else:
            self.control.setText(text)
         return True
	     		         	       		        	
        		        									
if __name__ == '__main__':
	
	
	def Submit(event=None):
     		   text = "hii"
                   if(checkbox1.Get_value()):
                       text = text + " you like  Cricket\n"
                   else:
            	       text = text + " you don't like Cricket\n"
    
                   if(checkbox2.Get_value()):
            		text = text + " you like Football\n"
            	   else:
            		text = text + "  you  don't like Football\n"
            		
            	   if(checkbox3.Get_value()):
            		text = text + " you like Tennis\n"
        	   else:
            		text = text + "  you  don't like Tennis\n"
    
                   text = text + " your sex is  "+rb1.Get_value()+"\n"
        	   #text = text + " your sex is  "+rb1.getValue()+"\n"
    
        	   textarea.Append_text("\n*************************\n"+text+"\n\n")
        	   return True 
	
	
	
	frame = Dashboard( 'Naveen Qt4' ,550,300)
	checkbox1 = Check_box(10,45,"Cricket",215,15)
    	checkbox2 = Check_box(10,70,"Football",215,15)
    	checkbox3 = Check_box(10,95,"Tennis",215,15)
    	submitBtn = Create_button(130,230,"Submit",120,30)
    	submitBtn.Click_listener(Submit)
    	frame.Add(checkbox1)
    	frame.Add(checkbox2)
    	frame.Add(checkbox3)
    	frame.Add(submitBtn)
    
    	rb1 = RadioButton(100,50)
   	rb1.addRadioButton("Male",10,160)
    	rb1.addRadioButton("Female ",110,160)
    	rb1.setButtonTrue(0)
    	frame.Add(rb1)
    	textarea = Text_area(250,10,150,100," Click submit button")
    	password = Password_field(300,230)
    	textfield=Text_field(300,260)
    	lb=Static_text(280,200,100,20,"naveen")
    	frame.Add(lb)
    	textarea.Clear_area()
        frame.Add(textarea)
        frame.Add(password)
        frame.Add(textfield)
	frame.Display()
		
			
