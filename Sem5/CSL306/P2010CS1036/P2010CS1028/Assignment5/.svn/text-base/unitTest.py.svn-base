from wx_GUI import *
import unittest

def ClickButton(event=None):    
    result = constraints(passwd1.getText(),passwd2.getText()) 
    if(result == 0):
        messagebox.setText("Password Changed Successfully!\n");
    elif(result == -1):        
        messagebox.setText("Both passwords don't match!\n")
    elif(result == -2):        
        messagebox.setText("Password less than six characters!\n")
    elif(result == -3):
        messagebox.setText("Password not alphanumeric!\n")
    elif(result == -4):
        messagebox.setText("Password contains only alphabets!\n")
    elif(result == -5):
        messagebox.setText("Password contains only digits!\n")        
    return

def constraints(passwd1,passwd2):
    if passwd1 != passwd2:
       return -1
    if(len(passwd1)<=6):           
       return -2
    if(str(passwd1).isalnum()):                 
        if(str(passwd1).isalpha()):          
            return -4   
        elif(str(passwd1).isdigit()):	  
            return -5
        else :			                     
            return 0
    else:                                           
       return -3

class TestCases(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(constraints("software1","software1"), 0)	

    def testMismatch(self):
        self.assertEqual(constraints("software1","software2"), -1)
        
    def testMismatchCase(self):
        self.assertEqual(constraints("software1","SOFTWARE1"), -1)  
            
    def testOneEmpty(self):
        self.assertEqual(constraints("software",""), -1)            

    def testLength(self):        
        self.assertEqual(constraints("soft1","soft1"), -2)
        
    def testBothEmpty(self):
        self.assertEqual(constraints("",""), -2)
        
    def testAplhaNum(self):
        self.assertEqual(constraints("&&&@&&&","&&&@&&&"), -3)

    def testAplha(self):
        self.assertEqual(constraints("software","software"), -4)

    def testNum(self):
        self.assertEqual(constraints("1234567","1234567"), -5)

if __name__ == '__main__':
    vista = Vista(1,'Change Password',500,350)
    user = ShowText("Username  ",10,23,500,20);
    username = TextArea("",160,20,300,20);

    currentpasswd = ShowText("Current Password  ",10,73,500,20);
    currentpassword = PasswordField("",160,70,300,20);

    newpasswd = ShowText("New Password  ",10,123,500,20);
    passwd1 = PasswordField("",160,120,300,20);
    newpasswd1 = ShowText("Confirm Password  ",10,173,500,20);
    passwd2 = PasswordField("",160,170,300,20);

    messagebox = TextBuffer("",160,220,300,100);

    changepasswd = Button("Change Password",5,250,150,30)
    changepasswd.clickTrigger(ClickButton)

    vista.addWidget(user);
    vista.addWidget(username);
    vista.addWidget(currentpasswd);
    vista.addWidget(currentpassword);  
    vista.addWidget(newpasswd);
    vista.addWidget(newpasswd1);
    vista.addWidget(passwd1);
    vista.addWidget(passwd2);     
    vista.addWidget(messagebox)     
    vista.addWidget(changepasswd)    

    vista.show()
   
    unittest.main()

