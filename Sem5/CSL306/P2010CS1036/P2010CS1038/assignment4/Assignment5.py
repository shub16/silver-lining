'''This file creates a window named "Password Change Application" and does the required checking for new password'''

import pygtk
pygtk.require('2.0')
import gtk

import P2010CS1038_PyGTK as assign4
import re as regular_exp

def isAlphaNumeric(str1):											#this checks a string whether alphanumeric or not 
	str1_alnum=regular_exp.findall('[a-zA-Z0-9]', str1)
	str1_matchNum=regular_exp.findall('[0-9]', str1)
	str1_matchAlpha=regular_exp.findall('[a-zA-Z]', str1)
	if len(str1_alnum)==len(str1) and len(str1_matchAlpha)>0 and len(str1_matchNum)>0:
		return 1
	else:
		return 0

'''This class checks validity of password '''
class change_password:
	def __init__(self, username, old_password, new_password, confirm_new_password):
		self.username=username
		self.old_password=old_password
		self.new_password=new_password
		self.confirm_new_password=confirm_new_password
		
	def check_password_validity(self):		
		if len(self.new_password)<=6:
			print("Password must have minimum 7 characters. Please re-enter!")
			return False		
		elif isAlphaNumeric(self.new_password)==0:
			print("Password must have atleast 1 alphabet,1 digit and no special characters. Please re-enter!")
			return False		
		elif self.new_password!=self.confirm_new_password:
			print("Password entered in the field New Password do not match with Confirm New Password. Please re-enter!")
			return False		
		else:
			return True


if __name__=="__main__":
	def OnPressed(button, uTBox, oldTBox, newTBox, confirmTBox):		#This function is bound to the submit button in the password change aplication
		user=uTBox.get_text()
		old_pwd=oldTBox.get_text()
		new_pwd=newTBox.get_text()
		confirm_pwd=confirmTBox.get_text()
		change_pwd=change_password(user, old_pwd, new_pwd, confirm_pwd)
	
		if change_pwd.check_password_validity()==True:
			print("Password successfully changed")
			return True
		elif change_pwd.check_password_validity()==False:
			newTBox.set_text("")
			confirmTBox.set_text("")
			return False
	

	frame=assign4.Windows("Password Change Application",100,100,300,300)
	st1=assign4.Statictext(frame,"")
	st1.set_text("Username")	
	tb1=assign4.SingleTextBox(frame,True)
		
	st2=assign4.Statictext(frame,"")
	st2.set_text("Old Password")
	tb2=assign4.SingleTextBox(frame,False)

	
	st3=assign4.Statictext(frame,"")
	st3.set_text("New Password")
	tb3=assign4.SingleTextBox(frame,False)

		
	st4=assign4.Statictext(frame,"")
	st4.set_text("Confirm New Password")
	tb4=assign4.SingleTextBox(frame,False)
	
	btn5=assign4.button(frame,"Submit")
	btn5.bind(OnPressed, tb1, tb2, tb3, tb4)

	align=assign4.Alignment(frame)
	align.add(st1,0,0,1)
	align.add(tb1,1,0,1)
	align.add(st2,2,0,1)
	align.add(tb2,3,0,1)
	align.add(st3,4,0,1)
	align.add(tb3,5,0,1)
	align.add(st4,6,0,1)
	align.add(tb4,7,0,1)
	align.add(btn5,8,1,1)
	frame.show_window(align)
	
	
	
	
