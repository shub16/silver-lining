import API_7 as root
import API_7 as shoot

def if_valid_pwd():
        ywindow = shoot.Xwindow(1,'Assignment 7_2' ,450,400)
        
        but=shoot.Button("Select",135,350,120,30)
        ywindow.add(but)

        # name and college name text area
        text=shoot.TextView('Name',10,10,150,20)
        text.setText("Your Name")
        ywindow.add(text)
        textt=shoot.TextView('College',180,10,250,20)
        textt.setText("College Name")
        ywindow.add(textt)
        
        #radio button creation
        app =shoot.Radio(100,25)
        app.addRadioButton("Delhi Zone",10,50)
        app.addRadioButton("Mumbai Zone",10,80)
        app.addRadioButton("Chennai Zone",10,110)
        app.addRadioButton("Kolkata Zone",10,140)
        ywindow.add(app)

        #check boxes creation is here
        check=shoot.CheckBox("Graduate",180,50,100,25)
        checkk=shoot.CheckBox('Professionally Experienced',180,80,100,25)
        checkkk=shoot.CheckBox("Indian",180,110,100,25)
        checkkkk=shoot.CheckBox("Never Criminalised",180,140,100,25)
        ywindow.add(check)
        ywindow.add(checkk)
        ywindow.add(checkkk)
        ywindow.add(checkkkk)

        #multiple line text area
        stat3 = shoot.TextView("",10,220,400,100)
        stat3.setText("Why should we Hire You...???")
        ywindow.add(stat3)
        ywindow.show()
    
def onclick():
    if_valid_pwd()
    return

########################################################################
xwindow = root.Xwindow(1, 'Assignment 7',225, 300)

textfield1 = root.TextView('Your Name',30,40,150,30)
textfield2 = root.TextView('Enter Your Password',30,100,150,30)

xwindow.add(textfield1)
xwindow.add(textfield2)

button=root.Button("Continue",50, 210, 100,25)
button.clickListener(onclick)
xwindow.add(button)
xwindow.show()


