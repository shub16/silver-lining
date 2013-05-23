import PyQT4_API,sys,os
import AnyGUI_API as todoList
from PyQt4 import QtGui
from PyQt4 import QtCore
from functools import partial 

global Account


'''# function called when button is pushed
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
		
def call_method(widgets):
            print ("\n Your Entered Datas \n\n");
            print ("****************************\n")
            print ("Your Name :  "+ widgets[1].getText());
            print ("Your Password :  "+ widgets[2].getText());
            if(widgets[3].getChecked != -1):
		    print ("Your Favourite Tool-Kit is :  "+widgets[4].getValue())
   
'''         	
def exit_method():
            sys.exit() 

# method called on Clicking Login Button
def login_method(widgets):

            if(str(widgets[1].getText())==USR and str(widgets[2].getText())==PSWD):
                widgets[0].Close()
                Account= "Admin"
                if(widgets[3].getChecked()==0):
                   todoList.new_win(0,0,Account)
                elif(widgets[3].getChecked()==1):
                   todoList.new_win(0,1,Account)
                elif(widgets[3].getChecked()==2):
		   todoList.new_win(0,2,Account)
                elif(widgets[3].getChecked()==3):
                   todoList.new_win(0,1,Account)
                else:
                   print "Error With Radio-Buttons"
            else:
                widgets[4].setText("UserName and Password donot Match")

#Method called on clicking GuestLogin Button
def guest_log(widgets):
            widgets[0].Close()
            Account="Guest"
	    if(widgets[3].getChecked()==0):
                   todoList.new_win(0,0,Account)
            elif(widgets[3].getChecked()==1):
                   todoList.new_win(0,1,Account)
            elif(widgets[3].getChecked()==2):
		   todoList.new_win(0,1,Account)
            elif(widgets[3].getChecked()==3):
                   todoList.new_win(0,3,Account)
            else:
                   print "Error With Radio-Buttons"


def aboutMe_method():
            print("\nThis document is Created By Santosh Kumar P2009CS1016\n"); 
			
# Method to Create the Widgets in the first Window
def CreateWidgets():

		
        WindowPanel = PyQT4_API.myWindow('AnyGUI Login Form' ,300,300,500,300)
        userLbl=PyQT4_API.Label("User Name :",250,50,80,30,WindowPanel)
        PswdLbl=PyQT4_API.Label("Password :",250,80,140,30,WindowPanel)
        GuestLabel=PyQT4_API.Label("Not Registered User : ?",120,220,170,30,WindowPanel)
        AdmLabel=PyQT4_API.Label("Administrator :",300,20,140,30,WindowPanel)
        CrctPswdLbl=PyQT4_API.Label("",220,160,280,30,WindowPanel)
        RadioLbl=PyQT4_API.Label("Choose ToolKit to Work With",20,15,160,30,WindowPanel)
        usrtb=PyQT4_API.TextBox("",340,55,150,20,WindowPanel)
        Pstb=PyQT4_API.PasswordBox("",340,85,150,20,WindowPanel)
        rb1=PyQT4_API.RadioButton("PyQT4",20,50,100,20,WindowPanel)
        rb1.setChecked(True)
        rb2=PyQT4_API.RadioButton("Wx-Python",20,70,100,20,WindowPanel)
        rb3=PyQT4_API.RadioButton("PyGTK",20,90,100,20,WindowPanel)
        rb4=PyQT4_API.RadioButton("Tkinter",20,110,100,20,WindowPanel)
        rbgrp=PyQT4_API.ButtonGroup(WindowPanel)
        rlist=[rb1,rb2,rb3,rb4]
        rbgrp.addButtons(rlist)
        widgets=[WindowPanel,usrtb,Pstb,rbgrp,CrctPswdLbl]
        guest_btn= PyQT4_API.Button("Guest Login",280,220,100,35,WindowPanel)
        guest_btn.buttonListener(guest_log,widgets)
        btn= PyQT4_API.Button("Login",320,120,100,35,WindowPanel)
        btn.buttonListener(login_method,widgets)
        WindowPanel.Show()
       
if __name__ == '__main__':
       USR= "csl306"
       PSWD="iitropar"
       app = QtGui.QApplication(sys.argv)
       CreateWidgets();
       sys.exit(app.exec_())
