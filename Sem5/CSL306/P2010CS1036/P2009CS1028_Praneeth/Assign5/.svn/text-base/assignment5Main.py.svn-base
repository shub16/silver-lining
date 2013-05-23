import Tkinter
import assignment4_for_import as TkGUI
import re

#checking whether a string has only alphanumeric values
def isAlphaNumeric(value):
    if re.match(r'^[\w.-]+$', value):
        return True;
    else:
        return False;

#checking whether the passwords satisfy the validation conditions
def checkValidity(user, oldPass, newPass, cfmPass):
    if len(newPass) <= 6:
        print "\nPassword lengths should be greater then 6\n"
        return False;

    elif not(isAlphaNumeric(newPass)):
        print "\nPasswords should be alphnumeric\n"
        return False;

    elif newPass != cfmPass:
        print "\nPasswords should match\n"
        return False;

    else:
        return True;

#Extract data from the Text fields, pass on to the checkValidity() function and then print info to terminal
def ExtractDataAndCheck(userName,oldPassword,newPassword,confirmPassword,statusvar):

    user = userName.textline.get();
    oldPass = oldPassword.textline.get();
    newPass = newPassword.textline.get();
    cfmPass = confirmPassword.textline.get();

    result = checkValidity(user, oldPass, newPass, cfmPass)

    if(result):
        statusvar.set("Password combination passed!");
    else:
        statusvar.set("Password combination failed! Check terminal for details");

def main():

#creating the GUI and calling the corresponding validation methods on clicking Submit button
    widget = TkGUI.Widgets()
    widget.setWindow(300, 400, "Tkinter GUI")

    TkGUI.Label(widget,10,20,0,"Username:")
    TkGUI.Label(widget,10,40,0,"Old Password:")
    TkGUI.Label(widget,10,60,0,"New Password:")
    TkGUI.Label(widget,10,80,0,"Confirm Password:")

    statusLabel = TkGUI.Label(widget,10,150,60,"")
    statusvar = Tkinter.StringVar()
    statusLabel.label.config(textvariable = statusvar)
    statusvar.set("Enter the Information in the fields")

    userName = TkGUI.TextLine(widget,150,20,20,"Normal")
    oldPassword = TkGUI.TextLine(widget,150,40,20,"Password")
    newPassword = TkGUI.TextLine(widget,150,60,20,"Password")
    confirmPassword = TkGUI.TextLine(widget,150,80,20,"Password")

    thisButton = TkGUI.Button(widget,90,200,1,0,"Submit")
    thisButton.button.config(command = lambda:ExtractDataAndCheck(userName,oldPassword,newPassword,confirmPassword,statusvar))    

    widget.endWindow()
                                                                 
        
if __name__ == '__main__':
    main()                                                                                  
