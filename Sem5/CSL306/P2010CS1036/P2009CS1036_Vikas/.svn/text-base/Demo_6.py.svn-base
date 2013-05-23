import WX

if __name__ == '__main__':
    
    xwindow = WX.Xwindow(1,'Assignment 6' ,510,300)
    
    #Dropdown valuelist
    cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
    valuelist = WX.DropDownList(cities,10,10,200,20,"<Select your city>")
    xwindow.add(valuelist)
    
    #checkboxs
    checkbox1 = WX.CheckBox("CheckBox1",10,45,215,15)
    checkbox2 = WX.CheckBox("CheckBox2",10,70,215,15)
    checkbox1.setValue(True)
    xwindow.add(checkbox1)
    xwindow.add(checkbox2)

    textview = WX.TextView("Demo text area",250,10,215,215)
    xwindow.add(textview)

    radiobutton=WX.Radio(100, 50)
    radiobutton.addRadioButton("Radio1",10,95)
    radiobutton.addRadioButton("Radio2",120,95)
    xwindow.add(radiobutton)
    
    submitBtn = WX.Button("Submit",200,230,120,30)
    
    xwindow.add(submitBtn)
    
    xwindow.show()
