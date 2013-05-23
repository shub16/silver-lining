from AnyGUI.xGUI import *
xGUI(Environment = "gtk")
'''
Package in AnyGUI
-------------------
from AnyGUI.fltkGUI import *    #FLTK GUI
from AnyGUI.tkGUI import *      #Tkinter GUI
from AnyGUI.wxGUI import *      #wxPython GUI
from AnyGUI.gtkGUI import *     #GTK GUI
from AnyGUI.qtGUI import *      #QtPy GUI

Dynamic evironment change
-------------------------
Environment will in
    wx    : wxPython            by Arink    2009cs1017
    fltk  : Fast Light Toolkit  by Kamal    2009cs1011
    gtk   : GTK Py              by Gaurav   2009cs1001
    qt    : PyQT                by Prateek  2009cs1002
    tk    : TKinter             by Pravesh  2009cs1001
'''

#Functions bind to button events
def SubmitButtonClick(event):
    report = " Your city is "+valuelist.getValue()+"\n"
    if(checkbox1.getValue()):
        report = report + " you have read the code\n"
    else:
        report = report + " you have not read the code\n"
        
    if(checkbox2.getValue()):
               report = report + " you have read the documentation\n"
    else:
        
        report = report + " you have not read the documentation\n"
        report = report + " you are "+rb1.getValue()+"\n"
        report = report + " you need "+rb2.getValue()+"\n"

    textarea.appendText("_______________________\n"+report+"\n\n")
    return True 

def AboutButtonClick(event):
    textarea.setText("Created by gtkGUI -v1.0\nAuthor : Gaurav Katoch\n\nhttp://10.1.0.140/trac/wiki/GauravKatoch\n")
    return True



    #Constructor canvas
canvas = Canvas(1, 'gtkGUI -v1.0 | Gaurav Katoch' ,510,300)

    #Dropdown valuelist
cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
canvas.add(valuelist)

    #checkboxs
checkbox1 = CheckBox("I have read the code.",10,45,215,15)
checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
checkbox1.setValue(True)
canvas.add(checkbox1)
canvas.add(checkbox2)

    #radioGroup1
rb1 = RadioGroup(60,50)
rb1.addRadioButton("Nice",10,110)
rb1.addRadioButton("Good",70,110)
rb1.addRadioButton("Great",140,110)
rb1.setButtonTrue(2)
canvas.add(rb1)

    #radioGroup2
rb2 = RadioGroup(100,50)
rb2.addRadioButton("Option #1",10,160)
rb2.addRadioButton("Option #2",110,160)
rb2.setButtonTrue(0)
canvas.add(rb2)

    #TextArea
textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
canvas.add(textarea)

    #Creating Buttons
submitBtn = Button("Submit",130,230,120,30)
aboutBtn = Button("About",260,230,120,30)

    #Callback methods on buttons click
submitBtn.clickListener(SubmitButtonClick)
aboutBtn.clickListener(AboutButtonClick)

    #Adding buttons to canvas
canvas.add(aboutBtn)
canvas.add(submitBtn)

canvas.show()
