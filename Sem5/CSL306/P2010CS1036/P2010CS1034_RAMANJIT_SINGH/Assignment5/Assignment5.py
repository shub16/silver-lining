#!/usr/bin/env python
from P2010CS1034_PyQt import *
import re						#regular_exp

#--------------------VALIDATION_METHOD---------------------

	#To checks whether a string is alphanumeric or not.
def AlphaNumeric(password):
	password_num=re.findall('[0-9]',password)
	password_alpha=re.findall('[a-zA-Z]',password)
	password_alpha_num=re.findall('[a-zA-Z0-9]',password)
	if len(password_alpha_num)==len(password) and len(password_alpha)>0 and len(password_num)>0:
		return True
	else:
		return False

def ReEnter(old_pwd_box,new_pwd_box,cnfrm_pwd_box):
	old_pwd_box.set_text("")
	new_pwd_box.set_text("")
	cnfrm_pwd_box.set_text("")

	#Cheching password validity.
def CheckPassword(usr_name,old_pwd,new_pwd,cnfrm_pwd):
	if len(new_pwd)<=6:
		print "Password must be of more than 6 characters.Please enter again."
		return False
	
	elif AlphaNumeric(new_pwd)==False or AlphaNumeric(cnfrm_pwd)==False:
		print "Password must contain atleast 1 alphabet,1 digit (Without special characters).Please enter again."
		return False
		
	elif new_pwd!=cnfrm_pwd:
		print "Password does not match.Please enter again."
		return False
		
	else:
		print "Password Changed Successfully."
		return True

	# This function is connected with 'Submit' button in the Change Password application.
def OnClick(window,usr_name_box,old_pwd_box, new_pwd_box, cnfrm_pwd_box):
	usr_name=usr_name_box.get_text()
	old_pwd=old_pwd_box.get_text()
	new_pwd=new_pwd_box.get_text()
	cnfrm_pwd=cnfrm_pwd_box.get_text()
	if CheckPassword(usr_name,old_pwd,new_pwd,cnfrm_pwd)==False:
		ReEnter(old_pwd_box,new_pwd_box,cnfrm_pwd_box)
	else:
		usr_name_box.set_text("")
		ReEnter(old_pwd_box,new_pwd_box,cnfrm_pwd_box)

#--------------------MAIN FUNCTION---------------------

def main():
		app = App()

		new=Windows("Change Password",500,250,350,200)
		grid=Alignment(new)

		Label1 = Statictext(new,"Username		")
		Label2 = Statictext(new,"Old Password		")
		Label3 = Statictext(new,"New Password	")
		Label4 = Statictext(new,"Confirm New Password	")

		line1 = SingleTextBox(new,1)
		line2 = SingleTextBox(new,0)
		line3 = SingleTextBox(new,0)
		line4 = SingleTextBox(new,0)
		
		btn1 = button(new,'Submit')
		btn2 = button(new,'Close')
		btn1.bind(OnClick,new,line1,line2,line3,line4)
		btn2.bind(new.close_window)
		
		grid.add(Label1,0,0,3)
		grid.add(line1,0,4,4)
		grid.add(Label2,1,0,3)
		grid.add(line2,1,4,4)
		grid.add(Label3,2,0,3)
		grid.add(line3,2,4,4)
		grid.add(Label4,3,0,3)
		grid.add(line4,3,4,4)
		grid.add(btn1,4,2,1)
		grid.add(btn2,4,4,1)
		
		new.show_window(grid)
		app.loop()
            
if __name__ == '__main__':
    main()


