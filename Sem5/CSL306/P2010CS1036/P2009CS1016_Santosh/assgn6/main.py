import PyQT4_API
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from functools import partial 
import re
'''
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
def call_method(widgets):
            print ("\n Your Entered Datas \n\n");
            print ("****************************\n")
            print ("Your Name :  "+ widgets[1].getText());
            print ("Your Password :  "+ widgets[2].getText());
            if(widgets[4].getChecked != -1):
			    print ("Your Favourite Tool-Kit is :  "+widgets[4].getValue())
            if(widgets[3].getCheckState()==True):
			   print ("You Love Animals")
            print("Your City is : "+ widgets[8].Selected());
            print("Your Favourite Animal is : "+ widgets[7].Selected());
            print("Your Birth Date is : %s"% widgets[5].getValue());
            print("You Rated the GUI as : %d"% widgets[6].getValue());
            	
def exit_method():
            sys.exit() 

def aboutMe_method():
            print("\nThis document is Created By Santosh Kumar P2009CS1016\n"); 
def CreateWidgets():

		
        
        WindowPanel = PyQT4_API.myWindow('PyQT4 Window By Santosh Kumar' ,300,100,520,450)
#        menubr=PyQT4_API.MenuBar(0,0,500,20,WindowPanel)
 #       menu_list=[['&File','&Exit',exit_method],['&About','&About Me',aboutMe_method]]
        userLbl=PyQT4_API.Label("User Name :",20,25,80,30,WindowPanel)
        PswdLbl=PyQT4_API.Label("Password",20,50,140,30,WindowPanel)
        RadioLbl=PyQT4_API.Label("Your Favourite Tool-Kit",350,15,160,30,WindowPanel)
        ComboLbl=PyQT4_API.Label("Your City",40,300,160,30,WindowPanel)
        ListLbl=PyQT4_API.Label("Your Favourite Animal",300,300,360,30,WindowPanel)        
        BirthLbl=PyQT4_API.Label("Your Birth Date",20,170,120,30,WindowPanel)
        RateLbl=PyQT4_API.Label("Please rate the GUI on (0-10) scale",20,370,220,30,WindowPanel)
        usrtb=PyQT4_API.TextBox("",150,30,150,20,WindowPanel)
        Pstb=PyQT4_API.PasswordBox("",150,55,150,20,WindowPanel)
        '''NewPstb=PyQT4_API.PasswordBox("",150,85,150,30,WindowPanel)
        ReNewPstb=PyQT4_API.PasswordBox("",150,120,150,30,WindowPanel)
'''
        ck1=PyQT4_API.CheckBox("I Love Animals ",20,45,150,110,WindowPanel)
        ck1.setCheckState(0)
        '''ck2=PyQT4_API.CheckBox("I Love Birds ",150,45,150,110,WindowPanel)
        ck2.setCheckState(2)
        ckBox= PyQT4_API.ButtonGroup(WindowPanel)'''
        #ckBox.addButtons([ck1,ck2])
        rb1=PyQT4_API.RadioButton("PyQT4",360,40,100,20,WindowPanel)
        rb1.setChecked(True)
        rb2=PyQT4_API.RadioButton("Wx-Python",360,60,100,20,WindowPanel)
        rb3=PyQT4_API.RadioButton("PyGTK",360,80,100,20,WindowPanel)
        rb4=PyQT4_API.RadioButton("Tkinter",360,100,100,20,WindowPanel)
        rbgrp=PyQT4_API.ButtonGroup(WindowPanel)
        rlist=[rb1,rb2,rb3,rb4]
        rbgrp.addButtons(rlist)
       # print (rbgrp.getCheck())
        cal1=PyQT4_API.Calendar(240,140,240,140,WindowPanel)  
        sld1=PyQT4_API.Slider(300,380,180,20,WindowPanel)
        sld1.setRange(0,10)
        comboList= ["Lucknow","Ahmedabad","Ropar","Mumbai","Muzaffarpur","NewDelhi","Chandigarh"]
        comboBox=PyQT4_API.ComboBox("My Combo Box",comboList,20,330,180,30,WindowPanel)
        listBox=PyQT4_API.ListBox("My List Box",300,330,180,30,WindowPanel)
        myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightangle"]
        listBox.addItems(myList)
        widgets=[WindowPanel,usrtb,Pstb,ck1,rbgrp,cal1,sld1,listBox,comboBox]
#        menubr.addItems(menu_list,widgets);
        btn= PyQT4_API.Button("Submit",100,415,100,30,WindowPanel)
        btn.buttonListener(call_method,widgets)
        Exit_btn= PyQT4_API.Button("Exit",300,415,100,30,WindowPanel)
        Exit_btn.buttonListener(exit_method)
        WindowPanel.show()
       

if __name__ == '__main__':
       app = QtGui.QApplication(sys.argv)
       CreateWidgets();
       sys.exit(app.exec_())
 
