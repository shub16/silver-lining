import WX


######### enter Username = "vikas" & Password = "p2009cs1036" #########


class Result() :
    def  __init__(self) :
        pass

def if_valid_pwd(n_pwd1, n_pwd2):
    if n_pwd1 == 'vikas' and n_pwd2 == 'p2009cs1036':
        print "password match"
        import authenticatedfile as c
    else :
        print "Passwords don't matches"
    

def onclick(event):
    a=textfield1.getText()
    b=textfield2.getText()
    if_valid_pwd(a,b)
    return


window = WX.Xwindow(1, 'Assignment5',225, 250)
label1=WX.LabelText('Username',30,20,100,20)
textfield1 = WX.TextView('',30,40,150,20)
label2=WX.LabelText('Password',30,80,100,20)
textfield2 = WX.TextView('',30,100,150,20)
window.add(textfield1)
window.add(label1)
window.add(textfield2)
window.add(label2)
button=WX.Button("Submit",50, 170, 100,25)
button.clickListener(onclick)
window.add(button)
window.show()


