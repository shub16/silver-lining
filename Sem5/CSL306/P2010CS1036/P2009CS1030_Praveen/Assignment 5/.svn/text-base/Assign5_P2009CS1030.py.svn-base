import QT

class Result() :
    def  __init__(self) :
        pass

def if_valid_pwd(n_pwd1, n_pwd2):
    result = Result()
    result.match = None
    if n_pwd1 == n_pwd2 :
        result.match = True
        result.text = "Passwords matches \n"
        result.value, alpha, numeric, no_char = False, False, False, 0
        for c in n_pwd1 :
            if not result.value :
                if (c >= 'a' and c <='z') or (c >= 'A' and c <='Z') :
                    alpha = True
                elif c >= '0' and c <= '9' :
                    numeric = True
                no_char = no_char + 1
                result.value = numeric and alpha and ( no_char>6 )
            else :                                                  # password is validated 
                break
        if result.value :
            result.text = result.text + "passwords satisfy the criteria \n"
        else :
            result.text = result.text + "passwords don't satisfy the criteria \n"
    else :
        result.text, result.value = "Passwords don't matches", False
    return result
    

def onclick(event):
    a=textfield2.getText()
    b=textfield3.getText()
    result = if_valid_pwd(a,b)
    print result.text
    return


xwindow = QT.Xwindow(1, 'Assignment 5',225, 300)
label1=QT.LabelText('Old Password',30,20,100,20)
textfield1 = QT.TextView('',30,40,150,20)
label2=QT.LabelText('New Password',30,80,100,20)
textfield2 = QT.TextView('',30,100,150,20)
label3=QT.LabelText('Confirm Password',30,140,100,20)
textfield3 = QT.TextView('',30,160,150,20)
xwindow.add(textfield1)
xwindow.add(label1)
xwindow.add(textfield2)
xwindow.add(label2)
xwindow.add(textfield3)
xwindow.add(label3)
button=QT.Button("Submit",50, 210, 100,25)
button.clickListener(onclick)
xwindow.add(button)
xwindow.show()