import QT as anyGUI

"""
import FLTK as anyGUI   #to use FLTK GUI API
import TK as anyGUI     #to use Tkinter GUI API
import WX as anyGUI     #to use wxPython GUI
import GTK as anyGUI    #to use GTK GUI API
import QT  as anyGUI    #to use pyQT GUI API
"""

if __name__ == '__main__':
    
    xwindow = anyGUI.Xwindow(1,'Developed using AnyGUI_API' ,300,250)
    
    #Adding Label to xwindow
    label = anyGUI.LabelText("This is a Label",10,10,280,20)
    xwindow.add(label)

    #Adding TextBox to xwindow
    textbox = anyGUI.TextView("This is a text Box",10,30,280,20)
    xwindow.add(textbox)
    
    #Adding CheckBox to xwindow
    checkbox1 = anyGUI.CheckBox("Check Box Button",20,55,215,15)
    checkbox1.setValue(True)
    xwindow.add(checkbox1)

    #Adding Radio Button to xwindow
    rbtn = anyGUI.Radio(100,50)
    rbtn.addRadioButton("Radio Button 1",20,75)
    rbtn.addRadioButton("Radio Button 2",190,75)
    xwindow.add(rbtn)
    
    #Adding TextLine to xwindow
    textline = anyGUI.TextLine("This is a text Line",10,140,280,20)
    xwindow.add(textline)
    
    #Adding a Button to xwindow
    submitBtn = anyGUI.Button("Submit",100,170,120,30)
    xwindow.add(submitBtn)
    
    xwindow.show()