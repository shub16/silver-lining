import WX

if __name__ == '__main__':
    
    xwindow = WX.Xwindow(1,'Assignment 4' ,510,300)
    
    #checkboxs
    checkbox1 = WX.CheckBox("CheckBox1",10,45,215,15)
    checkbox2 = WX.CheckBox("CheckBox2",10,70,215,15)
    checkbox1.setValue(True)
    xwindow.add(checkbox1)
    xwindow.add(checkbox2)

    textview = WX.TextView("Demo text area",250,10,215,180)
    xwindow.add(textview)

    radiobutton=WX.Radio(100, 50)
    radiobutton.addRadioButton("Radio1",10,95)
    radiobutton.addRadioButton("Radio2",120,95)
    xwindow.add(radiobutton)
    
    submitBtn = WX.Button("Submit",200,200,120,30)
    
    xwindow.add(submitBtn)
    
    xwindow.show()
