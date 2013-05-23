import sys
def generate():
    text_file = open("Output.txt", "w")
    text_file.write("\n**********Begin_Description**********\n\n")    
    text_file.write("Date and Time : %s\n\n"%(calender.getValue()))
    
    count=0

    text_file.write("Important Events : \n")
    if(ck1.getCheckState()):
        text_file.write("Anniversary \n")
        count=count+1
    if(ck2.getCheckState()):
        text_file.write("Birthday \n")
        count=count+1
    if(ck3.getCheckState()):
        text_file.write("Meeting \n")
        count=count+1
        text_file.write("Travel \n")
    if(ck4.getCheckState()):
        count=count+1
    if(ck5.getCheckState()):
        text_file.write("Family \n")
        count=count+1
    if(ck6.getCheckState()):
        text_file.write("Deadline \n")
        count=count+1
    if(ck7.getCheckState()):
        text_file.write("Leisure \n")
        count=count+1
    if(count==0):
        text_file.write("-None- \n")
    
    text_file.write("\nEvent rating/importance: %s"%sld1.getValue())
    
    text_file.write("\n\nEvent location: %s"%listBox.Selected())
    
    text_file.write("\n\nEvent time: %s"%timeBox.Selected())
    
    text_file.write("\n\nEvent Description:\n%s"%comments.getText())
    
    
    text_file.write("\n\n**********End_Description**********")    
   
    text_file.close()
    ok_label.setLabel("Output.txt generated")
   
def exit_mthd():
            sys.exit() 













def generate1(self):
    text_file = open("Output.txt", "w")
    text_file.write("\n**********Begin_Description**********\n\n")    
    text_file.write("Date and Time : %s\n\n"%(calender.getValue()))
    
    count=0

    text_file.write("Important Events : \n")
    if(ck1.getCheckState()):
        text_file.write("Anniversary \n")
        count=count+1
    if(ck2.getCheckState()):
        text_file.write("Birthday \n")
        count=count+1
    if(ck3.getCheckState()):
        text_file.write("Meeting \n")
        count=count+1
        text_file.write("Travel \n")
    if(ck4.getCheckState()):
        count=count+1
    if(ck5.getCheckState()):
        text_file.write("Family \n")
        count=count+1
    if(ck6.getCheckState()):
        text_file.write("Deadline \n")
        count=count+1
    if(ck7.getCheckState()):
        text_file.write("Leisure \n")
        count=count+1
    if(count==0):
        text_file.write("-None- \n")
    
    text_file.write("\nEvent rating/importance: %s"%sld1.getValue())
    
    text_file.write("\n\nEvent location: %s"%listBox.Selected())
    
    text_file.write("\n\nEvent time: %s"%timeBox.Selected())
    
    text_file.write("\n\nEvent Description:\n%s"%comments.getText())
    
    
    text_file.write("\n\n**********End_Description**********")    
   
    text_file.close()
    ok_label.setLabel("Output.txt generated")
   
def exit_mthd1(self):
            sys.exit() 










def new_win(oldGUI,newGUI,Account):
	

	if (newGUI==1):
	    import wxabhi as API
	elif(newGUI==0): 
	    import sys
	    from PyQt4 import QtGui
	    from PyQt4 import QtCore
	    import os
	    from functools import partial 
	    import re
	    import PyQT4_API as API
	elif(newGUI==3):
	    import sys
	    import os
	    from functools import partial 
	    import re
            import tkGUI_adi as API  
            import tkMessageBox
            import sys,os
            import Tkinter as root
            import Tkinter as tk
            import time
            import calendar

            try:
                import Tkinter
                import tkFont
            except ImportError: # py3k
                import tkinter as Tkinter
                import tkinter.font as tkFont
            import ttk
          
     
        global WindowPanel,hello_label,calender,comments,tag_label,ck1,ck2,ck3,ck4,ck5,ck6,ck7,imp_label,sld1,listBox,timeBox,ok_label;
	WindowPanel = API.myWindow('To-Do List With AnyGUI' ,350,150,900,700)
        welcome ="Welcome "+Account+ " !"
	hello_label=API.Label(welcome,150,5,150,80,WindowPanel)
        logged_label=API.Label("Guest Logged In.",650,5,150,80,WindowPanel)
	calender=API.Cld(420,60,340,240,WindowPanel)  

	comments=API.TextBox("\n    Enter event description here!!",40,60,340,240,WindowPanel)

	tag_label=API.Label("Tag Event:",40,310,100,50,WindowPanel)

	ck1=API.CheckBox("Anniversary ",40,350,150,30,WindowPanel)
	ck1.setCheckState(0)

	ck2=API.CheckBox("Birthday ",40,380,150,30,WindowPanel)
	ck2.setCheckState(0)

	ck3=API.CheckBox("Meeting ",40,410,150,30,WindowPanel)
	ck3.setCheckState(0)


	ck4=API.CheckBox("Travel ",40,440,150,30,WindowPanel)
	ck4.setCheckState(0)
            

	ck5=API.CheckBox("Family ",40,470,150,30,WindowPanel)
	ck5.setCheckState(0)

	ck6=API.CheckBox("Deadline ",40,500,150,30,WindowPanel)
	ck6.setCheckState(0)


	ck7=API.CheckBox("Leisure ",40,530,150,30,WindowPanel)
	ck7.setCheckState(0)
      
	imp_label=API.Label("Event importance:",510,320,200,50,WindowPanel)

	sld1=API.Slider(520,380,270,40,WindowPanel)
 	sld1.setRange(0,10)
        
       
	
	myList=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Chandigarh","Himachal Pradesh","Jammu and Kashmir","Srinagar and Jammu","Jharkhand","Karnataka","Kerala","Madya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttaranchal","Uttar Pradesh","West Bengal"]
	
	listBox=API.ComboBox("Location",myList,200,360,180,50,WindowPanel)
	
        
	timeList=["Morning","Afternoon","Evening","Night"]
	timeBox=API.ComboBox("Time",timeList,200,460,180,50,WindowPanel)
	
        Gen=API.Button("Generate Text!",460,460,150,60,WindowPanel)
        if(newGUI==3):
            Gen.buttonListener(generate)
        else:
            Gen.buttonListener(generate1)
        Extbtn=API.Button("Exit GUI",630,460,150,60,WindowPanel)
        if(newGUI==3):
            Extbtn.buttonListener(exit_mthd)
        else:
            Extbtn.buttonListener(exit_mthd1)

	
        ok_label=API.Label("",535,550,150,50,WindowPanel)
	WindowPanel.show()                
