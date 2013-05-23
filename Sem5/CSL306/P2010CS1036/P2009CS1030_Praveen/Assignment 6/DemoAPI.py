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
    label = anyGUI.LabelText("This is a Label and below is a List",10,10,280,20)
    xwindow.add(label)
    
    dates = ['1','2','3','4','5','6','7','8','9','10', '11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    years = ['1989', '1990', '1991', '1992','1993']
    datesList = anyGUI.DropDownList(dates,10,30,70,20,"Date")
    monthsList = anyGUI.DropDownList(months,90,30,60,20,"Month")
    yearsList = anyGUI.DropDownList(years,160,30,50,20,"Year")
    xwindow.add(monthsList)
    xwindow.add(datesList)
    xwindow.add(yearsList)

 
    #Adding TextBox to xwindow
    textbox = anyGUI.TextView("This is a text Box",10,55,280,20)
    xwindow.add(textbox)
    
    #Adding CheckBox to xwindow
    checkbox1 = anyGUI.CheckBox("Check Box Button",10,80,215,15)
    checkbox1.setValue(True)
    xwindow.add(checkbox1)

    #Adding Radio Button to xwindow
    rbtn = anyGUI.Radio(100,50)
    rbtn.addRadioButton("Radio Button 1",10,100)
    rbtn.addRadioButton("Radio Button 2",190,100)
    xwindow.add(rbtn)
    
    #Adding TextLine to xwindow
    textline = anyGUI.TextLine("This is a text Line",10,160,280,20)
    xwindow.add(textline)
    
    #Adding a Button to xwindow
    submitBtn = anyGUI.Button("Submit",100,190,120,30)
    xwindow.add(submitBtn)
    
    xwindow.show()