from qtGUI import *
import sys
from PyQt4 import QtGui, QtCore


      
def Submit():
    newps1 = NewPstb.getText();
    newps2 = ReNewPstb.getText();
    if(validate(newps1,newps2)):
        #print ("Success !!!  Password Successfully Changed ! ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
    else:
        print ("Retry by Entering new Password!  ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
 

def validate(newps1, newps2):
    if newps1 != newps2:			#Checking whether the passwords match or not
       print("\nError !!!!!  Passwords Don't Match! Please Enter Again. ")
       return False
    
    if(len(newps1)<=6):              		 #checking the length of the password
       print("\nError !!!!!  Length of the password should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):            
        
        if(str(newps1).isalpha()):               #checking if entered password has only alphabets
            print("\nError !!!!!  Entered password containg only alphabets.Enter alphanumeric values")
            return False   
        
        elif(str(newps1).isdigit()):	         #checking if entered password has only numerals
            print("\nError !!!!!  Entered password containg only numeral.Enter alphanumeric values")
            return False
        
        else :	
	    print ("\nSuccess  !!!  Password Successfully Changed ! ");	
            return True
    else:					#Checking for special characters                                         
       print ("\nError !!!!!  Special characters are not allowed.Enter only alphamueric values ");
       return False


if __name__ == '__main__':
   
	   
	canvas = Main_Window(1, 'Change Password' ,600,350)
	userLbl =    LabelText("Username         ",20,40,120,30)
	usrtb = TextField("",160,40,300,25)

	canvas.add_widget(userLbl)
	canvas.add_widget(usrtb)
	OldPswdLbl = LabelText("Current Password ",20,100,120,30)
	OldPstb= TextFieldPass("",160,100,300,25)

	canvas.add_widget(OldPswdLbl)
	canvas.add_widget(OldPstb)
	NewPswdLbl = LabelText("New Password     ",20,160,120,30)
	NewPstb= TextFieldPass("",160,160,300,25)

	canvas.add_widget(NewPswdLbl)
	canvas.add_widget(NewPstb)
	label =      LabelText("ConfirmPassword   ",20,220,120,30)
	ReNewPstb = TextFieldPass("",160,220,300,25)

	canvas.add_widget(label)
	canvas.add_widget(ReNewPstb)
	btn= Button("Register",235,280,120,30)

	btn.on_click(Submit)
	canvas.add_widget(btn)

	canvas.show()
