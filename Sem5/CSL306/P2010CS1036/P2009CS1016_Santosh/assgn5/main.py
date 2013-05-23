import sys,os
import PyQT4_API
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from functools import partial 

# function called when button is pushed
def Submit(widgets,self):
    newps1 = widgets[7].getText();
    newps2 = widgets[8].getText();
    if(IsValidPswd(newps1,newps2)):
        print (" Password Successfully Changed ! ");
        widgets[6].setText("");
        widgets[7].setText("");
        widgets[8].setText("");
	#   QtGui.QMessageBox.information(widgets[0], 'Information',"Password Successfully Changed !", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
    else:
        print (" Retry by Entering new Password!  ");
        widgets[6].setText("");
        widgets[7].setText("");
        widgets[8].setText("");
	  # QtGui.QMessageBox.information(widgets[0], 'Information',"Retry by Entering new Password!", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
    
 
    # call IsValidPswd to check the passwords
def IsValidPswd(newps1, newps2):
    if newps1 != newps2:
       print(" Password Error !  Passwords donot match! ")
       #QtGui.QMessageBox.critical(widgets[0], 'Password Error',"Passwords donot match!", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
       return False
    if(len(newps1)<=6):               # Check the length of the password
       print(" Password Error ! Password Length should be more than 6. ")
	   #QtGui.QMessageBox.critical(widgets[0], 'Password Error',"Password Length should be more than 6.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
       return False    
    if(str(newps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        if(str(newps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" Password Error ! Password cannot be only alphabet.Try combination! ")
			#QtGui.QMessageBox.critical(widgets[0], 'Password Error',"Password cannot be only digit or alphabet.Try combination!", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
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
'''
def call_metho(widgets):
            print ("\n Your Entered Datas \n\n");
            print ("****************************\n")
            print ("Your Name :  "+ widgets[6].getText());
            if(widgets[5].getChecked != -1):
			    print ("Your Favourite Tool-Kit is :  "+widgets[5].getValue())
            if(widgets[3].getCheckState()==True):
			   print ("You Love Animals")
            if(widgets[4].getCheckState()==True):
               print("You Love Birds")
            print("Your Favourite Animal is : "+ widgets[7].Selected());
			
'''		
def exit_method():
            sys.exit() 


def CreateWidgets():

		
        
        WindowPanel = PyQT4_API.myWindow('PyQT4 Window By Santosh Kumar' ,300,300,400,300)
        userLbl=PyQT4_API.Label("User Name :",20,15,80,30,WindowPanel)
        OldPswdLbl=PyQT4_API.Label("Old Password",20,50,140,30,WindowPanel)
        NewPswdLbl=PyQT4_API.Label("New Password",20,85,160,30,WindowPanel)
        ReNwPsLbl=PyQT4_API.Label("Repeat Password",20,120,160,30,WindowPanel)
        usrtb=PyQT4_API.TextBox("",150,15,150,30,WindowPanel)
        OldPstb=PyQT4_API.PasswordBox("",150,50,150,30,WindowPanel)
        NewPstb=PyQT4_API.PasswordBox("",150,85,150,30,WindowPanel)
        ReNewPstb=PyQT4_API.PasswordBox("",150,120,150,30,WindowPanel)
        '''
		ck1=CheckBox("I Love Animals ",20,45,150,50,WindowPanel)
        ck1.setCheckState(0)
        ck2=CheckBox("I Love Birds ",150,45,150,50,WindowPanel)
        ck2.setCheckState(2)
        ckBox= ButtonGroup(WindowPanel)
        ckBox.addButtons([ck1,ck2])
        rb1=RadioButton("PyQT4",10,140,100,20,WindowPanel)
        rb1.setChecked(True)
        rb2=RadioButton("Wx-Python",10,160,100,20,WindowPanel)
        rb3=RadioButton("PyGTK",10,180,100,20,WindowPanel)
        rb4=RadioButton("Tkinter",10,200,100,20,WindowPanel)
        rbgrp=ButtonGroup(WindowPanel)
        rlist=[rb1,rb2,rb3,rb4]
        rbgrp.addButtons(rlist)
       # print (rbgrp.getCheck())
        tb=TextBox("  ",100,15,150,30,WindowPanel)
        listBox=ListBox("My List Box",250,80,180,190,WindowPanel)
        myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightangle"]
        listBox.addItems(myList)
      '''
        
        widgets=[WindowPanel,userLbl,OldPswdLbl,NewPswdLbl,ReNwPsLbl,usrtb,OldPstb,NewPstb,ReNewPstb]
        btn= PyQT4_API.Button("Submit",30,180,100,35,WindowPanel)
        btn.buttonListener(Submit,widgets)
        Exit_btn= PyQT4_API.Button("Exit",200,180,100,35,WindowPanel)
        Exit_btn.buttonListener(exit_method)
        WindowPanel.show()
       

if __name__ == '__main__':
       app = QtGui.QApplication(sys.argv)
       CreateWidgets();
       sys.exit(app.exec_())
 
