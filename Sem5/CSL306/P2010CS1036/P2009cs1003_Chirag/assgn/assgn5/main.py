import sys
import Assignment5 as wxpython                                                           #importing my file
import re

def isAlphaNumeric(string):
    strMatchAlnum = re.findall('[a-zA-Z0-9]', string)
    strMatchNum = re.findall('[0-9]',string)
    strMatchAlpha = re.findall('[a-zA-z]',string)
    if len(string) == len(strMatchAlnum) and len(strMatchNum) > 0 and len(strMatchAlpha) > 0:
        return True
    else:
        return False

class changePassword:

    def __init__(self,username, oldPasswd, newPasswd, confirmPasswd):
        self.username = username
        self.oldPasswd = oldPasswd
        self.newPasswd = newPasswd
        self.confirmPasswd = confirmPasswd
        print self.newPasswd
        print self.confirmPasswd

    def checkPasswordValidity(self):

        if len(self.newPasswd) <= 6:
            print("Password must have more than 6 characters.")
            return False
        elif not(isAlphaNumeric(self.newPasswd)):
            print "Password must have atleast 1 alphabet and 1 digit."
            return False
        elif self.newPasswd != self.confirmPasswd:
            print "Passwords did not match."
            return False

        return True



def main():

    window = wxpython.Window(300,300,400,300,"Chirag Gupta") 

    uname = window.createTextArea(110,10,200, 30,"Normal","UserName")
    
    oldPwd = window.createTextArea(110,70,200, 30,"Password","Old Password")

    newPwd = window.createTextArea(110,130,200, 30,"Password","New Password")

    confirmPwd = window.createTextArea(110,190,200, 30,"Password","Confirm Password")
    
    button = window.createButton("Submit",150,250,100,30)
    List = [uname, oldPwd, newPwd, confirmPwd]

    def submitData(event):
        print List[0].getValue()
        uname = List[0].getValue()
        oldPwd = List[1].getValue()
        newPwd = List[2].getValue()
        confirmPwd = List[3].getValue()

        print oldPwd
        print newPwd
        print confirmPwd
        cp = changePassword(uname, oldPwd, newPwd, confirmPwd)
        if cp.checkPasswordValidity():
            print "Password changed successfully."
            sys.exit()
            return True
        else:
            List[1].setValue("")
            List[2].setValue("")
            List[3].setValue("")
            return False
        
    button.pressed(submitData)

    window.displayWindow()                                                                     #Ending window
        
if __name__ == '__main__':
    main()                                                                                  #Calling main function
