import WX

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


window = WX.Xwindow(1, 'Assignment5',225, 300)
label1=WX.LabelText('Old Password',30,20,100,20)
textfield1 = WX.TextView('',30,40,150,20)
label2=WX.LabelText('New Password',30,80,100,20)
textfield2 = WX.TextView('',30,100,150,20)
label3=WX.LabelText('Confirm Password',30,140,100,20)
textfield3 = WX.TextView('',30,160,150,20)
window.add(textfield1)
window.add(label1)
window.add(textfield2)
window.add(label2)
window.add(textfield3)
window.add(label3)
button=WX.Button("Submit",50, 210, 100,25)
button.clickListener(onclick)
window.add(button)
window.show()


