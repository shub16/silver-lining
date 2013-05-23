import tk_API as root
class Result :
    def  __init__(self) :
        pass

def if_valid_pwd(n_pwd1, n_pwd2):
    result = Result()
    result.match = None
    if n_pwd1 == n_pwd2 :
        result.match = True
        result.text = "Passwords Matched \n"
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
            result.text = result.text + "Passwords satisfy the criteria \n"
        else :
            result.text = result.text + "Passwords didn't satisfy the criteria \n"
    else :
        result.text, result.value = "Passwords didn't match", False
    return result
    

def onclick():
    a=textfield2.getText()
    b=textfield3.getText()
    result = if_valid_pwd(a,b)
    print result.text
    return

xwindow = root.Xwindow(1, 'Assignment5',225, 300)

textfield1 = root.TextView('Old Password',30,40,150,30)
textfield2 = root.TextView('New Password',30,100,150,30)
textfield3 = root.TextView('Confirm Password',30,160,150,30)

xwindow.add(textfield1)
xwindow.add(textfield2)
xwindow.add(textfield3)

button=root.Button("Submit",50, 210, 100,25)
button.clickListener(onclick)
xwindow.add(button)
xwindow.show()


