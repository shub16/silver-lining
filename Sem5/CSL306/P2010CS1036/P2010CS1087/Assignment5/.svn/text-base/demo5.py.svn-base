'''
	Python GUI Project:
	Software Engineering Course
	Author:
		Abhimanyu Niroola   - 2010CS1087 
		Abhishek Arora      - 2010CS1004
		Shubham Chaudhary   - 2010CS1011
		Deepak Garg	    - 2010CS1012
	IIT Ropar
	Mentor: Dr. Anil Seth
	Library Used: 
		1) WX Python
		2) TKinter
		3) PyQT
		4) PyGTK		
'''

#!/usr/bin/python
# Button and Text-Area
import re
import sys
if __name__ == '__main__':
    	print "--------Please select a Toolkit to run your code: ----------" 		# Provide user with all the GUI options available
	print "\tPress 1 for TKInter"
	print "\tPress 2 for GTK"
	print "\tPress 3 for Wx"
	print "\tPress 4 for PyQT"
	x = input("Please give your choice: ")			# Asking user to select a GUI
	b=False
	while(b==False):					# Prompt user until he doesnt provide us with 
		if x==1:					
			print "You have choosed Tkinter"	
			import API4_tk as API			# Import Tkinter API file
		elif x==2:
			print "You have choosed GTK"
			import API4_gtk as API			# Import GTK API file
		elif x==3:
			print "You have choosed WX"
			import API4_wx as API			# Import WX API file
		elif x==4:
			print "You have choosed PyQT"		# Import PyQT API file
			import API4_qt as API
		else:						# If user entered a invalid choice then ask user for a valid choice 
			print "\n---You have choosed a invalid option"		
			x = input("Please provide a valid choice: ")
			continue
		b=True

	
def isAlphaNumeric(string):
    strMatchAlnum = re.findall('[a-zA-Z0-9]', string)
    strMatchNum = re.findall('[0-9]',string)
    strMatchAlpha = re.findall('[a-zA-z]',string)
    if len(string) == len(strMatchAlnum) and len(strMatchNum) > 0 and len(strMatchAlpha) > 0:
        return True
    else:
        return False

class changePassword:

    def __init__(self, username, oldPasswd, newPasswd, confirmPasswd):
        self.username = username
        self.oldPasswd = oldPasswd
        self.newPasswd = newPasswd
        self.confirmPasswd = confirmPasswd
        #print self.newPasswd
        #print self.confirmPasswd

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

def submitData(List):
    uname = List[0]
    oldPwd = List[1]
    newPwd = List[2]
    confirmPwd = List[3]

    #print oldPwd
    #print newPwd
    #print confirmPwd
    cp = changePassword(uname, oldPwd, newPwd, confirmPwd)
    if cp.checkPasswordValidity():
        print "Password changed successfully."
        sys.exit()
        return True
    else:
	List[0]=''
        List[1]=''
        List[2]=''
        List[3]=''
        return False

			

if __name__ == "__main__":		    
	global List
	List=[]
	
	def test(event=None):
		List = [text.getText(), pass1.getText(),pass2.getText() , pass3.getText()]

		
		text.setText('')
		pass1.setText('')
		pass2.setText('')
		pass3.setText('')

		submitData(List)

	Frame = API.WindowFrame(1, 'login' ,510,300)
	username=API.Label('Username', 10, 10,150,30)
	oldpass=API.Label('Old Password', 10, 50,150,30)
	newpass=API.Label('New Password', 10, 90,150,30)
	confirmpass=API.Label('Coinfirm Password', 10, 130,150,30)
	
	text=API.TextLine(200,10,150,30)
	pass1=API.Password(200,50,150,30)		
	pass2=API.Password(200,90,150,30)		
	pass3=API.Password(200,130,150,30)		
	
	button=API.Button('submit',170,170,60,30)
	Frame.add(username)
	Frame.add(oldpass)
	Frame.add(newpass)
	Frame.add(confirmpass)
	Frame.add(text)
	Frame.add(pass1)
	Frame.add(pass2)
	Frame.add(pass3)
	Frame.add(button)

        List = [text.getText(), pass1.getText(),pass2.getText() , pass3.getText()]
        button.clickListener(test)
    

	Frame.show()
