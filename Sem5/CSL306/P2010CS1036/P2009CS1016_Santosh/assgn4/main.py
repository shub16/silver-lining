#This is a Demo Program which shows the functionality of the Assignment 4,A common API for the widgets.

import PyQT4_API
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from functools import partial 
import re


#method which is called when the Submit Button is Pressed

def call_method(widgets):
            print ("\n Your Entered Datas \n\n");
            print ("****************************\n")
            print ("Your Name :  "+ widgets[7].getText());
            if(widgets[6].getChecked != -1):
			    print ("Your Favourite Tool-Kit is :  "+widgets[6].getValue())
            if(widgets[4].getCheckState()==True):
			   print ("You Love Animals")
            if(widgets[5].getCheckState()==True):
               print("You Love Birds")
            print("Your Favourite Animal is : "+ widgets[8].Selected());

#Method which is called when Exit Button is pressed			
			
def exit_method():
            sys.exit() 


#This method will Create the required widgets with their specifications.
def CreateWidgets():
        
        WindowPanel = PyQT4_API.myWindow('PyQT4 Window By Santosh Kumar' ,50,50,450,400)
        nameLbl=PyQT4_API.Label("Your Name :",20,15,80,30,WindowPanel)
        toollbl=PyQT4_API.Label("Your Favourite Tool-Kit",15,100,140,40,WindowPanel)
        Listlbl=PyQT4_API.Label("Your Favourite Animal",280,30,160,60,WindowPanel)
        ck1=PyQT4_API.CheckBox("I Love Animals ",20,45,150,50,WindowPanel)
        ck1.setCheckState(0)
        ck2=PyQT4_API.CheckBox("I Love Birds ",150,45,150,50,WindowPanel)
        ck2.setCheckState(2)
       # ckBox= ButtonGroup(WindowPanel)
        #ckBox.addButtons([ck1,ck2])
        rb1=PyQT4_API.RadioButton("PyQT4",10,140,100,20,WindowPanel)
        rb1.setChecked(True)
        rb2=PyQT4_API.RadioButton("Wx-Python",10,160,100,20,WindowPanel)
        rb3=PyQT4_API.RadioButton("PyGTK",10,180,100,20,WindowPanel)
        rb4=PyQT4_API.RadioButton("Tkinter",10,200,100,20,WindowPanel)
        rbgrp=PyQT4_API.ButtonGroup(WindowPanel)
        rlist=[rb1,rb2,rb3,rb4]
        rbgrp.addButtons(rlist)
       # print (rbgrp.getCheck())
        tb=PyQT4_API.TextBox("  ",100,15,150,30,WindowPanel)
        listBox=PyQT4_API.ListBox("My List Box",250,80,180,190,WindowPanel)
        myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightangle"]
        listBox.addItems(myList)
        widgets=[WindowPanel,nameLbl,toollbl,Listlbl,ck1,ck2,rbgrp,tb,listBox]
        btn= PyQT4_API.Button("Print On Console",30,320,150,50,WindowPanel)
        btn.buttonListener(call_method,widgets)
        Exit_btn= PyQT4_API.Button("Exit",260,320,150,50,WindowPanel)
        Exit_btn.buttonListener(exit_method)
        WindowPanel.show()
        sys.exit(app.exec_())
 

if __name__ == '__main__':
       app = QtGui.QApplication(sys.argv);
       CreateWidgets();
       sys.exit(app.exec_())
